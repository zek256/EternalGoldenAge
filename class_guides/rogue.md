# Rogue

> *Cutthroats and shadow-walkers who strike from the dark with poisoned steel.*

The Rogue is a pure weapon class with no mana and no spells. Its free abilities form a ladder of
ever-harder strikes (Backstab, Kidney Shot, Eviscerate, Assassinate), plus a poison and two
whole-fight buffs. From 10 it fights with a blade in each hand and from 15 each hand may strike twice.
It grows STR and DEX equally, so it hits hard, rarely misses, and crits and dodges well. It has no
heal at all, so it relies on killing fast, dodging and potions.

## At a glance

| | |
|---|---|
| HP per level | 8 |
| Mana per level | 0 (Rogues use no mana) |
| Spell stats | none |
| Starting bonus | STR +2, DEX +2, CON +1 |
| Gains per level | STR +2, DEX +2, CON +1 |
| Armor | Leather (and cloth) |
| Shield | No |
| Weapons | Dagger, sword, bow |
| Starting gear | Worn dagger (2-4), padded tunic, leather boots, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | STR | DEX | CON | Weapon damage | Miss | Crit | Dodge | Armor |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 23 | 12 | 13 | 11 | 6-8 | 9.1% | 6.3% | 3.9% | 5 |
| 10 | 160 | 30 | 31 | 20 | 17-19 | 7.8% | 8.1% | 5.1% | 7 |
| 25 | 460 | 60 | 61 | 35 | 35-37 | 5.7% | 11.1% | 7.1% | 10 |
| 50 | 1160 | 110 | 111 | 60 | 65-67 | 2.2% | 16.1% | 10.4% | 15 |

STR is your damage and DEX your precision: by level 50 your auto-attacks almost never miss.

## Spells and abilities

All Rogue abilities are free and used with `ability <name>` (or `ab <name>`). There are no cooldowns: every attack can be used every round, and each new attack is a modest step up (12%) from the one before it, so **use your newest one**.

| Level | Name | Type | Cost | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Backstab** | ability | free | one foe | 1.5x weapon damage (~10 at L1, ~54 at L25, ~99 at L50 with the starting weapon) |
| 5 | **Poisoned Blade** | ability | free | one foe | 1x weapon damage (~12 at L5, ~36 at L25, ~66 at L50 with the starting weapon); Poison damage over time: 4 + 0.9/level + 0.2 STR per round for 4 rounds (~12 at L5, ~38 at L25, ~71 at L50 per round) |
| 10 | **Evasion** | ability | free | self | +15% dodge until the end of the fight |
| 10 | **Dual Wield** | passive | - | - | Wield a one-handed weapon in your off hand (the shield slot); it strikes beside your main hand every round for 65% damage. |
| 15 | **Double Attack** | passive | - | - | Each hand may strike a second time every round: a 40% chance when learned, rising evenly to certain at level 50. |
| 18 | **Kidney Shot** | ability | free | one foe | 1.68x weapon damage (~47 at L18, ~60 at L25, ~110 at L50 with the starting weapon) |
| 28 | **Eviscerate** | ability | free | one foe | 1.88x weapon damage (~75 at L28, ~124 at L50 with the starting weapon) |
| 40 | **Shadow Dance** | ability | free | self | +20% damage, +10% dodge until the end of the fight |
| 48 | **Assassinate** | ability | free | one foe | 2.11x weapon damage (~135 at L48, ~139 at L50 with the starting weapon) |

## How to play

**Every fight.** Evasion (from 10) and Shadow Dance (from 40) once each, then your newest strike every
round: Backstab, Kidney Shot from 18, Eviscerate from 28, Assassinate from 48. Against a long fight,
Poisoned Blade once adds a poison for 4 rounds.

**Weapons.** From 10, `wear` a second one-hander to hold it in your off hand (or `offhand <weapon>`).
Every strike, including the off hand's, rolls its own crit.

