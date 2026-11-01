# Warrior

> *Masters of blade and shield who stand in the front rank of every battle.*

The Warrior is the simplest class in the game: no mana, no spells, just weapons, armor and a set of
free abilities on cooldowns. It has the most HP of any class and wears the heaviest armor, so it
rarely dies, but it kills slowly and has only one self-heal. It is a good first class and the best
class to have in a past life, because it gives plate training and a huge STR and CON bonus.

## At a glance

| | |
|---|---|
| HP per level | 13 (the most of any class) |
| Mana per level | 0 (Warriors use no mana) |
| Spell stat | none |
| Starting bonus | STR +3, CON +3 |
| Gains per level | STR +2, CON +2, DEX +1 |
| Armor | Plate (and everything lighter) |
| Shield | Yes |
| Weapons | Dagger, sword, axe, blunt, two-handed, bow |
| Starting gear | Rusty shortsword (2-5), wooden shield, padded tunic, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | STR | DEX | CON | Weapon damage | Crit | Dodge |
|---|---|---|---|---|---|---|---|
| 1 | 28 | 13 | 10 | 13 | 7-10 | 6.0% | 3.7% |
| 10 | 232 | 31 | 19 | 31 | 17-20 | 6.9% | 4.3% |
| 25 | 715 | 61 | 34 | 61 | 35-38 | 8.4% | 5.3% |
| 50 | 1920 | 111 | 59 | 111 | 65-68 | 10.9% | 6.9% |

## Abilities

All Warrior abilities are free and are used with `ability <name>` (or `ab <name>`). Weapon damage
below is the average with the starting sword; a better weapon raises every one of them.

| Level | Ability | Cooldown | Target | Effect |
|---|---|---|---|---|
| 1 | **Slam** | 3 | one foe | 1.4x weapon damage, 30% chance to stun for 1 round (15% vs bosses). ~11 at L1, ~93 at L50 |
| 5 | **Battle Cry** | 8 | self | +25% damage for 5 rounds |
| 8 | **Second Wind** | 15 | self | Heal 35% of max HP |
| 12 | **Cleave** | 3 | all foes | 1.1x weapon damage to every enemy in the fight |
| 20 | **Shield Wall** | 8 | self | +20 armor + 3 per level for 4 rounds (+80 at L20, +170 at L50) |
| 30 | **Rampage** | 4 | one foe | 2.6x weapon damage. ~110 at L30, ~172 at L50 |
| 42 | **Avatar of War** | 12 | self | Heal 30% of max HP, then +60% damage and +2 armor per level for 5 rounds |

## How to play

**Levels 1-11.** Open every fight with `kill <target>`, then queue Slam whenever it is ready.
From 5, use Battle Cry at the start of anything that will last more than a few rounds. From 8,
Second Wind is your only heal: save it for when you drop under about half health. Early on the
Warrior has the shortest staying power of any class (about 2 fights in a row at level 10 before it
needs to rest), so sleep between fights and carry potions.

**Levels 12-29.** Cleave makes groups much easier, since you hit everything for 1.1x weapon damage
every three rounds. Shield Wall at 20 is a huge armor boost for four rounds: use it when a boss or a
hard hitter is about to land its big attack, or just on cooldown in long fights.

**Levels 30-50.** Rampage becomes your main damage button (2.6x weapon damage every 4 rounds).
A good rotation is Rampage, Slam, Slam on the in-between rounds, with Battle Cry kept up. At 42,
Avatar of War is both a heal and your biggest damage boost; use it when a fight turns bad, or at
the start of a boss fight once you are a little hurt so the heal is not wasted.

**Tips**
- Your damage is all physical, so heavily armored monsters (golems, constructs) take longer.
- Everything depends on your weapon. Upgrade it before anything else. Two-handed weapons have the
  biggest damage ranges, but you lose the shield's armor.
- With no mana, you never have to drink mana potions. Spend that gold on healing potions.

## Gear

Wear the best **plate** you can find, with a shield unless you are using a two-handed weapon. You
want STR first (damage), then CON (HP).

Notable late gear a Warrior can use: the obsidian greatblade (45, two-handed), the Khopesh of Ussreth
(48, sword), Flameheart (50, blunt, from Rekkn), Tidecaller (50, two-handed, from Nerevos), Gravesong
(50, sword, from Morthis), the Mountainheart Shield (50, from Ulmathra), gauntlets of the pyre (50,
plate), dreamsilver greaves (50, plate), stonestride boots (50, plate), and the mythic weapons that
anyone may wield: the Fang of Pyraxis and Eternity.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): the shelfcap breastplate (15,
plate chest), a rootmaul (16, two-handed), a sporethorn knife (18, dagger), a shelf-fungus shield (14),
the Mycelial Crown (20, any class) and the rootbound ring (20).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Strongman's
breastplate (27, plate chest), a roustabout's tent mallet (28, blunt), a knife-thrower's blade (29,
dagger), a roustabout's chain chausses (27, mail legs) and the brass ring (27, ring).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): the Gavel of the High
Justice (38, blunt), the Headsman's axe (32), a bailiff's halberd (36, two-handed), a warden's
greathelm (35) and sabatons (34) (plate), the shield of the scales (35) and the High Justice's chain of
office (38, neck).

From **Thornwick Hall** (43-49, west of the Stag Walk): the Vane longsword (49, sword) and the Vane
heirloom plate (49, plate chest) from Lord Aldric Vane, the Vane warhelm (46) and gauntlets (45) from
his knights and sworn swords, Mistress Hollin's cleaver (45, axe), Mr. Graves's silver salver (45,
shield), the Vane signet (49, ring) and Great-aunt Mathilde's cameo (46, neck).

## Best races

- **Ogre**: the highest STR and CON, plus +12% HP. The classic choice.
- **Orc**: +6% damage, good STR and CON.
- **Troll**: regenerates in combat, which helps a class with only one heal.
- **Human**: +5% HP and +5% damage.

## How it performs

The Warrior wins every same-level fight in the simulator but takes the longest (5-7 rounds) and
finishes with 60-73% HP. It survives about 2 fights in a row at level 10 and about 6 at level 30.
It beats every world boss at the boss's own level except the Bone King Varnoth (about 85%), and all
of them at boss level +3.

## Rebirth

In every later life, each of your stats, your HP per level and your mana pool are the best that any
class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Warrior life brings the **best STR and CON growth in the game** (shared with the Dread Knight) and
the **highest HP per level** (13), so every later life is as tough as a Warrior: a wizard reborn after
it has a Warrior's HP pool. It also gives **plate armor and shield training** and every weapon except
staffs and wands. The Warrior abilities you keep are all free, so they work in any later class.
