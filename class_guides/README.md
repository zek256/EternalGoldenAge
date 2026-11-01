# Class Guides

There is one guide for each of the eleven classes of Eternal Golden Age. Each guide covers how the
class grows, every spell and ability with its real numbers, what gear it can use, how to play it
from level 1 to 50, how it fares against bosses, and what it leaves behind when you are reborn.

| Class | Role | Grows most | Spell stat | Armor | Difficulty |
|---|---|---|---|---|---|
| [Warrior](warrior.md) | Weapon tank, no magic at all | STR, CON | none | plate + shield | Easy |
| [Paladin](paladin.md) | Holy knight, heals and shields itself | STR | WIS | plate + shield | Easy |
| [Dread Knight](dread_knight.md) | Dark knight, drains life | STR, CON | INT | plate + shield | Easy |
| [Ranger](ranger.md) | Archer with a wolf companion | STR, DEX | WIS | mail + shield | Easy |
| [Rogue](rogue.md) | Burst melee, dodges and stuns | STR, DEX | none | leather | Medium |
| [Bard](bard.md) | Songs that hurt, heal and buff | CHA | CHA | leather | Hard early, strong late |
| [Cleric](cleric.md) | Healer who smites | WIS | WIS | mail + shield | Easy |
| [Druid](druid.md) | Nature caster with roots and heals | WIS | WIS | leather | Medium |
| [Shaman](shaman.md) | Spirit caster with a wolf | WIS, CON | WIS | mail + shield | Easy |
| [Wizard](wizard.md) | Glass-cannon blaster | INT | INT | cloth | Hard |
| [Necromancer](necromancer.md) | Pets, drains and disease | INT | INT | cloth | Easy (strongest solo class) |

At level 50, [Gearing Up at Level 50](level_50_gear.md) shows what to buy, farm and chase next, class by class.

## How every class works

These rules are shared by all classes. The guides refer back to them.

### Stats

You never store stats. They are worked out every time from:

**race base + class starting bonus + class gains x (level - 1) + gear + buffs**

After a rebirth, the class part is the **best** of every class you have lived at your current level
(see Rebirth below).

Race base stats are around 10, so by level 50 your class gains (about 150 points spread over three
to five stats) matter far more than your race's starting numbers. Race **perks** (bonus HP, mana,
damage, crit or dodge) last the whole game and matter more than race stats.

| Stat | What it does |
|---|---|
| STR | Weapon damage, for every class |
| DEX | Precision, for every class: fewer misses; +1% crit per 10 DEX; +1% dodge per 15 DEX; +1 armor per 10 DEX |
| CON | Max HP: each point gives +0.2 HP per level (so +10 HP at level 50) |
| INT | Wizard, Necromancer and Dread Knight spells, and their mana pool |
| WIS | Cleric, Druid, Shaman, Paladin and Ranger spells, and their mana pool |
| CHA | Bard spells and mana pool |

### HP, mana and recovery

- **Max HP** = 10 + (class HP + 3) x level + CON x level x 0.2, times any race HP perk and the
  mastery bonus (+2% per class mastered).
- **Max mana** = 15 + class mana x level + spell stat x level x 0.1, times any race mana perk.
- In a fight you regain **2% of max mana per round**. Out of a fight, each 4-second tick restores
  **2% HP and 3% mana**, and **sleeping restores 10% of both per tick**.
- Levelling up fully restores HP and mana.

### Weapon attacks

- Weapon damage = the weapon's damage range + **0.35 x STR + 0.5 x level**, for every class.
  Casters gain little or no STR, so their auto-attacks stay weak; they win with spells.
- Auto-attacks miss **10% minus 0.07% per point of DEX**, never less than 2% (about 9% at 10 DEX,
  6% at 60, 2% from about 115). Weapon abilities (Slam, Backstab and the rest) always land and roll
  weapon damage times a multiplier.
