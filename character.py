"""The player character: stats, levelling, abilities, equipment and rebirth."""
import random

from data.abilities import ABILITIES, PASSIVES
from data.classes import CLASSES, STATS
from data.items import ARMOR_TIERS, DUAL_KINDS, FREE_KINDS, ITEMS, SLOTS
from data.races import RACES

MAX_LEVEL = 50
MASTERY_BONUS = 0.02  # max HP and damage per class mastered
MAX_TIER = 10
TIER_BONUS = 10  # to every stat per tier above 1 (not counted in balancing)
MISS_BASE, MISS_PER_DEX, MISS_FLOOR = 0.10, 0.0007, 0.02  # weapon swings: 9% at 10 DEX, 2% from about 115


def xp_for_level(level):
    """Experience needed to advance from `level` to `level + 1` (the same in every life).

    It grows faster than kill XP (level^1.5 in combat.monster_xp), so a level takes about
    6 same-level kills at 5-10 and about 10 near 50.
    """
    return int(65 * level ** 1.7)


class Pet:
    def __init__(self, name, max_hp, dmg_min, dmg_max, desc=""):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.dmg_min = dmg_min
        self.dmg_max = dmg_max
        self.desc = desc

    def to_dict(self):
        return dict(self.__dict__)

    @classmethod
    def from_dict(cls, d):
        p = cls(d["name"], d["max_hp"], d["dmg_min"], d["dmg_max"], d.get("desc", ""))
        p.hp = d["hp"]
        return p


