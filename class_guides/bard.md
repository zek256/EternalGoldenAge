# Bard

> *Wandering minstrels whose songs mend allies and shatter the minds of foes.*

The Bard is a CHA caster in leather who also fights with a blade. Its songs do a bit of everything:
sonic damage that ignores armor, a heal over time, a sleep, a long buff, a group-weakening dirge and
big area damage late on. It is the most demanding class to play early and the slowest at killing
bosses at its own level, but it scales very well and ends the game as one of the safest classes.

## At a glance

| | |
|---|---|
| HP per level | 8 |
| Mana per level | 4 |
| Attack stat | DEX |
| Spell stat | CHA |
| Starting bonus | CHA +3, DEX +2 |
| Gains per level | CHA +2, DEX +2, CON +1 |
| Armor | Leather (and cloth) |
| Shield | No |
| Weapons | Dagger, sword, blunt, wand |
| Starting gear | Worn dagger (2-4), padded tunic, leather cap, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | CHA | DEX | CON | Weapon damage | Crit | Dodge |
|---|---|---|---|---|---|---|---|---|
| 1 | 23 | 20 | 13 | 13 | 10 | 7-9 | 6.3% | 3.9% |
| 10 | 158 | 86 | 31 | 31 | 19 | 17-19 | 8.1% | 5.1% |
| 25 | 455 | 267 | 61 | 61 | 34 | 35-37 | 11.1% | 7.1% |
| 50 | 1150 | 770 | 111 | 111 | 59 | 65-67 | 16.1% | 10.4% |

The Bard is the only caster whose auto-attack keeps pace with a fighter's, because it attacks with
DEX, which it gains every level.

## Spells

All Bard magic is spells, cast with `cast <name>`. Cost is shown at the level you learn it and at
level 50.

| Level | Spell | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Discordant Note** | 5 / 30 | - | one foe | Sonic damage 10 + 2.4/level + 0.8 CHA (~22 at L1, ~118 at L25, ~218 at L50) |
| 3 | **Ballad of Mending** | 8 / 41 | - | self | Heal 5 + 1/level + 0.25 CHA now, then 4 + 1/level + 0.22 CHA per round for 5 rounds (~45 + 42/round at L25) |
| 8 | **Lullaby** | 17 / 59 | 5 | one foe | 75% chance to put it to sleep for 2 rounds (about 38% vs bosses) |
| 15 | **War March** | 36 / 88 | 10 | self | +25% damage and +8 + 1/level armor for 8 rounds |
| 24 | **Dirge of Despair** | 86 / 153 | - | all foes | Sonic damage over time 9 + 1.6/level + 0.4 CHA per round for 4 rounds (~71 at L24, ~133 at L50), and every foe deals 25% less damage for 4 rounds |
| 34 | **Crescendo** | 194 / 266 | 3 | all foes | Sonic damage 34 + 3.2/level + 0.95 CHA to every foe (~217 at L34, ~299 at L50) |
| 44 | **Legend's Anthem** | 292 / 324 | 12 | self | +45% damage for 6 rounds and a heal over time of 20 + 2/level + 0.4 CHA per round (~147-164) |

## How to play

**Levels 1-14.** Discordant Note is your main attack. It is strong for its cost and ignores armor.
Cast it, let an auto-attack happen while mana comes back, cast again. Ballad of Mending heals a little
at once and the rest over five rounds, so cast it a little before you need it, not at the last moment.
Lullaby at 8 takes a monster out for two rounds: use it on the most dangerous of a pair, or to buy time
for the Ballad to work.

**Levels 15-33.** War March lasts 8 rounds on a 10-round cooldown, so keep it up in every real fight:
it is +25% damage and some armor for very little mana. Dirge of Despair at 24 is your first group
spell, and it is also a strong defensive one: every foe deals a quarter less damage while its damage
ticks. Against groups, open with War March and Dirge.

**Levels 34-50.** Crescendo is heavy area damage every three rounds. At 44, Legend's Anthem is +45%
damage and a strong heal over time on one button. A boss fight: War March, Legend's Anthem, Dirge (for
the weaken), then Discordant Note, with Lullaby when it lands and Ballad of Mending to top up.

**Tips**
- All your spell damage is sonic and ignores armor, so heavily armored monsters are no harder for you.
- Bards burn mana fast in long fights. Carry mana potions for bosses.
- Boss fights at your own level are slow. Fighting bosses two or three levels above their level
  makes them far easier.

## Gear

Wear **leather**; no shields. CHA first (your spells and mana), then DEX (weapon, crit, dodge), then CON.

There are no CHA-focused weapons in the late game, so look for gear with broad stats: the Scepter of
the Sand Kings (48, wand, INT/WIS/CHA), Seluvar's Hollow Wand (40), the Ashen Crown (46, any class),
the Heart of Flame (50, neck), **the Death Mask** (50, leather), windwalker boots (50, leather), the
Crown of Trepth and the Hourglass Amulet, and the mythic weapons the Fang of Pyraxis and Eternity, which
give CHA along with everything else.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): a sporethorn knife (18,
dagger), mossfelt boots (15, leather), a glowcap pendant (16, neck, INT/WIS/CHA) and the Mycelial Crown
(20, any class).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Ringmaster's
scarlet coat (30, leather chest, DEX/CHA/CON) and baton (30, wand, INT/WIS/CHA), a knife-thrower's
blade (29, dagger), a roustabout's tent mallet (28, blunt), an acrobat's grips (26) and the brass ring
(27, ring, CHA).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): a notary's rod (35,
wand, INT/WIS/CHA), the seal of office (37, ring, WIS/CHA/INT), the High Justice's chain of office (38,
neck, CHA), a scrivener's penknife (33, dagger) and the Gavel of the High Justice (38, blunt).

From **Thornwick Hall** (43-49, west of the Stag Walk): a minstrel's lute (45, off-hand, CHA/DEX) from
the household minstrels, the first CHA-focused late item; Sir Corwin's rapier (47, sword, DEX/STR/CHA),
Lady Seraphine's hairpin (47, dagger), the Dowager's pearls (48, neck, WIS/CHA/CON), the Vane signet
(49, ring, CHA) and the Vane huntsman's jerkin (44) and breeches (43) (leather).

## Best races

- **Human**: CHA 12 to start, plus +5% HP, mana and damage. The best all-round Bard.
- **High elf**: CHA 12 and +12% mana, for a spell-heavy Bard.
- **Elf**: better DEX, +4% dodge and +2% crit.

## How it performs

The Bard wins every same-level fight in the simulator, fast (3-5 rounds), with 74-95% HP left, and it
has good staying power (about 4 fights in a row at levels 10 and 30). Bosses at their own level are its
weakness: about 45% against Old Mother Gristle, 60-85% against several others, but it wins essentially
every boss fight at boss level +3.

## Rebirth

A Bard life leaves you **+98 CHA, +98 DEX and +49 CON**, plus **leather** training and dagger, sword,
blunt and wand weapons. CHA does nothing for other classes, so a Bard life is mainly worth its DEX
bonus and its spells: Lullaby, Dirge of Despair and Legend's Anthem stay strong in any later class,
though they scale with CHA.
