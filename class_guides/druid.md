# Druid

> *Keepers of the old groves who call upon root, thorn, moon and storm.*

The Druid is a WIS caster in leather who mixes damage, healing and control. It has a cheap nuke from
level 1, a heal that keeps working after you cast it, roots that can hold a foe for two rounds, a moon
spell that burns and lingers, and a group attack from 32. It is one of the fastest killers in the
mid-levels and very steady overall.

## At a glance

| | |
|---|---|
| HP per level | 7 |
| Mana per level | 5 |
| Attack stat | STR |
| Spell stat | WIS |
| Starting bonus | WIS +3, INT +1, CON +1 |
| Gains per level | WIS +2, INT +1, CON +1, DEX +1 |
| Armor | Leather (and cloth) |
| Shield | No |
| Weapons | Staff, blunt, dagger |
| Starting gear | Oak staff (1-4), padded tunic, leather boots, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | WIS | CON | DEX | Weapon damage |
|---|---|---|---|---|---|---|
| 1 | 22 | 21 | 14 | 11 | 10 | 5-8 |
| 10 | 150 | 97 | 32 | 20 | 19 | 9-12 |
| 25 | 435 | 295 | 62 | 35 | 34 | 17-20 |
| 50 | 1110 | 825 | 112 | 60 | 59 | 29-32 |

The Druid's INT gain does nothing for its own spells; it only helps if a later life uses INT.

## Spells

All Druid magic is spells, cast with `cast <name>`. Cost is shown at the level you learn it and at
level 50.

| Level | Spell | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Thornlash** | 5 / 30 | - | one foe | Nature damage 7 + 1.6/level + 0.48 WIS (~15 at L1, ~76 at L25, ~140 at L50) |
| 3 | **Regrowth** | 8 / 41 | - | self | Heal 10 + 2/level + 0.5 WIS now, then 4 + 1.2/level + 0.25 WIS per round for 5 rounds (~91 + 49/round at L25) |
| 8 | **Entangling Roots** | 17 / 59 | 4 | one foe | Small nature damage, and a 75% chance to hold it for 2 rounds (about 38% vs bosses) |
| 15 | **Moonfire** | 43 / 106 | - | one foe | Arcane damage 16 + 2.4/level + 0.7 WIS (~81 at L15, ~214 at L50), then 5 + 1/level + 0.25 WIS per round for 4 rounds |
| 22 | **Barkskin** | 50 / 94 | 10 | self | +15 + 2.5/level armor for 6 rounds (+70 at L22, +140 at L50), and a small heal every round |
| 32 | **Starfall** | 184 / 266 | 3 | all foes | Arcane damage 34 + 3.2/level + 0.95 WIS to every foe (~208 at L32, ~300 at L50) |
| 44 | **Wrath of the Wild** | 318 / 354 | 5 | one foe | Nature damage 55 + 4.2/level + 1.25 WIS (~364 at L44, ~405 at L50), and heals you for 20% of your max HP |

## How to play

**Levels 1-14.** Thornlash is cheap and hits well; it is your attack. Regrowth heals a bit now and more
over five rounds, so cast it early in a fight that is going to hurt. Entangling Roots at 8 holds a foe
for two rounds: root the dangerous one, Thornlash it, and root again when the cooldown is up.

**Levels 15-31.** Moonfire hits harder than Thornlash and leaves a burn on the target; open with it,
then Thornlash while it burns, and reapply when it runs out. Barkskin at 22 is a big armor boost with a
little healing for six rounds: cast it before tough fights.

**Levels 32-50.** Starfall is your group attack, every three rounds. Wrath of the Wild at 44 is a huge
hit that also heals 20% of your health, so it doubles as an emergency heal. Against a boss: Barkskin,
Moonfire, Wrath of the Wild on cooldown, Thornlash in between, Roots when you need a breather, Regrowth
to top up.

**Tips**
- All your damage ignores armor.
- The roots are your safety net. A rooted monster does nothing for two rounds.
- Leather and no shield makes you softer than a Cleric or Shaman, so keep Barkskin up in long fights.

## Gear

Wear **leather**; no shields. WIS first, then CON.

Notable late gear: **the Dreamweaver's Staff** (50, staff, INT/WIS/CHA, from Somnara in the Plane of
Dreams), the dragonbone staff (47), the sunfire staff (40), the Sunforged Mace (43, blunt), drakehide
and windwalker boots (leather), the Death Mask (50, leather), the Pearl of the Deep (50, ring), the
Ring of the Archmage, and the mythic Fang of Pyraxis and Eternity.

From **the Mycelial Wards** (14-20, west of Westmarch's Old Watchtower): the Heartspore staff (20,
staff, INT/WIS) from the First Spore, mossfelt boots (15, leather), a glowcap pendant (16, neck), the
Mycelial Crown (20) and the rootbound ring (20, CON/WIS).

From **the Carnival That Never Closes** (26-30, south of the Badlands' Howling Pit): the Ringmaster's
scarlet coat (30, leather chest), a fortune teller's crystal ball (28, off-hand, INT/WIS), a
roustabout's tent mallet (28, blunt), a pair of dancing slippers (27, cloth) and the brass ring (27,
ring).

From **the Chancery of the Dead** (32-38, south of the Dustway's Gnoll Scrub): the Gavel of the High
Justice (38, blunt, STR/WIS), the seal of office (37, ring) and the chain of office (38, neck).

From **Thornwick Hall** (43-49, west of the Stag Walk): a gown of green brocade (47, cloth chest,
INT/WIS/CHA) from Lady Seraphine, silk evening gloves (46, cloth), Tobias's black grimoire (47,
off-hand), the Dowager's pearls (48, neck) and the Vane huntsman's jerkin (44, leather) if you want
armor over WIS.

## Best races

- **High elf**: WIS 13 and +12% mana.
- **Human**: +5% HP, mana and damage.
- **Elf**: +4% dodge and +2% crit, to cover your light armor.

## How it performs

The Druid wins every same-level fight in the simulator, and fast: about 2 rounds at level 15 and
under 4 later, with 68-94% HP left. It lasts about 4-5 fights in a row at levels 10 and 30. It beats
nearly every world boss at the boss's own level (about 90-95% against Gorrak and Ussreth, 85% against
Pyraxis), and all except Pyraxis (75%) at boss level +3.

## Rebirth

A Druid life leaves you **+98 WIS, +49 INT, +49 CON and +49 DEX**: a spread that helps both WIS and
INT casters. It gives only **leather** training and staff, blunt and dagger weapons. Entangling Roots
and Wrath of the Wild are strong in any later class.
