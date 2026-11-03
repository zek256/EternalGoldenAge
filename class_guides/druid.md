# Druid

> *Keepers of the old groves who call upon root, thorn, moon and storm.*

The Druid is an INT and WIS caster in leather who mixes damage and healing. Its five attack spells
form an even ladder from Thornlash to Wrath of the Wild (which also heals it), Moonfire adds a
lingering burn, Regrowth heals now and for 10 rounds after, and Barkskin hardens it for the whole
fight. It is one of the fastest killers in the mid-levels and very steady overall.

## At a glance

| | |
|---|---|
| HP per level | 7 |
| Mana per level | 5 (plus WIS) |
| Spell stats | INT (damage); WIS (healing) |
| Starting bonus | WIS +3, INT +1, CON +1 |
| Gains per level | WIS +2, INT +1, CON +1, DEX +1 |
| Armor | Leather (and cloth) |
| Shield | No |
| Weapons | Staff, blunt, dagger |
| Starting gear | Oak staff (1-4), padded tunic, leather boots, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | WIS | CON | INT | DEX | Weapon damage |
|---|---|---|---|---|---|---|---|
| 1 | 22 | 21 | 14 | 11 | 12 | 10 | 5-8 |
| 10 | 150 | 97 | 32 | 20 | 21 | 19 | 9-12 |
| 25 | 435 | 295 | 62 | 35 | 36 | 34 | 17-20 |
| 50 | 1110 | 825 | 112 | 60 | 61 | 59 | 29-32 |

The Druid's INT powers its damage spells; its WIS powers its heals and its mana.

## Spells and abilities

All Druid magic is spells, cast with `cast <name>`. There are no cooldowns: every attack can be used every round, and each new attack is a modest step up (12%) from the one before it, so **use your newest one**.

| Level | Name | Type | Cost | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Thornlash** | spell | 5 / 30 | one foe | Nature damage 7 + 2.13/level + 0.64 INT (~16 at L1, ~83 at L25, ~152 at L50) |
| 3 | **Regrowth** | spell | 8 / 41 | self | Heal 10 + 2/level + 0.5 WIS (~25 at L3, ~91 at L25, ~166 at L50), then 3 + 0.7/level + 0.15 WIS per round for 10 rounds (~7 at L3, ~29 at L25, ~54 at L50 per round); casting it again restarts the timer |
| 8 | **Entangling Roots** | spell | 8 / 30 | one foe | Nature damage 7.84 + 2.39/level + 0.72 INT (~40 at L8, ~93 at L25, ~171 at L50) |
| 15 | **Moonfire** | spell | 12 / 30 | one foe | Arcane damage 8.78 + 2.67/level + 0.8 INT (~69 at L15, ~104 at L25, ~191 at L50); Arcane damage over time: 5 + 1/level + 0.25 INT per round for 4 rounds (~26 at L15, ~39 at L25, ~70 at L50 per round) |
| 22 | **Barkskin** | spell | 50 / 94 | self | +9 armor + 1.5/level until the end of the fight; then 3 + 0.5/level + 0.1 WIS per round for 10 rounds (~19 at L22, ~21 at L25, ~39 at L50 per round); casting it again restarts the timer |
| 32 | **Starfall** | spell | 20 / 30 | one foe | Arcane damage 9.83 + 2.99/level + 0.9 INT (~144 at L32, ~214 at L50) |
| 44 | **Wrath of the Wild** | spell | 26 / 30 | one foe | Nature drain 11.01 + 3.35/level + 1.01 INT (~213 at L44, ~240 at L50) that heals you for 20% of what it deals |

## How to play

**Every fight.** Barkskin (from 22) once, then your newest attack spell every round: Thornlash,
Entangling Roots from 8, Moonfire from 15, Starfall from 32, Wrath of the Wild from 44 (which heals you
for a fifth of what it deals). Cast Regrowth when you drop under about half health; its heal over
time runs for 10 rounds and recasting it restarts the timer.

