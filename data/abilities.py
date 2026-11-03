"""Spells and class abilities.

Every entry is learned automatically when its class reaches `level`. After a
rebirth, abilities of previous classes are kept but only become usable once the
current level reaches the level at which they were first learned.

There are no cooldowns, stuns or area attacks (the user's design). Mana is the only limit.

kind     - "spell" (costs mana, scales with level) or "ability" (free)
cost     - base mana cost; actual cost = cost * (1 + growth * (level - 1))
growth   - optional cost growth per level (default COST_GROWTH, 0.1). The wizard's attack spells use
           WIZARD_GROWTH (0.2): its large mana pool and short fights left it spending ~5% a fight at 25
target   - "enemy" or "self"

Each class's attacks form a ladder: every new one is STEP (12%) stronger than the one before it at
the same level and costs the same, so the newest is always the one to use (`rung` scales a formula
up the ladder). Buffs last until the end of the fight, shields until used up, heals and drains are
limited only by mana, and heals over time run on a timer that a new cast resets.

Effect power = base + lvl * character_level + scale * character_stat
INT scales damage, damage over time and drains; WIS scales heals, heals over time and shields.
Summons scale with "INT/WIS", the higher of the two, and can't be called in combat.
"""

COST_GROWTH = 0.1    # default spell cost growth per level
WIZARD_GROWTH = 0.2  # the wizard's attack ladder (the user's choice, 2026-11-03; 0.3 before fights got longer)
from data.classes import HP_SCALE

STEP = 1.12  # each rung of a class's attack ladder is this much stronger than the last


def rung(k, *formula):
    """A formula (base, lvl, scale) or a weapon multiplier raised k steps up the attack ladder."""
    vals = tuple(round(x * STEP ** k, 2) for x in formula)
    return vals if len(vals) > 1 else vals[0]


def DMG(base, lvl, scale, stat, element="arcane"):
    return {"type": "damage", "base": base, "lvl": lvl, "scale": scale, "stat": stat, "element": element}


def WEAPON(mult):
    return {"type": "weapon", "mult": mult}


def _hp(*vals):
    """Healing and shield formulas are written in old HP units and stored times HP_SCALE."""
    return tuple(round(v * HP_SCALE, 2) for v in vals)


def HEAL(base, lvl, scale, stat):
    base, lvl, scale = _hp(base, lvl, scale)
    return {"type": "heal", "base": base, "lvl": lvl, "scale": scale, "stat": stat}


def HOT(base, lvl, scale, stat, turns, name):
    base, lvl, scale = _hp(base, lvl, scale)
    return {"type": "hot", "base": base, "lvl": lvl, "scale": scale, "stat": stat, "turns": turns, "name": name}


def DOT(base, lvl, scale, stat, turns, name, element="poison"):
    return {"type": "dot", "base": base, "lvl": lvl, "scale": scale, "stat": stat,
            "turns": turns, "name": name, "element": element}


def DRAIN(base, lvl, scale, stat, frac, element="shadow"):
    """Heals frac of the damage dealt, in old HP units (so frac x HP_SCALE of it)."""
    return {"type": "drain", "base": base, "lvl": lvl, "scale": scale, "stat": stat,
            "frac": round(frac * HP_SCALE, 3), "element": element}


def SHIELD(base, lvl, scale, stat):
    base, lvl, scale = _hp(base, lvl, scale)
    return {"type": "shield", "base": base, "lvl": lvl, "scale": scale, "stat": stat}


def BUFF(name, **mods):
    """Lasts until the end of the fight. mods: damage_pct, armor (flat), armor_lvl (per level), dodge, lifesteal
    (written in old HP units: the share of weapon damage healed is lifesteal x HP_SCALE)."""
    if "lifesteal" in mods:
        mods["lifesteal"] = round(mods["lifesteal"] * HP_SCALE, 3)
    return {"type": "buff", "name": name, "mods": mods}


