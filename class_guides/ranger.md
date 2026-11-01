# Ranger

> *Wardens of the wild places, deadly with bow and blade and kin to beasts.*

The Ranger is a DEX fighter that mostly uses free abilities, with a small WIS mana pool for a heal
and an animal companion. It hits hard and often, gets an area attack early, crits more than most
classes, and from level 16 brings a wolf that soaks up hits for it. It has the best staying power of
any class in the mid levels.

## At a glance

| | |
|---|---|
| HP per level | 9 |
| Mana per level | 2 |
| Attack stat | DEX |
| Spell stat | WIS |
| Starting bonus | DEX +3, WIS +1, CON +1 |
| Gains per level | DEX +2, STR +1, CON +1, WIS +1 |
| Armor | Mail (and everything lighter) |
| Shield | Yes |
| Weapons | Sword, dagger, axe, bow |
| Starting gear | Ash shortbow (2-5), padded tunic, leather boots, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | DEX | WIS | CON | Weapon damage | Crit | Dodge |
|---|---|---|---|---|---|---|---|---|
| 1 | 24 | 18 | 13 | 11 | 11 | 7-10 | 6.3% | 3.9% |
| 10 | 170 | 55 | 31 | 20 | 20 | 17-20 | 8.1% | 5.1% |
| 25 | 485 | 152 | 61 | 35 | 35 | 35-38 | 11.1% | 7.1% |
| 50 | 1210 | 415 | 111 | 60 | 60 | 65-68 | 16.1% | 10.4% |

DEX powers your weapon, your crit chance, your dodge and a little armor, so it does a lot for you.

## Spells and abilities

Abilities are free (`ab <name>`); spells cost mana (`cast <name>`). Cost is shown at the level you
learn it and at level 50. Weapon damage is the average with the starting bow.

| Level | Name | Type | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|---|
| 1 | **Aimed Shot** | ability | free | 2 | one foe | 1.6x weapon damage (~13 at L1, ~106 at L50) |
| 4 | **Hunter's Mend** | spell | 8 / 35 | - | self | Heal 9 + 2/level + 0.45 WIS (~23 at L4, ~136 at L50) |
| 10 | **Multishot** | ability | free | 3 | all foes | 0.95x weapon damage to every foe |
| 16 | **Call Bonded Wolf** | spell | 50 / 118 | 10 | self | Summon a grey timber wolf (~150 HP, 19-30 damage at L16; ~405 HP, 52-80 at L50) |
| 24 | **Serpent Sting** | ability | free | 4 | one foe | 0.9x weapon damage plus poison: 8 + 1.4/level + 0.3 DEX per round for 5 rounds (~59 at L24, ~111 at L50) |
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

Wear **mail** (or leather) and a bow. DEX first, then CON; WIS feeds Hunter's Mend and the wolf.

Signature late gear: **Stormcaller** (50, bow, DEX/WIS/CON), dropped by Caelestra in the Plane of
Stars. Also good: the dune recurve bow (40), Dragonscale Mail (48, mail), the sunsteel mail set (40),
windwalker boots (50, leather, DEX), the Band of the Four Winds (50, ring, DEX), and the mythic Fang
of Pyraxis and Eternity.

## Best races

- **Elf**: high DEX, +4% dodge and +2% crit.
- **Dark elf**: +5% crit.
- **Human**: +5% HP, mana and damage.
- **Orc**: +6% damage.

## How it performs

The Ranger wins every same-level fight in the simulator, a little slowly at low levels (5-8 rounds)
and quickly later (about 3 rounds at 30-45), finishing with 48-84% HP. It has the best staying power
of any class at level 30 (nearly 8 fights in a row). Its weak point is the hardest bosses: about
75% against Ussreth and 90% against Ghaldrek at the boss's own level, and about 65% against Pyraxis
(80% at +3). It beats every other boss at boss level +3.

## Rebirth

A Ranger life leaves you **+98 DEX, +49 STR, +49 CON and +49 WIS**, plus **mail armor and shield
training** and sword, dagger, axe and bow weapons. The DEX bonus raises crit, dodge and armor for any
later class. Aimed Shot, Multishot, Rain of Arrows and Deadeye are free abilities, though they scale
with your weapon, so they are best in a DEX or STR class.
