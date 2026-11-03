"""Turn-based combat: player actions, ability resolution, monster AI, rewards."""
import random

import ui
from character import MAX_LEVEL, Pet
from data.abilities import OFFHAND_MULT, double_attack_chance
from data.items import ITEMS
from data.monsters import MONSTERS

SELF_EFFECTS = {"heal", "heal_pct", "hot", "shield", "buff", "summon", "invisible"}
CRIT_MULT = 1.75
AGGRO_GAP = 6  # aggressive monsters ignore players this many levels above them


def level_gap_mult(attacker_level, defender_level):
    """Damage multiplier from the level difference: punching up hurts, punching down is soft."""
    diff = attacker_level - defender_level
    if diff >= 0:
        return min(1.4, 1 + 0.04 * diff)
    return max(0.4, 1 + 0.06 * diff)


def monster_xp(mon, player_level):
    d = MONSTERS[mon.id]
    base = (15 + 14.5 * mon.level ** 1.5) * d["xp"]
    diff = mon.level - player_level
    if diff > 0:
        mult = min(1.5, 1 + 0.1 * diff)
    elif diff < -3:
        mult = max(0.05, 1 - 0.12 * (-diff - 3))
    else:
        mult = 1.0
    return int(base * mult)


def con_color(mon_level, player_level):
    diff = mon_level - player_level
    if diff >= 5:
        return "bred", "deadly"
    if diff >= 3:
        return "red", "very dangerous"
    if diff >= 1:
        return "byellow", "challenging"
    if diff >= -2:
        return "bwhite", "an even match"
    if diff >= -6:
        return "bblue", "easy"
    if diff >= -10:
        return "bgreen", "trivial"
    return "grey", "beneath your notice"


def potion_drop(level):
    if level < 10:
        tier = ("minor_healing_potion", "minor_mana_potion")
    elif level < 25:
        tier = ("healing_potion", "mana_potion")
    elif level < 40:
        tier = ("greater_healing_potion", "greater_mana_potion")
    else:
        tier = ("supreme_healing_potion", "supreme_mana_potion")
    return random.choice(tier)


def resolve_self_effect(game, ab, eff):
    """Apply an effect whose target is the caster. Works in and out of combat."""
    p = game.player
    t = eff["type"]
    if t == "heal":
        amt = p.heal(p.power(eff) * random.uniform(0.9, 1.1))
        ui.say("You are healed for {} HP.".format(amt), "bgreen")
    elif t == "heal_pct":
        amt = p.heal(p.max_hp * eff["pct"])
        ui.say("You are healed for {} HP.".format(amt), "bgreen")
    elif t == "hot":
        val = max(1, int(p.power(eff)))
        p.add_effect({"type": "hot", "name": eff["name"], "value": val, "turns": eff["turns"], "fresh": True})
        ui.say("{} will heal you for {} HP each round for {} rounds.".format(eff["name"], val, eff["turns"]), "green")
    elif t == "shield":  # lasts until used up; a new shield replaces any old one
        val = int(p.power(eff))
        p.effects = [e for e in p.effects if e["type"] != "shield"]
        p.add_effect({"type": "shield", "name": ab["name"], "value": val})
        ui.say("A shield absorbs the next {} damage.".format(val), "bcyan")
    elif t == "buff":
        mods = dict(eff["mods"])
        if "armor_lvl" in mods:
            mods["armor"] = mods.get("armor", 0) + mods.pop("armor_lvl") * p.level
        p.add_effect({"type": "buff", "name": eff["name"], "mods": mods})  # until the end of the fight
        parts = []
        if mods.get("damage_pct"):
            parts.append("+{}% damage".format(int(mods["damage_pct"] * 100)))
        if mods.get("armor"):
            parts.append("+{} armor".format(int(mods["armor"])))
        if mods.get("dodge"):
            parts.append("+{}% dodge".format(int(mods["dodge"] * 100)))
        if mods.get("lifesteal"):
            parts.append("{}% lifesteal".format(int(mods["lifesteal"] * 100)))
        ui.say("{}: {} until the end of your next fight.".format(eff["name"], ", ".join(parts)), "bcyan")
    elif t == "invisible":
        p.add_effect({"type": "invisible", "name": eff["name"], "turns": eff["turns"]})
        ui.say("You are invisible. Aggressive monsters won't see you for about {} minutes.".format(
            round(eff["turns"] * 4 / 60)), "bcyan")
    elif t == "summon":
        stat = p.magic_stat(eff["stat"])
        hp = int(eff["hp_base"] + eff["hp_lvl"] * p.level + stat * 0.5)
        lo = int(eff["dmg_base"] + eff["dmg_lvl"] * p.level * 0.6 + stat * 0.08)
        hi = int(lo * 1.5) + 2
        if p.pet:
            ui.say("Your {} crumbles away as a new servant takes its place.".format(p.pet.name), "grey")
        p.pet = Pet(eff["name"], hp, lo, hi, eff["desc"])
        ui.say("{} now fights at your side ({} HP, {}-{} damage).".format(
            eff["name"][0].upper() + eff["name"][1:], hp, lo, hi), "bcyan")


