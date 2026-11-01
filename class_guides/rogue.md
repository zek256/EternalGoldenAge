# Rogue

> *Cutthroats and shadow-walkers who strike from the dark with poisoned steel.*

The Rogue is a pure weapon class with no mana and no spells. Everything it does is a free ability on a
cooldown: big single-target hits, poison, a long stun, and buffs that make it very hard to hit. It
gains more DEX than any other class, so it ends the game with the highest crit chance and dodge. It
has no heal at all, so it relies on killing fast, dodging and potions.

## At a glance

| | |
|---|---|
| HP per level | 8 |
| Mana per level | 0 (Rogues use no mana) |
| Attack stat | DEX |
| Spell stat | none |
| Starting bonus | DEX +4, CHA +1 |
| Gains per level | DEX +3, STR +1, CON +1 |
| Armor | Leather (and cloth) |
| Shield | No |
| Weapons | Dagger, sword, bow |
| Starting gear | Worn dagger (2-4), padded tunic, leather boots, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | DEX | STR | CON | Weapon damage | Crit | Dodge | Armor |
|---|---|---|---|---|---|---|---|---|
| 1 | 23 | 15 | 10 | 10 | 7-9 | 6.5% | 4.0% | 5 |
| 10 | 158 | 42 | 19 | 19 | 21-23 | 9.2% | 5.8% | 8 |
| 25 | 455 | 87 | 34 | 34 | 44-46 | 13.7% | 8.8% | 12 |
| 50 | 1150 | 162 | 59 | 59 | 83-85 | 21.2% | 13.8% | 20 |

At level 50 the Rogue's weapon bonus from DEX is the highest in the game, before gear.

## Abilities

All Rogue abilities are free and are used with `ability <name>` (or `ab <name>`). Weapon damage is the
average with the starting dagger.

| Level | Ability | Cooldown | Target | Effect |
|---|---|---|---|---|
| 1 | **Backstab** | 2 | one foe | 1.7x weapon damage (~13 at L1, ~142 at L50) |
| 5 | **Poisoned Blade** | 4 | one foe | 1.0x weapon damage plus poison: 4 + 0.9/level + 0.2 DEX per round for 4 rounds (~13 at L5, ~81 at L50) |
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
- Daggers have smaller damage ranges than swords; with DEX scaling it matters less, but upgrade your
  weapon whenever you can.

## Gear

Wear **leather**; you can't use shields. DEX first (damage, crit, dodge and armor all at once), then
CON.

Notable late gear: the Khopesh of Ussreth (48, sword), **Gravesong** (50, sword) and **the Death Mask**
(50, leather head, STR/DEX/CON), both from Morthis in the Plane of Death, drakehide boots (45) and
windwalker boots (50) in leather, the sandrunner's jerkin and gloves (40), the Band of the Four Winds
(50, ring), Stormcaller (50, bow), and the mythic Fang of Pyraxis and Eternity.

## Best races

- **Dark elf**: +5% crit, which with your DEX pushes you toward the 35% cap.
- **Elf**: the best DEX, +4% dodge and +2% crit.
- **Orc**: +6% damage.
- **Troll**: regenerates in combat, a heal for a class that has none.

## How it performs

The Rogue wins every same-level fight in the simulator in about 3-5 rounds with 66-80% HP left. It
lasts about 4 fights in a row at level 10 and 6 at level 30. It beat almost every world boss at the
boss's own level (95% against Gorrak and Pyraxis) and all of them at boss level +3.

## Rebirth

A Rogue life leaves you **+147 DEX, +49 STR and +49 CON**: the biggest single-stat bonus in the game.
Any later class gains a large boost to crit, dodge and armor. It gives only **leather** training and
dagger, sword and bow weapons. Kidney Shot, Evasion and Shadow Dance are free, so they make good tools
for later lives, especially casters who lack a stun or a defensive button.
