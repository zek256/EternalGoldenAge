# The world expansion: design and testing

The world of Eternal Golden Age grew from 55 rooms to 257 in five phases, plus a later addition, the Plane of Law. This file
records what each
phase added, the code that changed, how the new content was balanced, and how it was tested. The
original plan and the decisions behind it are in `EXPANSION_PLAN.md`.

| | Before | Now |
|---|---|---|
| Rooms | 55 | 257 |
| Monster types | 51 | 140 |
| Bosses | 6 | 19 |
| Items | 108 | 199 |
| Quests | 6 | 20 |
| Cities | 1 | 4 (Brightwater, Hearthdeep, Silverbough, Sunspire) |

## The shape of the world

Brightwater sits at the centre, with a road out of each gate. Each direction has its own theme
and gets harder the farther you go from town. The Planes of the Gods sit above it all.

| Direction | Theme | Levels | City |
|---|---|---|---|
| North | Northlands, crypt, swamp, Ironspine, Ashen Peaks, Ruins of Elandor | 9-52 | none |
| West | Westmarch farms, then the snowy Rimefells and the Deepdelve Mine | 3-22 | **Hearthdeep** (dwarves) |
| South | meadows and woods, then the ancient Eldergrove | 1-34 | **Silverbough** (elves) |
| East | the Dustway, the Redrock Badlands, then the Scorchsands desert | 8-49 | **Sunspire** (desert traders) |
| Above | the Planes of the Gods, reached from Brightwater's temple | 51-60 | none (endgame) |

- **Several areas per level range:** up to four, so players have variety and, in later lives, a
  different route each time. For example, levels 20-25 are found in the Ironspine, the Deepdelve
  Mine, the Redrock Badlands and the edge of the Eldergrove.
- **Loops:** the regions join up instead of ending in dead ends. The Rimefells connect to the
  Mirefen over a high pass, the Eldergrove reaches the Westmarch quarry, and the Scorchsands
  reach the Ruins of Elandor.
- **Distinct regions:** each region has its own monsters, damage element and gear drops.
- **Respawn:** death always returns you to the Temple of the Dawn in Brightwater.
- **Shops:** Brightwater's shops sell gear up to level 20. Each new city sells gear for its own
  level range:
  - Hearthdeep: dwarven gear for levels 12-24.
  - Silverbough: elven gear for levels 24-34.
  - Sunspire: desert gear for levels 38-44.

Run `python tools/draw_map.py` to draw `map.svg`, a map of every room.

## Phase 1: groundwork and the north (55 to 73 rooms)

- **Room files:** `data/rooms.py` was split into one file per region under `data/rooms/`, plus
  `npcs.py`.
- **Map tool:** `tools/draw_map.py` can draw any number of underground areas as separate boxes.
- **14 new monsters.**

| Region | New rooms | Levels |
|---|---|---|
| Ironspine Mountains | Griffon's Crag, Ogre Quarry, Hill Giants' Steading, Circle of Red Hands, Rimeglass Gorge, Rime Glacier, Jarls' Mead-Hall | 22-34 |
| Mirefen | Spawning Grounds, Bogwood Hollow, Leech Fens | 18-21 |
| Ruins of Elandor | Silvered Gardens, Sunken Amphitheatre, Hall of the Moon Court | 34-40 |
| Ashen Peaks | Meltwater Gorge, Smoking Scree, Burning Fields, Drake Roost, Forge of the Dragon Cult | 37-47 |

The Meltwater Gorge and Smoking Scree now sit between the Frost Throne and the Ashen Waste. They
fill the old jump from level 34 straight to 41.

## Phase 2: the west and Hearthdeep (73 to 110 rooms)

**Totals:** 14 new monsters, 20 new items and 4 new quests.

| Area | Rooms | Levels | What's there |
|---|---|---|---|
| West Gate | 1 | safe | Off Brightwater's North Gate |
| Westmarch | 8 | 3-10 | Farms, Thornbury hamlet, a goblin-infested quarry, the hill road |
| Rimefells | 12 | 10-20 | Snow wolves, frost goblins, ice spiders, yetis, frost wisps, snow trolls; a high pass east to the Mirefen |
| Hearthdeep | 10 | safe | The dwarven hold |
| Deepdelve Mine | 6 | 18-21 | Below Hearthdeep. Boss: **Ghaldrek the Stonewake** (21) |

