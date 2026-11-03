# Eternal Golden Age

An offline, single-player, text-based fantasy MUD/RPG in pure Python 3 (standard library only).

Begin in the town of Brightwater, clear rats from the inn cellar, hunt wolves in the Whispering
Woods, break the bandit chieftain, descend into the Crypt of Varnoth, aid the dwarves of Hearthdeep
in the snowbound west, and fight your way through the Mirefen, the Ironspine Mountains and the
haunted Ruins of Elandor to the lair of Pyraxis the Eternal Flame. At level 50, be **reborn** as a new class and carry your past lives with you.

## Running

Open a terminal in this folder (in File Explorer, click the address bar, type `cmd` and press Enter) and run:

```
python main.py
```

Requires Python 3.8+. No installation, no network. Colours are turned off if the `NO_COLOR`
environment variable is set.

Saves are written as JSON to `saves/<name>.json`.

## Commands

| command | what it does |
|---|---|
| `look` / `l` [thing] | describe the room, or look at a monster, person or item |
| `n` `s` `e` `w` `u` `d` (or `north`, `go north`...) | move |
| `run` <path>, or just the path | speedwalk: `nnes` or `run 3n2e` walks the path at two rooms a second (paste a `find` route straight in). Typing anything stops you. Each step shows the small map (even with `automap` off) and only the last room is described; it stops early at a missing exit, a sealed gate, or a monster that attacks. In a fight, only the first step counts, as a flee |
| `enter` <thing> | go into something a room's description tells you about, such as `enter mousehole` in the Willow Mill. These ways in aren't listed as exits, and you can't speedwalk or flee through them |
| `exits` | list exits and where they lead |
| `map` | a text map of the area around you: `#` you, `$` shop, `!` quest to take, `?` quest to hand in, `*` a living boss, `^` `v` stairs up/down. Rooms of neighbouring areas are grey |
| `automap` [on\|off] | show a small map (two rooms in every direction) under each room description. Saved with your character |
| `attack` / `k` / `kill` <target> | start a fight (`k rat`, `k 2.wolf` for the second wolf); during a fight, switch targets |
| `cast` / `c` <spell> [target] | cast a spell (`cast magic missile rat`, `c fireball`); in a fight it is used on the next round |
| `ability` / `ab` <name> [target] | use a class ability (`ab backstab`, `ab evasion`); in a fight it is used on the next round |
| `spells` / `abilities` | list all known spells and abilities, with locked ones greyed out |
| `consider` / `con` <target> | judge a monster's danger (colour-coded by level) |
| `flee` [dir] | try to escape combat (moving during combat also attempts to flee) |
| `inventory` / `i` | what you carry |
| `equipment` / `eq` | what you wear |
| `wear` / `wield` / `equip` <item> | equip an item (level and armor/weapon training apply, see below). With Dual Wield, a second one-handed weapon goes in your off hand if the shield slot is empty |
| `offhand` / `dual` <weapon> | with Dual Wield, hold a one-handed weapon in your off hand (the shield slot); `remove offhand` takes it off |
| `remove` <item or slot> | take something off |
| `use` / `drink` <potion> | drink a potion (in a fight you drink it next round, and still attack) |
| `examine` / `x` <item> | item details, compared with what you have equipped |
| `get` <item> / `get all` / `drop` <item> | pick up / drop |
| `talk` <person> | talk to NPCs; this turns in every finished quest and offers every quest you qualify for |
| `quests` / `journal` | quest log |
| `find` <quest name, number, or monster> | shortest route to your quest target (or the quest giver once it's done), e.g. `find vermin` prints `wd`. A route that needs `enter` says so, e.g. `sssw, then ENTER MOUSEHOLE, then nnnnen`. With one active quest, plain `find` works. Also `track` / `where` |
| `list`, `buy [qty] <item>`, `sell [qty or all] <item>`, `sell junk` | trade with merchants: Durgan Ironhand (weapons and armor, smithy), Elowen Silverthread (cloth, wands, orbs and rings for casters, west off the South Road), Mirela (potions) |
| `bank`, `deposit [qty or all] <item>`, `withdraw [qty or all] <item>` | store items you don't want to carry with Brother Oswin in the Sunvault, east of the Temple of the Dawn. Gold stays in your purse. Banked items are kept through rebirth, but don't count toward collect quests or open item gates until you withdraw them |
| `sleep` / `rest` | fall asleep and recover 10% of max HP and mana every tick (not with hostile monsters nearby) |
| `wake` / `stand` | get up (you also wake automatically when fully rested, or when attacked) |
| `pet` / `pet dismiss` | inspect or release your summoned companion |
| `stats` / `score` | character sheet: stats as [base/total], identity and record, condition, combat numbers, every class lived (current one highlighted), racial perk, pet and active effects |
| `level` | XP progress and upcoming abilities |
| `rebirth` | at level 50, be reborn as a new class (with every class mastered, rise a tier; see Tiers) |
| `alias <word> <command>` | create a shortcut: after `alias mm cast magic missile`, typing `mm` casts it (`mm rat` targets the rat). Built-in commands and directions can't be overridden. `alias` lists yours, `unalias <word>` removes one. Aliases are saved with your character. |
| `save`, `load`, `quit`, `help` | system |

The prompt shows your HP, mana and progress toward your next level in gold
(e.g. `<192/192 hp (100%) 350/350 mana (100%) EXP: 3%>`). In combat it adds your target's
remaining health in red `TARGET: 56%`, and `[ASLEEP]` while sleeping.
In room listings monsters are coloured by danger relative to your level
(grey/green/blue easy, white even, yellow/red dangerous), and `(!)` / `(?)` mark NPCs with a quest to
offer or turn in.

## Time and combat

The world runs on a real-time clock: every **4 seconds** is one game tick.

- **Combat:** `kill <target>` starts a fight, and your first attack lands at once. After that, one
  combat round happens every tick, and you automatically attack your current target each round.
  A spell, ability, potion or flee you type is queued and used on the next round, and your
  auto-attack still lands that round too. Moving during a fight also tries to flee.
- **No cooldowns, stuns or area attacks.** Every spell and ability can be used every round; mana
  is the only limit. Each class's attacks form a ladder in which every new one is a modest step
  up from the last, so a fight is simply: cast your buffs or shield, then use your newest attack
  every round, healing when you need to. Nothing stuns you, and you can't stun monsters; their
  big special attacks are heavy hits instead. Every attack hits one foe.
- **Buffs** last until the end of the fight (or, cast outside a fight, until the end of your next
  one). Buffs of the same kind don't stack: for each bonus (damage, armor, dodge, lifesteal) only
  your strongest buff counts. **Shields** last until they are used up, and a new shield replaces
  the old one. **Heals over time** run on a timer, and casting one again restarts it. **Weakening**
  curses on a monster last the whole fight.
- **Pets** can only be summoned outside a fight. A pet stays with you until it dies.
- **Invisibility** (wizard, level 20) hides you from aggressive monsters for 5 minutes, so they don't
  attack on sight and you can sleep near them. Bosses see through it, and in a boss room everything
  attacks. Casting any spell (even Invisibility again) or starting a fight reveals you, and anything
  hostile in the room attacks at once. It can't be cast in a fight.
- **Who attacks on sight:** aggressive monsters are rare. Only undead, demons, elementals, guards,
  cultists and bosses attack you as soon as you enter their room, and outside boss rooms at most
  one monster per room does. In a boss room, everything attacks. Animals and roaming humanoids
  (wolves, spiders, kobolds, lizardfolk, orcs...) leave you alone and only fight the one you
  attack; the others in the room stay out of it. `consider` tells you whether a monster will
  attack on sight.
- **Sleep:** while asleep you recover 10% of your max HP and mana each tick. You can't move or
  fight, but you can check `stats`, `inventory` and so on. You wake when fully rested, when
  attacked, or when you type `wake`.
- **Monsters** don't regenerate. Instead, when you leave a room (walking out, fleeing or dying),
  every monster in it recovers to full health and loses any curses or damage-over-time effects.
  A boss has to be beaten in one go.
- **Awake:** outside combat you slowly regenerate (2% HP and 3% mana per tick). Heals over time and
  monster respawns count in ticks.

## Races and classes

**Races:** human (+5% HP, mana and damage), high elf (+12% mana), elf (dodge/crit), dark elf (crit), gnome (mana/dodge),
ogre (+12% HP), troll (regeneration), undead (immune to poison/disease), orc (+6% damage).

**Classes:** warrior, cleric, wizard, bard, necromancer, shaman, druid, rogue, ranger, paladin,
dread knight. Each has its own HP and mana growth, per-level stat gains, and up to 7 spells/abilities
unlocked between levels 1 and 48. Every class swings its weapon with **STR** and aims with **DEX**.
Every class's damage spells (damage, damage over time, drains) scale with **INT**, and its heals,
heals over time and damage shields with **WIS**, which also feeds the mana pool. Pets use the
higher of the two. Each class's spells and abilities:

- Warrior: no spells or abilities, only the passives Dual Wield (1) and Double Attack (10)
- Cleric: Minor Healing, Smite, Divine Aegis, Greater Healing, Holy Wrath, Resurgence, Sunburst
- Wizard: Magic Missile, Frost Bolt, Fireball, Invisibility, Lightning Lance, Meteor
- Necromancer: Lifetap, Raise Skeleton (pet), Plague, Bone Spear, Siphon Soul, Bone Colossus, Wail of the Damned
- Shaman: Frost Shock, Ancestral Mending, Spirit Wolf (pet), Spirit of the Bear, Serpent Venom, Chain Lightning
- Druid: Thornlash, Regrowth, Entangling Roots, Moonfire, Barkskin, Starfall, Wrath of the Wild
- Rogue: Backstab, Poisoned Blade, Evasion, Kidney Shot, Eviscerate, Shadow Dance, Assassinate; Dual Wield, Double Attack
- Ranger: Aimed Shot, Hunter's Mend, Multishot, Bonded Wolf (pet), Serpent Sting, Rain of Arrows, Deadeye; Double Attack
- Paladin: Holy Strike, Holy Light, Blessing of Might, Divine Shield, Hammer of Justice, Consecration; Double Attack
- Dread Knight: Shadow Strike, Disease Cloud, Dread Aura, Dread Touch, Vampiric Embrace, Death Coil, Unholy Frenzy; Double Attack
- Bard: Discordant Note, Ballad of Mending, War March, Dirge of Despair, Crescendo, Legend's Anthem; Dual Wield

Each class has a full guide in [`class_guides/`](class_guides/README.md): stats by level, every spell
and ability with its numbers, gear, races, how to play it and what it leaves behind on rebirth. At level 50, [Gearing Up at Level 50](class_guides/level_50_gear.md) shows what to buy, farm and chase next for each class.

Spells cost mana, and the cost scales with level (the wizard's attack spells scale three times
as fast, so a fight costs a wizard a real share of its mana). Abilities are free. Both are learned automatically
on level up, and neither has a cooldown.

**Passives** are always on once learned, and like abilities they are kept through rebirth:

- **Dual Wield** (warrior at level 1, rogue and bard at 10): hold a one-handed weapon (dagger, sword, axe,
  blunt, or a mythic sword) in the off hand, in place of a shield or off-hand item. It strikes every
  round beside your main hand for 65% of a normal hit. A two-handed weapon, staff or bow in the main
  hand can't be paired with one.
- **Double Attack** (warrior at level 10; rogue, ranger, paladin and dread knight at 15): each hand may
  strike a second time every round. The chance is 40% when learned and rises evenly to 100% at 50.

A character with several lives learns each passive at the lowest level any of its classes gives it
(a rogue who was once a warrior dual wields from level 1). Warriors start with a rusty shortsword
in each hand.

With both, a level-50 character lands up to four blows a round, each with its own miss, crit and
damage line. If the target falls, the remaining blows go to the next enemy in the fight.

### Armor and weapon training

Each class is trained in one armor tier (and every lighter one), in some weapon families, and
perhaps in shields:

| class | armor | shield | weapons |
|---|---|---|---|
| Warrior | plate | yes | dagger, sword, axe, blunt, two-handed, bow |
| Paladin | plate | yes | sword, blunt, two-handed |
| Dread Knight | plate | yes | sword, axe, two-handed |
| Cleric | mail | yes | blunt, staff |
| Shaman | mail | yes | blunt, staff, axe |
| Ranger | mail | yes | sword, dagger, axe, bow |
| Rogue | leather | no | dagger, sword, bow |
| Bard | leather | no | dagger, sword, blunt, wand |
| Druid | leather | no | staff, blunt, dagger |
| Wizard | cloth | no | staff, wand, dagger |
| Necromancer | cloth | no | staff, wand, dagger |

Armor tiers run cloth < leather < mail < plate. Item lines show each piece's tier or weapon family,
in red when you aren't trained for it, and `examine` says why. Orbs and tomes held in the off hand
are not shields and anyone may carry them; so may rings, necklaces and the mythic artifacts
(Fang of Pyraxis, Eternity, the Ashen Crown, the Crown of Trepth). **Training is kept through
rebirth**: a character may use anything any of its lives was trained for, so a wizard who was once
a warrior may fight in plate with an axe.

## Character maths

- **HP** = 10 + (class HP + 3) x level + CON x level x 0.2 (x racial modifier, x mastery bonus)
- **Mana** = 15 + class mana x level + WIS x level x 0.1 (x racial modifier)
- **Stats** = race base + class starting bonus + class gains x (level - 1) + gear
- **Weapon damage** = weapon range + 0.35 x STR + 0.5 x level, for every class.
- **DEX** is precision for every class: +0.1% crit per point (max 35%), more dodge (max 25%), +1
  armor per 10, and fewer misses (auto-attacks miss 10% minus 0.07% per point of DEX, never below 2%).
- After a rebirth, the class figures above (stats, HP per level, mana) use the **best** of every
  class you have lived. See Rebirth.
- **XP to next level** = 65 x level^1.7, the same in every life no matter how many rebirths.
  A monster of your level is worth 15 + 14.5 x level^1.5, so a level takes about 6 such kills
  early on and about 10 near level 50.
- A monster is worth the same XP whatever your level; there is no bonus for fighting above
  yourself (higher monsters are worth more only because their level is higher). Monsters below
  you fall off fast: 2 levels below gives 88% of its value, 5 below 45% (about 4% of a level),
  10 below 4% (well under 1% of a level). They also hit you less.

## Rebirth

At level 50, `rebirth` lets you choose any other class:

- Level and XP reset to 1 / 0.
- You keep **every ability of every class you have lived**. Each becomes usable again when your
  current level reaches the level at which it was originally learned (a warrior-turned-wizard gets
  Dual Wield back at level 1 and Double Attack at 10, and a cleric-turned-rogue gets Smite back at 3).
- **Every stat, your HP and your mana take the best of all the classes you have lived**, at your
  current level. A level-10 warrior who was once a wizard has the wizard's level-10 INT and WIS
  (higher than a warrior's), the warrior's STR and CON, the warrior's HP growth and the wizard's
  mana per level. At level 25 it has the wizard's level-25 INT, and so on: each life starts on an equal
  footing and grows into its past strengths. The order of your lives never matters, only which
  classes you have lived.
- Each **class mastered** (lived to level 50) adds **+2% max HP and damage**, up to +22% with all
  eleven.
- You keep the **armor and weapon training** of every class you have lived (see above).
- All your gear goes into your pack, and you start in your new class's starting gear. Your old
  gear can be worn again once you reach its level. Experience needed per level is exactly the same as in your first life.

### Tiers

Every character starts at **Tier 1**. Once you have mastered **all eleven classes** (the last one at
level 50), your next `rebirth` raises you to the next tier instead, up to **Tier 10**:

- You choose any class, including the one you just finished, and start again at level 1 with that
  single class.
- Every past life is forgotten: their stats, HP and mana growth, mastery bonus, abilities and armor
  and weapon training are gone. The planes' gates that need every class mastered close again.
- In return **every stat gets +10 per tier above 1**, for good (Tier 2 +10, Tier 3 +20, up to +90 at
  Tier 10). A wizard with 10 INT at Tier 1 has 20 at Tier 2 and 30 at Tier 3.
- You keep everything else: gold, items, bank, completed quests, boss kills, kills, deaths, aliases.

Tiers are purely for fun: no monster or fight is tuned for them, so a high-tier character is meant to
be overpowered. Mastering all eleven classes at Tier 10 ends your journey: rebirth is closed and you
are known as **Emperor** *Name* **the Eternal**. `stats` and `level` show your tier.

## World

Town of Brightwater (inn, temple and the Sunvault bank beneath it, smithy, alchemist, Silverthread Arcana caster shop, barracks,
and the North, West and East Gates), Greenmeadow (1-5) with **the Underhedge** (5-10) behind a mousehole in its Willow Mill (`enter mousehole`), where a fairy ring shrinks you to the size of a mouse: a meadow of dewdrops, the roaring millrace, the ant road, a beetle cavalry of mouse knights, the mole kings' tunnels, the garden wall where Old Tom the cat prowls, and the Wasp Keep in a windfall apple (only the soldier ants, mole guards and wasps attack; Wenna Furrow, the shrunken miller, sells potions in the fairy ring), Whispering Woods and the bandit camp (4-10),
the Westmarch farms and goblin quarry (3-10), **the Mycelial Wards** (12-20) west of its Old Watchtower, a city grown from one vast fungal network whose capfolk share a partial hive mind (most ignore you; the spore wardens and the things of the Rot Ward and the deep network do not), with a quiet garden path south from the Gilled Houses into the Hedge Maze of Thornwick Hall, Barrowfield and the Crypt of Varnoth dungeon (9-17),
the snowy Rimefells (10-20) around the dwarven city of **Hearthdeep** (smith, rune-carver, alehouse
with potions) and the Deepdelve Mine below it (18-21), the Mirefen (15-22), the ancient Eldergrove
(20-34) around the elven city of **Silverbough** (bladesmith, moonweaver, inn with potions), reached
south through the Whispering Woods or from the Westmarch quarry, **Thornwick Hall** (40-50) west of
the Eldergrove's Stag Walk, the great house of the Vanes, where every huntsman, servant, guest and
kinsman can be fought on the way up to Lord Aldric Vane (a poacher in the deer park buys what comes
out of the house and sells potions; the area has no gate, so the gate wardens are a hard lesson at
25), the Ironspine Mountains with the
orc warcamp, the giants and the frost caverns (20-34), the Ruins of Elandor (32-41) with **the Painted Gallery** (36-42) behind the Hall of the Moon Court, where the court painter Ithilmir sealed pieces of the world into his canvases as Elandor fell: `enter seascape`, `enter winter`, `enter still life`, `enter salon` and `enter city` step into a storm-wrecked ship, a hunt that has run for a thousand years, a still life gone rotten and alive, a salon of portrait sitters and Elandor as it was, each with a named champion, and the unfinished self-portrait in his studio opens only to someone carrying the painter's palette (Sylwen, the painted curator, makes one from living pigment and sells potions), the Ashen
Peaks up to the dragon's lair (37-52), and to the east the Dustway caravan road (8-15), with **the Chancery of the Dead** (30-38) south of its Gnoll Scrub, a court where the dead bring their unfinished business (most of its ghosts are too busy with their cases to attack; the bailiffs and wardens are not, and the inner chambers open only to someone carrying a writ of audience from Clerk Quillon in the Office of Forms and Writs), with **the Clockwork Orchard** (38-44) south of its Archive of Wills, the estate of the gnome inventor Orrin Gearwhistle, where brass trees bear clockwork fruit around a cuckoo-clock tower, a mechanical pond, an unending tea party and a workshop, and Orrin has wound himself into the great orrery at its heart so that he will never die (only his sentries, hounds, escapement guardians and the foundry's molten springs attack; Assessor Morrow, a ghost of the Chancery sent to serve him a summons, waits at the passage and sells potions), the gnoll
canyons of the Redrock Badlands (18-27) with **the Carnival That Never Closes** (24-30) south of its Howling Pit, a centuries-old fairground that grows stranger the further in you go, from a cheerful midway to the always-midnight lots behind the tents and the Ringmaster in the big top (Pip at the prize booth sells gear lost by other adventurers), and the Scorchsands desert (35-49) around the golden city
of **Sunspire** (bladewright, silk bazaar, caravanserai with potions), with the Tomb of the Sand
Kings beneath a sunken pyramid (45-48) and **the Sugarwold** (44-49) north of the Salt Pans, a country of sweets baked at the edge of the salt by the witch Madame Marchpane, whose gingerbread folk were heroes once; its brown-sugar dunes run down into the Valley of the Kings, and a coal road behind her cottage climbs west to the Forge of the Dragon Cult in the Ashen Peaks (only her gingerbread soldiers, oven imps and the witch herself attack; Sir Edric Hale at the sugar pan sells potions). Brightwater's shops sell gear up to level 20; Hearthdeep
sells dwarven gear for levels 12-24, Silverbough elven gear for levels 24-34, and Sunspire desert
gear for levels 38-44.

**The Planes of the Gods (51-60).** A stair behind the altar of the Temple of the Dawn climbs to
the Threshold of the Gods, where a herald explains the way. Four first-tier planes open around it,
each guarded by a god's champion: Stars to the north, Dreams to the west, Death to the east, and to
the south Law, the gods' prison, kept by the paladin Stalworth Lightbearer. Each leads on to
an elemental plane ruled by an elemental lord: Stars to Air, Dreams to Earth, Death to Fire and
Law to Water, and each elemental plane stays sealed until you have slain the champion of the plane
before it. Above the Threshold, the Door of Eternity opens only once you have
slain all four elemental lords (your character remembers every boss it has killed, across all its
lives). At the end of the Plane of Eternity sits Lord Trepth, whose throne opens only to a
character who has leveled **every class to level 50** (your current class counts once it reaches 50).
The planes are built for reborn characters: with one life even their first-tier monsters are a
coin flip, with six lives the champions are hard but fair, the elemental lords need nearly every
class, and Lord Trepth needs every class you have ever learned. They drop mythic level-50 gear. Below level 50, their monsters give a great deal of experience to anyone strong
enough to survive them.

That is 257 rooms, 140 monster types including 19 bosses, and 199 items. Run
`python tools/draw_map.py` to draw `map.svg`, a map of every room.

**Quests:** Vermin in the Cellar (Bram, inn), Wolves at the Gate, The Bandit Chieftain, Trouble in
the Rimefells, The Skullsplitter Horde (Captain Halvard, barracks), The Bone King and The Hag of the
Mirefen and The Thirsting Dead (Sister Aveline, temple), The Blight Spreads (Elowen, Silverthread
Arcana), Highway Robbery and The Laughing Warlord (Old Marta, Dustway Waystation), Glass from the
Sands (Archivist Mehrun), Giants on the Causeway (Sun-Captain Idrisa) and The Last Sand King (Emira
Zahrin, all in Sunspire), Gumdrops at the Gate, Buttons of the Lost, The Witch's Guard and Out of the
Oven (Sir Edric Hale, the Sugarwold), The Ants' Larder, The Mole King's Tunnels, Paper and Stings and The
Queen in the Apple (Wenna Furrow, the Underhedge), Living Pigment, The Serpent of Saltmere, The White Stag,
Memento Mori, The Empty Frame, The Painted King and The Court Painter (Sylwen, the Painted Gallery), Evidence
for the Court, The Great Cuckoo, The Unending Tea, The Master Automaton and Serving the Summons (Assessor
Morrow, the Clockwork Orchard), Goblins in the
Henhouse (Farmer Haverick, Thornbury), Fur for the Gatewatch (Captain Orla, Hearthdeep), The
Stonewake (Thane Hargrim, Hearthdeep), The Sacred Herd and The Rotwood Circle (Warden-Captain
Faelan, Silverbough) and The Heart of the Blight (Speaker Saelwyn, Silverbough).

Dying returns you to the temple with half HP, losing 10% of the XP needed for your level. You keep
all your gold.

## Code layout

```
main.py          entry point, title menu, CLI flags
game.py          command parser, game clock, exploration, quests, find, aliases, shops, rebirth, save/load
character.py     Character (stats, HP/mana, levelling, abilities, equipment, rebirth, aliases) and Pet
combat.py        tick-based combat rounds, ability resolution, monster AI, XP/loot rewards
world.py         rooms, monster instances, respawning, world persistence
ui.py            colour, word wrap, background input reader
mapview.py       room grid layout and the in-game map / automap (the layout is shared with draw_map.py)
data/races.py    races and racial perks
data/classes.py  classes, stat growth, starting gear
data/abilities.py  all spells and abilities
data/items.py    weapons, armor, caster gear, potions, trophies
data/monsters.py monster templates, special attacks, loot tables
data/rooms/      the world map, one file per region, plus npcs.py
data/quests.py   quests
tools/           validate.py (data check), balance_sim.py, draw_map.py (draws map.svg)
```

Adding content is data-only: add a room to its region's file in `data/rooms/`, a monster to
`data/monsters.py`, an ability with `spell(...)` / `ability(...)` in `data/abilities.py`, and so on.
A new region file must also be listed in `REGIONS` in `data/rooms/__init__.py`.