def WEAKEN(pct, name="Weakened"):
    """The foe deals pct less damage for the rest of the fight."""
    return {"type": "weaken", "pct": pct, "name": name}


def INVISIBLE(turns):
    """Aggressive monsters don't see you (bosses do) for `turns` ticks; casting or fighting ends it."""
    return {"type": "invisible", "name": "Invisibility", "turns": turns}


def SUMMON(name, hp_base, hp_lvl, dmg_base, dmg_lvl, scale_stat, desc):
    return {"type": "summon", "name": name, "hp_base": hp_base, "hp_lvl": hp_lvl,
            "dmg_base": dmg_base, "dmg_lvl": dmg_lvl, "stat": scale_stat, "desc": desc}


ABILITIES = {}


def _add(aid, name, cls, level, kind, effects, cost=0, target="enemy", desc="", msg="", growth=COST_GROWTH):
    ABILITIES[aid] = {
        "id": aid, "name": name, "cls": cls, "level": level, "kind": kind, "cost": cost, "growth": growth,
        "target": target, "effects": effects, "desc": desc, "msg": msg,
    }


def spell(aid, name, cls, level, cost, effects, **kw):
    _add(aid, name, cls, level, "spell", effects, cost=cost, **kw)


def ability(aid, name, cls, level, effects, **kw):
    _add(aid, name, cls, level, "ability", effects, **kw)


# ---------------------------------------------------------------- Warrior
# The warrior is an auto-attack class: Dual Wield and Double Attack (PASSIVES below), no abilities.

# ---------------------------------------------------------------- Cleric
HOLY = (8, 2.13, 0.6)  # Smite, the first rung of the cleric's ladder
spell("minor_healing", "Minor Healing", "cleric", 1, 6, [HEAL(12, 3.11, 0.6, "WIS")], target="self",
      desc="A gentle prayer that mends wounds.", msg="Soft golden light knits your wounds closed.")
spell("smite", "Smite", "cleric", 3, 6, [DMG(*rung(0, *HOLY), "INT", "holy")],
      desc="Call down a lance of holy light upon a foe.", msg="A shaft of searing radiance strikes {t}!")
spell("divine_aegis", "Divine Aegis", "cleric", 8, 18, [SHIELD(15, 4.02, 1.0, "WIS")], target="self",
      desc="A shimmering ward that absorbs damage until it breaks.", msg="A dome of pale gold light surrounds you.")
spell("greater_healing", "Greater Healing", "cleric", 15, 18, [HEAL(35, 7.12, 1.1, "WIS")], target="self",
      desc="A powerful prayer of restoration.", msg="The Dawnfather's warmth floods through your body.")
spell("holy_wrath", "Holy Wrath", "cleric", 25, 6, [DMG(*rung(1, *HOLY), "INT", "holy")],
      desc="Holy fire bursts from the ground beneath a foe.", msg="A pillar of holy fire erupts beneath {t}!")
spell("resurgence", "Resurgence", "cleric", 35, 28, [HOT(8, 1.3, 0.18, "WIS", 10, "Resurgence")], target="self",
      desc="Steady divine renewal over 10 rounds.", msg="A radiant halo settles upon your brow.")
spell("sunburst", "Sunburst", "cleric", 45, 6, [DMG(*rung(2, *HOLY), "INT", "holy")],
      desc="Call down the noonday sun upon a single foe.", msg="The sky splits and the noonday sun descends upon {t}!")

# ---------------------------------------------------------------- Wizard
ARCANE = (6, 2.0, 0.6)  # Magic Missile, the first rung
spell("magic_missile", "Magic Missile", "wizard", 1, 5, [DMG(*rung(0, *ARCANE), "INT", "arcane")],
      growth=WIZARD_GROWTH, desc="Darts of pure force that never miss.", msg="Three darts of violet force streak toward {t}!")
