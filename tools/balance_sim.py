"""Balance simulator: every class fights monsters through the real combat code, with output silenced.

    python tools/balance_sim.py                 # all three reports
    python tools/balance_sim.py fights          # win% / rounds / HP left vs same-level monsters
    python tools/balance_sim.py groups          # the same against three monsters at once (boss rooms)
    python tools/balance_sim.py endurance       # consecutive fights survived without resting
    python tools/balance_sim.py bosses          # boss win% at boss level and boss level +3
    python tools/balance_sim.py endgame         # Planes of the Gods vs level-50 characters with 1/6/11 lives
    python tools/balance_sim.py unlock          # what a plate-wearing past life is worth to each class
    python tools/balance_sim.py gear            # best armor and HP each armor tier can reach, level by level
    options: --n 40 (fights per cell), --levels 1,5,10,20,30,40,50, --seed 3

The simulated player is a human with best-in-slot gear for their level (including boss drops,
so results are optimistic) among the items its class is trained for, and a simple AI: heal when low, recast a broken shield, cast each buff once, otherwise use
the ability with the best expected value (there are no cooldowns, so that is the newest attack). Bosses are fought with 5 healing potions.
Targets the game was tuned to: same-level fights cost ~25-55% HP and last ~6-8 rounds on average
(the user's choice, 2026-11-03; world monsters' WORLD_HP_MULT / WORLD_DMG_MULT); endurance 2-6 for most
classes; bosses mostly beatable at level +3. Endgame (monsters above level 50; a multi-life
character takes the best stats of every class it has lived): first-tier plane monsters a coin
flip with 1 life and easy with 6; plane champions ~80-95% with 6 lives; elemental lords ~95% with
11; Lord Trepth ~70% with 11 lives (every class 50-85%).
Every simulated character is Tier 1: tiers (+10 stats per tier) are deliberately never balanced for.
"""
import argparse
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import ui  # noqa: E402

ui.say = ui.out = ui.rule = lambda *a, **k: None  # silence the game

from character import MAX_LEVEL, Character  # noqa: E402
from combat import Combat, potion_drop, resolve_self_effect  # noqa: E402
from data.abilities import ABILITIES  # noqa: E402
from data.classes import CLASS_ORDER, CLASSES  # noqa: E402
from data.items import ARMOR_TIERS, DUAL_KINDS, ITEMS, SLOTS  # noqa: E402
from data.monsters import MONSTERS  # noqa: E402
from game import Game  # noqa: E402
from world import MonsterInstance  # noqa: E402

DEFAULT_LEVELS = [1, 3, 5, 8, 12, 16, 20, 25, 30, 35, 40, 45, 50]


def best_gear(p):
    main = {"STR": 2}
    if p.cdata["mana"]:  # casters weigh INT and WIS by how many of their spells scale with each
        used = [e["stat"] for a in ABILITIES.values() if a["cls"] == p.cls
                for e in a["effects"] if e.get("stat") in ("INT", "WIS")]
        for s in ("INT", "WIS"):
            main[s] = 0.7 + 1.3 * used.count(s) / max(1, len(used))

    def score(it):
        sc = it.get("armor", 0) * 1.5 + sum(v * main.get(s, 0.7) for s, v in it["stats"].items())
        if it["type"] == "weapon":
            sc += sum(it["dmg"]) * (1.5 if p.cdata["mana"] < 5 else 0.5)
        return sc

    for slot in SLOTS:
        cands = [i for i in ITEMS.values() if i.get("slot") == slot and i["level"] <= p.level
                 and p.trained_for(i["id"])[0]]
        if cands:
            p.equipment[slot] = max(cands, key=score)["id"]
    if p.has_passive("dual_wield"):  # dual wielders hold the best one-hander in each hand
        ones = [i for i in ITEMS.values() if i["type"] == "weapon" and i["kind"] in DUAL_KINDS
                and i["level"] <= p.level and p.trained_for(i["id"])[0]]
        if ones:
            p.equipment["weapon"] = p.equipment["shield"] = max(ones, key=score)["id"]


def nearby_monsters(level):
    """The three non-boss monster types closest to `level`."""
    cands = sorted((m for m in MONSTERS.values() if not m["boss"]), key=lambda m: abs(m["level"] - level))
    return [m["id"] for m in cands[:3]]


def setup(cls, level):
    p = Character("Sim", "human", cls)
    p.level = level
    best_gear(p)
    p.hp, p.mana = p.max_hp, p.max_mana
    g = Game(p)
    g.room_id = "cellar"
    g.check_aggro = lambda: None
    return g, p


