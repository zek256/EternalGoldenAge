# Paladin

> *Holy knights sworn to the Dawnfather, wielding sacred light and steel alike.*

The Paladin is a plate-wearing fighter with a small pool of holy magic. It hits with its weapon like
a Warrior, but it adds holy damage to its main strike, carries the biggest emergency heal in the game
(Lay on Hands, 60% of your health), and later gains a damage shield and an area spell that heals as
it burns. It is one of the safest classes to level.

## At a glance

| | |
|---|---|
| HP per level | 10 |
| Mana per level | 3 |
| Spell stat | WIS |
| Starting bonus | STR +2, WIS +2, CON +1 |
| Gains per level | STR +2, CON +1, WIS +1, CHA +1 |
| Armor | Plate (and everything lighter) |
| Shield | Yes |
| Weapons | Sword, blunt, two-handed |
| Starting gear | Training mace (2-5), wooden shield, padded tunic, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | STR | WIS | CON | Weapon damage |
|---|---|---|---|---|---|---|
| 1 | 25 | 19 | 12 | 12 | 11 | 6-9 |
| 10 | 180 | 66 | 30 | 21 | 20 | 17-20 |
| 25 | 510 | 180 | 60 | 36 | 35 | 35-38 |
| 50 | 1260 | 470 | 110 | 61 | 60 | 65-68 |

CHA does nothing for a Paladin. It is a leftover of the class's flavour.

## Spells and abilities

Abilities are free (`ab <name>`); spells cost mana (`cast <name>`). Cost is shown at the level you
learn it and at level 50.

| Level | Name | Type | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|---|
| 1 | **Holy Strike** | ability | free | 2 | one foe | 1.2x weapon damage plus holy damage of 3 + 1/level + 0.3 WIS (~7 at L1, ~71 at L50) |
| 5 | **Lay on Hands** | ability | free | 20 | self | Heal 60% of max HP |
| 10 | **Blessing of Might** | spell | 19 / 59 | 6 | self | +25% damage for 6 rounds |
| 18 | **Divine Shield** | spell | 59 / 130 | 10 | self | Absorbs 20 + 4/level + 1.0 WIS damage (~121 at L18, ~281 at L50) |
| 26 | **Hammer of Justice** | ability | free | 6 | one foe | 1.6x weapon damage, 90% chance to stun for 2 rounds (45% vs bosses) |
| 36 | **Consecration** | spell | 171 / 224 | 3 | all foes | Holy damage 25 + 2.6/level + 0.7 WIS to every foe (~151 at L36, ~197 at L50), and heals you 10 + 1.5/level + 0.3 WIS (~78-103) |
| 46 | **Avenging Wrath** | ability | free | 12 | self | Heal 30% of max HP and +60% damage for 5 rounds |

## How to play

**Levels 1-9.** Holy Strike every other round is your whole rotation. It costs nothing and adds a
little holy damage that ignores armor. From 5, Lay on Hands is a 60% heal on a 20-round cooldown:
use it once per hard fight when you drop below about 40%.

**Levels 10-25.** Blessing of Might is cheap and lasts as long as its cooldown, so you can keep
+25% damage up all the time. Cast it before you attack. Divine Shield at 18 absorbs a big chunk of
damage; cast it before a boss or when you see a big hit coming. Your mana pool is small, so these
two spells are most of what you can afford.

**Levels 26-50.** Hammer of Justice is a strong hit with a very reliable 2-round stun. Stun the
monster that is hurting you most, then work on it. Consecration at 36 is your area attack and a heal
at the same time, but it is expensive: use it on groups of two or more. Avenging Wrath at 46 is a
second big heal plus +60% damage; with Lay on Hands you have two emergency buttons.

**Tips**
- Most of your damage is physical, so armor matters, but Holy Strike's holy part, and Consecration,
  ignore it.
- A boss fight goes: Blessing of Might, Divine Shield, then Holy Strike and Hammer of Justice on
  cooldown, with Lay on Hands and Avenging Wrath as your heals.
- Watch your mana. A Paladin can run dry in a long fight if it casts Consecration too freely.

## Gear