- **Hearthdeep's people:**
  - Brakka Ironhand, Durgan's sister, sells dwarven arms and armour.
  - Tamsin Runecutter sells rune gear for casters.
  - Gilda Barrelbrew runs the alehouse and sells potions.
  - Captain Orla gives a quest to collect yeti fur.
  - Thane Hargrim gives a quest to kill the Stonewake.
- **How players find it:**
  - Captain Halvard's quest Trouble in the Rimefells (level 11) sends players west.
  - Durgan's greeting mentions his sister in Hearthdeep.
  - Farmer Haverick gives a level 5 quest in Thornbury.
- **Shop move:** Brightwater's level 22-24 stock now sells in Hearthdeep instead. That's the
  mithril sword, hunter's recurve, mithril hauberk, starsilk hood, wand of embers and tome of
  warding.

## Phase 3: the south and Silverbough (110 to 145 rooms)

**Totals:** 12 new monsters, 22 new items and 4 new quests.

| Area | Rooms | Levels | What's there |
|---|---|---|---|
| Greenmeadow | 1 | 2-4 | The Willow Mill |
| Whispering Woods | 2 | 8-10 | Fern Gully and the Old South Way, with brown bears |
| Eldergrove | 22 | 20-34 | Centaurs, owls, wood trolls, thorn sprites, greatstags, blighted treants, rotwood druids, blight wolves, gloom dryads. Boss: **Rotheart, the Blighted Oak** (33) |
| Silverbough | 10 | safe | The elven city in the trees |

- **Two ways in:** the Eldergrove is reached from the Old South Way in the Whispering Woods, and
  from the Westmarch quarry through its western arm.
- **Silverbough's people:**
  - Speaker Saelwyn gives a quest to kill Rotheart.
  - Warden-Captain Faelan gives two quests: cull the blighted stags, then hunt the rotwood druids.
  - Ilyra Leafsong sells elven arms and armour.
  - Caelum Moonweave sells caster gear.
  - Merewyn runs the inn and sells potions.
- **How players find it:** Elowen in Brightwater's Silverthread Arcana gives The Blight Spreads
  (level 24), which sends players south.

## Phase 4: the east and Sunspire (145 to 201 rooms)

**Totals:** 21 new monsters, 27 new items and 6 new quests.

| Area | Rooms | Levels | What's there |
|---|---|---|---|
| East Gate | 1 | safe | Off Brightwater's South Road |
| Dustway | 7 | 8-15 | Hyenas, highwaymen, gnolls, and the safe Dustway Waystation |
| Redrock Badlands | 10 | 18-27 | Gnolls, scorpions, wyverns, dust devils. Boss: **Yellowtooth, Gnoll Warlord** (26) |
| Scorchsands | 20 | 35-49 | Raiders, dune scorpions, salt wraiths, mirage stalkers, djinn, sand giants, great sandworms |
| Sunspire | 12 | safe | The walled desert city around its great obelisk |
| Tomb of the Sand Kings | 6 | 45-48 | Below a sunken pyramid. Boss: **Ussreth, the Last Sand King** (48) |

- **Two ways into the desert:** north from the Badlands, and down the stair below Elandor's Sunken
  Amphitheatre into the buried elven quarter.
- **New people:**
  - Old Marta (Dustway Waystation) gives two quests: kill highwaymen, then Yellowtooth.
  - Emira Zahrin (Sunspire) gives a quest to kill the last Sand King.
  - Sun-Captain Idrisa (Sunspire) gives a quest to kill sand giants.
  - Archivist Mehrun (Sunspire) gives a quest to collect desert glass.
  - Zahir the Bladewright (Sunspire) sells sunsteel arms and armour.
  - Amsa Silkwind (Sunspire) sells silk caster gear.
  - Nadim the Caravan-Master (Sunspire) sells potions, including supreme potions.
- **How players find it:** Sister Aveline's quest The Thirsting Dead (level 36) sends players to
  Sunspire.

## Phase 5: the Planes of the Gods (201 to 257 rooms)

### What was added: 56 rooms, levels 51-60

Phase 5 added 50 rooms. The Plane of Law (6 more rooms) was added afterwards as a fourth
first-tier plane.