def fight(g, p, mid, potions=0, max_rounds=60):
    """One fight to the death through the real Combat class. `mid` is a monster id or a list of them
    (a group that all fight at once). Returns (won, rounds, hp_fraction_left)."""
    room = g.room
    mons = [MonsterInstance(m) for m in ([mid] if isinstance(mid, str) else mid)]
    room.monsters = list(mons)
    for ab in p.usable_abilities():  # summon a pet before the pull (summons can't be cast in combat)
        summon = [e for e in ab["effects"] if e["type"] == "summon"]
        if summon and not p.pet and p.mana >= p.mana_cost(ab):
            p.mana -= p.mana_cost(ab)
            resolve_self_effect(g, ab, summon[0])
    g.combat = Combat(g, mons)
    pot = next(i for i in iter(lambda: potion_drop(mons[0].level), None) if i.endswith("healing_potion"))
    weapon_avg = lambda: sum(p.weapon_range()) / 2  # noqa: E731
    rounds = 0
    while g.combat and not g.combat.over and rounds < max_rounds:
        rounds += 1
        mon = g.combat.current_target()
        usable = [a for a in p.usable_abilities() if a["kind"] != "spell" or p.mana_cost(a) <= p.mana]
        active = {e.get("name") for e in p.effects}
        heals = [a for a in usable if a["target"] == "self"
                 and any(e["type"] == "heal" or (e["type"] == "hot" and e["name"] not in active)
                         for e in a["effects"])]
        shielded = any(e["type"] == "shield" for e in p.effects)

        def improves(e):  # only the strongest buff of each kind counts, so skip ones that add nothing
            mods = dict(e["mods"])
            mods["armor"] = mods.get("armor", 0) + mods.pop("armor_lvl", 0) * p.level
            return e["name"] not in active and any(v > p.buff_mod(k) for k, v in mods.items())
        buffs = [a for a in usable if a["target"] == "self"
                 and any(e["type"] == "buff" and improves(e) for e in a["effects"])]
        shields = [a for a in usable if a["target"] == "self" and not shielded
                   and any(e["type"] == "shield" for e in a["effects"])]
        offense = [a for a in usable if a["target"] != "self"]

        def value(a):
            sc = 0
            for e in a["effects"]:
                if e["type"] == "weapon":
                    sc += weapon_avg() * e["mult"]
                elif e["type"] in ("damage", "drain"):
                    sc += p.power(e)
                elif e["type"] == "dot" and not any(x.get("name") == e["name"] for x in mon.effects):
                    sc += p.power(e) * e["turns"] * 0.6
                elif e["type"] == "weaken" and not any(x.get("name") == e["name"] for x in mon.effects):
                    sc += weapon_avg() * 0.8
            return sc

        if p.hp < p.max_hp * 0.3 and not heals and potions:
            potions -= 1
            p.heal(ITEMS[pot]["heal"])
            g.combat.pass_turn(swing=True)
        elif p.hp < p.max_hp * 0.4 and heals:
            g.combat.player_ability(max(heals, key=lambda a: sum(p.power(e) for e in a["effects"]
                                                                 if e["type"] in ("heal", "hot"))), None)
        elif shields and (rounds <= 1 or p.hp < p.max_hp * 0.6):  # recast a shield once it breaks
            g.combat.player_ability(max(shields, key=lambda a: p.power(a["effects"][0])), None)
        elif buffs:  # buffs last the whole fight: cast each once
            g.combat.player_ability(max(buffs, key=lambda a: a["level"]), None)
        else:
            best = max(offense, key=value) if offense else None
            if best and value(best) > 0:  # every action comes with a swing
                g.combat.player_ability(best, mon)
            else:
                g.combat.player_attack(mon)
    won = all(m.hp <= 0 for m in mons)
    return won, rounds, (max(0, p.hp) / p.max_hp if won else 0.0)


def report_fights(levels, n):
    print("win% / avg rounds / avg HP% left, vs same-level monsters")
    print("lvl  " + " ".join("{:>13}".format(c[:13]) for c in CLASS_ORDER))
    for L in levels:
        mids = nearby_monsters(L)
        row = []
        for cls in CLASS_ORDER:
            res = []
            for _ in range(n):
                g, p = setup(cls, L)
                res.append(fight(g, p, random.choice(mids)))
            wins = [r for r in res if r[0]]
            row.append("{:>3.0f}%{:>4.1f}r{:>3.0f}%".format(
                100 * len(wins) / n, sum(r[1] for r in res) / n,
                100 * sum(r[2] for r in wins) / max(1, len(wins))))
        print("{:>3}  ".format(L) + " ".join("{:>13}".format(x) for x in row))


