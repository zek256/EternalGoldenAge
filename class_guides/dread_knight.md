# Dread Knight

> *Dark champions who bargain with death, draining the life of their foes.*

The Dread Knight is the dark mirror of the Paladin: a plate-wearing fighter whose magic is drawn from
INT instead of WIS. Instead of heals it has **drains and lifesteal**: each of its strikes (Shadow
Strike, Dread Touch, Death Coil) drains life to heal it, and two whole-fight buffs add lifesteal. It
also has a disease and a fear aura that weakens a foe for the whole fight. It shares the second-highest
HP of any class with the Paladin.

## At a glance

| | |
|---|---|
| HP per level | 10 |
| Mana per level | 3 (plus WIS) |
| Spell stats | INT (damage) |
| Starting bonus | STR +2, INT +1, WIS +1, CON +1 |
| Gains per level | STR +2, CON +1, INT +1, WIS +1 |
| Armor | Plate (and everything lighter) |
| Shield | Yes |
| Weapons | Sword, axe, two-handed |
| Starting gear | Rusty shortsword (2-5), wooden shield, padded tunic, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | STR | CON | INT | WIS | Weapon damage |
|---|---|---|---|---|---|---|---|
| 1 | 25 | 19 | 12 | 11 | 11 | 11 | 6-9 |
| 10 | 180 | 65 | 30 | 20 | 20 | 20 | 17-20 |
| 25 | 510 | 177 | 60 | 35 | 35 | 35 | 35-38 |
| 50 | 1260 | 465 | 110 | 60 | 60 | 60 | 65-68 |

## Spells and abilities

Abilities are free (`ability <name>`); spells cost mana (`cast <name>`). There are no cooldowns: every attack can be used every round, and each new attack is a modest step up (12%) from the one before it, so **use your newest one**.

| Level | Name | Type | Cost | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Shadow Strike** | ability | free | one foe | 1.2x weapon damage (~9 at L1, ~43 at L25, ~79 at L50 with the starting weapon); Shadow drain 3 + 1/level + 0.3 INT (~7 at L1, ~38 at L25, ~71 at L50) that heals you for 50% of what it deals |
| 4 | **Disease Cloud** | spell | 8 / 35 | one foe | Disease damage over time: 4 + 1/level + 0.25 INT per round for 5 rounds (~11 at L4, ~37 at L25, ~69 at L50 per round) |
| 10 | **Dread Aura** | spell | 23 / 71 | one foe | The foe deals 20% less damage for the rest of the fight |
| 15 | **Double Attack** | passive | - | - | Each hand may strike a second time every round: a 40% chance when learned, rising evenly to certain at level 50. |
| 18 | **Dread Touch** | ability | free | one foe | 1.34x weapon damage (~38 at L18, ~48 at L25, ~89 at L50 with the starting weapon); Shadow drain 3.36 + 1.12/level + 0.34 INT (~33 at L18, ~43 at L25, ~79 at L50) that heals you for 50% of what it deals |
| 26 | **Vampiric Embrace** | spell | 84 / 142 | self | 15% lifesteal on weapon hits until the end of the fight |
| 34 | **Death Coil** | ability | free | one foe | 1.51x weapon damage (~71 at L34, ~100 at L50 with the starting weapon); Shadow drain 3.76 + 1.25/level + 0.38 INT (~62 at L34, ~89 at L50) that heals you for 50% of what it deals |
| 44 | **Unholy Frenzy** | ability | free | self | +20% damage, 10% lifesteal on weapon hits until the end of the fight |

## How to play

**Every fight.** Dread Aura (from 10) once on the foe, Vampiric Embrace (from 26) and Unholy Frenzy
(from 44) once each, Disease Cloud once, then your newest strike every round: Shadow Strike, Dread
Touch from 18, Death Coil from 34. Every strike heals you for half of its drain.

**Tips**
- Your healing all comes from dealing damage, so heavily armored foes are your hardest fights.
- From 15, Double Attack adds extra weapon hits, which Vampiric Embrace turns into more healing.

## Gear

Wear **plate** and a shield. STR first, then CON; INT feeds Dread Touch and the drains, and WIS your mana.

Notable late gear: **Gravesong** (50, sword, from Morthis in the Plane of Death), the Khopesh of
Ussreth (48, sword), Tidecaller (50, two-handed), the obsidian greatblade and crescent greatsword
(two-handed), the Mountainheart Shield, plate from the elemental lords, and the mythic Fang of Pyraxis
and Eternity.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a darning-needle sword
(7, sword, DEX/STR) and a beetle-shell shield (8, shield, CON).

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): the shelfcap breastplate (15,
plate chest), a rootmaul (16, two-handed), a shelf-fungus shield (14), the Mycelial Crown (20, any
class) and the rootbound ring (20).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Strongman's
breastplate (27, plate chest) and the brass ring (27, ring).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): the Headsman's axe (32),
a bailiff's halberd (36, two-handed), a warden's greathelm (35) and sabatons (34) (plate), the shield
of the scales (35) and the High Justice's chain of office (38, neck).

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): an antler maul (39, two-handed, STR/CON), gauntlets of the painted king (41, plate hands,
STR/CON), sea-varnish greaves (37, plate legs, CON/STR), gilt sabatons (38, plate feet, CON/STR) and a
gilt frame shield (39, shield, CON). The White Stag drops the antler maul; the Painted King of Elandor
drops his gauntlets; the Saltmere Serpent drops sea-varnish greaves.

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): a gearwork blade (42,
sword, STR/DEX), a clockwork pruning axe (41, axe, STR/CON), a clockwork warhelm (43, plate head,
CON/STR), piston sabatons (43, plate feet, CON/STR) and a cog shield (43, shield, CON). The Master
Automaton drops the gearwork blade.

From **Thornwick Hall** (43-49, west of the Stag Walk): the Vane longsword (49, sword) and the Vane
heirloom plate (49, plate chest) from Lord Aldric Vane, the Vane warhelm (46) and gauntlets (45),
Mistress Hollin's cleaver (45, axe), Mr. Graves's silver salver (45, shield) or, for more INT, Tobias's
black grimoire (47, off-hand), and the Vane signet (49, ring).

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): a gingerbread
shield (47, shield, CON/STR). It drops from her gingerbread soldiers.

## Best races

- **Ogre**: high STR and CON, +12% HP.
- **Orc**: +6% damage, which also raises your drains.
- **Undead**: immune to poison and disease damage over time, and fits the theme.
- **Dark elf**: +5% crit and better INT, for a caster-leaning knight.

## How it performs

The Dread Knight wins every same-level fight in the simulator in 2.5-5.2 rounds, finishing with 81-96% HP. It survives about 5, 8 and 8 fights in a row at levels 10, 20 and 30 (the cap is 8). Against the world bosses it beats every one, at the boss's own level and at boss level +3. These figures are from November 2026, after cooldowns were removed.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Dread Knight life brings the **best STR growth in the game** (shared with several classes) and
10 HP per level, plus **plate armor and shield training** and sword, axe and two-handed weapons. Its
strikes and Unholy Frenzy are free, so any later class keeps a self-healing strike and a lifesteal
buff. It also passes on Double Attack to every later life.