spell("frost_bolt", "Frost Bolt", "wizard", 5, 5, [DMG(*rung(1, *ARCANE), "INT", "frost")],
      growth=WIZARD_GROWTH, desc="A shard of ice hurled at a foe.", msg="A jagged shard of ice hurtles at {t}!")
spell("fireball", "Fireball", "wizard", 16, 5, [DMG(*rung(2, *ARCANE), "INT", "fire")],
      growth=WIZARD_GROWTH, desc="A roaring ball of fire hurled at a foe.", msg="A roaring ball of fire bursts against {t}!")
spell("invisibility", "Invisibility", "wizard", 20, 20, [INVISIBLE(75)], target="self",
      desc="Vanish from sight for 5 minutes: aggressive monsters ignore you (bosses see through it). "
           "Casting any spell or starting a fight ends it.",
      msg="You trace a sigil in the air and fade from sight.")
spell("lightning_lance", "Lightning Lance", "wizard", 26, 5, [DMG(*rung(3, *ARCANE), "INT", "lightning")],
      growth=WIZARD_GROWTH, desc="A crackling spear of lightning.", msg="Thunder booms as a lance of lightning impales {t}!")
spell("meteor", "Meteor", "wizard", 40, 5, [DMG(*rung(4, *ARCANE), "INT", "fire")],
      growth=WIZARD_GROWTH, desc="Call a blazing star down from the heavens upon a foe.", msg="The heavens burn as a meteor crashes down upon {t}!")

# ---------------------------------------------------------------- Necromancer
SHADOW = (6, 1.86, 0.53)  # Lifetap, the first rung
spell("lifetap", "Lifetap", "necromancer", 1, 5, [DRAIN(*rung(0, *SHADOW), "INT", 0.25)],
      desc="Steal life from a foe to mend your own.", msg="Ghostly tendrils draw the life from {t}.")
spell("raise_skeleton", "Raise Skeleton", "necromancer", 4, 18,
      [SUMMON("a rattling skeleton", 20, 6, 2, 1.3, "INT/WIS", "A clattering skeleton with empty, burning eyes.")],
      target="self",
      desc="Raise a skeletal servant to fight for you (not in combat).", msg="Bones claw their way up from the earth and assemble!")
spell("plague", "Plague", "necromancer", 10, 12, [DOT(5, 1.1, 0.25, "INT", 5, "Plague", "disease")],
      desc="Infect a foe with a wasting disease.", msg="A sickly green miasma seeps into {t}.")
spell("bone_spear", "Bone Spear", "necromancer", 18, 5, [DMG(*rung(1, *SHADOW), "INT", "shadow")],
      desc="Hurl a spear of sharpened bone.", msg="A spear of jagged bone erupts from your palm toward {t}!")
spell("siphon_soul", "Siphon Soul", "necromancer", 28, 5, [DRAIN(*rung(2, *SHADOW), "INT", 0.25)],
      desc="Tear out a fragment of a foe's soul and devour it.", msg="You reach into {t} and tear free a shrieking wisp of soul!")
spell("bone_colossus", "Raise Bone Colossus", "necromancer", 38, 55,
      [SUMMON("a towering bone colossus", 60, 14, 6, 2.6, "INT/WIS", "A hulking giant of fused bones, ten feet tall.")],
      target="self",
      desc="Raise a towering colossus of fused bone (not in combat).", msg="The ground heaves as a colossus of bone rises screaming from the earth!")
spell("wail_of_the_damned", "Wail of the Damned", "necromancer", 46, 5,
      [DMG(*rung(3, *SHADOW), "INT", "shadow"), WEAKEN(0.2, "Terrified")],
      desc="Unleash the screams of the dead upon a foe, harming and terrifying it.", msg="The howls of a thousand damned souls burst from your throat at {t}!")