| Tier | Plane | Levels | Boss |
|---|---|---|---|
| - | Threshold of the Gods (2 safe rooms, with the Herald, who explains the way) | safe | - |
| 1 | Stars, Dreams, Death, Law | 51-55 | Caelestra the Star-Warden, Somnara the Dreamweaver, Morthis Keeper of the Dead, Stalworth Lightbearer (55) |
| 2 | Fire, Water, Earth, Air | 54-58 | Rekkn, Nerevos, Ulmathra, Zephyrion (58) |
| 3 | Eternity | 57-60 | **Lord Trepth (60)** |

- **Getting there:** a stair behind the altar of the Temple of the Dawn in Brightwater climbs up
  to the Threshold.
- **Layout:** the Threshold of the Gods is the hub, and the planes are laid out symmetrically
  around it. Each first-tier plane leads straight on to one elemental plane:

  | Direction from the Threshold | First tier | Leads on to |
  |---|---|---|
  | North | Stars | Air |
  | West | Dreams | Earth |
  | East | Death | Fire |
  | South | Law | Water |
  | Up | the Door of Eternity | the Plane of Eternity |

- **The Plane of Law:** the gods' own prison, through the Threshold's southern gate. It is all
  white stone, black bars and chains of light: the Gaol Gate, the
  Endless Cellblock, the Oubliette, the Warden's Walk and the Chain Yard, where chained penitents
  and iron wardens keep the gods' prisoners. At its heart is the Hall of Judgement, where
  **Stalworth Lightbearer** waits: a paladin in white plate, the first mortal Lord Trepth ever judged
  worthy to serve him. He drops the Lightbearer's Oath (a longsword) and the Shield of Judgement.
  From the Chain Yard, the prison's sluice gate opens south onto the Plane of Water.
- **The elemental planes:** each is sealed until the character has killed the champion of the
  first-tier plane that leads to it: Caelestra for Air, Somnara for Earth, Morthis for Fire and
  Stalworth for Water. A sealed way says which champion is still undefeated.
- **The Door of Eternity:** a bronze door at the top of a stair of light above the Threshold. It opens
  only once the character has killed all four elemental lords. If it is still shut, it tells you
  which lords remain.
- **Lord Trepth's throne:** it opens only for a character who has leveled every class to level 50. The
  current class counts once it reaches 50. The door lists the classes still missing.
- **The rest of the planes:** open to anyone who can survive them.
- **Rewards:**
  - The plane bosses and Lord Trepth drop 19 mythic level-50 items, including Trepth's sword Eternity,
    the Crown of Trepth and the Hourglass Amulet.
  - Characters below level 50 in later lives get large amounts of XP from plane monsters, if they
    are strong enough to survive them.

Files: `data/rooms/planes.py` (rooms, including Law), the end of `data/monsters.py` (monsters
and bosses), the "Mythic gear" section of `data/items.py`, and the Herald in `data/rooms/npcs.py`.

### Code changes

Phases 1-4 were data only. Phase 5 was the first to need game code.

- **Room gates:** a room can carry a `gate` (see `R()` in `data/rooms/common.py`):
  - `{"kills": [boss ids], "msg": ...}` requires the character to have killed every listed boss.
  - `{"all_classes": True, "msg": ...}` requires every class to have been lived to level 50.

  `Game.gate_block()` checks gates on normal movement and when fleeing. The dev command `goto`
  ignores them.
- **Kill record:** `Character.boss_kills` records every boss the character has ever killed, kept
  across rebirths. Old saves load with an empty list.
- **Mastered classes:** `Character.mastered_classes()` returns the past lives plus the current
  class once it is at level 50.
- **Balance simulator:** a new endgame mode, `python tools/balance_sim.py endgame`, tests level-50
  characters with 1, 6 and 11 lives lived, using best-in-slot gear.
- **Data check:** `tools/validate.py` now checks that gates only require bosses and that every
  gate has a refusal message.
- **Map:** `tools/draw_map.py` draws the Threshold and the eight first- and second-tier planes
  together in one box on the right of the map, and the Plane of Eternity in a box of its own, since it
  lies above the Threshold.

## Balance

### Levels 1-50 (phases 1-4)

Every new monster was compared with existing monsters of the same level, using the real combat
code with every class and best-in-slot gear. New monsters cost about the same HP per fight as
their neighbours.

- **Toughened after testing:**
  - The dragon cult flamecaller was too easy, so it was made tougher. It is still slightly
    easier than its neighbours, but it heals itself.
  - The scarab swarm was too easy, so it was made tougher.
