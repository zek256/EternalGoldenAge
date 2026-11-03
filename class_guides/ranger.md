# Ranger

> *Wardens of the wild places, deadly with bow and blade and kin to beasts.*

The Ranger is a STR and DEX fighter that mostly uses free abilities, with a small WIS mana pool for a
heal and an animal companion. Its shots form a ladder from Aimed Shot to Deadeye, Serpent Sting adds a
poison, and from 16 a wolf (called out of combat) soaks up hits for it. From 15 its weapon may strike
twice a round. It has the best staying power of any class in the mid levels.

## At a glance

| | |
|---|---|
| HP per level | 9 |
| Mana per level | 2 (plus WIS) |
| Spell stats | WIS (healing); pets use the higher of the two |
| Starting bonus | STR +2, DEX +2, WIS +1 |
| Gains per level | STR +2, DEX +2, CON +1 |
| Armor | Mail (and everything lighter) |
| Shield | Yes |
| Weapons | Sword, dagger, axe, bow |
| Starting gear | Ash shortbow (2-5), padded tunic, leather boots, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | STR | DEX | CON | WIS | Weapon damage | Miss | Crit | Dodge |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 24 | 18 | 12 | 12 | 10 | 11 | 6-9 | 9.2% | 6.2% | 3.8% |
| 10 | 168 | 46 | 30 | 30 | 19 | 11 | 17-20 | 7.9% | 8.0% | 5.0% |
| 25 | 480 | 92 | 60 | 60 | 34 | 11 | 35-38 | 5.8% | 11.0% | 7.0% |
| 50 | 1200 | 170 | 110 | 110 | 59 | 11 | 65-68 | 2.3% | 16.0% | 10.3% |

STR powers your weapon; DEX makes it land (fewer misses, more crits) and helps you dodge. Your WIS
stays low, so your mana pool is small: Hunter's Mend and the wolf are for when you need them most.

## Spells and abilities

Abilities are free (`ability <name>`); spells cost mana (`cast <name>`). There are no cooldowns: every attack can be used every round, and each new attack is a modest step up (12%) from the one before it, so **use your newest one**.

| Level | Name | Type | Cost | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Aimed Shot** | ability | free | one foe | 1.45x weapon damage (~10 at L1, ~52 at L25, ~96 at L50 with the starting weapon) |
| 4 | **Hunter's Mend** | spell | 8 / 35 | self | Heal 9 + 2/level + 0.45 WIS (~21 at L4, ~63 at L25, ~113 at L50) |
| 10 | **Multishot** | ability | free | one foe | 1.62x weapon damage (~29 at L10, ~59 at L25, ~107 at L50 with the starting weapon) |
| 15 | **Double Attack** | passive | - | - | Each hand may strike a second time every round: a 40% chance when learned, rising evenly to certain at level 50. |
| 16 | **Call Bonded Wolf** | spell | 50 / 118 | self | Summon a grey timber wolf (~205 HP, 26-41 damage at L25); only out of combat, and it stays until it dies |
| 24 | **Serpent Sting** | ability | free | one foe | 1x weapon damage (~35 at L24, ~36 at L25, ~66 at L50 with the starting weapon); Poison damage over time: 8 + 1.4/level + 0.3 STR per round for 5 rounds (~58 at L24, ~61 at L25, ~111 at L50 per round) |
| 34 | **Rain of Arrows** | ability | free | one foe | 1.82x weapon damage (~86 at L34, ~121 at L50 with the starting weapon) |
| 45 | **Deadeye** | ability | free | one foe | 2.04x weapon damage (~123 at L45, ~135 at L50 with the starting weapon) |

## How to play

**Before every fight.** Call your Bonded Wolf (from 16) if it is not with you: it can't be called in
combat.

**Every fight.** Your newest shot every round: Aimed Shot, Multishot from 10, Rain of Arrows from 34,
Deadeye from 45. From 24, Serpent Sting once at the start adds a poison for 5 rounds. Heal with
Hunter's Mend when you drop under about half health.

**Tips**
- Your shots scale with your weapon: a bow is the classic choice, but any trained weapon works.
- The wolf draws about a quarter of the attacks aimed at you.

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

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): a frost-varnished bow (37, bow, DEX/WIS), painted moonsteel gauntlets (39, mail hands,
STR/DEX) and a gilt frame shield (39, shield, CON).

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): a gearwork blade (42,
sword, STR/DEX), a clockwork pruning axe (41, axe, STR/CON), a brass gear-helm (43, mail head, CON/STR),
a brass-scale hauberk (43, mail chest, CON/DEX) and a cog shield (43, shield, CON). The Master Automaton
drops the gearwork blade.

From **Thornwick Hall** (43-49, west of the Stag Walk): the Vane hunting bow (45, bow, DEX/WIS) from
Hobb the gamekeeper, Sir Corwin's rapier (47, sword, DEX), Lady Seraphine's hairpin (47, dagger, DEX),
the Vane huntsman's jerkin (44) and breeches (43) (leather), Mr. Graves's silver salver (45, shield)
and Great-aunt Mathilde's cameo (46, neck).

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): a gingerbread
shield (47, shield, CON/STR), gingerbread gauntlets (46, mail hands, STR/DEX), toffee-glazed greaves
(46, mail legs, CON/STR), peppermint-scale boots (45, mail feet, CON/DEX) and a ring of spun sugar (48,
ring, DEX/CON/INT). Madame Marchpane drops the ring of spun sugar; the rest come from her realm.

## Best races

- **Orc**: STR 13 and +6% damage.
- **Human**: +5% HP, mana and damage.
- **Dark elf**: +5% crit.
- **Elf**: +4% dodge and +2% crit.

## How it performs

The Ranger wins every same-level fight in the simulator in 2.7-4.5 rounds, finishing with 63-90% HP. It survives about 5, 8 and 8 fights in a row at levels 10, 20 and 30 (the cap is 8). Against the world bosses it wins 95-100% at the boss's own level and 100% at boss level +3. These figures are from November 2026, after cooldowns were removed.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Ranger life brings strong STR and DEX growth (matching the Rogue), plus **mail armor and shield
training** and sword, dagger, axe and bow weapons. Its shots are free abilities that scale with your
weapon, so they work in any later life that keeps a good weapon. It also passes on Double Attack to
every later life.
