"""Playable classes.

  hp          - hit points gained per level (before CON)
  mana        - mana gained per level (WIS adds to the pool for every class)
  start       - one-time stat bonus at character creation
  gains       - stats gained on every level up (49 level-ups from 1 to 50)
  armor       - heaviest armor tier worn (data.items.ARMOR_TIERS); lighter tiers are allowed too
  shield      - may use shields (mail and plate wearers)
  weapons     - weapon families wielded (data.items.WEAPON_KINDS)
  gear        - starting equipment (item ids); a second weapon goes in the off hand
Armor and weapon training carries over: a character may use anything any of its lives could.
STR powers weapon damage and DEX weapon accuracy for every class (see character.Character).
INT powers damage spells (damage, damage over time, drains) and WIS powers healing, shields and the
mana pool, for every class; summons take the higher of the two.
Stats, HP and mana per level take the best of every class a character has lived (Character.base_stat).
"""

STATS = ["STR", "DEX", "CON", "INT", "WIS"]

# Player HP units (the user's choice, 2026-11-03: players and ordinary monsters should have roughly the
# same HP). Player max HP, every heal, heal over time, shield, drain and lifesteal, potions, pet HP and
# all monster damage are multiplied by it together, so balance doesn't move. Percent-based healing
# (regen, sleep, heal_pct) already follows max HP and is not multiplied again.
HP_SCALE = 4.05  # 2.7 gave parity at ~7-round fights; x1.5 with WORLD_HP_MULT 3.0 keeps it at ~10

CLASSES = {
    "warrior": {
        "name": "Warrior", "hp": 13, "mana": 0,
        "start": {"STR": 3, "CON": 3},
        "gains": {"STR": 2, "CON": 2, "DEX": 1},
        "armor": "plate", "shield": True, "weapons": ["dagger", "sword", "axe", "blunt", "two-handed", "bow"],
        "gear": ["rusty_shortsword", "rusty_shortsword", "padded_tunic"],
        "desc": "Masters of blade and shield who stand in the front rank of every battle.",
    },
    "paladin": {
        "name": "Paladin", "hp": 10, "mana": 3,
        "start": {"STR": 2, "WIS": 1, "INT": 1, "CON": 1},
        "gains": {"STR": 2, "CON": 1, "WIS": 1, "INT": 1},
        "armor": "plate", "shield": True, "weapons": ["sword", "blunt", "two-handed"],
        "gear": ["training_mace", "wooden_shield", "padded_tunic"],
        "desc": "Holy knights sworn to the Dawnfather, wielding sacred light and steel alike.",
    },
    "dread knight": {
        "name": "Dread Knight", "hp": 10, "mana": 3,
        "start": {"STR": 2, "INT": 1, "WIS": 1, "CON": 1},
        "gains": {"STR": 2, "CON": 1, "INT": 1, "WIS": 1},
        "armor": "plate", "shield": True, "weapons": ["sword", "axe", "two-handed"],
        "gear": ["rusty_shortsword", "wooden_shield", "padded_tunic"],
        "desc": "Dark champions who bargain with death, draining the life of their foes.",
    },
    "ranger": {
        "name": "Ranger", "hp": 9, "mana": 2,
        "start": {"STR": 2, "DEX": 2, "WIS": 1},
        "gains": {"STR": 2, "DEX": 2, "CON": 1},
        "armor": "mail", "shield": True, "weapons": ["sword", "dagger", "axe", "bow"],
        "gear": ["ash_shortbow", "padded_tunic", "leather_boots"],
        "desc": "Wardens of the wild places, deadly with bow and blade and kin to beasts.",
    },
    "rogue": {
        "name": "Rogue", "hp": 8, "mana": 0,
        "start": {"STR": 2, "DEX": 2, "CON": 1},
        "gains": {"STR": 2, "DEX": 2, "CON": 1},
        "armor": "leather", "shield": False, "weapons": ["dagger", "sword", "bow"],
        "gear": ["worn_dagger", "padded_tunic", "leather_boots"],
        "desc": "Cutthroats and shadow-walkers who strike from the dark with poisoned steel.",
    },
    "bard": {
        "name": "Bard", "hp": 8, "mana": 9,
        "start": {"INT": 2, "WIS": 1, "STR": 1, "DEX": 1},
        "gains": {"INT": 1, "WIS": 1, "STR": 1, "DEX": 1, "CON": 1},
        "armor": "leather", "shield": False, "weapons": ["dagger", "sword", "blunt", "wand"],
        "gear": ["worn_dagger", "padded_tunic", "leather_cap"],
        "desc": "Wandering minstrels whose songs mend allies and shatter the minds of foes.",
    },
    "cleric": {
        "name": "Cleric", "hp": 7, "mana": 10,
        "start": {"WIS": 3, "INT": 1, "CON": 1},
        "gains": {"WIS": 2, "INT": 1, "CON": 1, "STR": 1},
        "armor": "mail", "shield": True, "weapons": ["blunt", "staff"],
        "gear": ["training_mace", "wooden_shield", "padded_tunic"],
        "desc": "Priests of the light, unmatched healers who smite the wicked and the undead.",
    },
    "druid": {
        "name": "Druid", "hp": 7, "mana": 5,
        "start": {"WIS": 3, "INT": 1, "CON": 1},
        "gains": {"WIS": 2, "INT": 1, "CON": 1, "DEX": 1},
        "armor": "leather", "shield": False, "weapons": ["staff", "blunt", "dagger"],
        "gear": ["oak_staff", "padded_tunic", "leather_boots"],
        "desc": "Keepers of the old groves who call upon root, thorn, moon and storm.",
    },
    "shaman": {
        "name": "Shaman", "hp": 8, "mana": 5,
        "start": {"WIS": 2, "INT": 1, "CON": 2},
        "gains": {"WIS": 2, "INT": 1, "CON": 1, "STR": 1},
        "armor": "mail", "shield": True, "weapons": ["blunt", "staff", "axe"],
        "gear": ["training_mace", "padded_tunic", "leather_cap"],
        "desc": "Spirit-speakers of the tribes, who call down ancestral fury and healing.",
    },
    "wizard": {
        "name": "Wizard", "hp": 5, "mana": 10,
        "start": {"INT": 4, "WIS": 1},
        "gains": {"INT": 3, "WIS": 1, "CON": 1},
        "armor": "cloth", "shield": False, "weapons": ["staff", "wand", "dagger"],
        "gear": ["oak_staff", "linen_robe", "apprentice_hood"],
        "desc": "Scholars of the arcane who bend fire, frost and lightning to their will.",
    },
    "necromancer": {
        "name": "Necromancer", "hp": 5, "mana": 12,
        "start": {"INT": 4, "CON": 1},
        "gains": {"INT": 3, "CON": 1, "WIS": 1},
        "armor": "cloth", "shield": False, "weapons": ["staff", "wand", "dagger"],
        "gear": ["oak_staff", "linen_robe", "apprentice_hood"],
        "desc": "Forbidden scholars of death who raise the fallen to fight at their side.",
    },
}

CLASS_ORDER = ["warrior", "cleric", "wizard", "bard", "necromancer", "shaman",
               "druid", "rogue", "ranger", "paladin", "dread knight"]