# ---------------------------------------------------------------- Shaman
SPIRIT = (6, 1.93, 0.56)  # Frost Shock, the first rung
spell("frost_shock", "Frost Shock", "shaman", 1, 5, [DMG(*rung(0, *SPIRIT), "INT", "frost")],
      desc="A biting blast of spirit-frost.", msg="Spirit-frost crackles across {t}!")
spell("ancestral_mending", "Ancestral Mending", "shaman", 3, 6, [HEAL(10, 2.2, 0.55, "WIS")], target="self",
      desc="Your ancestors mend your wounds.", msg="Whispering ancestors lay spectral hands upon you.")
spell("spirit_wolf", "Spirit Wolf", "shaman", 8, 20,
      [SUMMON("a spectral spirit wolf", 20, 6, 3, 1.3, "INT/WIS", "A translucent blue wolf with eyes like stars.")],
      target="self",
      desc="Summon a wolf from the spirit world (not in combat).", msg="A ghostly howl answers your call, and a spirit wolf bounds to your side!")
spell("spirit_of_the_bear", "Spirit of the Bear", "shaman", 15, 15,
      [BUFF("Spirit of the Bear", damage_pct=0.12, armor=6, armor_lvl=0.9)], target="self",
      desc="The great bear's strength fills you for the fight (+12% damage, +armor).", msg="The great Bear-Spirit's strength swells within you.")
spell("serpent_venom", "Venom of the Serpent", "shaman", 24, 12,
      [DOT(8, 1.5, 0.4, "INT", 5, "Serpent Venom", "poison"), WEAKEN(0.15, "Envenomed")],
      desc="Spirit-venom that poisons a foe and weakens it for the fight.", msg="A spectral serpent sinks its fangs into {t}!")
spell("chain_lightning", "Chain Lightning", "shaman", 34, 5, [DMG(*rung(1, *SPIRIT), "INT", "lightning")],
      desc="Lightning that strikes a foe again and again.", msg="Lightning arcs from your totem and strikes {t} again and again!")

# ---------------------------------------------------------------- Druid
NATURE = (7, 2.13, 0.64)  # Thornlash, the first rung
spell("thornlash", "Thornlash", "druid", 1, 5, [DMG(*rung(0, *NATURE), "INT", "nature")],
      desc="A whip of thorny vines lashes a foe.", msg="Thorny vines burst from the earth and lash {t}!")
spell("regrowth", "Regrowth", "druid", 3, 7, [HEAL(10, 2.0, 0.5, "WIS"), HOT(3, 0.7, 0.15, "WIS", 10, "Regrowth")], target="self",
      desc="An instant heal followed by steady renewal for 10 rounds.", msg="Green leaves unfurl across your skin, healing as they grow.")
spell("entangling_roots", "Entangling Roots", "druid", 8, 5, [DMG(*rung(1, *NATURE), "INT", "nature")],
      desc="Gnarled roots seize a foe and crush it.", msg="Gnarled roots erupt and coil around {t}, crushing tight!")
spell("moonfire", "Moonfire", "druid", 15, 5,
      [DMG(*rung(2, *NATURE), "INT", "arcane"), DOT(5, 1.0, 0.25, "INT", 4, "Moonfire", "arcane")],
      desc="Silver moonlight burns a foe and lingers.", msg="A column of silver moonfire engulfs {t}!")
spell("barkskin", "Barkskin", "druid", 22, 16, [BUFF("Barkskin", armor=9, armor_lvl=1.5), HOT(3, 0.5, 0.1, "WIS", 10, "Barkskin")],
      target="self",
      desc="Your skin hardens into living oak for the fight (+armor, slow healing).", msg="Your skin cracks and hardens into living oak bark.")
spell("starfall", "Starfall", "druid", 32, 5, [DMG(*rung(3, *NATURE), "INT", "arcane")],
      desc="Stars rain from the sky upon a foe.", msg="Shards of starlight rain down upon {t}!")