class Combat:
    def __init__(self, game, enemies):
        self.game = game
        self.enemies = []
        self.over = False
        self.target = None
        self.queued = None  # the player's action for the next round, on top of the auto-attack
        for e in enemies:
            self.add(e)

    # ------------------------------------------------------------------ the round clock
    def queue(self, desc, action):
        self.queued = action
        ui.say(desc, "cyan")

    def current_target(self):
        if self.target is None or not self.target.alive or self.target not in self.enemies:
            alive = self.living()
            self.target = alive[0] if alive else None
        return self.target

    def auto_attack(self):
        target = self.current_target()
        if target:
            self.player_attack(target)
        else:
            self.end_round()

    def round(self):
        """One combat round, fired by the game clock."""
        if self.queued:
            action, self.queued = self.queued, None
            action()
        else:
            self.auto_attack()

    @property
    def p(self):
        return self.game.player

    @property
    def room(self):
        return self.game.room

    def add(self, mon):
        if mon not in self.enemies and mon.alive:
            self.enemies.append(mon)

    def living(self):
        return [e for e in self.enemies if e.alive]

    def find_target(self, word):
        """Find an engaged enemy, or a monster in the room (which then joins the fight)."""
        if not word:
            alive = self.living()
            return alive[0] if alive else None
        mon = self.game.find_monster(word, prefer=self.living())
        if mon:
            self.add(mon)
        return mon

    # ------------------------------------------------------------------ damage helpers
    def damage_monster(self, mon, raw, physical, element="physical", can_crit=True):
        dmg = raw * level_gap_mult(self.p.level, mon.level)
        if physical:
            dmg *= 1 - mon.armor / (mon.armor + 50 + 10 * mon.level)
        crit = can_crit and random.random() < self.p.crit_chance
        if crit:
            dmg *= CRIT_MULT
        dmg = max(1, int(dmg * random.uniform(0.9, 1.1)))
        mon.hp -= dmg
        ls = self.p.buff_mod("lifesteal")
        if ls and physical:
            self.p.heal(dmg * ls)
        return dmg, crit

    def report_hit(self, verb, mon, dmg, crit, color="bgreen"):
        crit_txt = ui.c(" CRITICAL!", "byellow", "bold") if crit else ""
        ui.out(ui.c("{} {} for {} damage.".format(verb, mon.name, dmg), color) + crit_txt)

    # ------------------------------------------------------------------ player actions
    def player_attack(self, mon):
        self.swing(mon)
        self.end_round()

    def swing(self, mon=None):
        """The auto-attack. It lands every round, alongside any action you take.
        Dual Wield adds an off-hand strike and Double Attack may repeat each hand, so up to four."""
        p = self.p
        hands = [("weapon", 1.0, "You strike", "You swing at {} but miss!")]
        if p.offhand_weapon():
            hands.append(("shield", OFFHAND_MULT, "Your off hand strikes", "Your off-hand blow misses {}!"))
        again = double_attack_chance(p.level, p.passive_level("double_attack")) if p.has_passive("double_attack") else 0
        for slot, mult, verb, miss in hands:
            for n in range(2):
                if n and random.random() >= again:
                    break
                mon = mon if mon and mon.alive else self.current_target()
                if not mon:
                    return
                if random.random() < p.miss_chance:
                    ui.say(miss.format(mon.name), "grey")
                else:
                    dmg, crit = self.damage_monster(mon, p.roll_weapon(mult, slot), physical=True)
                    self.report_hit(verb + (" again, hitting" if n else ""), mon, dmg, crit)

    def player_ability(self, ab, target):
        p = self.p
        cost = p.mana_cost(ab) if ab["kind"] == "spell" else 0
        p.mana -= cost
        if ab["target"] == "enemy":
            targets = [target]
            tname = target.name
        else:
            targets = []
            tname = "yourself"
        ui.say("{}".format(ab["msg"].format(t=tname)), "bmagenta")
        for eff in ab["effects"]:
            if eff["type"] in SELF_EFFECTS:
                resolve_self_effect(self.game, ab, eff)
            else:
                for mon in targets:
                    if mon.alive:
                        self.apply_offensive(eff, mon, ab)
        self.swing(target)
        self.end_round()

    def apply_offensive(self, eff, mon, ab):
        p = self.p
        t = eff["type"]
        if t == "weapon":
            dmg, crit = self.damage_monster(mon, p.roll_weapon(eff["mult"]), physical=True)
            self.report_hit(ab["name"] + " hits", mon, dmg, crit)
        elif t == "damage":
            dmg, crit = self.damage_monster(mon, p.power(eff) * p.damage_mult, physical=False, element=eff["element"])
            self.report_hit("{} sears".format(ab["name"]), mon, dmg, crit, "bmagenta")
        elif t == "drain":
            dmg, crit = self.damage_monster(mon, p.power(eff) * p.damage_mult, physical=False)
            healed = p.heal(dmg * eff["frac"])
            self.report_hit("{} drains".format(ab["name"]), mon, dmg, crit, "bmagenta")
            if healed:
                ui.say("You absorb {} HP.".format(healed), "bgreen")
        elif t == "dot":
            val = max(1, int(p.power(eff) * p.damage_mult))
            mon.add_effect({"type": "dot", "name": eff["name"], "value": val, "turns": eff["turns"]})
            ui.say("{} is afflicted by {} ({} per round).".format(mon.short(), eff["name"], val), "magenta")
        elif t == "weaken":  # lasts the whole fight
            mon.add_effect({"type": "weaken", "name": eff["name"], "pct": eff["pct"]})
            ui.say("{} is {} (-{}% damage).".format(mon.short(), eff["name"].lower(), int(eff["pct"] * 100)), "magenta")

    def pass_turn(self, swing=False):
        """The player spends the round on something else: a potion or a failed escape (still swinging)."""
        if swing:
            self.swing()
        self.end_round()

    # ------------------------------------------------------------------ round resolution
    def end_round(self):
        g, p = self.game, self.p
        self.tick_player_effects()
        # pet acts
        alive = self.living()
        if p.pet and alive:
            mon = random.choice(alive)
            raw = random.randint(p.pet.dmg_min, p.pet.dmg_max)
            dmg, crit = self.damage_monster(mon, raw, physical=True, can_crit=False)
            ui.say("{} savages {} for {} damage.".format(p.pet.name[0].upper() + p.pet.name[1:], mon.name, dmg), "cyan")
        self.process_deaths()
        # newly arrived aggressive monsters join
        for m in self.room.living():
            if m.aggro and m not in self.enemies and m.level >= p.level - AGGRO_GAP:
                self.add(m)
                ui.say("{} joins the fight!".format(m.short()), "red")
        # monsters act
        for mon in self.living():
            if p.hp <= 0:
                break
            self.monster_act(mon)
        # monster effects
        for mon in self.living():
            self.tick_monster_effects(mon)
        self.process_deaths()
        # regeneration
        p.mana = min(p.max_mana, p.mana + max(1, int(p.max_mana * 0.02)))
        if p.perk("regen_mult", 1.0) > 1.0 and p.hp > 0:
            p.heal(p.max_hp * 0.02)
        g.world.tick(1, avoid_room=self.room.id)
        if p.hp <= 0:
            self.over = True
            g.player_died()
            return
        if not self.living():
            self.over = True
            ui.say("The battle is over. You are victorious!", "byellow")
            g.end_combat()
            return
        self.status_line()

    def tick_player_effects(self):
        p = self.p
        keep = []
        for e in p.effects:
            if e.get("fresh"):
                e["fresh"] = False
                keep.append(e)
                continue
            if "turns" not in e:  # buffs last the fight, shields until used up
                keep.append(e)
                continue
            if e["type"] == "dot":
                p.hp -= e["value"]
                ui.say("{} burns you for {} damage.".format(e["name"], e["value"]), "red")
            elif e["type"] == "hot":
                amt = p.heal(e["value"])
                if amt:
                    ui.say("{} heals you for {} HP.".format(e["name"], amt), "green")
            e["turns"] -= 1
            if e["turns"] > 0:
                keep.append(e)
            elif e["type"] == "hot":
                ui.say("{} fades.".format(e["name"]), "grey")
        p.effects = keep

    def tick_monster_effects(self, mon):
        keep = []
        for e in mon.effects:
            if e["type"] == "dot":
                mon.hp -= e["value"]
                ui.say("{} suffers {} damage from {}.".format(mon.short(), e["value"], e["name"]), "magenta")
            if "turns" not in e:  # debuffs last the whole fight
                keep.append(e)
                continue
            e["turns"] -= 1
            if e["turns"] > 0:
                keep.append(e)
        mon.effects = keep

    def monster_act(self, mon):
        p = self.p
        special = None
        for sp in mon.specials:
            if random.random() < sp["chance"]:
                special = sp
                break
        if special and special["type"] == "heal":
            amt = int(mon.max_hp * special["mult"])
            mon.hp = min(mon.max_hp, mon.hp + amt)
            ui.say("{} {} (+{} HP)".format(mon.short(), special["msg"], amt), "red")
            return
        # pets draw some of the attacks
        if p.pet and random.random() < 0.25 and not special:
            dmg = int(random.randint(mon.dmg_min, mon.dmg_max) * mon.weaken_mult())
            p.pet.hp -= dmg
            ui.say("{} hits {} for {} damage.".format(mon.short(), p.pet.name, dmg), "yellow")
            if p.pet.hp <= 0:
                ui.say("{} is destroyed!".format(p.pet.name[0].upper() + p.pet.name[1:]), "bred")
                p.pet = None
            return
        miss = p.dodge + 0.05 + max(0, (p.level - mon.level) * 0.02)
        if random.random() < miss:
            what = special["name"] if special else "attack"
            ui.say("You dodge {}'s {}.".format(mon.name, what.lower() if not special else what), "grey")
            return
        raw = random.randint(mon.dmg_min, mon.dmg_max) * mon.weaken_mult() * level_gap_mult(mon.level, p.level)
        physical = True
        if special:
            st = special["type"]
            if st == "big":
                raw *= special["mult"]
            elif st == "drain":
                raw *= special["mult"]
                physical = False
            elif st == "dot":
                raw *= 0.6
        dmg = raw
        if physical:
            dmg *= 1 - p.armor / (p.armor + 40 + 6 * mon.level)
        dmg = max(1, int(dmg))
        absorbed_before = dmg
        dmg = p.absorb(dmg)
        p.hp -= dmg
        shield_txt = " ({} absorbed)".format(absorbed_before - dmg) if absorbed_before != dmg else ""
        if special:
            ui.say("{} {} [{}] {} damage{}.".format(mon.short(), special["msg"], special["name"], dmg, shield_txt), "bred")
            st = special["type"]
            if st == "drain":
                mon.hp = min(mon.max_hp, mon.hp + dmg)
            elif st == "dot":
                if special["element"] in p.perk("immune", []):
                    ui.say("Your undead flesh shrugs off the {}.".format(special["element"]), "grey")
                else:
                    val = max(1, int((mon.dmg_min + mon.dmg_max) / 2 * special["mult"]))
                    p.add_effect({"type": "dot", "name": special["name"], "value": val,
                                  "turns": special["turns"]})
        else:
            ui.say("{} hits you for {} damage{}.".format(mon.short(), dmg, shield_txt), "red")

    def process_deaths(self):
        for mon in list(self.enemies):
            if not mon.alive and not getattr(mon, "rewarded", False):
                mon.rewarded = True
                self.reward(mon)

    def reward(self, mon):
        g, p = self.game, self.p
        ui.say("{} collapses, slain!".format(mon.short()), "byellow")
        g.world.monster_died(self.room, mon)
        p.kills += 1
        d = MONSTERS[mon.id]
        for line, color in p.gain_xp(monster_xp(mon, p.level)) if p.level < MAX_LEVEL else []:
            ui.say(line, color) if color else ui.out(line)
        gold = int(random.randint(mon.level + 1, mon.level * 3 + 3) * d["gold"])
        if gold:
            p.gold += gold
            ui.say("You loot {} gold coins.".format(gold), "yellow")
        drops = [iid for iid, chance in d["loot"] if random.random() < chance]
        if random.random() < 0.12:
            drops.append(potion_drop(mon.level))
        for iid in drops:
            p.inventory.append(iid)
            ui.say("You loot {}.".format(ITEMS[iid]["name"]), "bwhite")
        g.on_kill(mon.id)

    def status_line(self):
        p = self.p
        if p.pet:
            ui.out(ui.c("{} [{}/{}]".format(p.pet.name[0].upper() + p.pet.name[1:], p.pet.hp, p.pet.max_hp), "cyan"))
        for m in self.living():
            ui.out(ui.c("{} {} [{}/{}]".format(m.short(), m.health_word(), m.hp, m.max_hp), "red"))
