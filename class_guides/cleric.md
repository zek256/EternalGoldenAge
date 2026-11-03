# Cleric

> *Priests of the light, unmatched healers who smite the wicked and the undead.*

The Cleric is a WIS caster in mail with a shield, with some INT for its holy damage. It has the best healing in the game: two direct
heals, a damage ward and a heal over time. Its damage comes from holy spells that ignore armor, and it
gets a strong group attack at 25 and one of the biggest single hits in the game at 45. It is slow to
kill early but almost never dies.

## At a glance

| | |
|---|---|
| HP per level | 7 |
| Mana per level | 10 (plus WIS) |
| Spell stats | INT (damage); WIS (healing, shields) |
| Starting bonus | WIS +3, INT +1, CON +1 |
| Gains per level | WIS +2, INT +1, CON +1, STR +1 |
| Armor | Mail (and everything lighter) |
| Shield | Yes |
| Weapons | Blunt, staff |
| Starting gear | Training mace (2-5), wooden shield, padded tunic, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | WIS | CON | INT | STR | Weapon damage |
|---|---|---|---|---|---|---|---|
| 1 | 22 | 26 | 13 | 11 | 11 | 10 | 6-9 |
| 10 | 150 | 146 | 31 | 20 | 20 | 19 | 13-16 |
| 25 | 435 | 417 | 61 | 35 | 35 | 34 | 26-29 |
| 50 | 1110 | 1070 | 111 | 60 | 60 | 59 | 47-50 |

## Spells

All Cleric magic is spells, cast with `cast <name>`. Cost is shown at the level you learn it and at
level 50.

| Level | Spell | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Minor Healing** | 6 / 35 | - | self | Heal 12 + 3.11/level + 0.6 WIS (~22 at L1, ~126 at L25, ~234 at L50) |
| 3 | **Smite** | 7 / 35 | - | one foe | Holy damage 8 + 1.6/level + 0.45 INT (~18 at L3, ~63 at L25, ~115 at L50) |
| 8 | **Divine Aegis** | 20 / 71 | 6 | self | A ward that absorbs 15 + 4.02/level + 1 WIS damage (~74 at L8, ~327 at L50) |
| 15 | **Greater Healing** | 43 / 106 | - | self | Heal 35 + 7.12/level + 1.1 WIS (~186 at L15, ~513 at L50) |
| 25 | **Holy Wrath** | 102 / 177 | 3 | all foes | Holy damage 20 + 2.5/level + 0.6 INT to every foe (~103 at L25, ~181 at L50) |
| 35 | **Resurgence** | 123 / 165 | 6 | self | Heal 15 + 2.56/level + 0.35 WIS every round for 5 rounds (~132-181 per round) |
| 45 | **Sunburst** | 324 / 354 | 5 | one foe | Holy damage 60 + 4.5/level + 1.3 INT (~334 at L45, ~363 at L50), 50% chance to stun for 1 round (25% vs bosses) |

## How to play

**Levels 1-14.** Smite is your attack from level 3 (before that, melee and Minor Healing). Cast Smite,
let mana recover with an auto-attack or two, and heal when you need it. Divine Aegis at 8 absorbs a
good chunk of damage: cast it at the start of every fight that matters, and again whenever it comes off
cooldown in a long one.

**Levels 15-34.** Greater Healing is a huge heal; use it instead of Minor Healing whenever you are well
down. Holy Wrath at 25 hits every foe for more than a Smite, every three rounds, and is your answer to
groups. A normal fight: Divine Aegis, then Smite or Holy Wrath, healing as needed.

**Levels 35-50.** Resurgence heals every round for five rounds; with Divine Aegis up, you can stand in
almost any fight. Sunburst at 45 is one of the strongest single hits in the game and can stun. Against
a boss: Divine Aegis, Resurgence, then Sunburst whenever it is ready and Smite in between, with Greater
Healing as your emergency button.

**Tips**
- All your damage is holy and ignores armor.
- Your melee is weak (you attack with STR but gain only 1 a level), so don't rely on auto-attacks.
- Your mana pool is one of the largest in the game. You can afford to heal often, but Sunburst and Holy
  Wrath are expensive; carry mana potions for bosses.

