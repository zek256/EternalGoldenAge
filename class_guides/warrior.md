# Warrior

> *Masters of blade and shield who stand in the front rank of every battle.*

The Warrior is the simplest class in the game: no mana, no spells, just weapons, armor and two free
abilities on cooldowns. Its damage comes from its own swings: it fights with a weapon in each hand
from level 1, and from 10 each hand may strike twice, so a level-50 Warrior lands four blows every round
without pressing a button. It has the most HP of any class and wears the heaviest armor, so it rarely
dies. It is a good first class and a strong past life, because it gives plate training, a huge STR and
CON bonus, and both Dual Wield and Double Attack.

## At a glance

| | |
|---|---|
| HP per level | 13 (the most of any class) |
| Mana per level | 0 (Warriors use no mana) |
| Spell stats | none |
| Starting bonus | STR +3, CON +3 |
| Gains per level | STR +2, CON +2, DEX +1 |
| Armor | Plate (and everything lighter) |
| Shield | Yes |
| Weapons | Dagger, sword, axe, blunt, two-handed, bow |
| Starting gear | Two rusty shortswords (2-5, one in each hand), padded tunic, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | STR | CON | DEX | Weapon damage | Crit | Dodge |
|---|---|---|---|---|---|---|---|
| 1 | 28 | 13 | 13 | 10 | 7-10 | 6.0% | 3.7% |
| 10 | 232 | 31 | 31 | 19 | 17-20 | 6.9% | 4.3% |
| 25 | 715 | 61 | 61 | 34 | 35-38 | 8.4% | 5.3% |
| 50 | 1920 | 111 | 111 | 59 | 65-68 | 10.9% | 6.9% |

## Abilities and passives

The two abilities are free and are used with `ability <name>` (or `ab <name>`). The passives are
always on once learned.

| Level | Ability | Cooldown | Target | Effect |
|---|---|---|---|---|
| 1 | **Second Wind** | 15 | self | Heal 35% of max HP |
| 1 | **Dual Wield** | passive | - | Hold a one-handed weapon (dagger, sword, axe or blunt) in the off hand, in place of a shield. It strikes every round beside your main hand for 65% damage. |
| 10 | **Double Attack** | passive | - | Each hand may strike a second time every round: 40% chance at 10, rising evenly to 100% at 50 (55% at 20, 70% at 30, 85% at 40) |
| 20 | **Shield Wall** | 8 | self | +20 armor + 3 per level for 4 rounds (+80 at L20, +170 at L50) |

Every strike rolls its own miss, crit and damage, and each one is shown on its own line. When the
target dies, the remaining strikes that round carry on to the next enemy in the fight.

## How to play

**Levels 1-19.** Open every fight with `kill <target>` and let your two swords work. Second Wind is
your only heal: save it for when you drop under about half health, and carry potions. Upgrade both
weapons as you go: `wear` a one-hander and it replaces the main hand, or goes into the off hand if
the shield slot is empty (`offhand <weapon>` puts it there directly). From 10, Double Attack makes
fights noticeably shorter.

**Levels 20-50.** Shield Wall is a huge armor boost for four rounds: use it when a boss or a hard
hitter is about to land its big attack, or on cooldown in long fights. Otherwise just fight. Late
Warriors finish most same-level fights in 4-6 rounds.

**Tips**
- Your damage is all physical, so heavily armored monsters (golems, constructs) take longer.
- Everything depends on your weapons. Upgrade the main hand first: it strikes for full damage.
- Two-handed weapons, staffs and bows can't be paired with an off-hand weapon. A two-hander with a
  shield is the defensive choice; two one-handers hit much harder.
- `remove offhand` takes the off-hand weapon off; `eq` shows it as `offhand:`.
- With no mana, you never have to drink mana potions. Spend that gold on healing potions.

## Gear

Wear the best **plate** you can find. Carry the best two one-handed weapons you can find (two copies of the
same one work), or a two-hander and a shield when you want armor over damage. You want STR first (damage), then
CON (HP).

Notable late gear a Warrior can use: the obsidian greatblade (45, two-handed), the Khopesh of Ussreth
(48, sword), Flameheart (50, blunt, from Rekkn), Tidecaller (50, two-handed, from Nerevos), Gravesong
(50, sword, from Morthis), the Mountainheart Shield (50, from Ulmathra), gauntlets of the pyre (50,
plate), dreamsilver greaves (50, plate), stonestride boots (50, plate), and the mythic weapons that
anyone may wield: the Fang of Pyraxis and Eternity.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a darning-needle sword
(7, sword, DEX/STR), a whisker-strung bow (9, bow, DEX) and a beetle-shell shield (8, shield, CON). Old
Tom the cat drops the whisker-strung bow.

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

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): a frost-varnished bow (37, bow, DEX/WIS), an antler maul (39, two-handed, STR/CON),
gauntlets of the painted king (41, plate hands, STR/CON), sea-varnish greaves (37, plate legs, CON/STR),
gilt sabatons (38, plate feet, CON/STR) and a gilt frame shield (39, shield, CON). The White Stag drops
the antler maul; the Painted King of Elandor drops his gauntlets; the Saltmere Serpent drops sea-varnish
greaves.

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): a gearwork blade (42,
sword, STR/DEX), a clockwork pruning axe (41, axe, STR/CON), Orrin's great wrench (44, blunt,
STR/WIS/CON), a clockwork warhelm (43, plate head, CON/STR), piston sabatons (43, plate feet, CON/STR)
and a cog shield (43, shield, CON). The Master Automaton drops the gearwork blade; Orrin Gearwhistle
drops his great wrench.

From **Thornwick Hall** (43-49, west of the Stag Walk): the Vane longsword (49, sword) and the Vane
heirloom plate (49, plate chest) from Lord Aldric Vane, the Vane warhelm (46) and gauntlets (45) from
his knights and sworn swords, Mistress Hollin's cleaver (45, axe), Mr. Graves's silver salver (45,
shield), the Vane signet (49, ring) and Great-aunt Mathilde's cameo (46, neck).

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): a gingerbread
shield (47, shield, CON/STR). It drops from her gingerbread soldiers.

## Best races

- **Ogre**: the highest STR and CON, plus +12% HP. The classic choice.
- **Orc**: +6% damage, good STR and CON.
- **Troll**: regenerates in combat, which helps a class with only one heal.
- **Human**: +5% HP and +5% damage.

## How it performs

The Warrior wins every same-level fight in the simulator. It takes 4-6 rounds a fight up to level 20
and 4-5 from 25 (7 around 40), finishing with 58-86% HP. It survives about 3 fights in
a row at level 10, 7-8 at 20 and the simulator's cap of 8 at 30. It beat every world boss in the
simulator, at the boss's own level and at boss level +3.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Warrior life brings the **best STR and CON growth in the game** (shared with the Dread Knight) and
the **highest HP per level** (13), so every later life is as tough as a Warrior: a wizard reborn after
it has a Warrior's HP pool. It also gives **plate armor and shield training**, every weapon except
staffs and wands, and **Dual Wield** (1) and **Double Attack** (10) in every later life, so a
wizard reborn after it swings twice with each hand. The rogue shares both passives, the bard has Dual
Wield and the ranger, paladin and dread knight have Double Attack, so a Warrior life is not the only
way to get them. Second Wind and Shield Wall are free, so they work in any later class.