spell("wrath_of_the_wild", "Wrath of the Wild", "druid", 44, 5, [DRAIN(*rung(4, *NATURE), "INT", 0.2, "nature")],
      desc="The whole forest rises against a foe, and its strength flows into you.", msg="The forest itself rises in fury against {t}!")

# ---------------------------------------------------------------- Rogue
BLADE = 1.5  # Backstab, the first rung
ability("backstab", "Backstab", "rogue", 1, [WEAPON(rung(0, BLADE))],
        desc="Slip behind your foe and drive your blade home.", msg="You slip into {t}'s blind spot and strike!")
ability("poisoned_blade", "Poisoned Blade", "rogue", 5, [WEAPON(1.0), DOT(4, 0.9, 0.2, "STR", 4, "Deadly Poison", "poison")],
        desc="A strike with a venom-coated blade.", msg="Your venom-slick blade bites into {t}.")
ability("evasion", "Evasion", "rogue", 10, [BUFF("Evasion", dodge=0.15)], target="self",
        desc="Become harder to hit for the fight (+15% dodge).", msg="You become a blur of motion.")
ability("kidney_shot", "Kidney Shot", "rogue", 18, [WEAPON(rung(1, BLADE))],
        desc="A brutal blow to a foe's kidney.", msg="You drive a brutal blow into {t}'s kidney!")
ability("eviscerate", "Eviscerate", "rogue", 28, [WEAPON(rung(2, BLADE))],
        desc="A vicious gutting strike.", msg="Your blades flash in a vicious, gutting strike against {t}!")
ability("shadow_dance", "Shadow Dance", "rogue", 40, [BUFF("Shadow Dance", damage_pct=0.2, dodge=0.1)], target="self",
        desc="Melt into the shadows for the fight: +20% damage and +10% dodge.", msg="The shadows embrace you like an old friend.")
ability("assassinate", "Assassinate", "rogue", 48, [WEAPON(rung(3, BLADE))],
        desc="A single perfect, lethal strike.", msg="Time seems to stop as you find the perfect opening in {t}'s guard...")

# ---------------------------------------------------------------- Ranger
ARROW = 1.45  # Aimed Shot, the first rung
ability("aimed_shot", "Aimed Shot", "ranger", 1, [WEAPON(rung(0, ARROW))],
        desc="A carefully aimed strike at a vital spot.", msg="You draw a slow breath, take aim at {t}, and loose!")
spell("hunters_mend", "Hunter's Mend", "ranger", 4, 6, [HEAL(9, 2.0, 0.45, "WIS")], target="self",
      desc="Woodland lore and a whispered prayer mend your wounds.", msg="You murmur an old woodland prayer and your wounds close.")
ability("multishot", "Multishot", "ranger", 10, [WEAPON(rung(1, ARROW))],
        desc="A quick volley of arrows into a single foe.", msg="You loose a fan of arrows into {t}!")
spell("bonded_wolf", "Call Bonded Wolf", "ranger", 16, 20,
      [SUMMON("a grey timber wolf", 25, 7, 3, 1.5, "INT/WIS", "A loyal grey wolf, scarred and keen-eyed.")],
      target="self",
      desc="Call your loyal animal companion to your side (not in combat).", msg="You whistle sharply, and a grey wolf lopes out of the brush to your side.")
ability("serpent_sting", "Serpent Sting", "ranger", 24, [WEAPON(1.0), DOT(8, 1.4, 0.3, "STR", 5, "Serpent Sting", "poison")],
        desc="A venomed arrow that poisons for 5 rounds.", msg="A green-fletched arrow strikes {t}, its venom spreading.")
ability("rain_of_arrows", "Rain of Arrows", "ranger", 34, [WEAPON(rung(2, ARROW))],
        desc="Arrow after arrow, loosed at a single foe.", msg="Your arrows rain down upon {t}!")
ability("deadeye", "Deadeye", "ranger", 45, [WEAPON(rung(3, ARROW))],
        desc="A legendary shot that finds the heart.", msg="The world narrows to a single point on {t}. You release.")

