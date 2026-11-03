# Bard

> *Wandering minstrels whose songs mend allies and shatter the minds of foes.*

The Bard is an INT and WIS caster in leather who also fights with a blade, in each hand from level 10.
Its songs do a bit of everything: sonic damage that ignores armor (Discordant Note, then Crescendo),
a heal that keeps working for 10 rounds, a whole-fight march, a dirge that weakens a foe for the whole
fight, and a late anthem that does both. It is the most demanding class to play early, but it scales
well and ends the game as one of the safest classes.

## At a glance

| | |
|---|---|
| HP per level | 8 |
| Mana per level | 9 (plus WIS) |
| Spell stats | INT (damage); WIS (healing) |
| Starting bonus | INT +2, WIS +1, STR +1, DEX +1 |
| Gains per level | INT +1, WIS +1, STR +1, DEX +1, CON +1 |
| Armor | Leather (and cloth) |
| Shield | No |
| Weapons | Dagger, sword, blunt, wand |
| Starting gear | Worn dagger (2-4), padded tunic, leather cap, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | INT | STR | DEX | WIS | CON | Weapon damage | Miss | Crit | Dodge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 23 | 25 | 12 | 11 | 12 | 11 | 10 | 6-8 | 9.2% | 6.2% | 3.8% |
| 10 | 158 | 125 | 21 | 20 | 21 | 20 | 19 | 14-16 | 8.5% | 7.1% | 4.4% |
| 25 | 455 | 327 | 36 | 35 | 36 | 35 | 34 | 26-28 | 7.5% | 8.6% | 5.4% |
| 50 | 1150 | 765 | 61 | 60 | 61 | 60 | 59 | 48-50 | 5.7% | 11.1% | 7.1% |

The Bard grows a little STR and DEX every level, so its blade stays useful between songs, but its
real damage is its INT-powered music, and WIS feeds its healing songs and mana.

## Spells and abilities

All Bard magic is spells, cast with `cast <name>`. There are no cooldowns: every attack can be used every round, and each new attack is a modest step up (12%) from the one before it, so **use your newest one**.

| Level | Name | Type | Cost | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Discordant Note** | spell | 5 / 30 | one foe | Sonic damage 10 + 3.22/level + 0.8 INT (~22 at L1, ~119 at L25, ~219 at L50) |
| 3 | **Ballad of Mending** | spell | 8 / 41 | self | Heal 5 + 1.26/level + 0.25 WIS (~12 at L3, ~45 at L25, ~83 at L50), then 3 + 0.75/level + 0.13 WIS per round for 10 rounds (~6 at L3, ~26 at L25, ~48 at L50 per round); casting it again restarts the timer |
| 10 | **Dual Wield** | passive | - | - | Wield a one-handed weapon in your off hand (the shield slot); it strikes beside your main hand every round for 65% damage. |
| 15 | **War March** | spell | 36 / 88 | self | +20% damage, +6 armor + 0.8/level until the end of the fight |
| 24 | **Dirge of Despair** | spell | 40 / 71 | one foe | Sonic damage over time: 9 + 2.01/level + 0.4 INT per round for 4 rounds (~71 at L24, ~73 at L25, ~133 at L50 per round); the foe deals 20% less damage for the rest of the fight |
| 34 | **Crescendo** | spell | 22 / 30 | one foe | Sonic damage 11.2 + 3.61/level + 0.9 INT (~174 at L34, ~246 at L50) |
| 44 | **Legend's Anthem** | spell | 159 / 177 | self | +15% damage until the end of the fight; then 10 + 1.2/level + 0.2 WIS per round for 10 rounds (~73 at L44, ~82 at L50 per round); casting it again restarts the timer |

## How to play

**Every fight.** War March (from 15) and Legend's Anthem (from 44) once each, Dirge of Despair (from
24) once on the foe, then your newest attack spell every round: Discordant Note, Crescendo from 34.
Cast Ballad of Mending when you drop under about half health; its heal over time runs for 10 rounds.

**Weapons.** From 10, `wear` a second one-hander to hold it in your off hand (or `offhand <weapon>`):
your blades swing every round alongside your songs.

**Tips**
- Sonic damage ignores armor.
- Mana is the only limit on your healing.

## Gear

Wear **leather**; no shields. INT first (your damage songs), then WIS (healing songs and mana), STR (weapon
damage) and DEX (hits, crit, dodge), then CON.