**Tips**
- Your spells ignore armor.
- Mana is the only limit on your healing.

## Gear

Wear **leather**; no shields. INT first (all your damage spells), then WIS (Regrowth, Barkskin and your
mana), then CON.

Notable late gear: **the Dreamweaver's Staff** (50, staff, INT/WIS, from Somnara in the Plane of
Dreams), the dragonbone staff (47), the sunfire staff (40), the Sunforged Mace (43, blunt), drakehide
and windwalker boots (leather), the Death Mask (50, leather), **dreamsilk trousers** (50, cloth legs,
INT/WIS, from Somnara), the Pearl of the Deep (50, ring), the
Ring of the Archmage, and the mythic Fang of Pyraxis and Eternity.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): an acorn helm (6,
leather head, DEX), a beetle-shell jerkin (7, leather chest, DEX/CON), snailskin leggings (6, leather
legs, DEX), mole-claw gloves (9, leather hands, STR/DEX) and an amber pendant (10, neck, WIS/CON).
Grubbin the Mole King drops mole-claw gloves; the Wasp Queen drops the amber pendant.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): the Heartspore staff (20,
staff, INT/WIS) from the First Spore, mossfelt boots (15, leather), a glowcap pendant (16, neck), the
Mycelial Crown (20) and the rootbound ring (20, CON/WIS).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Ringmaster's
scarlet coat (30, leather chest), a fortune teller's crystal ball (28, off-hand, INT/WIS), a
roustabout's tent mallet (28, blunt), a pair of dancing slippers (27, cloth) and the brass ring (27,
ring).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): the Gavel of the High
Justice (38, blunt, STR/WIS), the seal of office (37, ring) and the chain of office (38, neck).

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): Ithilmir's maulstick (42, staff, INT/WIS), the Countess's kid gloves (39, leather
hands, DEX/INT) and a candle of still flame (38, off-hand, INT/WIS/CON). Ithilmir drops his maulstick;
Countess Isaura drops the Countess's kid gloves; the Memento Skull drops the candle of still flame.

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): Orrin's great wrench
(44, blunt, STR/WIS/CON), the pendulum staff (44, staff, INT/WIS), tinker's gloves (43, leather
hands, DEX/STR) and the orrery amulet (44, neck, INT/WIS/STR). Orrin Gearwhistle drops his great wrench,
the pendulum staff and the orrery amulet; the Clockwork Hostess drops tinker's gloves.

From **Thornwick Hall** (43-49, west of the Stag Walk): a gown of green brocade (47, cloth chest,
INT/WIS) from Lady Seraphine, silk evening gloves (46, cloth), Tobias's black grimoire (47,
off-hand), the Dowager's pearls (48, neck) and the Vane huntsman's jerkin (44, leather) if you want
armor over WIS.

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): Madame
Marchpane's rolling pin (49, blunt, STR/WIS/CON), a candy-cane mace (47, blunt, STR/WIS), a licorice
hood (46, leather head, DEX/CON) and taffy-grip gloves (46, leather hands, DEX/STR). Madame Marchpane
drops the rolling pin; the rest come from her realm.

## Best races

- **High elf**: WIS 13 and +12% mana.
- **Human**: +5% HP, mana and damage.
- **Elf**: +4% dodge and +2% crit, to cover your light armor.

## How it performs

The Druid wins every same-level fight in the simulator in 2.4-5.5 rounds, finishing with 62-84% HP. It survives about 5, 8 and 8 fights in a row at levels 10, 20 and 30 (the cap is 8). Against the world bosses it wins 60-100% at the boss's own level and 95-100% at boss level +3. These figures are from November 2026, after cooldowns were removed.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Druid life brings strong WIS growth (shared with the Cleric and Shaman), plus **leather** training
and staff, blunt and dagger weapons. It adds little in stats once you have a Cleric life, but Regrowth
and Barkskin are good tools in any later class.
