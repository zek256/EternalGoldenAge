# Shaman

> *Spirit-speakers of the tribes, who call down ancestral fury and healing.*

The Shaman is a sturdy WIS caster in mail with a shield and a spirit wolf. It has the most HP of any
caster, a heal, a pet from level 8, a damage-and-armor buff, a poison that weakens, chain lightning for
groups, and a late-game heal-and-damage avatar. It is a forgiving, well-rounded class.

## At a glance

| | |
|---|---|
| HP per level | 8 |
| Mana per level | 5 |
| Attack stat | STR |
| Spell stat | WIS |
| Starting bonus | WIS +3, CON +2 |
| Gains per level | WIS +2, CON +2, STR +1 |
| Armor | Mail (and everything lighter) |
| Shield | Yes |
| Weapons | Blunt, staff, axe |
| Starting gear | Training mace (2-5), padded tunic, leather cap, 3 minor healing potions |

## Growth

Average race, starting gear only (see the [README](README.md#about-the-numbers)).

| Level | HP | Mana | WIS | CON | STR | Weapon damage |
|---|---|---|---|---|---|---|
| 1 | 23 | 21 | 13 | 12 | 10 | 6-9 |
| 10 | 180 | 96 | 31 | 30 | 19 | 13-16 |
| 25 | 585 | 292 | 61 | 60 | 34 | 26-29 |
| 50 | 1660 | 820 | 111 | 110 | 59 | 47-50 |

At level 50 a Shaman has more HP than a Paladin, thanks to its CON.

## Spells

All Shaman magic is spells, cast with `cast <name>`. Cost is shown at the level you learn it and at
level 50.

| Level | Spell | Cost | Cooldown | Target | Effect |
|---|---|---|---|---|---|
| 1 | **Frost Shock** | 5 / 30 | - | one foe | Frost damage 6 + 1.45/level + 0.42 WIS (~12 at L1, ~67 at L25, ~125 at L50) |
| 3 | **Ancestral Mending** | 7 / 35 | - | self | Heal 10 + 2.2/level + 0.55 WIS (~25 at L3, ~98 at L25, ~181 at L50) |
| 8 | **Spirit Wolf** | 34 / 118 | 10 | self | Summon a spirit wolf (~81 HP, 11-18 damage at L8; ~200 HP, 27-42 at L25; ~375 HP, 50-77 at L50) |
| 15 | **Spirit of the Bear** | 36 / 88 | 10 | self | +20% damage and +10 + 1.5/level armor for 6 rounds |
| 24 | **Venom of the Serpent** | 79 / 142 | - | one foe | Poison 8 + 1.5/level + 0.4 WIS per round for 5 rounds (~67 at L24, ~127 at L50), and the foe deals 20% less damage for 4 rounds |
| 34 | **Chain Lightning** | 206 / 283 | 3 | all foes | Lightning damage 35 + 3/level + 0.9 WIS to every foe (~208 at L34, ~284 at L50) |
| 44 | **Ancestral Avatar** | 292 / 324 | 12 | self | Heal 45% of your max HP and +40% damage for 5 rounds |

## How to play

**Levels 1-7.** Frost Shock and Ancestral Mending. Shamans start slow but are hard to kill.

**Levels 8-23.** Call the Spirit Wolf before every outing. It attacks every round and takes about a
quarter of the enemies' normal attacks. Its stats are fixed when summoned, so call it again every few
levels, and recall it when it dies. Spirit of the Bear at 15 is a cheap buff; keep it up in real
fights.

**Levels 24-50.** Venom of the Serpent is a strong poison that also weakens its target. Put it on
the most dangerous foe, then Frost Shock. Chain Lightning at 34 handles groups. At 44, Ancestral
Avatar is a 45% heal and a damage boost in one: your emergency button and your boss opener. Against a
boss: wolf, Spirit of the Bear, Venom, Frost Shock, with Ancestral Mending and Ancestral Avatar to
heal.

**Tips**
- Your spells ignore armor; your wolf's bites don't.
- Venom of the Serpent stacks a weaken on top of the poison, which makes it worth casting even on
  foes that will die soon if they hit hard.
- You are the tankiest caster, so you can afford to melee a little while your mana refills.

## Gear

Wear **mail** and a shield. WIS first, then CON.

Notable late gear: the Sunforged Mace (43, blunt, STR/WIS), Flameheart (50, blunt), the dragonbone
staff and **the Dreamweaver's Staff** (staffs, giving up the shield), Dragonscale Mail (48, mail), the
Burial Mask of Ussreth (48, mail), the sunsteel mail set, the Shield of Judgement (50, CON/WIS), the
Pearl of the Deep (50, ring), and the mythic Fang of Pyraxis and Eternity.

## Best races

- **High elf**: WIS 13 and +12% mana.
- **Human**: +5% HP, mana and damage.
- **Troll**: regenerates in combat; your CON makes up for its low WIS.

## How it performs

The Shaman wins every same-level fight in the simulator in about 4 rounds with 66-83% HP left. It
lasts about 5 fights in a row at levels 10 and 30. It beat every world boss at the boss's own level
except Pyraxis (about 90%), and nearly all at boss level +3.

## Rebirth

A Shaman life leaves you **+98 WIS, +98 CON and +49 STR**, plus **mail armor and shield training** and
blunt, staff and axe weapons. The CON bonus is a big HP boost for any later class, and Spirit Wolf
gives any later caster a pet, though it scales with WIS.
