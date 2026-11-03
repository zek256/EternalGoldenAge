# Paladin

> *Holy knights sworn to the Dawnfather, wielding sacred light and steel alike.*

The Paladin is a plate-wearing fighter with a small pool of holy magic. It hits with its weapon like
a Warrior, but each of its strikes (Holy Strike, Hammer of Justice, Consecration) adds holy damage
that ignores armor. It heals with Holy Light, blesses its arm for the whole fight and later gains a
damage shield. From 15 its weapon may strike twice a round. It is one of the safest classes to level.

## At a glance

| | |
|---|---|
| HP per level | 10 |
| Mana per level | 3 (plus WIS) |
| Spell stats | INT (damage); WIS (healing, shields) |
| Starting bonus | STR +2, WIS +1, INT +1, CON +1 |
| Gains per level | STR +2, CON +1, WIS +1, INT +1 |
| Armor | Plate (and everything lighter) |
| Shield | Yes |
| Weapons | Sword, blunt, two-handed |
| Starting gear | Training mace (2-5), wooden shield, padded tunic, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | STR | CON | INT | WIS | Weapon damage |
|---|---|---|---|---|---|---|---|
| 1 | 102 | 64 | 12 | 11 | 11 | 11 | 6-9 |
| 10 | 729 | 110 | 30 | 20 | 20 | 20 | 17-20 |
| 25 | 2065 | 222 | 60 | 35 | 35 | 35 | 35-38 |
| 50 | 5103 | 510 | 110 | 60 | 60 | 60 | 65-68 |

INT powers the holy damage of Holy Strike and Consecration; WIS powers Divine Shield, Consecration's
heal and your mana.

## Spells and abilities

Abilities are free (`ability <name>`); spells cost mana (`cast <name>`). There are no cooldowns: every attack can be used every round, and each new attack is a modest step up (12%) from the one before it, so **use your newest one**.

| Level | Name | Type | Cost | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Holy Strike** | ability | free | one foe | 1.2x weapon damage (~9 at L1, ~43 at L25, ~79 at L50 with the starting weapon); Holy damage 3 + 1/level + 0.3 INT (~7 at L1, ~38 at L25, ~71 at L50) |
| 5 | **Holy Light** | spell | 11 / 47 | self | Heal 48.6 + 11.34/level + 2.23 WIS (~138 at L5, ~409 at L25, ~749 at L50) |
| 10 | **Blessing of Might** | spell | 19 / 59 | self | +20% damage until the end of the fight |
| 15 | **Double Attack** | passive | - | - | Each hand may strike a second time every round: a 40% chance when learned, rising evenly to certain at level 50. |
| 18 | **Divine Shield** | spell | 65 / 142 | self | A ward that absorbs 81 + 16.2/level + 4.05 WIS damage until it breaks (~486 at L18, ~628 at L25, ~1134 at L50); casting it again restores it |
| 26 | **Hammer of Justice** | ability | free | one foe | 1.34x weapon damage (~50 at L26, ~89 at L50 with the starting weapon); Holy damage 3.36 + 1.12/level + 0.34 INT (~44 at L26, ~79 at L50) |
| 36 | **Consecration** | ability | free | one foe | 1.51x weapon damage (~74 at L36, ~100 at L50 with the starting weapon); Holy damage 3.76 + 1.25/level + 0.38 INT (~66 at L36, ~89 at L50) |

## How to play

**Every fight.** Blessing of Might (from 10) once and Divine Shield (from 18) at the start, then your
newest strike every round: Holy Strike, Hammer of Justice from 26, Consecration from 36. Heal with
Holy Light when you drop under about half health, and recast Divine Shield when it breaks if your
mana allows.

**Tips**
- Your mana pool is small: it goes on Holy Light first. Your strikes are free.
- The holy part of every strike ignores armor.

## Gear

Wear **plate** and a shield. STR first, then CON; WIS helps your shield, heals and mana, and INT your holy damage.

Signature late gear: **the Lightbearer's Oath** (50, sword, STR/WIS/CON) and **the Shield of
Judgement** (50, shield, CON/WIS), both from Stalworth Lightbearer in the Plane of Law, a fellow
paladin. Also good: the Sunforged Mace (43, blunt, STR/WIS), Flameheart (50, blunt), Tidecaller and
the obsidian greatblade (two-handed), the Mountainheart Shield, and the mythic Fang of Pyraxis and
Eternity.

From **the Underhedge** (6-10, `enter mousehole` in Greenmeadow's Willow Mill): a darning-needle sword
(7, sword, DEX/STR), a beetle-shell shield (8, shield, CON) and an amber pendant (10, neck,
WIS/CON). The Wasp Queen drops the amber pendant.

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
WIS/CON).

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

The Paladin wins every same-level fight in the simulator in 5.8-11.7 rounds, finishing with 60-98% HP. It survives about 8, 8 and 8 fights in a row at levels 10, 20 and 30 (the cap is 8). Against the world bosses it beats every one, at the boss's own level and at boss level +3. These figures are from November 2026, after monsters of level 50 and below got three times the HP and 40% of the damage and player HP was raised to match theirs.

## Rebirth

In every later life, each of your stats, your HP per level and your mana per level are the best that
any class you have lived would have at your current level (see the [README](README.md#rebirth)), and each
class mastered adds +2% max HP and damage.

A Paladin life brings strong STR growth and 10 HP per level, plus **plate armor and shield training**
and sword, blunt and two-handed weapons. Holy Light gives any later class a heal that scales with WIS,
and its strikes are free. It also passes on Double Attack to every later life.
