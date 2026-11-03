# Eternal Golden Age

Offline single-player text MUD in pure Python 3, standard library only (no dependencies, no network).
`README.md` is the player-facing manual; keep it in sync when gameplay or commands change.
`class_guides/` has one guide per class (numbers from the game's formulas and `balance_sim.py`);
update them when classes, abilities, stat formulas or class gear change. `class_guides/level_50_gear.md`
lists the best level 40-50 and plane gear per class and where it drops; update it when such gear is added.

## Running and testing

```
python main.py                 # play
```

`main.py` takes no command-line flags (removed at the user's request). The dev commands
(`setlevel`, `goto`, `addgold`, `give`) still exist in `game.py` but only work on a `Game` built
with `dev=True` (direct calls). For a faster clock or fixed seed in tests, set
`game.TICK_SECONDS` / `random.seed()` from a small launcher script in the temp copy.

There is no build step and no unit test suite. Verify changes by:
- **Data check**: `python tools/validate.py` after any edit to `data/`. It checks two-way exits,
  that every room is reachable, spawns, loot, shops, quests (givers, prereqs, collectable targets),
  class gear and ability classes, and exits 1 on errors.
- **Balance**: `python tools/balance_sim.py [fights|endurance|bosses|endgame|unlock|gear] [--n 30] [--levels 1,12,30]`
  runs every class through the real `Combat` code with output silenced. The tuning targets are
  in its docstring. It fights one monster at a time with best-in-slot gear, so it is optimistic.
  Re-run it after touching combat formulas, monster multipliers or class growth.
- **Map**: `python tools/draw_map.py [out.svg]` redraws `map.svg` (every room, exits, areas, levels,
  bosses) after room changes. It lays rooms on a grid from their exits and exits with an error if
  two rooms land on the same square, so it doubles as a geography check for new regions. Areas
  that would overlap the surface (dungeons below, realms above) go in the `INSETS` list in
  `mapview.py` and are drawn as separate boxes. New areas need a colour in its `COLORS` table.
  The same layout drives the in-game `map` / `automap` (`mapview.py`), which shows one layer
  (the surface or one inset) at a time.
- **World expansion**: `EXPANSION_PLAN.md` holds the agreed plan (regions, level ranges, phases).
- **Scripted play**: pipe commands into `main.py`. Piped input arrives instantly, so no game ticks
  pass between lines. Combat rounds and sleep need real time, so for those drive the game with
  delays between lines (a small `subprocess` script that writes a line, sleeps, writes the next)
  together with a short tick (`game.TICK_SECONDS = 0.3` set by a launcher before `main.main()`).
- **Direct calls**: import `game.Game` with a `Character`, stub `ui.say/out/rule` to no-ops, and
  call methods (`cmd_attack`, `attempt_flee`, `world_tick`) to check logic without the clock.

**Always test in a copy outside this folder** (e.g. `%TEMP%\zektest`, copy `*.py` and `data/`).
The user plays from this folder, and `saves/` holds their real characters. Never delete,
overwrite or "clean up" anything in `saves/`. Windows can't launch Python from very long paths,
so keep the temp path short.

Git: the user commits manually. Don't run `git init`, commit or connect remotes unless asked.

## Architecture

```
main.py       CLI flags, title menu; starts ui's input thread; sets game.TICK_SECONDS
game.py       Game: command dispatch, game clock, exploration, quests, find, aliases, shops,
              sleep, rebirth, save/load, character creation
character.py  Character (stats, HP/mana, XP, abilities, equipment, rebirth) and Pet
combat.py     Combat: one round per tick, ability resolution, monster AI, rewards
world.py      MonsterInstance, Room (spawning + aggression rule), World (respawns, persistence)
ui.py         colour, wrapping, background stdin reader, prompt tracking
mapview.py    room grid layout (shared with tools/draw_map.py), text map and automap rendering
data/         all content as plain Python data (races, classes, abilities, items, monsters, quests)
data/rooms/   one module per region, each with a ROOMS dict, merged in __init__ (REGIONS list,
              duplicate ids raise); NPCs in npcs.py; START_ROOM/RESPAWN_ROOM in __init__
```

### The game clock (game.Game.run)
- A daemon thread reads stdin into a queue (`ui.start_input`). The main loop waits on that queue
  until the next tick: either a typed line arrives (`handle`) or the tick fires (`game_tick`).
- A tick is a combat round (`Combat.round`) when fighting, otherwise `world_tick`: awake regen
  (2% HP and 3% mana) or sleep (10%), effect and cooldown timers, respawns.
- **Never call `input()`.** It races the reader thread. Use `game.ask()` / `ui.read_line()`.
  The clock pauses during `ask()` prompts (menus, quit and rebirth confirmations).
- Moving does **not** advance time. Only ticks do.
- Speedwalking (`cmd_run`, `parse_path`, `walk_step`): `run nnes` or a bare path word like `3n2e`
  that isn't a command or alias. The first step is immediate; the rest sit in `Game.walk` and
  the main loop takes one every `WALK_SECONDS` (0.5), a second timer beside the tick. Any typed
  line stops it ("You stop."), as does `check_aggro` finding an attacker; in combat only the
  first step is used, as a flee. `run` is not a flee alias (by the user's choice). Direct
  `handle()` calls only take the first step: call `walk_step()` yourself for the rest.

### Combat flow
- `kill X` or an offensive spell out of combat calls `start_combat`. The first action resolves
  immediately and `reset_clock()` gives a full tick before round 2.
- In combat, typed actions don't act right away. `Combat.queue()` stores one action
  (spell/ability/potion/flee), and the next `round()` runs it. Queued abilities are re-validated
  when they fire (`ability_round`).
- **The auto-attack lands every round alongside the action** (the user's choice): `player_ability`
  ends with `Combat.swing()`, and potions and failed flees call `pass_turn(swing=True)`. Only a
  stun (`pass_turn()`) skips the swing. Monster HP was raised by `world.MONSTER_HP_MULT` (1.3)
  to keep fight lengths and the endgame where they were.
- A second slot, `Combat.held`, keeps one ability that was used while still cooling down
  (`use_ability` calls `Combat.hold` instead of refusing). Each `round()` first tries
  `fire_held()`: once off cooldown it fires and takes the round, leaving `queued` for the next
  round; if `ability_error` fails then (usually mana) it is dropped. Stuns delay both slots.
- `end_round`: player effects tick, pet attacks, aggressive room monsters join, monsters act,
  monster effects tick, mana regen, cooldowns, world respawn tick, then death/victory checks.
- Effect timing gotcha: effects the player applies to themselves are created with `fresh: True`
  so the end-of-round tick doesn't eat a turn. Monster-applied effects must **not** be fresh.
  Player stuns are applied during the monster phase, after the player tick, so they last
  into the next round. Monster stuns are consumed when the monster tries to act.
  Cooldowns are set to `cooldown + 1` in combat for the same reason.
- `level_gap_mult` scales damage both ways by level difference. Monsters below the player
  also miss more.

### Aggression rules (deliberately rare, Aardwolf-style)
- Template flag `aggro` in `data/monsters.py`: only undead, demons, elementals, guards,
  cultists and bosses. Animals and roaming humanoids are passive. Exception: the Chancery of the
  Dead's ghosts are passive (they are busy with their cases); only its bailiffs and wardens attack.
  The carnival's trapped spirits are passive too; its roustabouts, night barkers and clowns attack.
  In the Mycelial Wards only the spore wardens, bone-blooms and thought-spores attack.
- `Room.spawn` enforces the per-room rule: a room containing a boss makes **every** monster
  aggressive. Any other room allows at most `max_aggro` (default 1) aggressive instances, and
  extras spawn passive. Aggression is per instance and is not saved; it is recomputed on load.
- Aggressive monsters ignore players more than `AGGRO_GAP` (6) levels above them.
- Attacking a passive monster fights only that one. Passive neighbours never join, but
  aggressive monsters in the room do.
- `Game.leave_room()` (called from `go()` and `player_died()`) restores every monster in the room
  being left to full HP and clears its effects. Monsters have no other regeneration.

### Player and progression
- Stats are **derived, not stored**: race base + the **best** `class start + class gains x (level-1)`
  over every lived class (`Character.base_stat`/`class_stat`) + gear + buffs. Only level, XP, gear,
  effects etc. are persisted.
- **Rebirth order must never matter** (the user's rule): stats, HP per level and the mana pool all
  take the best of `lived_classes()` at the current level, so a character depends only on which
  classes it has lived. Each mastered class adds `MASTERY_BONUS` (2%) to max HP and to
  `damage_mult` (weapons and spells).
- **STR is weapon damage and DEX is precision for every class** (the user's rule; there is no
  per-class attack stat). Weapon damage = range + 0.35 STR + 0.5 level. DEX gives crit, dodge, armor
  and a lower miss chance on auto-attacks (`Character.miss_chance`: 10% - 0.07% per DEX, floor 2%).
  The rogue, ranger and bard grow STR +2/+2/+1 for this reason.
- **INT and WIS work the same for every class** (the user's rule, 2026-11-03; there is no CHA):
  INT scales damage, dot and drain effects, WIS scales heal, hot and shield effects and the mana pool
  (`Character.max_mana`: 15 + best class `mana` x level + 0.1 WIS x level). Summons use `"INT/WIS"`,
  the higher of the two (`Character.magic_stat`). Every class still gains exactly 5 whole points a
  level (the user's preference). When stats moved, heal/shield (and the bard's damage) per-level terms
  were raised so single-class characters at 50 kept their power; hybrid damage was deliberately not
  raised, because a multi-life character's INT 161 would stack on it. Necromancer mana is held at 12
  per level (full compensation would be 16) so best-of rebirth doesn't pair it with a cleric's WIS.
- HP and mana formulas live in `Character.max_hp/max_mana`. XP per level is
  `65 * level^1.7`, identical in every life (no rebirth penalty, by the user's choice).
  Kill XP (`combat.monster_xp`) is `15 + 14.5 * level^1.5`, so same-level kills per level climb
  from ~6 at 5-10 to ~10 at 50 (~390 per life). The user wants late levels never faster than
  early ones, and only a bit slower. Quest XP is fixed per quest in `data/quests.py`.
- Rebirth (level 50): the old class is appended to `past_lives` as `{"cls": id}` (no stat totals
  are stored). Abilities of every lived class stay known and unlock at their original level. All gear
  is unequipped into the pack, then the new class's starting `gear` is equipped.
- Tiers (`Character.tier`, 1-`MAX_TIER` 10): once every class is mastered, `rebirth` calls
  `Game.ascend` and `Character.rebirth` raises the tier and clears `past_lives` instead of appending
  (stats, mastery, abilities, training all reset; gold, items, bank, quests, boss kills stay). Every
  stat gets `TIER_BONUS` (10) x (tier - 1) in `base_stat`. Tier 10 with every class mastered is
  `eternal`: rebirth is refused and `display_name` is "Emperor <name> the Eternal" (stats header, greetings).
  **Tiers are never balanced for** (the user's rule): sims and tuning assume Tier 1.
- Race perks are keys in `RACES[...]["perks"]` read via `Character.perk()`: hp_mult,
  mana_mult, dmg_mult, crit, dodge, regen_mult, immune, xp_mult (supported, currently unused).
- Ability power = `base + lvl*level + scale*stat`. Spell cost scales `cost * (1 + 0.1*(level-1))`.

### Monsters
Templates only set multipliers. Real HP, damage and armor come from level in `MonsterInstance`
(`(20 + 15L)` HP times `MONSTER_HP_MULT`, etc.). To make a monster tougher, change its multipliers, not raw numbers.
Specials: big / dot / stun / drain / heal. Bosses respawn after 120 ticks, others after 30.
Monsters above level 50 (the Planes of the Gods) use larger multipliers (hp 3.5-5.6, dmg 2.6-3.4
for regulars; champions 4.85-6.6 / 2.3-2.9; elemental lords 6.4-10.5 / 2.5-3.25; Lord Trepth
7.4 / 2.35), because multi-life characters take the best stats of every class they have lived.
Everything from level 57 up got +12% HP after the INT/WIS rework.

### Gates and boss kills
- A room may carry `gate` (see `data/rooms/common.R`): `{"kills": [boss ids], "msg"}`,
  `{"item": item id, "msg"}` (carried, not used up) or `{"all_classes": True, "msg"}`.
  `Game.gate_block(rid)` checks it in `cmd_move` and when fleeing; `goto` ignores it. `validate.py`
  checks gate kills are bosses and gate items exist.
- `Character.boss_kills` records every boss id ever slain (set in `Game.on_kill`, kept across
  rebirths). `Character.mastered_classes()` = past lives + the current class once at level 50.
- Each elemental plane's first room needs the champion of the first-tier plane before it (Stars ->
  Air, Dreams -> Earth, Death -> Fire, Law -> Water). The Door of Eternity needs the four elemental lords; Lord Trepth's throne needs every class mastered.
  Killing him grants no title (by the user's choice).
- The Chancery of the Dead's Door of Audience needs a `writ_of_audience`, the reward for Clerk
  Quillon's first quest; he also sells duplicates.
- Hidden exits: a room's `hidden` field (`{dir: {"words", "prompt", "hint", "msg"}}`, see `data/rooms/common.R`)
  marks an ordinary exit as taken only with `enter <word>` (`cmd_enter`). It stays in `exits`, so maps,
  `find`, insets and `validate.py` treat it normally, but the Exits line, `exits`, speedwalks, fleeing
  and the `v`/`^` map marker skip it, walking that way prints the hint, and `find` prints
  `ENTER <WORD>` in its route (`route_text`). `look` prints the `prompt` ("Type ENTER MOUSEHOLE...")
  in bold magenta under the description, so the command stands out (the user's request). Used by the Willow Mill's mousehole into the Underhedge (by the user's choice).

### Inventory and items
- Inventory is a flat list of item ids (duplicates = quantity). Equipment is `{slot: id}` over
  `items.SLOTS` (one ring slot).
- Armor and weapon training: every weapon and armor item has a `kind` (a `WEAPON_KINDS` family,
  an `ARMOR_TIERS` tier, `shield`, or the free kinds `offhand`, `jewelry`, `any`). Classes set
  `armor` (heaviest tier), `shield` and `weapons`. `Character.trained_for` takes the union over
  `lived_classes()`, so training survives rebirth (the user wants that as a reason to live a plate
  class). `load_game` moves untrained gear from old saves into the pack. `validate.py` checks kinds
  fit slots and that starting gear is allowed; `balance_sim.py gear` shows each tier's best
  armor by level (look for gaps when adding items), and `unlock` measures a plate past life.
- Loot and gold go straight into the inventory on kill. Ground items only come from `drop`.
- Sell price is always `value // 3`. Buy price = `value`.

### Quests, NPCs, find
- Quests are `kill` (counted in `on_kill`) or `collect` (counted from inventory, removed on
  turn-in). They are offered and turned in through `talk`, which turns in every ready quest and
  accepts every available one at once (progress lines only when there is nothing else to say).
  `prereq` and `min_level` gate them.
- `find` runs a BFS over room exits to the nearest room that *spawns* the target (or the quest
  giver once ready). It doesn't check whether the monster is currently alive.

### Player aliases
Stored in `Character.aliases` and saved. They are expanded once at the top of `handle()`,
with extra words appended. `reserved_words()` (every `cmd_*`, `ALIASES`, directions, `go`)
can never be aliased, and an alias can't start with another alias.

## Conventions

- New command: add `cmd_<name>(self, args)` to `Game`. It is picked up automatically. Add short
  forms to `Game.ALIASES`, and add it to `NO_COMBAT` / `SLEEP_OK` if relevant, to the `HELP`
  table and to the README.
- Content goes in `data/` via the helper constructors (`weapon()`, `armor()`, `M()`, `R()`,
  `spell()`, `ability()`). Room exits must be two-way.
- All output goes through `ui.say` (wrapped), `ui.out` (raw) or `ui.rule`. Never use `print`
  directly: `ui._emit` tracks the open prompt and starts on a fresh line under it.
- Combat lines are not indented, and the round shows no HP/mana bar row (user preference).
  HP, mana and level % live in the prompt.
- Text tone is high fantasy. Room descriptions are 2-4 sentences.
- Save format: `saves/<name>.json` = `{version, player, room, world}`. New `Character` fields
  need a default in `from_dict` (see `aliases`) so old saves still load.

## Balance notes

Tuned with `tools/balance_sim.py`: same-level fights cost roughly 25-55% HP, and bosses are
beatable at level+3 with potions. Necromancer, with its pet and drain, is the strongest solo
class. That is intended. Wizards are fragile and get no area spell until Fireball at 16.
With armor training, wizards rely on Mana Shield (strengthened to 15 + 4.5/level + 1.3 INT when
cloth-only gear went in, and to 17 + 5.2/level + 1.5 INT when the auto-attack began landing
alongside every action, a change that helped melee classes far more than casters; since the INT/WIS
rework it is 17 + 6.79/level + 1.5 WIS, and wizards grow INT 3 / WIS 2 with no DEX); they clear
ordinary fights with lots of HP to spare but are 65-100% (about 87% on average) against bosses at
the boss's own level. Note: the sims of 2026-11-01 show same-level fights costing only ~0-50% HP
(median ~20%), easier than the 25-55% target, both before and after the swing change. Bards used to be too slow to kill bosses (30+ rounds);
Discordant Note was raised to 10 + 2.4/level + 0.8 CHA and their unused INT gain became DEX.
They now win 55-100% of boss fights at the boss's own level (the Bog Hag, about 40%, is the
hardest) and essentially all at +3. After the INT/WIS rework (bards grow INT/WIS/STR/DEX/CON +1 each,
Discordant Note 10 + 3.22/level + 0.8 INT) they win 53-100% at the boss's own level (Old Mother
Gristle is the hardest) and all at +3. The rework (2026-11-03) also cost shamans and dread knights a
point of CON a level (about -28% HP at 50); the user accepted that.

Endgame (`balance_sim.py endgame`, level-50 characters with 1/6/11 lives, best-in-slot gear),
retuned 2026-11-01 for the best-of rebirth rule: first-tier plane monsters are 25-55% for a 1-life
character (the level-54 ones near 0%) and trivial with 6; plane champions ~65-90% with 6 lives and
100% with 11; elemental lords ~0-50% with 6 lives and ~90-97% with 11; Lord Trepth ~70% with 11
(every class about 50-85%). After the swing change and `MONSTER_HP_MULT` 1.3: champions ~88-97%
with 6 lives, lords 4-43% with 6 and 86-92% with 11, Lord Trepth ~65% with 11. After the INT/WIS
rework and +12% HP from level 57: champions 95-100% with 6 lives, lords 5-39% with 6 and 90-99%
with 11, Lord Trepth ~69% with 11 (worst class 45%). The user asked for Trepth to need a full every-class character with
good gear. Six lives already hold most of the best stats, so the 6-to-11 gap comes mainly from the
mastery bonus (+12% vs +22%) and the remaining classes' growth (the rogue's and ranger's DEX).
