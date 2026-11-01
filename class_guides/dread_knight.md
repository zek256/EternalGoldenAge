# Dread Knight

> *Dark champions who bargain with death, draining the life of their foes.*

The Dread Knight is the dark mirror of the Paladin: a plate-wearing fighter whose magic is drawn from
INT instead of WIS. Instead of heals it has **drains and lifesteal**, so it heals itself by hurting
things. It also has a disease, a fear aura that weakens every foe, and Dread Touch, the hardest single
free hit in the game for its level. It has the second-highest HP of any class.

## At a glance

| | |
|---|---|
| HP per level | 10 |
| Mana per level | 3 |
| Attack stat | STR |
| Spell stat | INT |
| Starting bonus | STR +2, INT +2, CON +1 |
| Gains per level | STR +2, CON +2, INT +1 |
| Armor | Plate (and everything lighter) |
| Shield | Yes |
| Weapons | Sword, axe, two-handed |
| Starting gear | Rusty shortsword (2-5), wooden shield, padded tunic, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | STR | INT | CON | Weapon damage |
|---|---|---|---|---|---|---|
| 1 | 25 | 19 | 12 | 12 | 11 | 6-9 |
| 10 | 198 | 66 | 30 | 21 | 29 | 17-20 |
| 25 | 630 | 180 | 60 | 36 | 59 | 35-38 |
| 50 | 1750 | 470 | 110 | 61 | 109 | 65-68 |

## Spells and abilities

Abilities are free (`ab <name>`); spells cost mana (`cast <name>`). Cost is shown at the level you
learn it and at level 50.

| Level | Name | Type | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|---|
| 1 | **Shadow Strike** | ability | free | 2 | one foe | 1.2x weapon damage, plus a drain of 3 + 1/level + 0.3 INT (~7 at L1, ~71 at L50) that heals you for 60% of what it deals |
| 4 | **Disease Cloud** | spell | 8 / 35 | - | one foe | Disease damage over time: 4 + 1/level + 0.25 INT per round for 5 rounds (~11 at L4, ~69 at L50) |
| 10 | **Dread Aura** | spell | 23 / 71 | 6 | all foes | Every foe deals 25% less damage for 5 rounds |
| 18 | **Dread Touch** | ability | free | 20 | one foe | Shadow damage of 40 + 5/level + 1.5 INT (~173 at L18, ~381 at L50) |
| 26 | **Vampiric Embrace** | spell | 84 / 142 | 8 | self | Your weapon hits heal you for 25% of the damage they deal, for 6 rounds |
| 34 | **Death Coil** | spell | 138 / 189 | 3 | one foe | Drain of 30 + 3.2/level + 0.9 INT (~179 at L34, ~244 at L50) that heals you for 80% of what it deals |
| 44 | **Unholy Frenzy** | ability | free | 12 | self | +50% damage and 30% lifesteal for 5 rounds |

## How to play

**Levels 1-9.** Shadow Strike every other round. It hits harder than an auto-attack and heals you a
little each time. Disease Cloud at 4 is cheap: put it on anything that will take more than a couple
of rounds to kill.

**Levels 10-25.** Dread Aura cuts every enemy's damage by a quarter for five rounds, and its
cooldown is six, so you can keep it up nearly all the time in a hard fight. Open with it against
groups and bosses. At 18 you get Dread Touch, a huge free nuke on a long cooldown (20 rounds). Use it
to open a boss fight or to finish a dangerous monster fast.

**Levels 26-50.** Vampiric Embrace turns every weapon hit into healing. With it up, Shadow Strike
heals you twice. Death Coil at 34 is a big drain that heals for 80% of what it deals, usable every
three rounds. At 44, Unholy Frenzy stacks with Vampiric Embrace (55% lifesteal and +50% damage): in a
long fight, buff with both and you will often out-heal the damage coming in.

**Tips**
- Your healing all comes from dealing damage, so a Dread Knight does worst when it is stunned or can't
  hit. Keep Dread Aura up against monsters that stun.
- Lifesteal only works on physical damage, so it heals from your weapon hits and abilities like
  Shadow Strike, not from spells.
- Drains and Disease Cloud ignore armor, which helps against golems and plated monsters.

## Gear

Wear **plate** and a shield. STR first, then CON; INT feeds Dread Touch, the drains and your mana.

Notable late gear: **Gravesong** (50, sword, from Morthis in the Plane of Death), the Khopesh of
Ussreth (48, sword), Tidecaller (50, two-handed), the obsidian greatblade and crescent greatsword
(two-handed), the Mountainheart Shield, plate from the elemental lords, and the mythic Fang of Pyraxis
and Eternity.

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Strongman's
breastplate (27, plate chest) and the brass ring (27, ring).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): the Headsman's axe (32),
a bailiff's halberd (36, two-handed), a warden's greathelm (35) and sabatons (34) (plate), the shield
of the scales (35) and the High Justice's chain of office (38, neck).

From **Thornwick Hall** (43-49, west of the Stag Walk): the Vane longsword (49, sword) and the Vane
heirloom plate (49, plate chest) from Lord Aldric Vane, the Vane warhelm (46) and gauntlets (45),
Mistress Hollin's cleaver (45, axe), Mr. Graves's silver salver (45, shield) or, for more INT, Tobias's
black grimoire (47, off-hand), and the Vane signet (49, ring).

## Best races

- **Ogre**: high STR and CON, +12% HP.
- **Orc**: +6% damage, which also raises your drains.
- **Undead**: immune to poison and disease damage over time, and fits the theme.
- **Dark elf**: +5% crit and better INT, for a caster-leaning knight.

## How it performs

The Dread Knight wins every same-level fight in the simulator in 3-5 rounds and finishes with 70-93%
HP, one of the best results of any melee class. It lasts about 4 fights in a row at both level 10
and level 30, and it beat every world boss at the boss's own level.

## Rebirth

A Dread Knight life leaves you **+98 STR, +98 CON and +49 INT**, plus **plate armor and shield
training** and sword, axe and two-handed weapons. Shadow Strike, Dread Touch and Unholy Frenzy are
free abilities, so any later class keeps a strong free nuke and a lifesteal buff. It is almost as good
a past life as the Warrior, with more INT and less DEX.
