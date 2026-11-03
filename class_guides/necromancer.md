# Necromancer

> *Forbidden scholars of death who raise the fallen to fight at their side.*

The Necromancer is an INT caster in cloth who never fights alone. From level 4 a skeleton fights
beside it and takes hits for it, its attacks include drains that heal it, its disease ignores armor,
and at 38 it can raise a bone colossus with more HP than many players. Pets can only be raised out of
combat, so raise one before every fight. It is the strongest solo class in the game, by design.

## At a glance

| | |
|---|---|
| HP per level | 5 |
| Mana per level | 12 (plus WIS) |
| Spell stats | INT (damage); pets use the higher of the two |
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
| 1 | 81 | 73 | 17 | 11 | 13 | 5-8 |
| 10 | 526 | 202 | 44 | 20 | 22 | 9-12 |
| 25 | 1559 | 452 | 89 | 35 | 37 | 17-20 |
| 50 | 4090 | 970 | 164 | 60 | 62 | 29-32 |

## Spells and abilities

All Necromancer magic is spells, cast with `cast <name>`. There are no cooldowns: every attack can be used every round, and each new attack is a modest step up (12%) from the one before it, so **use your newest one**.

| Level | Name | Type | Cost | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Lifetap** | spell | 5 / 30 | one foe | Shadow drain 6 + 1.86/level + 0.53 INT (~16 at L1, ~99 at L25, ~185 at L50) that heals you for 101% of what it deals |
| 4 | **Raise Skeleton** | spell | 23 / 106 | self | Summon a rattling skeleton (~867 HP, 28-44 damage at L25); only out of combat, and it stays until it dies |
| 10 | **Plague** | spell | 23 / 71 | one foe | Disease damage over time: 5 + 1.1/level + 0.25 INT per round for 5 rounds (~27 at L10, ~54 at L25, ~101 at L50 per round) |
| 18 | **Bone Spear** | spell | 14 / 30 | one foe | Shadow damage 6.72 + 2.08/level + 0.59 INT (~84 at L18, ~111 at L25, ~207 at L50) |
| 28 | **Siphon Soul** | spell | 18 / 30 | one foe | Shadow drain 7.53 + 2.33/level + 0.66 INT (~137 at L28, ~232 at L50) that heals you for 101% of what it deals |
| 38 | **Raise Bone Colossus** | spell | 258 / 324 | self | Summon a towering bone colossus (~2657 HP, 75-114 damage at L38); only out of combat, and it stays until it dies |
| 46 | **Wail of the Damned** | spell | 28 / 30 | one foe | Shadow damage 8.43 + 2.61/level + 0.74 INT (~240 at L46, ~260 at L50); the foe deals 20% less damage for the rest of the fight |

## How to play

**Before every fight.** Raise your pet (the Bone Colossus from 38, a skeleton before that). You can't
raise one in combat, so if it dies mid-fight, finish the fight and raise another.

**Every fight.** Plague (from 10) once, then your newest attack spell every round: Lifetap, Bone
Spear from 18, Siphon Soul from 28, Wail of the Damned from 46 (which also weakens the foe for the
rest of the fight). Lifetap and Siphon Soul heal you for a quarter of what they deal.

**Tips**
- Your pet draws about a quarter of the attacks aimed at you.
- Shadow and disease damage ignore armor.

## Gear

Wear **cloth** and a staff or wand. INT first, then CON; WIS adds mana. An off-hand item (the sunlit codex) fills
your empty shield slot.

Notable late gear: the same as the Wizard: **the Dreamweaver's Staff**, the dragonbone staff, the
Scepter of the Sand Kings, Seluvar's Hollow Wand, **starweave robes**, **starstep slippers**, **dreamsilk
trousers**, the silkwind cloth set, the
Ring of the Archmage, the Pearl of the Deep, the sunlit codex, and the mythic Fang of Pyraxis and
Eternity.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a hawthorn wand (8,
wand, INT/WIS), a thistledown robe (7, cloth chest, INT/WIS), dandelion-silk trousers (8, cloth
legs, INT/WIS) and petal slippers (7, cloth feet, INT). Grubbin the Mole King drops the hawthorn
wand; the Wasp Queen drops the thistledown robe.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): the Heartspore staff (20,
staff, INT/WIS) from the First Spore, a glowcap pendant (16, neck, INT/WIS), the Mycelial Crown
(20, any class) and a sporethorn knife (18, dagger).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Ringmaster's
baton (30, wand, INT/WIS), a fortune teller's crystal ball (28, off-hand, INT/WIS), a pair of
dancing slippers (27, cloth, INT/WIS) and a knife-thrower's blade (29, dagger).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): a notary's rod (35,
wand, INT/WIS) from the magistrates and advocates, and the seal of office (37, ring, WIS/INT).

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): Ithilmir's brush (42, wand, INT/WIS), Ithilmir's maulstick (42, staff, INT/WIS),
a smock of living paint (42, cloth chest, INT/WIS), painted silk slippers (38, cloth feet, INT/WIS)
and a candle of still flame (38, off-hand, INT/WIS/CON). Ithilmir drops his brush, his maulstick and the
smock of living paint; the Memento Skull drops the candle of still flame.

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): the pendulum staff
(44, staff, INT/WIS), a jeweller's circlet (42, cloth head, INT/WIS) and the orrery amulet (44,
neck, INT/WIS/STR). Orrin Gearwhistle drops the pendulum staff and the orrery amulet; the Great Cuckoo
drops the jeweller's circlet.

From **Thornwick Hall** (43-49, west of the Stag Walk): a gown of green brocade (47, cloth chest,
INT/WIS) from Lady Seraphine, silk evening gloves (46, cloth, INT/WIS) from the ladies and guests,
and Tobias's black grimoire (47, off-hand, INT/WIS/CON) from Master Tobias.

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): a sugarglass
wand (49, wand, INT/WIS), a spun-sugar cowl (46, cloth head, INT/WIS), candy-striped trousers
(46, cloth legs, INT/WIS), gumdrop slippers (46, cloth feet, INT/WIS/DEX) and a peppermint amulet (47,
neck, INT/WIS/CON). Madame Marchpane drops the sugarglass wand and the spun-sugar cowl; the rest come
from her realm.

## Best races

- **Undead**: immune to poison and disease damage over time, and the obvious fit.
- **Gnome**: the best INT, +6% mana and +3% dodge.
- **High elf**: +12% mana.
- **Dark elf**: +5% crit on your spells.

## How it performs

The Necromancer wins every same-level fight in the simulator in 6.0-12.4 rounds, finishing with 65-99% HP. It survives about 6, 3 and 8 fights in a row at levels 10, 20 and 30 (the cap is 8). Against the world bosses it beats every one, at the boss's own level and at boss level +3. These figures are from November 2026, after monsters of level 50 and below got three times the HP and 40% of the damage and player HP was raised to match theirs.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Necromancer life brings the **best INT growth in the game** (shared with the Wizard) and the
**most mana per level**, but only **cloth** training with staff, wand and dagger weapons. Raise Skeleton
and Raise Bone Colossus give any later class a pet at full Necromancer strength, since you keep the INT
they scale with.