def report_endurance(levels, n, cap=8):
    print("consecutive same-level fights survived (3 ticks of regen between, cap {})".format(cap))
    print("lvl  " + " ".join("{:>7}".format(c[:7]) for c in CLASS_ORDER))
    for L in levels:
        mids = nearby_monsters(L)
        row = []
        for cls in CLASS_ORDER:
            total = 0
            for _ in range(n):
                g, p = setup(cls, L)
                survived = 0
                while survived < cap:
                    won, _, _ = fight(g, p, random.choice(mids))
                    if not won or p.hp <= 0:
                        break
                    survived += 1
                    for _ in range(3):
                        g.world_tick()
                total += survived
            row.append("{:>7.1f}".format(total / n))
        print("{:>3}  ".format(L) + " ".join(row))


def report_bosses(n):
    print("boss win% with 5 healing potions: at boss level / at boss level +3")
    print("{:<30}".format("") + " ".join("{:>9}".format(c[:9]) for c in CLASS_ORDER))
    for b in (m for m in MONSTERS.values() if m["boss"] and m["level"] <= MAX_LEVEL + 2):
        row = []
        for cls in CLASS_ORDER:
            rates = []
            for offset in (0, 3):
                L = min(50, b["level"] + offset)
                wins = 0
                for _ in range(n):
                    g, p = setup(cls, L)
                    wins += fight(g, p, b["id"], potions=5)[0]
                rates.append(100 * wins / n)
            row.append("{:>3.0f}/{:<3.0f}".format(*rates))
        print("{:<30}".format(b["name"][:29]) + " ".join("{:>9}".format(x) for x in row))


def report_groups(levels, n):
    """Three same-level monsters at once, as in a boss room where every monster attacks."""
    print("win% / avg rounds / avg HP% left, vs three same-level monsters at once (with 3 healing potions)")
    print("lvl  " + " ".join("{:>13}".format(c[:13]) for c in CLASS_ORDER))
    for L in levels:
        mids = nearby_monsters(L)
        row = []
        for cls in CLASS_ORDER:
            res = []
            for _ in range(n):
                g, p = setup(cls, L)
                res.append(fight(g, p, [random.choice(mids) for _ in range(3)], potions=3))
            wins = [r for r in res if r[0]]
            row.append("{:>3.0f}%{:>4.1f}r{:>3.0f}%".format(
                100 * len(wins) / n, sum(r[1] for r in res) / n,
                100 * sum(r[2] for r in wins) / max(1, len(wins))))
        print("{:>3}  ".format(L) + " ".join("{:>13}".format(x) for x in row))


ENDGAME_LIVES = (1, 6, 11)


def setup_lives(cls, lives):
    """A level-50 character in `cls` who has lived `lives` classes in all (this one included)."""
    g, p = setup(cls, MAX_LEVEL)
    for other in [c for c in CLASS_ORDER if c != cls][:lives - 1]:
        p.past_lives.append({"cls": other})
    best_gear(p)
    p.hp, p.mana = p.max_hp, p.max_mana
    return g, p


def report_endgame(n):
    """Planes of the Gods (monsters above level 50): win% for characters with 1, 6 and 11 lives."""
    print("level-50 win% vs the planes, averaged over classes (bosses with 5 potions): "
          + " / ".join("{} li{}".format(x, "fe" if x == 1 else "ves") for x in ENDGAME_LIVES)
          + "   [worst class at 11 lives]")
    mids = sorted((m for m in MONSTERS.values() if m["level"] > MAX_LEVEL), key=lambda m: (m["boss"], m["level"]))
    for m in mids:
        rates, worst = [], 100
        for lives in ENDGAME_LIVES:
            total = 0
            for cls in CLASS_ORDER:
                wins = sum(fight(*setup_lives(cls, lives), m["id"], potions=5 if m["boss"] else 0)[0]
                           for _ in range(n))
                total += wins
                if lives == ENDGAME_LIVES[-1]:
                    worst = min(worst, 100 * wins / n)
            rates.append(100 * total / (n * len(CLASS_ORDER)))
        print("{:<34} L{}  ".format(m["name"][:33], m["level"])
              + " / ".join("{:>3.0f}%".format(r) for r in rates) + "   [{:.0f}%]".format(worst))


