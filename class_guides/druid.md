# Druid

> *Keepers of the old groves who call upon root, thorn, moon and storm.*

The Druid is an INT and WIS caster in leather who mixes damage, healing and control. It has a cheap nuke from
level 1, a heal that keeps working after you cast it, roots that can hold a foe for two rounds, a moon
spell that burns and lingers, and a group attack from 32. It is one of the fastest killers in the
mid-levels and very steady overall.

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

## Spells

All Druid magic is spells, cast with `cast <name>`. Cost is shown at the level you learn it and at
level 50.

| Level | Spell | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Thornlash** | 5 / 30 | - | one foe | Nature damage 7 + 1.6/level + 0.48 INT (~14 at L1, ~64 at L25, ~116 at L50) |
| 3 | **Regrowth** | 8 / 41 | - | self | Heal 10 + 2/level + 0.5 WIS now, then 4 + 1.2/level + 0.25 WIS per round for 5 rounds (~91 + 49/round at L25) |
| 8 | **Entangling Roots** | 17 / 59 | 4 | one foe | Small nature damage, and a 75% chance to hold it for 2 rounds (about 38% vs bosses) |
| 15 | **Moonfire** | 43 / 106 | - | one foe | Arcane damage 16 + 2.4/level + 0.7 INT (~70 at L15, ~178 at L50), then 5 + 1/level + 0.25 INT per round for 4 rounds |
| 22 | **Barkskin** | 50 / 94 | 10 | self | +15 + 2.5/level armor for 6 rounds (+70 at L22, +140 at L50), and a small heal every round |
| 32 | **Starfall** | 184 / 266 | 3 | all foes | Arcane damage 34 + 3.2/level + 0.95 INT to every foe (~177 at L32, ~251 at L50) |
| 44 | **Wrath of the Wild** | 318 / 354 | 5 | one foe | Nature damage 55 + 4.2/level + 1.25 INT (~308 at L44, ~341 at L50), and heals you for 20% of your max HP |

## How to play

**Levels 1-14.** Thornlash is cheap and hits well; it is your attack. Regrowth heals a bit now and more
over five rounds, so cast it early in a fight that is going to hurt. Entangling Roots at 8 holds a foe
for two rounds: root the dangerous one, Thornlash it, and root again when the cooldown is up.

**Levels 15-31.** Moonfire hits harder than Thornlash and leaves a burn on the target; open with it,
then Thornlash while it burns, and reapply when it runs out. Barkskin at 22 is a big armor boost with a
little healing for six rounds: cast it before tough fights.

**Levels 32-50.** Starfall is your group attack, every three rounds. Wrath of the Wild at 44 is a huge
hit that also heals 20% of your health, so it doubles as an emergency heal. Against a boss: Barkskin,
Moonfire, Wrath of the Wild on cooldown, Thornlash in between, Roots when you need a breather, Regrowth
to top up.

**Tips**
- All your damage ignores armor.
- The roots are your safety net. A rooted monster does nothing for two rounds.
- Leather and no shield makes you softer than a Cleric or Shaman, so keep Barkskin up in long fights.

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

The Druid wins every same-level fight in the simulator, and fast: about 3 rounds at levels 15-20 and
under 5 later, with 57-90% HP left. It lasts about 4 fights in a row at level 10 and 6 at level 30.
It beats nearly every world boss at the boss's own level (about 87% against Ussreth and Pyraxis,
93-97% against Ithilmir, Orrin Gearwhistle and the High Justice), and all except Pyraxis (about 83%)
at boss level +3.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Druid life brings strong WIS growth (shared with the Cleric and Shaman), plus **leather** training and staff, blunt
and dagger weapons. It adds little in stats once you have a Cleric life, but Entangling Roots and Wrath
of the Wild are strong in any later class.