## Gear

Wear **mail** and a shield. WIS first (your heals, Divine Aegis and your mana), then INT (Smite, Holy Wrath and Sunburst), then
CON.

Notable late gear: the Sunforged Mace (43, blunt, STR/WIS), the dragonbone staff (47), **the
Dreamweaver's Staff** (50, staff, INT/WIS, from Somnara), the sunfire staff (40), Dragonscale Mail
(48, mail), the Burial Mask of Ussreth (48, mail), **tidescale legguards** (50, mail legs, WIS/CON, from
Nerevos), the sunsteel mail set, the Shield of Judgement (50,
CON/WIS), the Pearl of the Deep (50, ring, INT/WIS), the Ring of the Archmage, the amulet of the
obelisk, the sunlit codex (off-hand) and the mythic Fang of Pyraxis and Eternity. A staff means giving
up your shield.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a beetle-shell shield
(8, shield, CON) and an amber pendant (10, neck, WIS/CON). The Wasp Queen drops the amber pendant.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): the Heartspore staff (20,
staff, INT/WIS), a capshell hauberk (17, mail chest), rootweave chausses (16, mail legs), a
shelf-fungus shield (14), a glowcap pendant (16, neck) and the rootbound ring (20, CON/WIS).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): a roustabout's
tent mallet (28, blunt), a roustabout's chain chausses (27, mail legs), a fortune teller's crystal ball
(28, off-hand, INT/WIS) and the brass ring (27, ring).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): the Gavel of the High
Justice (38, blunt, STR/WIS), a bailiff's hauberk (34, mail chest), the shield of the scales (35,
CON/WIS), the seal of office (37, ring) and the chain of office (38, neck).

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): Ithilmir's maulstick (42, staff, INT/WIS), painted moonsteel gauntlets (39, mail
hands, STR/DEX) and a gilt frame shield (39, shield, CON). Ithilmir drops his maulstick.

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): Orrin's great wrench
(44, blunt, STR/WIS/CON), the pendulum staff (44, staff, INT/WIS), a brass gear-helm (43, mail head,
CON/STR), a brass-scale hauberk (43, mail chest, CON/DEX), a cog shield (43, shield, CON) and the orrery
amulet (44, neck, INT/WIS/STR). Orrin Gearwhistle drops his great wrench, the pendulum staff and the
orrery amulet.

From **Thornwick Hall** (43-49, west of the Stag Walk): Mr. Graves's silver salver (45, shield), the
Dowager's pearls (48, neck, WIS/CON), silk evening gloves (46, cloth, INT/WIS) and Tobias's
black grimoire (47, off-hand) if you would rather have INT and WIS than a shield.

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): Madame
Marchpane's rolling pin (49, blunt, STR/WIS/CON), a candy-cane mace (47, blunt, STR/WIS), a gingerbread
shield (47, shield, CON/STR), gingerbread gauntlets (46, mail hands, STR/DEX), toffee-glazed greaves
(46, mail legs, CON/STR) and peppermint-scale boots (45, mail feet, CON/DEX). Madame Marchpane drops the
rolling pin; the rest come from her realm.

## Best races

- **High elf**: WIS 13 and +12% mana.
- **Human**: +5% HP, mana and damage.
- **Troll**: regenerates in combat, though its WIS is low.

## How it performs

The Cleric wins every same-level fight in the simulator in 3-8 rounds and finishes with 72-99% HP. It
lasts about 3-4 fights in a row at level 10 and nearly 8 at level 30. It beat nearly every world boss
at the boss's own level (about 83% against the High Justice, 87% against Orrin Gearwhistle and 93%
against Seluvar and Ithilmir) and all of them at boss level +3.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Cleric life brings strong WIS growth (shared with the Druid and Shaman) and the best heals, plus **mail armor and shield training** and
blunt and staff weapons. Every later life heals like a Cleric: Divine Aegis, Greater Healing and
Resurgence scale with WIS, and you keep the Cleric's WIS, so they stay excellent heals in any class.