def training_only_life(p, cls):
    """Give `p` the armor and weapon training of `cls` but none of its stats, HP, mana, abilities or
    mastery bonus, so the report measures the gear unlock alone."""
    mine = p.cls

    def trained_for(iid):
        p.lived_classes = lambda: {mine, cls}  # only while checking training
        try:
            return Character.trained_for(p, iid)
        finally:
            del p.lived_classes
    p.trained_for = trained_for
    best_gear(p)
    p.hp, p.mana = p.max_hp, p.max_mana


def report_unlock(levels, n):
    print("same-level fights: own training / with a warrior's armor and weapon training (no stats)")
    print("cells: HP% left after a win, then max HP and armor; endurance = fights in a row")
    print("lvl  {:<14}{:>22}{:>22}{:>16}".format("class", "own", "+plate", "endurance"))
    for L in levels:
        mids = nearby_monsters(L)
        for cls in CLASS_ORDER:
            if CLASSES[cls]["armor"] == "plate":
                continue
            cells, endure = [], []
            for unlock in (False, True):
                def make():
                    g, p = setup(cls, L)
                    if unlock:
                        training_only_life(p, "warrior")
                    return g, p
                res = [fight(*make(), random.choice(mids)) for _ in range(n)]
                wins = [r for r in res if r[0]]
                g, p = make()
                cells.append("{:>3.0f}%w {:>3.0f}%hp {:>4}/{:<3}".format(
                    100 * len(wins) / n, 100 * sum(r[2] for r in wins) / max(1, len(wins)), p.max_hp, p.armor))
                total = 0
                for _ in range(n):
                    g, p = make()
                    survived = 0
                    while survived < 8 and fight(g, p, random.choice(mids))[0] and p.hp > 0:
                        survived += 1
                        for _ in range(3):
                            g.world_tick()
                    total += survived
                endure.append(total / n)
            print("{:>3}  {:<14}{:>22}{:>22}{:>9.1f} /{:>4.1f}".format(L, cls[:14], cells[0], cells[1], *endure))
        print()


def report_gear(levels):
    """For each armor tier: the most armor and HP a character limited to that tier can wear at each level.
    Big jumps between neighbouring levels, or a tier far behind the one below it, show gaps in the items."""
    body = ["head", "chest", "hands", "legs", "feet"]
    rep = {"cloth": "wizard", "leather": "rogue", "mail": "cleric", "plate": "warrior"}
    print("best body-armor total per tier (head+chest+hands+legs+feet), with that tier's best piece level per slot")
    for L in levels:
        row = []
        for tier in ARMOR_TIERS:
            p = Character("Sim", "human", rep[tier])
            p.level = L
            parts, total = [], 0
            for slot in body:
                cands = [i for i in ITEMS.values() if i.get("slot") == slot and i["level"] <= L
                         and i["kind"] == tier]
                best = max(cands, key=lambda i: i["armor"], default=None)
                total += best["armor"] if best else 0
                parts.append(str(best["level"]) if best else "-")
            row.append("{:<7} {:>3} ({})".format(tier, total, ",".join(parts)))
        print("{:>3}  ".format(L) + "   ".join(row))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("report", nargs="?", default="all",
                    choices=["all", "fights", "groups", "endurance", "bosses", "endgame", "unlock", "gear"])
    ap.add_argument("--n", type=int, default=30, help="simulated fights per table cell")
    ap.add_argument("--levels", default=",".join(map(str, DEFAULT_LEVELS)), help="comma-separated levels")
    ap.add_argument("--seed", type=int, default=3)
    opts = ap.parse_args()
    random.seed(opts.seed)
    levels = [int(x) for x in opts.levels.split(",")]
    if opts.report in ("all", "fights"):
        report_fights(levels, opts.n)
        print()
    if opts.report in ("all", "groups"):
        report_groups(levels, opts.n)
        print()
    if opts.report in ("all", "endurance"):
        report_endurance(levels, opts.n)
        print()
    if opts.report in ("all", "bosses"):
        report_bosses(opts.n)
        print()
    if opts.report in ("all", "endgame"):
        report_endgame(opts.n)
    if opts.report == "unlock":
        report_unlock(levels, opts.n)
    if opts.report == "gear":
        report_gear(levels)


if __name__ == "__main__":
    main()
