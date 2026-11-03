# Rogue

> *Cutthroats and shadow-walkers who strike from the dark with poisoned steel.*

The Rogue is a pure weapon class with no mana and no spells. Everything it does is a free ability on a
cooldown: big single-target hits, poison, a long stun, and buffs that make it very hard to hit. It
grows STR for damage and DEX for precision equally, so it hits hard, rarely misses, and crits and
dodges well. It
has no heal at all, so it relies on killing fast, dodging and potions.

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

## Abilities

All Rogue abilities are free and are used with `ability <name>` (or `ab <name>`). Weapon damage is the
average with the starting dagger.

| Level | Ability | Cooldown | Target | Effect |
|---|---|---|---|---|
| 1 | **Backstab** | 2 | one foe | 1.7x weapon damage (~13 at L1, ~142 at L50) |
| 5 | **Poisoned Blade** | 4 | one foe | 1.0x weapon damage plus poison: 4 + 0.9/level + 0.2 STR per round for 4 rounds (~12 at L5, ~71 at L50) |
| 10 | **Evasion** | 8 | self | +40% dodge for 3 rounds |
| 18 | **Kidney Shot** | 6 | one foe | 1.0x weapon damage, 85% chance to stun for 2 rounds (about 43% vs bosses) |
| 28 | **Eviscerate** | 4 | one foe | 2.8x weapon damage (~140 at L28, ~235 at L50) |
| 40 | **Shadow Dance** | 10 | self | +50% damage and +25% dodge for 4 rounds |
| 48 | **Assassinate** | 6 | one foe | 4.2x weapon damage (~340 at L48, ~352 at L50), the biggest weapon multiplier in the game |

## How to play

**Levels 1-17.** Backstab every other round. From 5, apply Poisoned Blade at the start of each fight
(its poison ignores armor), then Backstab. Evasion at 10 makes you nearly impossible to hit for three
rounds: use it when a monster is about to hurt you badly, or to cover the start of a hard fight.

**Levels 18-39.** Kidney Shot is a reliable 2-round stun: two free rounds of hitting without being
hit. Eviscerate at 28 is your main big hit. A good loop: Poisoned Blade, Kidney Shot, Eviscerate,
Backstab, Backstab, then again as things come off cooldown. The `cooldowns` command helps you track it.

**Levels 40-50.** Shadow Dance gives +50% damage and +25% dodge for four rounds. Save Eviscerate and,
from 48, Assassinate for while it is up: an Assassinate under Shadow Dance is 6.3x weapon damage,
and nearly 11x on a crit.

**Tips**
- You have **no heal**. Carry plenty of healing potions, sleep between fights, and lean on Evasion and
  stuns to avoid damage rather than recovering from it.
- No group attack: the Rogue fights one target at a time, so packs of monsters are dangerous. Stun one
  and kill the other first.
- Daggers have smaller damage ranges than swords, so upgrade your weapon whenever you can.

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

The Rogue wins every same-level fight in the simulator in about 3-6 rounds with 57-84% HP left (it
takes the most damage at levels 1-16). It lasts about 3 fights in a row at level 10 and 6-7 at level
30. It beat almost every world boss at the boss's own level (97% against Rask, Old Mother Gristle,
Seluvar and Pyraxis) and all of them at boss level +3.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Rogue life brings strong STR and DEX growth (matching the Ranger): later lives hit harder, miss less,
crit and dodge more. It gives only **leather** training and dagger, sword and bow weapons. Kidney Shot,
Evasion and Shadow Dance are free, so they make good tools for later lives, especially casters who lack
a stun or a defensive button.
