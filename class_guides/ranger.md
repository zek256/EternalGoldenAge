# Ranger

> *Wardens of the wild places, deadly with bow and blade and kin to beasts.*

The Ranger is a STR and DEX fighter that mostly uses free abilities, with a small WIS mana pool for a heal
and an animal companion. It hits hard and often, gets an area attack early, crits more than most
classes, and from level 16 brings a wolf that soaks up hits for it. It has the best staying power of
any class in the mid levels.

## At a glance

| | |
|---|---|
| HP per level | 9 |
| Mana per level | 2 |
| Spell stat | WIS |
| Starting bonus | STR +2, DEX +2, WIS +1 |
| Gains per level | STR +2, DEX +2, CON +1 |
| Armor | Mail (and everything lighter) |
| Shield | Yes |
| Weapons | Sword, dagger, axe, bow |
| Starting gear | Ash shortbow (2-5), padded tunic, leather boots, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | STR | DEX | CON | Weapon damage | Miss | Crit | Dodge |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 24 | 18 | 12 | 12 | 10 | 6-9 | 9.2% | 6.2% | 3.8% |
| 10 | 168 | 46 | 30 | 30 | 19 | 17-20 | 7.9% | 8.0% | 5.0% |
| 25 | 480 | 92 | 60 | 60 | 34 | 35-38 | 5.8% | 11.0% | 7.0% |
| 50 | 1200 | 170 | 110 | 110 | 59 | 65-68 | 2.3% | 16.0% | 10.3% |

STR powers your weapon; DEX makes it land (fewer misses, more crits) and helps you dodge. Your WIS
stays low, so your mana pool is small: Hunter's Mend and the wolf are for when you need them most.

## Spells and abilities

Abilities are free (`ab <name>`); spells cost mana (`cast <name>`). Cost is shown at the level you
learn it and at level 50. Weapon damage is the average with the starting bow.

| Level | Name | Type | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|---|
| 1 | **Aimed Shot** | ability | free | 2 | one foe | 1.6x weapon damage (~13 at L1, ~106 at L50) |
| 4 | **Hunter's Mend** | spell | 8 / 35 | - | self | Heal 9 + 2/level + 0.45 WIS (~23 at L4, ~136 at L50) |
| 10 | **Multishot** | ability | free | 3 | all foes | 0.95x weapon damage to every foe |
| 16 | **Call Bonded Wolf** | spell | 50 / 118 | 10 | self | Summon a grey timber wolf (~150 HP, 19-30 damage at L16; ~405 HP, 52-80 at L50) |
| 24 | **Serpent Sting** | ability | free | 4 | one foe | 0.9x weapon damage plus poison: 8 + 1.4/level + 0.3 STR per round for 5 rounds (~59 at L24, ~111 at L50) |
| 34 | **Rain of Arrows** | ability | free | 4 | all foes | 1.6x weapon damage to every foe |
| 45 | **Deadeye** | ability | free | 5 | one foe | 3.6x weapon damage (~217 at L45, ~239 at L50) |

## How to play

**Levels 1-15.** Aimed Shot every other round is most of your damage. Hunter's Mend is a cheap heal;
your mana pool is small, so it is your main use for mana. Multishot at 10 handles groups.

**Levels 16-33.** Call the wolf before you go hunting and keep it alive. It attacks every round and
takes about a quarter of the enemies' normal attacks, which is a lot of damage you don't take. Its
stats are fixed when you call it, so call it again every few levels. Serpent Sting at 24 adds strong
poison damage that ignores armor: use it on anything tough, then alternate Aimed Shot.

**Levels 34-50.** Rain of Arrows is a full-power area attack (1.6x on every foe every four rounds),
and Deadeye at 45 is your big single-target hit. A boss rotation: wolf up, Serpent Sting, Deadeye,
Aimed Shot, and Serpent Sting again when it wears off.

**Tips**
- Your attacks are physical, so armored monsters resist them. Serpent Sting's poison does not.
- Bows are your best weapons but you can also use a sword or axe with a shield for extra armor.
- If the wolf dies mid-fight, recall it as soon as the cooldown allows.

## Gear

Wear **mail** (or leather) and a bow. STR and DEX first, then CON; WIS feeds Hunter's Mend and the wolf.

Signature late gear: **Stormcaller** (50, bow, DEX/WIS/CON), dropped by Caelestra in the Plane of
Stars. Also good: the dune recurve bow (40), Dragonscale Mail (48, mail), **tidescale legguards** (50,
mail legs, from Nerevos), **the Ferryman's gloves** (50, leather, from Morthis), the sunsteel mail set (40),
windwalker boots (50, leather, DEX), the Band of the Four Winds (50, ring, DEX), and the mythic Fang
of Pyraxis and Eternity.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a darning-needle sword
(7, sword, DEX/STR), the Wasp Queen's stinger (10, dagger, DEX/STR), a whisker-strung bow (9, bow, DEX)
and a beetle-shell shield (8, shield, CON). The Wasp Queen drops her stinger; Old Tom the cat drops the
whisker-strung bow.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): a capshell hauberk (17, mail
chest), rootweave chausses (16, mail legs), mossfelt boots (15, leather), a sporethorn knife (18,
dagger, DEX), a shelf-fungus shield (14) and the Mycelial Crown (20, any class).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): a knife-thrower's
blade (29, dagger, DEX), a roustabout's chain chausses (27, mail legs), an acrobat's grips (26,
leather) and the brass ring (27, ring).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): a bailiff's hauberk (34,
mail chest), the Headsman's axe (32), a scrivener's penknife (33, dagger, DEX) and the shield of the
scales (35).

From **Thornwick Hall** (43-49, west of the Stag Walk): the Vane hunting bow (45, bow, DEX/WIS) from
Hobb the gamekeeper, Sir Corwin's rapier (47, sword, DEX), Lady Seraphine's hairpin (47, dagger, DEX),
the Vane huntsman's jerkin (44) and breeches (43) (leather), Mr. Graves's silver salver (45, shield)
and Great-aunt Mathilde's cameo (46, neck).

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): a gingerbread
shield (47, shield, CON/STR), gingerbread gauntlets (46, mail hands, STR/DEX), toffee-glazed greaves
(46, mail legs, CON/STR), peppermint-scale boots (45, mail feet, CON/DEX) and a ring of spun sugar (48,
ring, DEX/CON/CHA). Madame Marchpane drops the ring of spun sugar; the rest come from her realm.

## Best races

- **Orc**: STR 13 and +6% damage.
- **Human**: +5% HP, mana and damage.
- **Dark elf**: +5% crit.
- **Elf**: +4% dodge and +2% crit.

## How it performs

The Ranger wins every same-level fight in the simulator, a little slowly at low levels (4-6 rounds)
and quickly later (about 3-4 rounds from level 25), finishing with 51-83% HP. It lasts about 4 fights
in a row at level 10 and the simulator's cap of 8 at level 30. Its weak point is the hardest bosses:
about 83% against the High Justice, Ussreth and Pyraxis at the boss's own level, and 93% against
Pyraxis at boss level +3. It beats every other boss at boss level +3.

## Rebirth

In every later life, each of your stats, your HP per level and your mana pool are the best that any
class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Ranger life brings strong STR and DEX growth (matching the Rogue), plus **mail armor and shield
training** and sword, dagger, axe and bow weapons. Aimed Shot, Multishot, Rain of Arrows and Deadeye
are free abilities that scale with your weapon, and every class swings with STR, so they work in any
later life that keeps a good weapon.
