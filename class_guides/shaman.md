# Shaman

> *Spirit-speakers of the tribes, who call down ancestral fury and healing.*

The Shaman is a sturdy WIS and INT caster in mail with a shield and a spirit wolf. It has the most HP of any
caster, a heal, a pet from level 8, a damage-and-armor buff, a poison that weakens, chain lightning for
groups, and a late-game heal-and-damage avatar. It is a forgiving, well-rounded class.

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
| 1 | 23 | 21 | 12 | 12 | 11 | 10 | 6-9 |
| 10 | 162 | 95 | 30 | 21 | 20 | 19 | 13-16 |
| 25 | 465 | 290 | 60 | 36 | 35 | 34 | 26-29 |
| 50 | 1170 | 815 | 110 | 61 | 60 | 59 | 47-50 |

At level 50 a Shaman has more HP than a Paladin, thanks to its CON.

## Spells

All Shaman magic is spells, cast with `cast <name>`. Cost is shown at the level you learn it and at
level 50.

| Level | Spell | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Frost Shock** | 5 / 30 | - | one foe | Frost damage 6 + 1.45/level + 0.42 INT (~12 at L1, ~56 at L25, ~103 at L50) |
| 3 | **Ancestral Mending** | 7 / 35 | - | self | Heal 10 + 2.2/level + 0.55 WIS (~25 at L3, ~98 at L25, ~180 at L50) |
| 8 | **Spirit Wolf** | 34 / 118 | 10 | self | Summon a spirit wolf (~81 HP, 11-18 damage at L8; ~200 HP, 27-42 at L25; ~375 HP, 50-77 at L50) |
| 15 | **Spirit of the Bear** | 36 / 88 | 10 | self | +20% damage and +10 + 1.5/level armor for 6 rounds |
| 24 | **Venom of the Serpent** | 79 / 142 | - | one foe | Poison 8 + 1.5/level + 0.4 INT per round for 5 rounds (~57 at L24, ~107 at L50), and the foe deals 20% less damage for 4 rounds |
| 34 | **Chain Lightning** | 206 / 283 | 3 | all foes | Lightning damage 35 + 3/level + 0.9 INT to every foe (~176 at L34, ~239 at L50) |
| 44 | **Ancestral Avatar** | 292 / 324 | 12 | self | Heal 45% of your max HP and +40% damage for 5 rounds |

## How to play

**Levels 1-7.** Frost Shock and Ancestral Mending. Shamans start slow but are hard to kill.

**Levels 8-23.** Call the Spirit Wolf before every outing. It attacks every round and takes about a
quarter of the enemies' normal attacks. Its stats are fixed when summoned, so call it again every few
levels, and recall it when it dies. Spirit of the Bear at 15 is a cheap buff; keep it up in real
fights.

**Levels 24-50.** Venom of the Serpent is a strong poison that also weakens its target. Put it on
the most dangerous foe, then Frost Shock. Chain Lightning at 34 handles groups. At 44, Ancestral
Avatar is a 45% heal and a damage boost in one: your emergency button and your boss opener. Against a
boss: wolf, Spirit of the Bear, Venom, Frost Shock, with Ancestral Mending and Ancestral Avatar to
heal.

**Tips**
- Your spells ignore armor; your wolf's bites don't.
- Venom of the Serpent stacks a weaken on top of the poison, which makes it worth casting even on
  foes that will die soon if they hit hard.
- You are the tankiest caster, so you can afford to melee a little while your mana refills.

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

The Shaman wins every same-level fight in the simulator in about 3-5 rounds with 73-88% HP left. It
lasts about 4 fights in a row at level 10 and 6 at level 30. It beat nearly every world boss
at the boss's own level (about 97% against Orrin Gearwhistle and Ussreth) and all of them at boss
level +3.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Shaman life brings strong WIS growth, plus **mail armor and shield training** and blunt, staff and axe weapons. Spirit Wolf
gives any later class a pet, and Ancestral Avatar a 45% heal.
