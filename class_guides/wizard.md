# Wizard

> *Scholars of the arcane who bend fire, frost and lightning to their will.*

The Wizard is the purest damage caster in the game, and the most fragile. It has the lowest HP of any
class and can only wear cloth, but it kills ordinary monsters faster than anything else and has one
of the largest mana pools. Its five attack spells form an even ladder, from Magic Missile to Meteor,
so every fight plays the same way. Its defense is Mana Shield, a large damage ward it can recast
whenever it breaks.

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

## Spells and abilities

All Wizard magic is spells, cast with `cast <name>`. There are no cooldowns: every attack can be used every round, and each new attack is a modest step up (12%) from the one before it, so **use your newest one**.

| Level | Name | Type | Cost | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Magic Missile** | spell | 5 / 30 | one foe | Arcane damage 6 + 2/level + 0.6 INT (~18 at L1, ~109 at L25, ~204 at L50) |
| 5 | **Frost Bolt** | spell | 7 / 30 | one foe | Frost damage 6.72 + 2.24/level + 0.67 INT (~37 at L5, ~122 at L25, ~228 at L50) |
| 10 | **Mana Shield** | spell | 38 / 118 | self | A ward that absorbs 17 + 6.79/level + 1.5 WIS damage until it breaks (~132 at L10, ~279 at L25, ~524 at L50); casting it again restores it |
| 16 | **Fireball** | spell | 12 / 30 | one foe | Fire damage 7.53 + 2.51/level + 0.75 INT (~94 at L16, ~137 at L25, ~256 at L50) |
| 26 | **Lightning Lance** | spell | 18 / 30 | one foe | Lightning damage 8.43 + 2.81/level + 0.84 INT (~158 at L26, ~286 at L50) |
| 40 | **Meteor** | spell | 24 / 30 | one foe | Fire damage 9.44 + 3.15/level + 0.94 INT (~261 at L40, ~321 at L50) |

## How to play

**Every fight.** Cast Mana Shield (from 10) before you start, then your newest attack spell every
round: Magic Missile, Frost Bolt from 5, Fireball from 16, Lightning Lance from 26, Meteor from 40.
Recast Mana Shield whenever it breaks; it costs about as much mana as it saves you in HP, but you
have little HP and a lot of mana.

**Tips**
- All your damage ignores armor.
- A full mana pool easily covers a fight. Long boss fights with many shield recasts are where you
  may need a mana potion.
- Wizards have no heal. Fight one monster at a time when you can, carry healing potions, and
  consider a healer past life for later lives.

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

The Wizard wins every same-level fight in the simulator in 2.1-5.3 rounds, finishing with 61-100% HP. It survives about 7, 8 and 8 fights in a row at levels 10, 20 and 30 (the cap is 8). Against the world bosses it wins 90-100% at the boss's own level and 100% at boss level +3. These figures are from November 2026, after cooldowns were removed.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Wizard life brings the **best INT growth in the game** (shared with the Necromancer) and strong
WIS growth, but only **cloth** training with staff, wand and dagger weapons. Any later class
casts with a Wizard's INT and WIS: Mana Shield and Meteor stay at full strength whatever you become.