**Tips**
- No heal: drink potions early, and rest between hard fights.
- Every attack in the game hits one foe, so packs of monsters are dangerous for a class with no heal.

## Gear

Wear **leather**; you can't use shields. STR and DEX together (STR for damage; DEX for hits, crit,
dodge and armor), then CON.

Notable late gear: the Khopesh of Ussreth (48, sword), **Gravesong** (50, sword) and **the Death Mask**
(50, leather head, STR/DEX/CON) and **the Ferryman's gloves** (50, leather, DEX/STR), all from Morthis
in the Plane of Death, drakehide boots (45) and
windwalker boots (50) in leather, the sandrunner's jerkin and gloves (40), the Band of the Four Winds
(50, ring), Stormcaller (50, bow), and the mythic Fang of Pyraxis and Eternity.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a darning-needle sword
(7, sword, DEX/STR), a wasp-sting dagger (8, dagger, DEX), the Wasp Queen's stinger (10, dagger,
DEX/STR), a whisker-strung bow (9, bow, DEX), an acorn helm (6, leather head, DEX), a beetle-shell
jerkin (7, leather chest, DEX/CON), snailskin leggings (6, leather legs, DEX) and mole-claw gloves (9,
leather hands, STR/DEX). The Wasp Queen drops her stinger; Old Tom the cat drops the whisker-strung bow;
Grubbin the Mole King drops mole-claw gloves.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): a sporethorn knife (18,
dagger, DEX), mossfelt boots (15, leather, DEX) and the Mycelial Crown (20, any class).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): a knife-thrower's
blade (29, dagger, DEX) from Mirela, the Ringmaster's scarlet coat (30, leather chest, DEX/INT), an
acrobat's grips (26, leather) and the brass ring (27, ring).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): a scrivener's penknife
(33, dagger, DEX/INT), the only dagger between Serpentfang at 15 and the Thornwick hairpin at 47.

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): a palette knife (38, dagger, DEX/INT), a frost-varnished bow (37, bow, DEX/WIS) and the
Countess's kid gloves (39, leather hands, DEX/INT). Countess Isaura drops the Countess's kid gloves.

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): a gearwork blade (42,
sword, STR/DEX) and tinker's gloves (43, leather hands, DEX/STR). The Master Automaton drops the
gearwork blade; the Clockwork Hostess drops tinker's gloves.

From **Thornwick Hall** (43-49, west of the Stag Walk): Lady Seraphine's hairpin (47, dagger, DEX), the
first new dagger since Serpentfang at 15, Sir Corwin's rapier (47, sword, DEX), the Vane hunting bow
(45), the Vane huntsman's jerkin (44) and breeches (43) (leather) and Great-aunt Mathilde's cameo (46,
neck).

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): a rock-candy
dagger (45, dagger, DEX/STR), a licorice hood (46, leather head, DEX/CON), taffy-grip gloves (46,
leather hands, DEX/STR) and a ring of spun sugar (48, ring, DEX/CON/INT). Madame Marchpane drops the
ring of spun sugar; the rest come from her realm.

## Best races

- **Orc**: STR 13 and +6% damage.
- **Dark elf**: +5% crit, which with your DEX pushes you toward the 35% cap.
- **Elf**: +4% dodge and +2% crit.
- **Troll**: regenerates in combat, a heal for a class that has none.

## How it performs

The Rogue wins every same-level fight in the simulator in 3.0-4.0 rounds, finishing with 68-85% HP. It survives about 3, 4 and 8 fights in a row at levels 10, 20 and 30 (the cap is 8). Against the world bosses it beats every one, at the boss's own level and at boss level +3. These figures are from November 2026, after cooldowns were removed.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Rogue life brings strong STR and DEX growth (matching the Ranger): later lives hit harder, miss less,
crit and dodge more. It gives only **leather** training and dagger, sword and bow weapons. Its strikes
are free, so they make good tools for later lives that keep a good weapon. It also passes on Dual
Wield and Double Attack to every later life (the Warrior has both too, at earlier levels).
