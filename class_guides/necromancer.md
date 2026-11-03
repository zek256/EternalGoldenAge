# Necromancer

> *Forbidden scholars of death who raise the fallen to fight at their side.*

The Necromancer is an INT caster in cloth who never fights alone. From level 4 a skeleton fights
beside it and takes hits for it, its main attack heals it, its disease ignores armor, and at 38 it can
raise a bone colossus with more HP than many players. It is the strongest solo class in the game, by
design: a good class to learn on despite its cloth armor.

## At a glance

| | |
|---|---|
| HP per level | 5 |
| Mana per level | 6 |
| Spell stat | INT |
| Starting bonus | INT +4, CON +1 |
| Gains per level | INT +3, CON +1, WIS +1 |
| Armor | Cloth only |
| Shield | No |
| Weapons | Staff, wand, dagger |
| Starting gear | Oak staff (1-4), linen robe, apprentice's hood, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | INT | CON | WIS | Weapon damage |
|---|---|---|---|---|---|---|
| 1 | 20 | 22 | 17 | 11 | 13 | 5-8 |
| 10 | 130 | 119 | 44 | 20 | 22 | 9-12 |
| 25 | 385 | 387 | 89 | 35 | 37 | 17-20 |
| 50 | 1010 | 1135 | 164 | 60 | 62 | 29-32 |

## Spells

All Necromancer magic is spells, cast with `cast <name>`. Cost is shown at the level you learn it and
at level 50.

| Level | Spell | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Lifetap** | 5 / 30 | - | one foe | Drain 6 + 1.4/level + 0.4 INT (~14 at L1, ~76 at L25, ~141 at L50); heals you for 35% of what it deals |
| 4 | **Raise Skeleton** | 23 / 106 | 10 | self | Summon a skeleton (~57 HP, 7-12 damage at L4; ~214 HP, 28-44 at L25; ~402 HP, 54-83 at L50) |
| 10 | **Plague** | 23 / 71 | - | one foe | Disease damage 5 + 1.1/level + 0.25 INT per round for 5 rounds (~27 at L10, ~101 at L50) |
| 18 | **Bone Spear** | 59 / 130 | - | one foe | Shadow damage 18 + 2.8/level + 0.8 INT (~122 at L18, ~289 at L50) |
| 28 | **Siphon Soul** | 126 / 201 | 3 | one foe | Drain 25 + 3/level + 0.9 INT (~197 at L28, ~322 at L50); heals you for 60% of what it deals |
| 38 | **Raise Bone Colossus** | 258 / 324 | 15 | self | Summon a bone colossus (~656 HP, 75-114 damage at L38; ~842 HP, 97-147 at L50). It replaces your skeleton |
| 46 | **Wail of the Damned** | 330 / 354 | 5 | all foes | Shadow damage 40 + 3.2/level + 1.0 INT to every foe (~339 at L46, ~364 at L50); every foe deals 30% less damage for 4 rounds |

## How to play

**Levels 1-9.** Lifetap is your attack and your heal at once. From 4, raise a skeleton before every
outing: it attacks every round and takes about a quarter of the enemies' normal attacks. Its stats are
fixed when it is raised, so raise a new one every few levels, and right away when it dies.

**Levels 10-27.** Put Plague on anything that will live more than a couple of rounds (it ignores
armor), then Lifetap. Bone Spear at 18 is your hardest single hit: use it to finish things quickly. A
normal fight: skeleton up, Plague, Bone Spear, Lifetap as needed for health.

**Levels 28-50.** Siphon Soul is a big drain every three rounds that heals for 60% of what it deals;
it is both your damage and your healing. At 38, raise the Bone Colossus instead of the skeleton: it
has three times the HP and hits much harder. Wail of the Damned at 46 is your area attack and also
weakens every foe. Against a boss: Colossus, Plague, Siphon Soul on cooldown, Bone Spear in between.

**Tips**
- With a pet out, fewer attacks reach you. Keep it alive and you can fight things a cloth wearer
  shouldn't.
- Drains, Plague and Bone Spear all ignore armor; your pet's attacks don't.
- You have no direct heal. Lifetap and Siphon Soul are it, so keep hitting things when you are hurt.