# ---------------------------------------------------------------- Paladin
SMITE_W, SMITE_D = 1.2, (3, 1.0, 0.3)  # Holy Strike, the first rung: a weapon blow plus holy damage
ability("holy_strike", "Holy Strike", "paladin", 1, [WEAPON(rung(0, SMITE_W)), DMG(*rung(0, *SMITE_D), "INT", "holy")],
        desc="A weapon strike wreathed in holy light.", msg="Your weapon blazes with holy light as you strike {t}!")
spell("holy_light", "Holy Light", "paladin", 5, 8, [HEAL(12, 2.8, 0.55, "WIS")], target="self",
      desc="The Dawnfather's light mends your wounds.", msg="Warm golden light pours down upon you and closes your wounds.")
spell("blessing_of_might", "Blessing of Might", "paladin", 10, 10, [BUFF("Blessing of Might", damage_pct=0.2)], target="self",
      desc="The Dawnfather blesses your arm for the fight (+20% damage).", msg="Golden light blesses your sword-arm.")
spell("divine_shield", "Divine Shield", "paladin", 18, 24, [SHIELD(20, 4, 1.0, "WIS")], target="self",
      desc="A ward of faith that absorbs damage until it breaks.", msg="A radiant shield of faith flares into being around you.")
ability("hammer_of_justice", "Hammer of Justice", "paladin", 26,
        [WEAPON(rung(1, SMITE_W)), DMG(*rung(1, *SMITE_D), "INT", "holy")],
        desc="A hammer-blow of divine judgment.", msg="A spectral hammer of light descends with your blow upon {t}!")
ability("consecration", "Consecration", "paladin", 36,
        [WEAPON(rung(2, SMITE_W)), DMG(*rung(2, *SMITE_D), "INT", "holy")],
        desc="A blow that hallows the ground beneath a foe and burns it.", msg="The ground beneath {t} blazes with consecrated light as you strike!")

# ---------------------------------------------------------------- Dread Knight
REAP_W, REAP_D = 1.2, (3, 1.0, 0.3)  # Shadow Strike, the first rung: a weapon blow plus a drain
DK_STRIKE = 3  # base mana cost of the strike ladder (every dread knight ability costs mana: the user's choice, 2026-11-03)
spell("shadow_strike", "Shadow Strike", "dread knight", 1, DK_STRIKE,
      [WEAPON(rung(0, REAP_W)), DRAIN(*rung(0, *REAP_D), "INT", 0.5)],
      desc="A strike that drinks a sip of your foe's life.", msg="Your blade, wreathed in shadow, drinks from {t}!")
spell("disease_cloud", "Disease Cloud", "dread knight", 4, 6, [DOT(4, 1.0, 0.25, "INT", 5, "Disease Cloud", "disease")],
      desc="A cloud of festering disease.", msg="A cloud of festering spores billows around {t}.")
spell("dread_aura", "Dread Aura", "dread knight", 10, 12, [WEAKEN(0.2, "Dread")],
      desc="Your aura of terror weakens a foe for the fight (-20% damage).", msg="An aura of soul-chilling dread pours from you over {t}.")
spell("dread_touch", "Dread Touch", "dread knight", 18, DK_STRIKE,
      [WEAPON(rung(1, REAP_W)), DRAIN(*rung(1, *REAP_D), "INT", 0.5)],
      desc="Channel death itself through your blade.", msg="You lay your blade upon {t} and death itself flows through it!")
spell("vampiric_embrace", "Vampiric Embrace", "dread knight", 26, 24, [BUFF("Vampiric Embrace", lifesteal=0.15)], target="self",
      desc="Your weapon hits heal you for {}% of the damage they deal, for the fight.".format(int(15 * HP_SCALE)), msg="Your veins run black with a vampiric hunger.")