class Character:
    def __init__(self, name, race, cls):
        self.name = name
        self.race = race
        self.cls = cls
        self.level = 1
        self.xp = 0
        self.gold = 20
        self.tier = 1         # +1 each time every class is mastered; resets past_lives
        self.past_lives = []  # [{"cls": id}], one per class mastered before this life (this tier)
        self.inventory = []   # item ids, duplicates allowed
        self.bank = []        # item ids stored in the Sunvault in Brightwater
        self.equipment = {s: None for s in SLOTS}
        self.quests = {}      # quest id -> {"status": "active"|"done", "count": n}
        self.effects = []     # buffs (whole fight), shields (until used up), hots and dots (timed)
        self.pet = None
        self.aliases = {}     # player-defined shortcut -> command line
        self.automap = False  # show a small map under every room description
        self.kills = 0
        self.deaths = 0
        self.boss_kills = []  # boss ids this character has ever slain (across all lives)
        self.wear_kit(cls)
        self.inventory += ["minor_healing_potion"] * 3
        self.hp = self.max_hp
        self.mana = self.max_mana

    # ------------------------------------------------------------------ data
    @property
    def cdata(self):
        return CLASSES[self.cls]

    @property
    def rdata(self):
        return RACES[self.race]

    def perk(self, key, default):
        return self.rdata["perks"].get(key, default)

    @property
    def class_name(self):
        return self.cdata["name"]

    @property
    def eternal(self):
        """Every class mastered at the final tier: the end of the road."""
        return self.tier >= MAX_TIER and len(self.mastered_classes()) == len(CLASSES)

    @property
    def display_name(self):
        return "Emperor {} the Eternal".format(self.name) if self.eternal else self.name

    @property
    def race_name(self):
        return self.rdata["name"]

    # ------------------------------------------------------------------ stats
    # Every lived class counts the same, whatever the order: each stat, max HP and max mana take the
    # best that any of them would have at the current level. Mastered classes add a flat bonus.
    def class_stat(self, cls, stat, level=None):
        """What `cls` alone contributes to `stat` at `level` (race not included)."""
        level = self.level if level is None else level
        c = CLASSES[cls]
        return c["start"].get(stat, 0) + c["gains"].get(stat, 0) * (level - 1)

    def base_stat(self, stat, level=None):
        return (self.rdata["stats"][stat] + max(self.class_stat(c, stat, level) for c in self.lived_classes())
                + self.tier_bonus)

    @property
    def tier_bonus(self):
        """+10 to every stat per tier above the first."""
        return TIER_BONUS * (self.tier - 1)

    @property
    def mastery_bonus(self):
        """+2% max HP and damage for every class mastered (lived to the level cap)."""
        return 1 + MASTERY_BONUS * len(self.mastered_classes())

    def gear_stat(self, stat):
        return sum(ITEMS[i]["stats"].get(stat, 0) for i in self.equipment.values() if i)

    def stat(self, stat):
        return self.base_stat(stat) + self.gear_stat(stat)

    def buff_mod(self, key):
        """Buffs of the same kind don't stack: for each bonus, the strongest active buff counts."""
        return max((e.get("mods", {}).get(key, 0) for e in self.effects if e["type"] == "buff"), default=0)

    @property
    def max_hp(self):
        per_level = max(CLASSES[c]["hp"] for c in self.lived_classes())
        hp = 10 + (per_level + 3) * self.level + self.stat("CON") * self.level * 0.2
        return int(hp * self.perk("hp_mult", 1.0) * self.mastery_bonus)

    @property
    def max_mana(self):
        mana = 15 + max(CLASSES[c]["mana"] for c in self.lived_classes()) * self.level + self.stat("WIS") * self.level * 0.1
        return int(mana * self.perk("mana_mult", 1.0))

    @property
    def armor(self):
        a = sum(ITEMS[i].get("armor", 0) for i in self.equipment.values() if i)
        return int(a + self.stat("DEX") / 10 + self.buff_mod("armor"))

    @property
    def crit_chance(self):
        return min(0.35, 0.05 + self.stat("DEX") / 1000 + self.perk("crit", 0))

    @property
    def dodge(self):
        base = min(0.25, 0.03 + self.stat("DEX") / 1500 + self.perk("dodge", 0))
        return min(0.6, base + self.buff_mod("dodge"))

    @property
    def miss_chance(self):
        """Chance that a weapon swing misses: DEX is precision for every class."""
        return max(MISS_FLOOR, MISS_BASE - self.stat("DEX") * MISS_PER_DEX)

    @property
    def damage_mult(self):
        return self.perk("dmg_mult", 1.0) * (1 + self.buff_mod("damage_pct")) * self.mastery_bonus

    def weapon_range(self, slot="weapon"):
        """STR powers weapon damage for every class. slot="shield" is the off-hand weapon."""
        w = self.equipment.get(slot)
        lo, hi = ITEMS[w]["dmg"] if w else (1, 3)
        bonus = self.stat("STR") * 0.35 + self.level * 0.5
        return int(lo + bonus), int(hi + bonus)

    def roll_weapon(self, mult=1.0, slot="weapon"):
        lo, hi = self.weapon_range(slot)
        return random.randint(lo, hi) * mult * self.damage_mult

    def offhand_weapon(self):
        """The weapon held in the off hand (the shield slot), if Dual Wield allows it."""
        iid, main = self.equipment.get("shield"), self.equipment.get("weapon")
        if iid and main and ITEMS[iid]["type"] == "weapon" and self.has_passive("dual_wield"):
            return iid
        return None

    def power(self, eff):
        """Raw magnitude for a scaling ability effect."""
        return eff["base"] + eff["lvl"] * self.level + eff["scale"] * self.magic_stat(eff["stat"])

    def magic_stat(self, stat):
        """A stat for ability scaling; "INT/WIS" (summons) takes the higher of the two."""
        return max(self.stat(s) for s in stat.split("/"))

    # ------------------------------------------------------------------ xp
    @property
    def xp_needed(self):
        return xp_for_level(self.level)

    def gain_xp(self, amount):
        """Add experience and handle level-ups. Returns a list of message lines."""
        msgs = []
        if self.level >= MAX_LEVEL:
            return msgs
        amount = int(amount * self.perk("xp_mult", 1.0))
        self.xp += amount
        xp_needed = xp_for_level(self.level)
        if xp_needed > 0:
            percent = amount / xp_needed * 100
            msgs.append(("You gain {} experience. ({:.1f}% of your level)".format(amount, percent), "bcyan"))
        else:
            msgs.append(("You gain {} experience.".format(amount), "bcyan"))
        while self.level < MAX_LEVEL and self.xp >= self.xp_needed:
            self.xp -= self.xp_needed
            msgs += self.level_up()
        if self.level >= MAX_LEVEL:
            self.xp = 0
        return msgs

    def level_up(self):
        before = {s: self.stat(s) for s in STATS}
        hp0, mana0 = self.max_hp, self.max_mana
        self.level += 1
        msgs = [("", None),
                ("*** You have reached level {}! ***".format(self.level), "byellow"),
                ]
        gains = ["{} +{}".format(s, self.stat(s) - before[s]) for s in STATS if self.stat(s) > before[s]]
        msgs.append(("Your training as a {} pays off: {}.".format(self.class_name, ", ".join(gains)), "yellow"))
        msgs.append(("Max HP +{}, Max Mana +{}.".format(self.max_hp - hp0, self.max_mana - mana0), "yellow"))
        self.hp, self.mana = self.max_hp, self.max_mana
        for pid, pa, lvl in self.known_passives():
            if lvl == self.level:
                msgs.append(("You have learned {}! {}".format(pa["name"], pa["desc"]), "bmagenta"))
        for ab in self.abilities_unlocked_at(self.level):
            tag = "spell" if ab["kind"] == "spell" else "ability"
            origin = "" if ab["cls"] == self.cls else " (remembered from a past life as a {})".format(
                CLASSES[ab["cls"]]["name"])
            msgs.append(("You have learned the {} {}!{}".format(tag, ab["name"], origin), "bmagenta"))
        if self.level == MAX_LEVEL and self.eternal:
            msgs.append(("Every path is walked, ten times over. You are {}, and your journey is complete.".format(
                self.display_name), "byellow"))
        elif self.level == MAX_LEVEL and self.can_ascend():
            msgs.append(("You have mastered every path. You may now REBIRTH into Tier {}.".format(self.tier + 1), "bmagenta"))
        elif self.level == MAX_LEVEL:
            msgs.append(("You have reached the pinnacle of mortal power. You may now REBIRTH.", "bmagenta"))
        return msgs

    # ------------------------------------------------------------------ abilities
    def lived_classes(self):
        return {self.cls} | {life["cls"] for life in self.past_lives}

    def known_abilities(self):
        """Every ability from the current and past classes, learned or not yet, sorted by level."""
        classes = self.lived_classes()
        abs_ = [a for a in ABILITIES.values() if a["cls"] in classes]
        return sorted(abs_, key=lambda a: (a["level"], a["cls"] != self.cls, a["name"]))

    def passive_level(self, pid):
        """The level this character learns a passive at (the lowest any lived class gives), or None."""
        levels = [lvl for c, lvl in PASSIVES[pid]["classes"].items() if c in self.lived_classes()]
        return min(levels) if levels else None

    def known_passives(self):
        """(id, passive, level learned) for every passive any lived class grants, learned or not yet."""
        return [(pid, pa, self.passive_level(pid)) for pid, pa in PASSIVES.items() if self.passive_level(pid)]

    def has_passive(self, pid):
        lvl = self.passive_level(pid)
        return lvl is not None and self.level >= lvl

    def usable_abilities(self):
        return [a for a in self.known_abilities() if a["level"] <= self.level]

    def abilities_unlocked_at(self, level):
        return [a for a in self.known_abilities() if a["level"] == level]

    def mana_cost(self, ab):
        return int(round(ab["cost"] * (1 + 0.1 * (self.level - 1))))

    # ------------------------------------------------------------------ effects
    def add_effect(self, eff):
        # refresh same-named effects instead of stacking them
        self.effects = [e for e in self.effects if e.get("name") != eff.get("name")]
        self.effects.append(eff)

    @property
    def invisible(self):
        return any(e["type"] == "invisible" for e in self.effects)

    def has_effect(self, etype):
        return any(e["type"] == etype for e in self.effects)

    def heal(self, amount):
        amount = max(0, int(amount))
        before = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        return self.hp - before

    def absorb(self, dmg):
        """Let shields soak damage. Returns remaining damage."""
        for e in self.effects:
            if e["type"] == "shield" and dmg > 0:
                soak = min(e["value"], dmg)
                e["value"] -= soak
                dmg -= soak
        self.effects = [e for e in self.effects if not (e["type"] == "shield" and e["value"] <= 0)]
        return dmg

    # ------------------------------------------------------------------ items
    def armor_tier(self):
        """Index into ARMOR_TIERS of the heaviest armor any of this character's lives could wear."""
        return max(ARMOR_TIERS.index(CLASSES[c]["armor"]) for c in self.lived_classes())

    def trained_for(self, iid):
        """Whether the current class or a past life could use this item (level aside). Returns (ok, why)."""
        it = ITEMS[iid]
        kind, lived = it["kind"], self.lived_classes()
        if kind in FREE_KINDS:
            return True, ""
        if it["type"] == "weapon":
            if any(kind in CLASSES[c]["weapons"] for c in lived):
                return True, ""
            return False, "You have no training with {} weapons.".format(
                "two-handed" if kind == "two-handed" else kind)
        if kind == "shield":
            if any(CLASSES[c]["shield"] for c in lived):
                return True, ""
            return False, "You have no training with shields."
        if ARMOR_TIERS.index(kind) <= self.armor_tier():
            return True, ""
        return False, "You have no training in {} armor.".format(kind)

    def can_equip(self, iid, offhand=False):
        it = ITEMS[iid]
        if it["type"] not in ("weapon", "armor"):
            return False, "You can't equip that."
        ok, why = self.trained_for(iid)
        if not ok:
            return False, why
        if it["level"] > self.level:
            return False, "You must be level {} to use {}.".format(it["level"], it["name"])
        if offhand:
            if it["type"] != "weapon":
                return False, "Only a weapon can be wielded in your off hand."
            if not self.has_passive("dual_wield"):
                return False, "You have not learned to wield two weapons."
            if it["kind"] not in DUAL_KINDS:
                return False, "{} is too unwieldy for your off hand.".format(it["name"][0].upper() + it["name"][1:])
            main = self.equipment.get("weapon")
            if not main or ITEMS[main]["kind"] not in DUAL_KINDS:
                return False, "You need a one-handed weapon in your main hand first."
        return True, ""

    def wants_offhand(self, iid):
        """Whether `wear` should put this weapon in the off hand: a one-hander, Dual Wield learned,
        a one-hander already in the main hand and nothing in the shield slot."""
        it, main = ITEMS[iid], self.equipment.get("weapon")
        return (it["type"] == "weapon" and it["kind"] in DUAL_KINDS and self.has_passive("dual_wield")
                and main is not None and ITEMS[main]["kind"] in DUAL_KINDS and not self.equipment.get("shield"))

    def slot_of(self, iid):
        """The slot an equipped item is in (a weapon may be in the shield slot), or None."""
        return next((s for s, v in self.equipment.items() if v == iid), None)

    def drop_untrained(self):
        """Move equipped items this character isn't trained for into the inventory (older saves).
        Returns the item ids moved."""
        moved = [(s, iid) for s, iid in self.equipment.items() if iid and not self.trained_for(iid)[0]]
        off = self.equipment.get("shield")
        if off and ITEMS[off]["type"] == "weapon" and not self.has_passive("dual_wield"):
            moved.append(("shield", off))
        for s, _ in moved:
            self.unequip(s)
        return [iid for _, iid in moved]

    def equip(self, iid, offhand=False):
        """Equip from the pack. Returns (ok, why) on failure, (True, [items moved to the pack])."""
        ok, why = self.can_equip(iid, offhand)
        if not ok:
            return False, why
        slot = "shield" if offhand else ITEMS[iid]["slot"]
        self.inventory.remove(iid)
        removed = []
        old = self.equipment.get(slot)
        if old:
            self.inventory.append(old)
            removed.append(old)
        self.equipment[slot] = iid
        # a two-handed, staff or bow main hand can't keep an off-hand weapon
        off = self.equipment.get("shield")
        if slot == "weapon" and ITEMS[iid]["kind"] not in DUAL_KINDS and off and ITEMS[off]["type"] == "weapon":
            removed.append(self.unequip("shield"))
        self.clamp()
        return True, removed

    def unequip(self, slot):
        iid = self.equipment.get(slot)
        if iid:
            self.equipment[slot] = None
            self.inventory.append(iid)
            self.clamp()
        return iid

    def clamp(self):
        self.hp = min(self.hp, self.max_hp)
        self.mana = min(self.mana, self.max_mana)

    # ------------------------------------------------------------------ rebirth
    def rebirth(self, new_cls):
        """Start a new life as `new_cls`. Once every class is mastered, it starts the next tier
        instead: past lives are forgotten (stats, mastery, abilities, training) and only the tier
        bonus remains. Gold, items, quests and boss kills always carry over."""
        if self.can_ascend():
            self.tier += 1
            self.past_lives = []
        else:
            self.past_lives.append({"cls": self.cls})
        self.cls = new_cls
        self.level = 1
        self.xp = 0
        self.effects = []
        self.pet = None
        # every piece of gear goes into the pack, and the new class starts in its own kit
        removed = [iid for iid in self.equipment.values() if iid]
        self.inventory += removed
        self.equipment = {s: None for s in SLOTS}
        given = self.wear_kit(new_cls)
        self.hp, self.mana = self.max_hp, self.max_mana
        return removed, given

    def wear_kit(self, cls):
        """Put on a class's starting gear; a second weapon goes in the off hand. Returns the item ids."""
        given = list(CLASSES[cls]["gear"])
        for iid in given:
            slot = ITEMS[iid]["slot"]
            self.equipment["shield" if slot == "weapon" and self.equipment.get("weapon") else slot] = iid
        return given

    # ------------------------------------------------------------------ persistence
    def to_dict(self):
        d = {k: v for k, v in self.__dict__.items() if k != "pet"}
        d["pet"] = self.pet.to_dict() if self.pet else None
        return d

    @classmethod
    def from_dict(cls, d):
        ch = cls.__new__(cls)
        ch.__dict__.update({k: v for k, v in d.items() if k != "pet"})
        ch.pet = Pet.from_dict(d["pet"]) if d.get("pet") else None
        for s in SLOTS:
            ch.equipment.setdefault(s, None)
        ch.__dict__.setdefault("aliases", {})  # saves from before aliases existed
        ch.__dict__.setdefault("boss_kills", [])
        ch.__dict__.setdefault("automap", False)
        ch.__dict__.setdefault("bank", [])
        ch.__dict__.setdefault("tier", 1)
        ch.__dict__.pop("cooldowns", None)  # saves from before cooldowns were removed
        ch.effects = [e for e in ch.effects if e["type"] != "stun"]
        return ch

    def mastered_classes(self):
        """Classes lived all the way to the level cap: every past life, plus this one if it is maxed."""
        done = {life["cls"] for life in self.past_lives}
        if self.level >= MAX_LEVEL:
            done.add(self.cls)
        return done

    def can_ascend(self):
        """Every class mastered in this tier, and a higher tier left to reach."""
        return self.tier < MAX_TIER and len(self.mastered_classes()) == len(CLASSES)