## Gear

Wear **cloth** and a staff or wand. INT first, then CON. An off-hand item (the sunlit codex) fills
your empty shield slot.

Notable late gear: the same as the Wizard: **the Dreamweaver's Staff**, the dragonbone staff, the
Scepter of the Sand Kings, Seluvar's Hollow Wand, **starweave robes**, **starstep slippers**, **dreamsilk
trousers**, the silkwind cloth set, the
Ring of the Archmage, the Pearl of the Deep, the sunlit codex, and the mythic Fang of Pyraxis and
Eternity.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a hawthorn wand (8,
wand, INT/WIS/CHA), a thistledown robe (7, cloth chest, INT/WIS), dandelion-silk trousers (8, cloth
legs, INT/WIS) and petal slippers (7, cloth feet, INT/CHA). Grubbin the Mole King drops the hawthorn
wand; the Wasp Queen drops the thistledown robe.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): the Heartspore staff (20,
staff, INT/WIS/CHA) from the First Spore, a glowcap pendant (16, neck, INT/WIS), the Mycelial Crown
(20, any class) and a sporethorn knife (18, dagger).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Ringmaster's
baton (30, wand, INT/WIS/CHA), a fortune teller's crystal ball (28, off-hand, INT/WIS), a pair of
dancing slippers (27, cloth, INT/WIS) and a knife-thrower's blade (29, dagger).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): a notary's rod (35,
wand, INT/WIS/CHA) from the magistrates and advocates, and the seal of office (37, ring, WIS/CHA/INT).

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): Ithilmir's brush (42, wand, INT/WIS/CHA), Ithilmir's maulstick (42, staff, INT/WIS/CHA),
a smock of living paint (42, cloth chest, INT/WIS/CHA), painted silk slippers (38, cloth feet, INT/WIS)
and a candle of still flame (38, off-hand, INT/WIS/CON). Ithilmir drops his brush, his maulstick and the
smock of living paint; the Memento Skull drops the candle of still flame.

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): the pendulum staff
(44, staff, INT/WIS/CHA), a jeweller's circlet (42, cloth head, INT/WIS) and the orrery amulet (44,
neck, INT/WIS/STR). Orrin Gearwhistle drops the pendulum staff and the orrery amulet; the Great Cuckoo
drops the jeweller's circlet.

From **Thornwick Hall** (43-49, west of the Stag Walk): a gown of green brocade (47, cloth chest,
INT/WIS/CHA) from Lady Seraphine, silk evening gloves (46, cloth, INT/WIS) from the ladies and guests,
and Tobias's black grimoire (47, off-hand, INT/WIS/CON) from Master Tobias.

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): a sugarglass
wand (49, wand, INT/WIS/CHA), a spun-sugar cowl (46, cloth head, INT/WIS/CHA), candy-striped trousers
(46, cloth legs, INT/WIS), gumdrop slippers (46, cloth feet, INT/WIS/DEX) and a peppermint amulet (47,
neck, INT/WIS/CON). Madame Marchpane drops the sugarglass wand and the spun-sugar cowl; the rest come
from her realm.

## Best races

- **Undead**: immune to poison and disease damage over time, and the obvious fit.
- **Gnome**: the best INT, +6% mana and +3% dodge.
- **High elf**: +12% mana.
- **Dark elf**: +5% crit on your spells.

## How it performs

The Necromancer is the strongest solo class. It wins every same-level fight in the simulator in about
3-4 rounds with 67-97% HP left, and it has the best staying power at low levels (about 7 fights in a
row at level 10, 7 at level 30). It beat every world boss at the boss's own level except Rask and
Yellowtooth (90% each) and a few at 97%, and all of them at boss level +3.

## Rebirth

In every later life, each of your stats, your HP per level and your mana pool are the best that any
class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Necromancer life brings the **best INT growth in the game** (shared with the Wizard) and the
**biggest mana pool**, but only **cloth** training with staff, wand and dagger weapons. Raise Skeleton
and Raise Bone Colossus give any later class a pet at full Necromancer strength, since you keep the INT
they scale with, and Siphon Soul is an excellent self-heal.