Wear **plate** and a shield. STR first, then CON; WIS helps your shield and Consecration.

Signature late gear: **the Lightbearer's Oath** (50, sword, STR/WIS/CON) and **the Shield of
Judgement** (50, shield, CON/WIS), both from Stalworth Lightbearer in the Plane of Law, a fellow
paladin. Also good: the Sunforged Mace (43, blunt, STR/WIS), Flameheart (50, blunt), Tidecaller and
the obsidian greatblade (two-handed), the Mountainheart Shield, and the mythic Fang of Pyraxis and
Eternity.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a darning-needle sword
(7, sword, DEX/STR), a beetle-shell shield (8, shield, CON) and an amber pendant (10, neck,
WIS/CHA/CON). The Wasp Queen drops the amber pendant.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): the shelfcap breastplate (15,
plate chest), a rootmaul (16, two-handed), a shelf-fungus shield (14), the Mycelial Crown (20, any
class) and the rootbound ring (20, CON/WIS/STR).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Strongman's
breastplate (27, plate chest), a roustabout's tent mallet (28, blunt) and the brass ring (27, ring).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): the Gavel of the High
Justice (38, blunt, STR/WIS), a bailiff's halberd (36, two-handed), a warden's greathelm (35) and
sabatons (34) (plate), the shield of the scales (35, CON/WIS), and the chain (38, neck) and seal of
office (37, ring).

From **the Painted Gallery** (37-42, behind Elandor's Hall of the Moon Court; each painting is entered
with `enter`): an antler maul (39, two-handed, STR/CON), gauntlets of the painted king (41, plate hands,
STR/CON), sea-varnish greaves (37, plate legs, CON/STR), gilt sabatons (38, plate feet, CON/STR) and a
gilt frame shield (39, shield, CON). The White Stag drops the antler maul; the Painted King of Elandor
drops his gauntlets; the Saltmere Serpent drops sea-varnish greaves.

From **the Clockwork Orchard** (41-44, south of the Chancery's Archive of Wills): a gearwork blade (42,
sword, STR/DEX), Orrin's great wrench (44, blunt, STR/WIS/CON), a clockwork warhelm (43, plate head,
CON/STR), piston sabatons (43, plate feet, CON/STR), a cog shield (43, shield, CON) and the orrery
amulet (44, neck, INT/WIS/STR). The Master Automaton drops the gearwork blade; Orrin Gearwhistle drops
his great wrench and the orrery amulet.

From **Thornwick Hall** (43-49, west of the Stag Walk): the Vane longsword (49, sword) and the Vane
heirloom plate (49, plate chest) from Lord Aldric Vane, the Vane warhelm (46) and gauntlets (45), Mr.
Graves's silver salver (45, shield), the Vane signet (49, ring) and the Dowager's pearls (48, neck,
WIS/CHA/CON).

From **the Sugarwold** (44-49, north of the Scorchsands' Salt Pans): Madame
Marchpane's rolling pin (49, blunt, STR/WIS/CON), a candy-cane mace (47, blunt, STR/WIS) and a
gingerbread shield (47, shield, CON/STR). Madame Marchpane drops the rolling pin; the rest come from her
realm.

## Best races

- **Ogre**: the strongest STR and CON, plus +12% HP.
- **Orc**: +6% damage.
- **Human**: +5% HP, mana and damage. Well rounded for a hybrid.
- **Troll**: regenerates in combat.

## How it performs

The Paladin wins every same-level fight in the simulator, a little slowly (3-7 rounds) but with
plenty of health left (59-96%, above 85% from level 25). It has strong staying power: about 3-4 fights
in a row at level 10 and the simulator's cap of 8 at level 30, among the best of any class. It beat
every world boss at the boss's own level except Rask and Rotheart (97% each), and all of them at boss
level +3.

## Rebirth

In every later life, each of your stats, your HP per level and your mana pool are the best that any
class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Paladin life brings strong STR growth and 10 HP per level, plus **plate armor and shield training**
and sword, blunt and two-handed weapons. Its best gift is its abilities: Lay on Hands and Avenging
Wrath are free, so any later class keeps two big heals that cost no mana, which is very valuable for
fragile casters.