spell("death_coil", "Death Coil", "dread knight", 34, DK_STRIKE,
      [WEAPON(rung(2, REAP_W)), DRAIN(*rung(2, *REAP_D), "INT", 0.5)],
      desc="A blow wrapped in a coil of death.", msg="A shrieking coil of black fire lashes {t} with your blow!")
spell("unholy_frenzy", "Unholy Frenzy", "dread knight", 44, 30, [BUFF("Unholy Frenzy", damage_pct=0.2, lifesteal=0.1)], target="self",
      desc="An unholy frenzy for the fight: +20% damage and {}% lifesteal.".format(int(10 * HP_SCALE)), msg="An unholy frenzy seizes you, and you laugh with a voice not your own!")

# ---------------------------------------------------------------- Bard
SONG = (10, 3.22, 0.8)  # Discordant Note, the first rung
spell("discordant_note", "Discordant Note", "bard", 1, 5, [DMG(*rung(0, *SONG), "INT", "sonic")],
      desc="A jarring note that rattles a foe's skull.", msg="You strike a jarring, discordant note at {t}!")
spell("ballad_of_mending", "Ballad of Mending", "bard", 3, 7, [HEAL(5, 1.26, 0.25, "WIS"), HOT(3, 0.75, 0.13, "WIS", 10, "Ballad of Mending")], target="self",
      desc="A soothing ballad that heals now and over 10 rounds.", msg="You hum a soothing ballad and your wounds begin to close.")
spell("war_march", "War March", "bard", 15, 15, [BUFF("War March", damage_pct=0.2, armor=6, armor_lvl=0.8)], target="self",
      desc="A rousing march for the fight (+20% damage, +armor).", msg="You strike up a rousing war march!")
spell("dirge_of_despair", "Dirge of Despair", "bard", 24, 12, [DOT(9, 2.01, 0.4, "INT", 4, "Dirge", "sonic"), WEAKEN(0.2, "Despair")],
      desc="A mournful dirge that hurts a foe over time and saps its will for the fight.", msg="You sing a dirge of such sorrow that {t} falters.")
spell("crescendo", "Crescendo", "bard", 34, 5, [DMG(*rung(1, *SONG), "INT", "sonic")],
      desc="A shattering crescendo of sound.", msg="Your song swells to a shattering crescendo against {t}!")
spell("legends_anthem", "Legend's Anthem", "bard", 44, 30,
      [BUFF("Legend's Anthem", damage_pct=0.15), HOT(10, 1.2, 0.2, "WIS", 10, "Legend's Anthem")], target="self",
      desc="The anthem of legends: +15% damage for the fight and strong healing for 10 rounds.", msg="You sing the Anthem of Legends, and the air itself trembles!")


# ---------------------------------------------------------------- Passives
# Always on once learned: no command. Like abilities they are kept through rebirth.
# `classes` maps each class that teaches one to the level it is learned at; a character learns it at
# the lowest level any of its lived classes gives, so the order of lives never matters.
# Combat.swing reads them through Character.has_passive.
OFFHAND_MULT = 0.65  # off-hand swings deal this share of a normal hit

PASSIVES = {
    "dual_wield": {
        "name": "Dual Wield", "classes": {"warrior": 1, "rogue": 10, "bard": 10},
        "desc": "Wield a one-handed weapon in your off hand (the shield slot); it strikes beside your main "
                "hand every round for {}% damage.".format(int(OFFHAND_MULT * 100)),
    },
    "double_attack": {
        "name": "Double Attack", "classes": {"warrior": 10, "rogue": 15, "ranger": 15, "paladin": 15, "dread knight": 15},
        "desc": "Each hand may strike a second time every round: a 40% chance when learned, rising evenly "
                "to certain at level 50.",
    },
}


def double_attack_chance(level, learned):
    """Chance for each hand to strike again in a round, Double Attack having been learned at `learned`."""
    return min(1.0, 0.4 + 0.6 * (level - learned) / max(1, 50 - learned))
