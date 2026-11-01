# Wizard

> *Scholars of the arcane who bend fire, frost and lightning to their will.*

The Wizard is the purest damage caster in the game, and the most fragile. It has the lowest HP of any
class and can only wear cloth, but it kills ordinary monsters faster than anything else and has the
largest mana pool. Its defense is Mana Shield, a large damage ward that it should keep up in every
fight. It gets no group attack until Fireball at 16.

## At a glance

| | |
|---|---|
| HP per level | 5 (the least of any class) |
| Mana per level | 6 (the most of any class) |
| Spell stat | INT |
| Starting bonus | INT +4, WIS +1 |
| Gains per level | INT +3, WIS +1, DEX +1 |
| Armor | Cloth only |
| Shield | No |
| Weapons | Staff, wand, dagger |
| Starting gear | Oak staff (1-4), linen robe, apprentice's hood, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | INT | DEX | WIS | Weapon damage |
|---|---|---|---|---|---|---|
| 1 | 20 | 22 | 17 | 10 | 14 | 5-8 |
| 10 | 110 | 119 | 44 | 19 | 23 | 9-12 |
| 25 | 260 | 387 | 89 | 34 | 38 | 17-20 |
| 50 | 510 | 1135 | 164 | 59 | 63 | 29-32 |

With no CON gain at all, a Wizard ends at about half the HP of most casters. CON gear and past lives
help a lot.

## Spells

All Wizard magic is spells, cast with `cast <name>`. Cost is shown at the level you learn it and at
level 50.

| Level | Spell | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Magic Missile** | 5 / 30 | - | one foe | Arcane damage 6 + 1.5/level + 0.45 INT (~15 at L1, ~83 at L25, ~154 at L50) |
| 5 | **Frost Bolt** | 13 / 53 | - | one foe | Frost damage 10 + 2/level + 0.5 INT (~34 at L5, ~104 at L25, ~192 at L50), 30% chance to freeze it for 1 round (15% vs bosses) |
| 10 | **Mana Shield** | 27 / 83 | 6 | self | A ward that absorbs 15 + 4.5/level + 1.3 INT damage (~117 at L10, ~243 at L25, ~453 at L50) |
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

Wear **cloth** and a staff or wand. INT first, then CON for survival. An off-hand item (the sunlit
codex) fills your empty shield slot.

Notable late gear: **the Dreamweaver's Staff** (50, staff, INT/WIS/CHA, from Somnara), the dragonbone
staff (47), the Scepter of the Sand Kings (48, wand), Seluvar's Hollow Wand (40), **starweave robes**
(50, cloth, INT/WIS/CHA, from Caelestra), **starstep slippers** (50, cloth, INT/WIS, from Caelestra),
**dreamsilk trousers** (50, cloth, INT/WIS, from Somnara), the silkwind gloves, trousers and slippers (cloth, 40-42), the
Ring of the Archmage (40), the Pearl of the Deep (50, ring), the sunlit codex (40, off-hand), the Ashen
Crown, and the mythic Fang of Pyraxis and Eternity.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): the Heartspore staff (20,
staff, INT/WIS/CHA) from the First Spore, a glowcap pendant (16, neck, INT/WIS), the Mycelial Crown
(20, any class) and a sporethorn knife (18, dagger).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Ringmaster's
baton (30, wand, INT/WIS/CHA), a fortune teller's crystal ball (28, off-hand, INT/WIS), a pair of
dancing slippers (27, cloth, INT/WIS) and a knife-thrower's blade (29, dagger).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): a notary's rod (35,
wand, INT/WIS/CHA) from the magistrates and advocates, and the seal of office (37, ring, WIS/CHA/INT).

From **Thornwick Hall** (43-49, west of the Stag Walk): a gown of green brocade (47, cloth chest,
INT/WIS/CHA) from Lady Seraphine, silk evening gloves (46, cloth, INT/WIS) from the ladies and guests,
and Tobias's black grimoire (47, off-hand, INT/WIS/CON) from Master Tobias.

## Best races

- **Gnome**: the best INT, +6% mana and +3% dodge.
- **High elf**: INT 13 and +12% mana.
- **Dark elf**: +5% crit, which applies to your spells.
- **Ogre**: an odd choice, but +12% HP and high CON cover a Wizard's biggest weakness.

## How it performs

The Wizard wins every same-level fight in the simulator in about 3-4 rounds, finishing with 80-100%
HP thanks to Mana Shield. It lasts about 3 fights in a row at level 10 and 5-6 at level 30. Bosses at
their own level are harder: 70-95% for most, 75% against Ussreth and 80% against Pyraxis. At boss level
+3 it wins all of them except Pyraxis (65%).

## Rebirth

In every later life, each of your stats, your HP per level and your mana pool are the best that any
class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Wizard life brings the **best INT growth in the game** (shared with the Necromancer) and the
**biggest mana pool**, but only **cloth** training with staff, wand and dagger weapons. Any later class
casts with a Wizard's INT and mana: Mana Shield, Lightning Lance and Meteor stay at full strength
whatever you become.
