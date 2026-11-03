# Shaman

> *Spirit-speakers of the tribes, who call down ancestral fury and healing.*

The Shaman is a sturdy WIS and INT caster in mail with a shield and a spirit wolf. It has the most HP
of any caster, a heal, a pet from level 8 (raised out of combat), a damage-and-armor buff that lasts
the whole fight, a poison that weakens, and Chain Lightning at 34. It is a forgiving, well-rounded
class.

## At a glance

| | |
|---|---|
| HP per level | 8 |
| Mana per level | 5 (plus WIS) |
| Spell stats | INT (damage); WIS (healing); pets use the higher of the two |
| Starting bonus | WIS +2, INT +1, CON +2 |
| Gains per level | WIS +2, INT +1, CON +1, STR +1 |
| Armor | Mail (and everything lighter) |
| Shield | Yes |
| Weapons | Blunt, staff, axe |
| Starting gear | Training mace (2-5), padded tunic, leather cap, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | WIS | CON | INT | STR | Weapon damage |
|---|---|---|---|---|---|---|---|
| 1 | 94 | 66 | 12 | 12 | 11 | 10 | 6-9 |
| 10 | 656 | 140 | 30 | 21 | 20 | 19 | 13-16 |
| 25 | 1883 | 335 | 60 | 36 | 35 | 34 | 26-29 |
| 50 | 4738 | 860 | 110 | 61 | 60 | 59 | 47-50 |

At level 50 a Shaman has more HP than a Paladin, thanks to its CON.

## Spells and abilities

All Shaman magic is spells, cast with `cast <name>`. There are no cooldowns: every attack can be used every round, and each new attack is a modest step up (12%) from the one before it, so **use your newest one**.

| Level | Name | Type | Cost | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Frost Shock** | spell | 5 / 30 | one foe | Frost damage 6 + 1.93/level + 0.56 INT (~14 at L1, ~73 at L25, ~136 at L50) |
| 3 | **Ancestral Mending** | spell | 7 / 35 | self | Heal 40.5 + 8.91/level + 2.23 WIS (~101 at L3, ~397 at L25, ~729 at L50) |
| 8 | **Spirit Wolf** | spell | 34 / 118 | self | Summon a spectral spirit wolf (~810 HP, 27-42 damage at L25); only out of combat, and it stays until it dies |
| 15 | **Spirit of the Bear** | spell | 36 / 88 | self | +12% damage, +6 armor + 0.9/level until the end of the fight |
| 24 | **Venom of the Serpent** | spell | 40 / 71 | one foe | Poison damage over time: 8 + 1.5/level + 0.4 INT per round for 5 rounds (~57 at L24, ~59 at L25, ~107 at L50 per round); the foe deals 15% less damage for the rest of the fight |
| 34 | **Chain Lightning** | spell | 22 / 30 | one foe | Lightning damage 6.72 + 2.16/level + 0.63 INT (~107 at L34, ~152 at L50) |

## How to play

**Before every fight.** Call your Spirit Wolf (from 8) if it is not with you: it can't be called in
combat.

**Every fight.** Spirit of the Bear (from 15) once, Venom of the Serpent (from 24) once to poison and
weaken the foe, then your newest attack spell every round: Frost Shock, Chain Lightning from 34. Heal
with Ancestral Mending when you drop under about half health.

**Tips**
- Your heal has no cooldown: mana is the only limit.
- The wolf draws about a quarter of the attacks aimed at you.

## Gear

Wear **mail** and a shield. WIS first (your heals, the wolf and your mana), then INT (Frost Shock,
Venom of the Serpent and Chain Lightning), then CON.

Notable late gear: the Sunforged Mace (43, blunt, STR/WIS), Flameheart (50, blunt), the dragonbone
staff and **the Dreamweaver's Staff** (staffs, giving up the shield), Dragonscale Mail (48, mail), the
Burial Mask of Ussreth (48, mail), **tidescale legguards** (50, mail legs, WIS/CON, from Nerevos), the
sunsteel mail set, the Shield of Judgement (50, CON/WIS), the
Pearl of the Deep (50, ring), and the mythic Fang of Pyraxis and Eternity.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a beetle-shell shield
(8, shield, CON) and an amber pendant (10, neck, WIS/CON). The Wasp Queen drops the amber pendant.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): the Heartspore staff (20,
staff), a capshell hauberk (17, mail chest), rootweave chausses (16, mail legs), a shelf-fungus shield
(14), a glowcap pendant (16, neck) and the rootbound ring (20, CON/WIS).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): a roustabout's
tent mallet (28, blunt), a roustabout's chain chausses (27, mail legs), a fortune teller's crystal ball
(28, off-hand) and the brass ring (27, ring).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): the Gavel of the High
Justice (38, blunt, STR/WIS), the Headsman's axe (32), a bailiff's hauberk (34, mail chest), the shield
of the scales (35, CON/WIS), the seal of office (37, ring) and the chain of office (38, neck).

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): Ithilmir's maulstick (42, staff, INT/WIS), painted moonsteel gauntlets (39, mail
hands, STR/DEX) and a gilt frame shield (39, shield, CON). Ithilmir drops his maulstick.

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): a clockwork pruning
axe (41, axe, STR/CON), Orrin's great wrench (44, blunt, STR/WIS/CON), the pendulum staff (44, staff,
INT/WIS), a brass gear-helm (43, mail head, CON/STR), a brass-scale hauberk (43, mail chest,
CON/DEX), a cog shield (43, shield, CON) and the orrery amulet (44, neck, INT/WIS/STR). Orrin
Gearwhistle drops his great wrench, the pendulum staff and the orrery amulet.

From **Thornwick Hall** (43-49, west of the Stag Walk): Mistress Hollin's cleaver (45, axe, STR/CON),
Mr. Graves's silver salver (45, shield), the Dowager's pearls (48, neck, WIS/CON) and silk evening
gloves (46, cloth, INT/WIS).

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): Madame
Marchpane's rolling pin (49, blunt, STR/WIS/CON), a candy-cane mace (47, blunt, STR/WIS), a gingerbread
shield (47, shield, CON/STR), gingerbread gauntlets (46, mail hands, STR/DEX), toffee-glazed greaves
(46, mail legs, CON/STR) and peppermint-scale boots (45, mail feet, CON/DEX). Madame Marchpane drops the
rolling pin; the rest come from her realm.

## Best races

- **High elf**: WIS 13 and +12% mana.
- **Human**: +5% HP, mana and damage.
- **Troll**: regenerates in combat; your CON makes up for its low WIS.

## How it performs

The Shaman wins every same-level fight in the simulator in 6.5-13.9 rounds, finishing with 59-79% HP. It survives about 5, 7 and 4 fights in a row at levels 10, 20 and 30. Against the world bosses it wins 70-100% at the boss's own level and every one at boss level +3. These figures are from November 2026, after monsters of level 50 and below got three times the HP and 40% of the damage and player HP was raised to match theirs.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Shaman life brings strong WIS growth, plus **mail armor and shield training** and blunt, staff and
axe weapons. Spirit Wolf gives any later class a pet, and Spirit of the Bear a whole-fight buff.
