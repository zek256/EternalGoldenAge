# Wizard

> *Scholars of the arcane who bend fire, frost and lightning to their will.*

The Wizard is the purest damage caster in the game, and the most fragile. It has the lowest HP of any
class and can only wear cloth, but it kills ordinary monsters faster than anything else and has the
one of the largest mana pools. Its defense is Mana Shield, a large damage ward that it should keep up in every
fight. It gets no group attack until Fireball at 16.

## At a glance

| | |
|---|---|
| HP per level | 5 (the least of any class) |
| Mana per level | 10 (plus WIS) |
| Spell stats | INT (damage); WIS (shields) |
| Starting bonus | INT +4, WIS +1 |
| Gains per level | INT +3, WIS +2 |
| Armor | Cloth only |
| Shield | No |
| Weapons | Staff, wand, dagger |
| Starting gear | Oak staff (1-4), linen robe, apprentice's hood, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | INT | WIS | Weapon damage |
|---|---|---|---|---|---|
| 1 | 20 | 26 | 17 | 14 | 5-8 |
| 10 | 110 | 147 | 44 | 32 | 9-12 |
| 25 | 260 | 420 | 89 | 62 | 17-20 |
| 50 | 510 | 1075 | 164 | 112 | 29-32 |

With no CON gain at all, a Wizard ends at about half the HP of most casters. CON gear and past lives
help a lot.

## Spells

All Wizard magic is spells, cast with `cast <name>`. Cost is shown at the level you learn it and at
level 50.

| Level | Spell | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Magic Missile** | 5 / 30 | - | one foe | Arcane damage 6 + 1.5/level + 0.45 INT (~15 at L1, ~83 at L25, ~154 at L50) |
| 5 | **Frost Bolt** | 13 / 53 | - | one foe | Frost damage 10 + 2/level + 0.5 INT (~34 at L5, ~104 at L25, ~192 at L50), 30% chance to freeze it for 1 round (15% vs bosses) |
| 10 | **Mana Shield** | 27 / 83 | 6 | self | A ward that absorbs 17 + 6.79/level + 1.5 WIS damage (~132 at L10, ~279 at L25, ~524 at L50) |
| 16 | **Fireball** | 60 / 142 | 2 | all foes | Fire damage 15 + 2.2/level + 0.6 INT to every foe (~87 at L16, ~223 at L50) |
| 26 | **Lightning Lance** | 112 / 189 | 2 | one foe | Lightning damage 30 + 3.6/level + 1.05 INT (~220 at L26, ~382 at L50) |
| 40 | **Meteor** | 368 / 442 | 5 | all foes | Fire damage 60 + 4/level + 1.3 INT to every foe (~394 at L40, ~473 at L50) |

## How to play

**Levels 1-9.** Magic Missile, then Frost Bolt from 5 (it hits harder and can freeze). Kill things
before they reach you. You will take every hit at full force, so rest often and never fight two
things at once if you can help it.

**Levels 10-15.** Mana Shield changes everything. It absorbs more than your whole HP bar at these
levels, and its cooldown (6) is short. Cast it **before** every fight and again as soon as it comes back.

**Levels 16-39.** Fireball finally lets you take on groups, every other round. Lightning Lance at 26
is your best single-target spell: alternate it with Frost Bolt. A normal fight: Mana Shield, Lightning
Lance, Frost Bolt, Lightning Lance.

**Levels 40-50.** Meteor is the biggest area spell in the game. Against packs, Meteor, then Fireball
while it cools down. Against a boss: Mana Shield, then Lightning Lance and Frost Bolt, re-shielding on
every cooldown and drinking potions early rather than late.

**Tips**
- All your damage ignores armor.
- Spell costs grow fast with level. You have a big mana pool, but long boss fights can drain it: carry
  mana potions.
- Wizards have no heal. A past life as a Paladin (Lay on Hands, Avenging Wrath) or a Warrior (Second
  Wind) gives you free heals and a much bigger HP pool.

## Gear

Wear **cloth** and a staff or wand. INT first, then WIS (Mana Shield and your mana), then CON for survival. An off-hand item (the sunlit
codex) fills your empty shield slot.

Notable late gear: **the Dreamweaver's Staff** (50, staff, INT/WIS, from Somnara), the dragonbone
staff (47), the Scepter of the Sand Kings (48, wand), Seluvar's Hollow Wand (40), **starweave robes**
(50, cloth, INT/WIS, from Caelestra), **starstep slippers** (50, cloth, INT/WIS, from Caelestra),
**dreamsilk trousers** (50, cloth, INT/WIS, from Somnara), the silkwind gloves, trousers and slippers (cloth, 40-42), the
Ring of the Archmage (40), the Pearl of the Deep (50, ring), the sunlit codex (40, off-hand), the Ashen
Crown, and the mythic Fang of Pyraxis and Eternity.

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

- **Gnome**: the best INT, +6% mana and +3% dodge.
- **High elf**: INT 13 and +12% mana.
- **Dark elf**: +5% crit, which applies to your spells.
- **Ogre**: an odd choice, but +12% HP and high CON cover a Wizard's biggest weakness.

## How it performs

The Wizard wins every same-level fight in the simulator in about 3-5 rounds, finishing with 85-100%
HP thanks to Mana Shield. It lasts about 3 fights in a row at level 10 and nearly 8 at level 30.
Bosses at their own level are harder: 70-100% for most, about 57% against the High Justice and
Ussreth. At boss level +3 it wins nearly all of them except Pyraxis (about 73%).

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Wizard life brings the **best INT growth in the game** (shared with the Necromancer) and strong
WIS growth, but only **cloth** training with staff, wand and dagger weapons. Any later class
casts with a Wizard's INT and WIS: Mana Shield, Lightning Lance and Meteor stay at full strength
whatever you become.