There are few bard weapons in the late game, so look for gear with INT, WIS or broad stats: the Scepter of
the Sand Kings (48, wand, INT/WIS), Seluvar's Hollow Wand (40), the Ashen Crown (46, any class),
the Heart of Flame (50, neck), **the Death Mask** (50, leather), **the Ferryman's gloves** (50, leather,
DEX/STR/INT, from Morthis), windwalker boots (50, leather), the
Crown of Trepth and the Hourglass Amulet, and the mythic weapons the Fang of Pyraxis and Eternity, which
give INT and WIS along with everything else.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a darning-needle sword
(7, sword, DEX/STR), a wasp-sting dagger (8, dagger, DEX), the Wasp Queen's stinger (10, dagger,
DEX/STR), a hawthorn wand (8, wand, INT/WIS), an acorn helm (6, leather head, DEX), a beetle-shell
jerkin (7, leather chest, DEX/CON), snailskin leggings (6, leather legs, DEX), mole-claw gloves (9,
leather hands, STR/DEX) and an amber pendant (10, neck, WIS/CON). The Wasp Queen drops her stinger
and the amber pendant; Grubbin the Mole King drops the hawthorn wand and mole-claw gloves.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): a sporethorn knife (18,
dagger), mossfelt boots (15, leather), a glowcap pendant (16, neck, INT/WIS) and the Mycelial Crown
(20, any class).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Ringmaster's
scarlet coat (30, leather chest, DEX/INT/CON) and baton (30, wand, INT/WIS), a knife-thrower's
blade (29, dagger), a roustabout's tent mallet (28, blunt), an acrobat's grips (26) and the brass ring
(27, ring, INT).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): a notary's rod (35,
wand, INT/WIS), the seal of office (37, ring, WIS/INT), the High Justice's chain of office (38,
neck, INT), a scrivener's penknife (33, dagger) and the Gavel of the High Justice (38, blunt).

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): a palette knife (38, dagger, DEX/INT), Ithilmir's brush (42, wand, INT/WIS), the
Countess's kid gloves (39, leather hands, DEX/INT) and a candle of still flame (38, off-hand,
INT/WIS/CON). Ithilmir drops his brush; Countess Isaura drops the Countess's kid gloves; the Memento
Skull drops the candle of still flame.

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): a gearwork blade (42,
sword, STR/DEX), Orrin's great wrench (44, blunt, STR/WIS/CON) and tinker's gloves (43, leather hands,
DEX/STR). The Master Automaton drops the gearwork blade; Orrin Gearwhistle drops his great wrench; the
Clockwork Hostess drops tinker's gloves.

From **Thornwick Hall** (43-49, west of the Stag Walk): a minstrel's lute (45, off-hand, INT/DEX) from
the household minstrels, a rare late item made for bards; Sir Corwin's rapier (47, sword, DEX/STR/INT),
Lady Seraphine's hairpin (47, dagger), the Dowager's pearls (48, neck, WIS/CON), the Vane signet
(49, ring, INT) and the Vane huntsman's jerkin (44) and breeches (43) (leather).

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): Madame
Marchpane's rolling pin (49, blunt, STR/WIS/CON), a candy-cane mace (47, blunt, STR/WIS), a rock-candy
dagger (45, dagger, DEX/STR), a sugarglass wand (49, wand, INT/WIS), a licorice hood (46, leather
head, DEX/CON), taffy-grip gloves (46, leather hands, DEX/STR) and a ring of spun sugar (48, ring,
DEX/CON/INT). Madame Marchpane drops the rolling pin, the sugarglass wand and the ring of spun sugar;
the rest come from her realm.

## Best races

- **Human**: +5% HP, mana and damage. The best all-round Bard.
- **High elf**: INT 13, WIS 13 and +12% mana, for a spell-heavy Bard.
- **Elf**: +4% dodge and +2% crit.

## How it performs

The Bard wins every same-level fight in the simulator in 3.3-7.8 rounds, finishing with 64-98% HP. It survives about 6, 6 and 8 fights in a row at levels 10, 20 and 30 (the cap is 8). Against the world bosses it beats every one, at the boss's own level and at boss level +3. These figures are from November 2026, after monsters of level 50 and below got twice the HP and 60% of the damage.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Bard life brings even growth in every stat, plus **leather** training and dagger, sword, blunt and
wand weapons. Other classes grow each stat faster, so a Bard life is mainly worth its songs: War
March, Dirge of Despair and Legend's Anthem are good in any later class. It also passes on Dual Wield
to every later life.