- **The new world bosses** were tested at their own level and at their level +3, with 5 potions:

| Boss | Level | Compared with |
|---|---|---|
| Ghaldrek the Stonewake | 21 | about as hard as Varnoth and Old Mother Gristle |
| Yellowtooth, Gnoll Warlord | 26 | about as hard as Warlord Gorrak |
| Rotheart, the Blighted Oak | 33 | about as hard as Gorrak and Seluvar |
| Ussreth, the Last Sand King | 48 | between Seluvar and Pyraxis |

### The Planes (phase 5, original rebirth system)

> **Superseded (2026-11-01).** These figures describe the original system, where past lives added
> their stat gains together. Past lives now give the best of each class's stats instead, and the
> plane monsters were retuned to match. See [Rebirth rework and retune](#rebirth-rework-and-retune-2026-11-01) below.

Win rates from `balance_sim.py endgame`, for level-50 characters averaged over all classes. Boss
fights use 5 potions.

| Fight | 1 life | 6 lives | 11 lives |
|---|---|---|---|
| First-tier monsters | about 50% (they kill you half the time) | trivial | trivial |
| Plane champions (including Stalworth) | 0% | 89-100% | 100% |
| Elemental lords | 0% | 27-65% | 100% |
| Lord Trepth | 0% | **0%** | **68-75%** (every class 50-90%) |

- **Without mythic gear:** an 11-life character with no mythic gear at all still beats Trepth about
  60% of the time. Good equipment matters but is not strictly required.
- **Why the multipliers were so large:** past-life stat bonuses make multi-life characters
  enormously strong. A 6-life character already beat a standard level 60 boss every time, so plane
  monsters use much bigger multipliers than anything else in the game:

  | Monsters | HP multiplier | Damage multiplier |
  |---|---|---|
  | Regulars | 3.3-5.5 | 2.6-3.6 |
  | Plane bosses | 7.5-11 | 3.3-3.9 |
  | Lord Trepth | 15 | 5.3 |

  This is also recorded in `CLAUDE.md`.
- **The Plane of Law** was tested the same way when it was added. Its chained penitents and
  iron wardens beat a 1-life character 25-41% of the time, like the other first-tier monsters, and
  Stalworth is about as hard as Caelestra and Morthis.
- **Tuning changes during testing:**
  - Lord Trepth was too hard at first (41% with 11 lives). His HP went from 18 to 15 and his damage
    from 5.6 to 5.3.
  - The first-tier regular monsters were too easy for a 1-life character (50-84% wins), so they
    were toughened.
  - The Lords of Water and Earth were softer than Fire and Air, so they were toughened.

### Rebirth rework and retune (2026-11-01)

**What changed.**
- **The order of rebirths no longer matters.** Past lives used to add their full stat gains
  together; now each stat, HP per level and the mana pool take the best that any lived class would
  have at the character's current level.
- **Each class mastered adds +2% max HP and +2% damage**, up to +22% with all eleven.
- **STR is weapon damage and DEX is precision, for every class.** The per-class attack stat is gone.
  DEX gives crit, dodge, armor and a lower miss chance: auto-attacks miss 10% minus 0.07% per DEX,
  never below 2% (it was a flat 7%).
- **New growth:**
  - Rogue: STR +2, DEX +2, CON +1 (was DEX +3, STR +1, CON +1).
  - Ranger: STR +2, DEX +2, CON +1 (was DEX +2, STR +1, CON +1, WIS +1).
  - Bard: CHA +2, STR +1, DEX +1, CON +1 (was CHA +2, DEX +2, CON +1).
- **Poisons:** Poisoned Blade and Serpent Sting now scale with STR instead of DEX.

All runs used `tools/balance_sim.py` in a temp copy of the game, with best-in-slot gear (so the
numbers are optimistic) and 5 potions in boss fights.

#### Levels 1-50 (first-life characters)

Baseline and new runs used the same settings (`fights --n 20`, `bosses --n 20`, `endurance --n 15`,
seed 3).

- **Same-level fights:** every class still wins 100% at every level tested (5, 15, 25, 35, 45, 50),
  with HP left within a few points of the baseline. The three rebalanced classes:

  | Class | HP left at 15 | HP left at 35 | HP left at 50 |
  |---|---|---|---|
  | Rogue | 54% → 59% | 77% → 80% | 85% → 83% |
  | Bard | 69% → 67% | 76% → 75% | 96% → 97% |
  | Ranger (first try, see below) | 54% → 48% | 75% → 74% | 81% → 73% |

- **Endurance** (fights in a row) moved by about one fight or less for every class at levels 10,
  30 and 50 (the largest change: the druid at 50, 7.2 to 6.0).
- **Bosses** (win % at the boss's level / at level +3): almost every result stayed the same or
  improved, mostly from the rebalanced classes:

  | Boss | Rogue before → after | Bard before → after |
  |---|---|---|
  | Rask the Bandit Chieftain | 100/100 → 100/100 | 70/100 → 95/100 |
  | Varnoth the Bone King | 100/100 → 100/100 | 60/100 → 85/100 |
  | Old Mother Gristle | 100/100 → 100/100 | 50/100 → 55/100 |
  | the First Spore | 100/100 → 95/100 | 50/100 → 45/100 |
  | the High Justice | 100/100 → 100/100 | 65/100 → 80/100 |
  | Pyraxis the Eternal Flame | 100/95 → 100/100 | 100/95 → 95/90 |

- **The ranger fell behind on the hardest bosses** with its first new growth (STR +2, DEX +1,
  CON +1, WIS +1): Seluvar 75%, the High Justice 60%, Ussreth 65%, Pyraxis 50%. It had lost the crit
  and dodge that DEX used to give. Five options were tested (30 fights each, at the boss's level and
  at +3; Pyraxis is level 52, so both of his columns are fought at level 50):

  | Ranger growth | Seluvar | High Justice | Ussreth | Pyraxis | Ringmaster |
  |---|---|---|---|---|---|
  | STR 2, DEX 1, CON 1, WIS 1 (first try) | 90/100 | 76/100 | 83/100 | 43/53 | 86/100 |
  | **STR 2, DEX 2, CON 1 (chosen)** | **93/100** | **83/100** | **90/100** | **70/66** | **83/100** |
  | STR 2, DEX 2, WIS 1 | 73/96 | 56/96 | 56/100 | 30/56 | 83/100 |
  | first try, 10 HP per level | 93/100 | 73/100 | 80/100 | 66/56 | 90/100 |
  | STR 2, DEX 2, CON 1, 10 HP per level | 100/100 | 83/100 | 83/100 | 70/60 | 93/100 |

  The chosen growth puts the ranger back where it was before the change (Pyraxis 75/60 then, 70/66
  now) without raising its HP per level.

#### The Planes under the new rule, before the retune

With the old multipliers, multi-life characters were now far too weak (`endgame --n 6`):

| Fight | 1 life | 6 lives | 11 lives |
|---|---|---|---|
| First-tier monsters (51-54) | 2-45% | 98-100% | 100% |
| Elemental-plane monsters (55-57) | 0% | 79-100% | 98-100% |
| Hourglass golem / paradox (58-59, Eternity) | 0% | 36% / 2% | 94% / 44% |
| Plane champions | 0% | 3-29% | 77-100% |
| Elemental lords | 0% | 0% | 8-55% |
| Lord Trepth | 0% | 0% | **0%** |

#### The retune

A script searched, for each monster, for one factor applied to both its HP and damage multipliers
that hit a target win rate (a binary search, 3 fights per class per step, all 11 classes). Targets:

- **Champions:** about 80% with 6 lives.
- **Elemental lords:** about 92% with 11 lives.
- **Eternity regulars:** about 95% with 11 lives.
- **Lord Trepth:** about 70% with 11 lives.

| Monster | Factor | HP mult | Damage mult | 6 lives | 11 lives |
|---|---|---|---|---|---|
| Caelestra, the Star-Warden | 0.82 | 8.0 → 6.6 | 3.5 → 2.9 | 85% | 100% |
| Somnara, the Dreamweaver | 0.74 | 8.5 → 6.3 | 3.3 → 2.45 | 82% | 100% |
| Morthis, Keeper of the Dead | 0.65 | 7.5 → 4.85 | 3.6 → 2.3 | 94% | 100% |
| Stalworth Lightbearer | 0.82 | 8.0 → 6.55 | 3.4 → 2.8 | 82% | 100% |
| Rekkn, Lord of Flame | 0.68 | 9.5 → 6.45 | 3.8 → 2.55 | 9% | 100% |
| Nerevos, Lord of the Tides | 0.85 | 11.0 → 9.4 | 3.8 → 3.25 | 3% | 94% |
| Ulmathra, Lord of Stone | 0.81 | 11.0 → 8.9 | 3.7 → 3.0 | 6% | 97% |
| Zephyrion, Lord of the Winds | 0.64 | 9.0 → 5.75 | 3.9 → 2.5 | 33% | 97% |
| a chronal sentinel | 1.00 | 5.0 (unchanged) | 3.4 (unchanged) | 94% | 100% |
| an hourglass golem | 0.91 | 5.5 → 5.0 | 3.4 → 3.1 | 52% | 97% |
| a paradox | 0.73 | 4.8 → 3.5 | 3.6 → 2.65 | 73% | 97% |
| Lord Trepth | 0.44 | 15.0 → 6.6 | 5.3 → 2.35 | 3% | 79% |

The first-tier and elemental-plane regulars were left alone: they already matched their targets.

**Lord Trepth fine-tuning.** His search landed slightly generous, so three factors were compared
with 12 fights per class at 11 lives:

| Factor | HP mult | Damage mult | Average | Weakest class | Strongest class |
|---|---|---|---|---|---|
| **0.44 (chosen)** | **6.6** | **2.33** | **69%** | **ranger 50%** | **bard 83%** |
| 0.455 | 6.83 | 2.41 | 48% | druid 17% | rogue 67% |
| 0.47 | 7.05 | 2.49 | 42% | wizard 17% | shaman 67% |

His damage was rounded to 2.35 in the data.

#### Final results

The full endgame report after the retune (`endgame --n 6`, seed 5). The last column is the weakest
class with all 11 classes lived:

| Monster | Level | 1 life | 6 lives | 11 lives | Weakest class |
|---|---|---|---|---|---|
| a star eagle | 51 | 42% | 100% | 100% | 100% |
| a dreamstalker | 52 | 30% | 100% | 100% | 100% |
| a pale horse | 52 | 55% | 100% | 100% | 100% |
| a chained penitent | 52 | 44% | 100% | 100% | 100% |
| a celestial sentinel | 53 | 35% | 100% | 100% | 100% |
| an iron warden | 53 | 27% | 100% | 100% | 100% |
| a sleepwalking giant | 54 | 0% | 100% | 100% | 100% |
| a reaper | 54 | 5% | 100% | 100% | 100% |
| an efreet, tide, granite and storm elemental | 55 | 0% | 100% | 100% | 100% |
| a pyre phoenix | 57 | 0% | 85% | 100% | 100% |
| an abyssal kraken | 57 | 0% | 86% | 100% | 100% |
| a crystal basilisk | 57 | 0% | 83% | 97% | 83% |
| a thunderbird | 57 | 0% | 95% | 100% | 100% |
| a chronal sentinel | 57 | 0% | 76% | 100% | 100% |
| an hourglass golem | 58 | 0% | 61% | 98% | 83% |
| a paradox | 59 | 0% | 56% | 97% | 83% |
| Pyraxis the Eternal Flame | 52 | 95% | 100% | 100% | 100% |
| Caelestra, the Star-Warden | 55 | 0% | 79% | 100% | 100% |
| Somnara, the Dreamweaver | 55 | 0% | 64% | 100% | 100% |
| Morthis, Keeper of the Dead | 55 | 5% | 89% | 100% | 100% |
| Stalworth Lightbearer | 55 | 2% | 76% | 100% | 100% |
| Rekkn, Lord of Flame | 58 | 0% | 23% | 88% | 50% |
| Nerevos, Lord of the Tides | 58 | 0% | 2% | 88% | 67% |
| Ulmathra, Lord of Stone | 58 | 0% | 6% | 92% | 83% |
| Zephyrion, Lord of the Winds | 58 | 0% | 48% | 97% | 83% |
| **Lord Trepth** | 60 | 0% | 3% | **73%** | 33% |

In summary:

| Fight | 1 life | 6 lives | 11 lives |
|---|---|---|---|
| First-tier monsters | 27-55% (the level-54 ones about 0-5%) | 100% | 100% |
| Elemental-plane and Eternity monsters | 0% | 56-100% | 97-100% |
| Plane champions | 0-5% | 64-89% | 100% |
| Elemental lords | 0% | 2-48% | 88-97% |
| Lord Trepth | 0% | 3% | **73%** (every class about 50-85%) |

**Notes on the results.**
- **Small samples.** With 6 fights per class, single-class figures are noisy. Lord Trepth's weakest
  class shows 33% here but was 50% in the 12-fight run above, which is the better estimate.
- **The 6-to-11-life gap is smaller than before** for stats, because six well-chosen lives already
  hold most of the best stats. What remains comes from the mastery bonus (+12% against +22%) and
  the classes the sim's 6-life characters lack (mostly the rogue's and ranger's DEX).
- **The elemental lords are steep:** under 50% with 6 lives, about 90% with 11. Since the Door of
  Eternity needs all four lords and Lord Trepth's throne needs every class, this matches the
  intended path: the lords are a late-game wall, and Trepth is the last fight of a full run.
- **How the sim builds a 6-life character:** the class plus the first five other classes in
  `CLASS_ORDER` (warrior, cleric, wizard, bard, necromancer). A different set of six would score a
  little differently.

#### Checks

| Check | Result |
|---|---|
| The level-10 example | A warrior with a wizard past life has the wizard's level-10 INT (41) and the warrior's STR and CON (31 each) |
| Order independence | A wizard who was once a warrior and a warrior who was once a wizard have identical stats, HP per level and mana pool |
| Level 50 | After wizard 50 → warrior 50, INT is exactly the wizard's 161, and the mastery bonus is +4% |
| Real rebirth | A wizard reborn as a warrior through the game's own `rebirth` command shows the new rules text, stores the past life as just its class, and the score sheet reads correctly |
| Data check | `validate.py` passes |
| Saves | Untouched; no existing character has rebirthed, so no save conversion was needed |

## Testing

All testing was done in a copy of the game outside this folder (`%TEMP%\zektest`), so `saves/`
was never touched.

### Every phase

| Check | Result |
|---|---|
| Data check (`python tools/validate.py`) | Passes after every phase. Final: 257 rooms, 140 monsters (19 bosses), 199 items, 20 quests |
| Map (`python tools/draw_map.py`) | No rooms overlap, so the geography is consistent in every region |
| Room split (phase 1) | The world data was identical before and after splitting `data/rooms.py` |
| New monsters | Compared with existing monsters of the same level for every class |
| Walks | Every new room and loop walked in the real game, including all four cities and the boss rooms |
| NPCs | Every new NPC's quest or shop list checked |
| Existing saves | Copies of existing saves loaded after every phase, finally with all 257 rooms |

### The Planes (phase 5)

| Check | Result |
|---|---|
| Door of Eternity | Refuses entry and lists the missing lords; opens once all four are killed |
| Lord Trepth's throne | Refuses entry and lists the missing classes, including the current class below level 50; opens when every class is mastered |
| Kill record | Bosses are recorded on kill; ordinary monsters are not |
| Saves | The kill record survives a save round trip; old saves without it load with an empty list |
| Rooms | All 56 plane rooms are reachable by walking from the temple with the game's own movement, checked again after the planes were reorganized around the Threshold |
| Stalworth | His kill is recorded like the other plane bosses |
| Live game | A scripted run through the real game loop (temple, stair, Threshold, the Herald, the Door of Eternity) worked |

### Re-running the checks

```
python tools/validate.py
python tools/draw_map.py
python tools/balance_sim.py fights
python tools/balance_sim.py bosses
python tools/balance_sim.py endgame --n 10
```

- **`validate.py`:** run after any change to `data/`.
- **`draw_map.py`:** run after adding rooms. It stops with an error if two rooms land on the same
  square.
- **`balance_sim.py fights` and `bosses`:** cover levels 1-52.
- **`balance_sim.py endgame`:** lists every monster above level 50 with its win rate for 1, 6 and
  11 lives, plus the worst class at 11 lives. Re-run it after changing plane monster multipliers,
  class stat growth or mythic gear.

## Documentation

- **`README.md`:** the player-facing manual. Its world section and quest list cover everything
  above.
- **`CLAUDE.md`:** notes for development: the room package, gates and boss kills, the endgame
  balance targets, and the map tool.
- **`EXPANSION_PLAN.md`:** the original plan, the decisions made along the way, and a progress
  log for each phase.
- **`map.svg`:** the finished world.

Nothing has been committed.