- **Physical damage** (auto-attacks, weapon abilities, pets) is reduced by the monster's armor.
  **Spell damage, drains and damage over time ignore armor.**

### Crits, dodge and armor

- **Crit chance** = 5% + DEX/1000 + race perk, capped at 35%. A crit does **1.75x**. Spells and
  weapon abilities can crit; damage over time and pets can't.
- **Dodge** = 3% + DEX/1500 + race perk (capped at 25%), plus dodge buffs such as Evasion (capped
  at 60% in total). You also dodge an extra 5%, plus 2% per level you are above the monster.
- **Armor** = gear armor + DEX/10 + armor buffs. It cuts a monster's physical hits by
  armor / (armor + 40 + 6 x monster level). Monster drain attacks ignore armor.

### Spells and abilities

- **Spells** cost mana and are cast with `cast <name> [target]`. **Abilities** are free, run on
  cooldowns, and are used with `ability <name>` (or `ab <name>`). Both are learned automatically
  at their level; `spells` lists them and `cooldowns` (`cd`) shows what is cooling down.
- Mana cost grows with your level: **cost x (1 + 0.1 x (level - 1))**, so a spell costs 5.9x its
  base cost at level 50.
- Spell power = **base + per-level x level + scale x stat**. The guides give the formula and
  example values.
- Damage buffs (+% damage) raise weapon hits, spell damage, drains and damage over time, but not
  pets.
- In a fight, a spell or ability you type is **queued** and used next round, and your auto-attack
  still lands that round too. If it is still cooling down, it is **held** and fires the moment it
  is ready.
- A buff, heal over time or shield with the same name **refreshes** rather than stacking.
- **Stuns** you cast have half their listed chance against bosses.
- **Damage shields** absorb damage after armor and last up to 10 rounds or until used up.
- **Lifesteal** heals you only from physical damage.

### Pets (Necromancer, Shaman, Ranger)

A pet attacks a random enemy every round for physical damage and draws about a quarter of the
enemies' ordinary attacks (never their special attacks). It stays until it is destroyed, you
`pet dismiss` it, or you summon another (which replaces it). Pet HP and damage are fixed when it
is summoned, so re-summon after levelling. You can only have one pet.

### Armor and weapon training

Armor tiers are cloth < leather < mail < plate, and each class can wear its own tier and every
lighter one. Shields need shield training. Weapons come in families (dagger, sword, axe, blunt,
two-handed, staff, wand, bow). Jewelry, off-hand items and "any" items (the mythic weapons) are
free for everyone. **Training carries across rebirths**: after one life as a plate class, every
later life can wear plate.

### Level difference

Damage is scaled by level difference both ways: each level you are above a monster adds 4% to your
damage (up to +40%); each level below it takes 6% off (down to -60%). Monsters below you also miss
more often.

### Rebirth

At level 50 you may be reborn as any other class. From then on, at every level, **each of your
stats, your HP per level and your mana pool are the best that any class you have lived would have at
that level**. A level-10 warrior who was once a wizard has the wizard's level-10 INT, and the
warrior's own STR, CON and HP growth. The order of your lives never matters, only which classes you
have lived. Each **class mastered** (lived to level 50) also adds **+2% max HP and damage**, up to
+22% with all eleven. You keep every spell and ability you have ever learned (each unlocks again at
its original level), your armor and weapon training, and your boss kills. Each guide ends with what
that class brings to later lives.

## About the numbers

The tables in each guide were computed from the game's own formulas for a character with **10 in
every stat from race, no race perk and only the class's starting gear**. Your numbers will be higher
with real gear, a good race or past lives, but the shape is the same. Level-50 HP leaves out the
+2% mastery bonus you get for mastering your class on reaching 50. Mana costs depend only on
level, so they are exact.

The "How it performs" sections come from `tools/balance_sim.py` (October 2026), which fights
monsters with a simple AI and best-in-slot gear for the level. Treat them as optimistic.
