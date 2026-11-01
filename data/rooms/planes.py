"""The Planes of the Gods, above the Temple of the Dawn (51-60).

The Threshold of the Gods is the hub. Tier one opens on its four sides, and each leads straight on to
one elemental plane: Stars (north) to Air, Dreams (west) to Earth, Death (east) to Fire, and Law
(south) to Water. Each elemental plane opens only once its first-tier champion is slain. The Plane
of Eternity lies above the Threshold, through the Door of Eternity, which
opens once all four elemental lords are slain. Lord Trepth's throne opens only for a character who has
lived every class to level 50.
"""
from data.rooms.common import R

ELEMENTAL_LORDS = ["lord_fire", "lord_water", "lord_earth", "lord_air"]

ROOMS = {
    # ================================================================= THE THRESHOLD (safe)
    "threshold_stair": R(
        "The Stair of Dawn", "Threshold of the Gods",
        "A stair of white light climbs from behind the altar of the Temple of the Dawn into a sky with "
        "no ground beneath it. Far below, Brightwater is a toy town. Above, the stair ends at a court "
        "of white stone where gates of light stand open on worlds that are not this one.",
        {"d": "temple", "u": "threshold_court"}, safe=True),
    "threshold_court": R(
        "The Threshold of the Gods", "Threshold of the Gods",
        "A court of white stone floats in an endless golden sky. Four gates stand open around it: "
        "north onto a night full of stars, west onto a moonlit forest that sways as if asleep, east "
        "onto a grey twilight where pale fires burn, and south onto a wall of white stone and black "
        "bars. High above, a door of bronze hangs in the sky at the top of a stair of light. A herald "
        "in white waits beside a fountain of light.",
        {"d": "threshold_stair", "n": "stars_gate", "w": "dreams_gate", "e": "death_gate", "s": "law_gate",
         "u": "eternity_door"},
        npcs=["herald"], safe=True),

    # ================================================================= PLANE OF LAW (51-55)
    "law_gate": R(
        "Plane of Law: The Gaol Gate", "Plane of Law",
        "The southern gate of the Threshold opens onto a gate of black bars twenty feet high, set in a "
        "wall of white stone that runs left and right forever. Above it, letters of light spell out "
        "THE LAW IS ETERNAL. The gate stands open, and somewhere within, chains are dragging on stone.",
        {"n": "threshold_court", "s": "law_cellblock"},
        spawns=[("chained_penitent", 2)], level=(51, 52)),
    "law_cellblock": R(
        "Plane of Law: The Endless Cellblock", "Plane of Law",
        "Tiers of cells rise above you into a haze of light, row upon row, more than can be counted. "
        "Every door is barred with light, and behind each one sits a god, a giant or a spirit serving a "
        "sentence measured in ages. Iron wardens walk the galleries, keys ringing at their belts.",
        {"n": "law_gate", "w": "law_oubliette", "e": "law_wardens_walk", "s": "law_chain_yard"},
        spawns=[("iron_warden", 1), ("chained_penitent", 1)], level=(52, 53)),
    "law_oubliette": R(
        "Plane of Law: The Oubliette", "Plane of Law",
        "A round pit in the floor drops into darkness so deep that the light of the plane cannot reach "
        "it, covered by a grate of white iron. The prisoners down there were forgotten on purpose. Some "
        "of them have climbed out, still wearing their chains.",
        {"e": "law_cellblock"},
        spawns=[("chained_penitent", 3)], level=(51, 52)),
    "law_wardens_walk": R(
        "Plane of Law: The Warden's Walk", "Plane of Law",
        "A narrow gallery runs along the top of the cell tiers, lined with racks of shackles and iron "
        "keys. The wardens patrol it without rest, and their visored heads turn as one toward the "
        "sound of your footsteps.",
        {"w": "law_cellblock"},
        spawns=[("iron_warden", 2), ("chained_penitent", 1)], level=(53, 54)),
    "law_chain_yard": R(
        "Plane of Law: The Chain Yard", "Plane of Law",
        "An open yard of white flagstones, where the prisoners are brought out in chains to walk in "
        "endless circles under the eyes of the wardens. The chains are anchored to a pillar at the "
        "centre, carved with the scales of the law. East, great doors stand open on a hall of judgement. "
        "To the south, the prison's great sluice gate holds back a bright and endless sea.",
        {"n": "law_cellblock", "e": "law_hall", "s": "water_gate"},
        spawns=[("iron_warden", 2), ("chained_penitent", 1)], level=(53, 54)),
    "law_hall": R(
        "Plane of Law: The Hall of Judgement", "Plane of Law",
        "A courtroom vast enough to try a god, with a judge's bench of white marble beneath a pair of "
        "golden scales that hang from nothing. Before the bench stands a paladin in shining plate, his "
        "sword engraved with every law ever written. 'I am Stalworth Lightbearer, warden of this "
        "place,' he says. 'Lord Trepth judged me worthy. Now I judge you.'",
        {"w": "law_chain_yard"},
        spawns=[("stalworth", 1)], level=(55, 55)),

    # ================================================================= PLANE OF STARS (51-55)
    "stars_gate": R(
        "Plane of Stars: The Stargate", "Plane of Stars",
        "You step through the gate onto a road of silver light laid across the night. There is no "
        "ground and no horizon, only stars, near enough to touch and far enough to drown in. Great "
        "dark eagles wheel between them, their feathers pricked with light.",
        {"s": "threshold_court", "n": "stars_isles"},
        spawns=[("star_eagle", 2)], level=(51, 52)),
    "stars_isles": R(
        "Plane of Stars: The Drifting Isles", "Plane of Stars",
        "A cluster of floating islands drifts among the stars, joined by bridges of light, each isle "
        "crowned with an observatory of white marble. Sentinels of silver stand at every bridge. "
        "North, the greatest isle carries a hall whose roof is the night itself.",
        {"s": "stars_gate", "w": "stars_aerie", "e": "stars_storm", "n": "stars_hall"},
        spawns=[("star_eagle", 1), ("celestial_sentinel", 1)], level=(52, 53)),
    "stars_aerie": R(
        "Plane of Stars: The Great Aerie", "Plane of Stars",
        "A floating crag is woven over with nests the size of houses, built from the masts of ships "
        "and the tails of comets. Star eagles screech and take wing at your approach.",
        {"e": "stars_isles"},
        spawns=[("star_eagle", 3)], level=(51, 52)),
    "stars_storm": R(
        "Plane of Stars: The Comet Road", "Plane of Stars",
        "Comets stream past in a river of fire and ice, so close that their tails sting your skin. The "
        "sentinels stand in the stream unmoving. A path of starlight climbs north toward a storm "
        "that hangs among the stars.",
        {"w": "stars_isles", "n": "stars_thunder"},
        spawns=[("celestial_sentinel", 2), ("star_eagle", 1)], level=(53, 54)),
    "stars_thunder": R(
        "Plane of Stars: The Starstorm", "Plane of Stars",
        "At the end of the comet road, a storm of black cloud boils among the stars, struck by lightning "
        "every few heartbeats. The air tastes of iron. Above it, the night tears open onto a place of "
        "pure wind: the Plane of Air.",
        {"s": "stars_storm", "n": "air_gate"},
        spawns=[("celestial_sentinel", 2), ("star_eagle", 1)], level=(53, 54)),
    "stars_hall": R(
        "Plane of Stars: The Hall of the Star-Warden", "Plane of Stars",
        "A hall of white pillars open to the night, with every constellation turning slowly overhead. "
        "On a throne of silver sits a woman of starlight with folded wings and a bow of light across "
        "her knees. 'Few mortals reach my hall,' says Caelestra. 'Fewer leave it. Show me why the "
        "king should know your name.'",
        {"s": "stars_isles"},
        spawns=[("caelestra", 1)], level=(55, 55)),

    # ================================================================= PLANE OF DREAMS (51-55)
    "dreams_gate": R(
        "Plane of Dreams: The Ivory Gate", "Plane of Dreams",
        "You pass through a gate of carved ivory into a forest under a moon that is far too large. The "
        "trees sway though there is no wind, and the ground gives softly underfoot, like a bed. Pale "
        "shapes slip between the trunks, never quite where you look.",
        {"e": "threshold_court", "w": "dreams_meadow"},
        spawns=[("dreamstalker", 2)], level=(51, 52)),
    "dreams_meadow": R(
        "Plane of Dreams: The Moonlit Meadow", "Plane of Dreams",
        "A meadow of silver grass where every flower is closed, as if asleep. Doors stand alone in the "
        "grass with nothing behind them, and some of them are open. A giant walks slowly among them "
        "with its eyes shut.",
        {"e": "dreams_gate", "w": "dreams_roots", "n": "dreams_forest"},
        spawns=[("dreamstalker", 2), ("sleepwalker", 1)], level=(52, 53)),
    "dreams_forest": R(
        "Plane of Dreams: The Forest of Sleep", "Plane of Dreams",
        "The trees here grow so close that you must squeeze between them, and they breathe slowly, in "
        "and out, like sleepers. Some of them have faces, and the faces are dreaming.",
        {"s": "dreams_meadow", "w": "dreams_house"},
        spawns=[("sleepwalker", 2)], level=(53, 54)),
    "dreams_house": R(
        "Plane of Dreams: The Remembered House", "Plane of Dreams",
        "A house stands in a clearing, and you know it, though you have never been here. Its rooms "
        "are bigger inside than out and never in the same order twice. Something tall and pale "
        "follows you from room to room, always one door behind.",
        {"e": "dreams_forest", "s": "dreams_roots"},
        spawns=[("sleepwalker", 1), ("dreamstalker", 2)], level=(53, 54)),
    "dreams_roots": R(
        "Plane of Dreams: The Roots of the Dream", "Plane of Dreams",
        "The whole forest grows from the roots of one great tree, as thick as rivers and silver in the "
        "moonlight. Below, they plunge down into the dark, toward a deep place of stone: the Plane "
        "of Earth. West, a soft grey light spills from a hollow in the tree.",
        {"e": "dreams_meadow", "n": "dreams_house", "w": "dreams_loom", "s": "earth_gate"},
        spawns=[("dreamstalker", 1), ("sleepwalker", 1)], level=(53, 54)),
    "dreams_loom": R(
        "Plane of Dreams: The Loom of Sleep", "Plane of Dreams",
        "Inside the hollow of the great tree, a woman of moonlight sits at a loom of silver, weaving "
        "a cloth that shows every dream being dreamed in every world. Moths sleep in her hair. 'You "
        "are dreaming this,' says Somnara. 'Let us see if you wake.'",
        {"e": "dreams_roots"},
        spawns=[("somnara", 1)], level=(55, 55)),

    # ================================================================= PLANE OF DEATH (51-55)
    "death_gate": R(
        "Plane of Death: The Gate of Bones", "Plane of Death",
        "Beyond the gate is a twilight that never ends, grey and still and smelling of cold ash. Pale "
        "horses with no riders and no shadows graze on grey grass, and lift their heads to watch you "
        "pass.",
        {"w": "threshold_court", "e": "death_road"},
        spawns=[("pale_horse", 2)], level=(51, 52)),
    "death_road": R(
        "Plane of Death: The Road of the Dead", "Plane of Death",
        "A long road of grey stone runs into the twilight, and the dead walk it in silence: kings and "
        "beggars, soldiers and children, all going the same way. None of them look at you, but the "
        "hooded reapers who walk beside them do.",
        {"w": "death_gate", "n": "death_ossuary", "e": "death_pyres"},
        spawns=[("pale_horse", 2), ("reaper", 1)], level=(52, 53)),
    "death_ossuary": R(
        "Plane of Death: The Ossuary of the Gods", "Plane of Death",
        "Halls of bone run on forever, their walls stacked with the skulls of gods who died in the "
        "first ages of the world, every one of them still wearing its crown. Reapers walk the halls, "
        "counting.",
        {"s": "death_road", "e": "death_river"},
        spawns=[("reaper", 2)], level=(53, 54)),
    "death_river": R(
        "Plane of Death: The River of Forgetting", "Plane of Death",
        "A black river slides past without a sound, and the dead wade into it and do not come out. "
        "Whoever drinks from it forgets their name. On the far bank, something pale waits for you to "
        "cross.",
        {"w": "death_ossuary", "s": "death_pyres"},
        spawns=[("reaper", 2), ("pale_horse", 1)], level=(53, 54)),
    "death_pyres": R(
        "Plane of Death: The Pyre Fields", "Plane of Death",
        "Funeral pyres burn in rows to the edge of sight, and the smoke rises in the shapes of the "
        "people who burned. South, the flames run together into a world made only of fire. East, a "
        "hall of grey stone stands with its doors open.",
        {"w": "death_road", "n": "death_river", "e": "death_hall", "s": "fire_gate"},
        spawns=[("pale_horse", 2)], level=(53, 54)),
    "death_hall": R(
        "Plane of Death: The Hall of the Last Breath", "Plane of Death",
        "A hall of grey stone, silent as a held breath, where a great book lies open on a lectern of "
        "bone. A gaunt giant in a robe of ash turns its pages by the light of a cold blue lantern. "
        "'Every name ends here,' says Morthis. 'I have been keeping a page for yours.'",
        {"w": "death_pyres"},
        spawns=[("morthis", 1)], level=(55, 55)),

    # ================================================================= PLANE OF FIRE (54-58)
    "fire_gate": R(
        "Plane of Fire: The Burning Gate", "Plane of Fire",
        "You step out of the smoke of the pyres onto a plain of black glass beneath a sky of flame. The heat "
        "would kill a lesser being in a breath. Spirits of fire with brass bracers turn their burning "
        "eyes on you.",
        {"n": "death_pyres", "s": "fire_lava"},
        spawns=[("efreet", 2)], level=(54, 55),
        gate={"kills": ["morthis"],
              "msg": "The flames to the south burn grey and cold, and will not let the living through. Only "
                     "one whose name the Keeper of the Dead has failed to write may pass."}),
    "fire_lava": R(
        "Plane of Fire: The Sea of Lava", "Plane of Fire",
        "A sea of molten rock stretches to every horizon, crossed by causeways of black glass. Birds of "
        "living fire skim the surface, and the efreet bathe in it.",
        {"n": "fire_gate", "w": "fire_cinders", "e": "fire_pyre", "s": "fire_furnace"},
        spawns=[("efreet", 1), ("pyre_phoenix", 1)], level=(55, 56)),
    "fire_cinders": R(
        "Plane of Fire: The Cinder Fields", "Plane of Fire",
        "Fields of white-hot cinders drift like snow in a wind of fire. The efreet hunt here in "
        "packs, laughing.",
        {"e": "fire_lava"},
        spawns=[("efreet", 2)], level=(55, 56)),
    "fire_pyre": R(
        "Plane of Fire: The Phoenix Pyre", "Plane of Fire",
        "A mountain of burning wood that never burns away, where the phoenixes come to die and be "
        "reborn. Eggs of fire crack open in the flames.",
        {"w": "fire_lava"},
        spawns=[("pyre_phoenix", 2)], level=(56, 57)),
    "fire_furnace": R(
        "Plane of Fire: The Great Furnace", "Plane of Fire",
        "A furnace the size of a city roars in the heart of the plane, and the light of it is too "
        "bright to look at. South, in the white heart of the flame, something vast is waiting.",
        {"n": "fire_lava", "s": "fire_throne"},
        spawns=[("pyre_phoenix", 1), ("efreet", 1)], level=(56, 57)),
    "fire_throne": R(
        "Plane of Fire: The Throne of Flame", "Plane of Fire",
        "At the heart of the Great Furnace, on a throne of white-hot stone, sits a giant with a crown "
        "of fire and a hammer that is a captive star. Rekkn rises. 'Burn bright,' he says, 'and I "
        "will remember your light.'",
        {"n": "fire_furnace"},
        spawns=[("lord_fire", 1)], level=(58, 58)),

    # ================================================================= PLANE OF WATER (54-58)
    "water_gate": R(
        "Plane of Water: The Bright Shore", "Plane of Water",
        "Beyond the prison's sluice gate, a shore of white sand runs down to the Plane of Water: an "
        "ocean without a bottom or a far shore, where you can somehow breathe. Waves with cold eyes "
        "roll in toward you, as if the sea itself were the last guard of the gaol.",
        {"n": "law_chain_yard", "s": "water_shallows"},
        spawns=[("tide_elemental", 2)], level=(54, 55),
        gate={"kills": ["stalworth"],
              "msg": "The sluice gate is shut and sealed with a lock of white light. Only the warden of "
                     "the prison holds the key."}),
    "water_shallows": R(
        "Plane of Water: The Endless Shallows", "Plane of Water",
        "Blue-green water stretches in every direction, waist-deep and warm. Reefs rise to the west, "
        "kelp forests sway to the east, and to the south the sea floor drops away into a blackness "
        "that goes down forever.",
        {"n": "water_gate", "s": "water_abyss", "w": "water_reef", "e": "water_kelp"},
        spawns=[("tide_elemental", 1), ("abyssal_kraken", 1)], level=(55, 56)),
    "water_reef": R(
        "Plane of Water: The Coral Cathedral", "Plane of Water",
        "A reef has grown into the shape of a vast cathedral, with spires of coral and windows of "
        "living fish. Tide elementals move through its aisles like a congregation.",
        {"e": "water_shallows"},
        spawns=[("tide_elemental", 2)], level=(55, 56)),
    "water_kelp": R(
        "Plane of Water: The Kelp Forest", "Plane of Water",
        "Kelp as tall as the trees of the Eldergrove sways in a slow current, dimming the light to "
        "green. Tentacles as thick as towers coil between the stalks.",
        {"w": "water_shallows"},
        spawns=[("abyssal_kraken", 1), ("tide_elemental", 1)], level=(56, 57)),
    "water_abyss": R(
        "Plane of Water: The Abyss", "Plane of Water",
        "You sink into the lightless deep, where the cold is crushing and the only light comes from "
        "the eyes of things that should not exist. Krakens drift past like thunderclouds. Further "
        "down, a palace of green sea-glass glows on the edge of the abyss.",
        {"n": "water_shallows", "s": "water_throne"},
        spawns=[("abyssal_kraken", 2)], level=(56, 57)),
    "water_throne": R(
        "Plane of Water: The Palace of the Tides", "Plane of Water",
        "A palace of green sea-glass stands on the brink of the abyss, its halls flooded with silver "
        "light. On a throne of pearl sits a crowned giant with a trident of coral. 'The tide takes "
        "all things,' says Nerevos. 'Let us see if it takes you.'",
        {"n": "water_abyss"},
        spawns=[("lord_water", 1)], level=(58, 58)),

    # ================================================================= PLANE OF EARTH (54-58)
    "earth_gate": R(
        "Plane of Earth: The Root Descent", "Plane of Earth",
        "The roots of the dreaming tree plunge down through solid rock, and you follow them into "
        "the Plane of Earth, a world of stone without a sky. Shapes of living granite step out of "
        "the walls.",
        {"n": "dreams_roots", "s": "earth_caverns"},
        spawns=[("granite_elemental", 2)], level=(54, 55),
        gate={"kills": ["somnara"],
              "msg": "You climb down among the roots, and find yourself climbing up them again. The way "
                     "down is only a dream, and the Dreamweaver will not let you wake from it."}),
    "earth_caverns": R(
        "Plane of Earth: The Endless Caverns", "Plane of Earth",
        "Caverns open one into another without end, lit by veins of glowing ore. Crystal glitters to "
        "the west, great roots grip the stone to the east, and a deeper dark lies to the south.",
        {"n": "earth_gate", "w": "earth_crystal", "e": "earth_root", "s": "earth_deeps"},
        spawns=[("granite_elemental", 1), ("crystal_basilisk", 1)], level=(55, 56)),
    "earth_crystal": R(
        "Plane of Earth: The Crystal Gardens", "Plane of Earth",
        "Crystals as tall as towers grow in a cavern of blinding light, and statues of glass stand "
        "among them: everything the basilisks have ever looked at.",
        {"e": "earth_caverns"},
        spawns=[("crystal_basilisk", 2)], level=(56, 57)),
    "earth_root": R(
        "Plane of Earth: The Root of the World", "Plane of Earth",
        "The deepest roots of the world tree pierce the stone here, older than mountains, and granite "
        "elementals tend them like gardeners.",
        {"w": "earth_caverns"},
        spawns=[("granite_elemental", 2)], level=(55, 56)),
    "earth_deeps": R(
        "Plane of Earth: The Grinding Deeps", "Plane of Earth",
        "The walls of the deeps move, slowly, grinding against each other with a sound that you feel "
        "in your teeth. Basilisks of living crystal pick their way across the shifting floor. South, "
        "a mountain is waiting.",
        {"n": "earth_caverns", "s": "earth_throne"},
        spawns=[("crystal_basilisk", 2), ("granite_elemental", 1)], level=(56, 57)),
    "earth_throne": R(
        "Plane of Earth: The Heart of the Mountain", "Plane of Earth",
        "A cavern so vast that you cannot see its walls, and at its heart a mountain that is not a "
        "mountain. It opens two crystal eyes. 'I was here before your world,' says Ulmathra, 'and I "
        "will be here after it. Strike, and be remembered.'",
        {"n": "earth_deeps"},
        spawns=[("lord_earth", 1)], level=(58, 58)),

    # ================================================================= PLANE OF AIR (54-58)
    "air_gate": R(
        "Plane of Air: The Windgate", "Plane of Air",
        "Above the starstorm there is no ground at all, only a sky of silver wind that holds you up like "
        "water. Columns of black cloud howl past, crackling with lightning.",
        {"s": "stars_thunder", "n": "air_cyclone"},
        spawns=[("storm_elemental", 2)], level=(54, 55),
        gate={"kills": ["caelestra"],
              "msg": "The tear in the night above the storm is sealed with a lattice of starlight. Only "
                     "the Star-Warden's leave opens the way to the winds."}),
    "air_cyclone": R(
        "Plane of Air: The Eye of the Cyclone", "Plane of Air",
        "You stand in the calm eye of a cyclone a hundred leagues across, its walls a spinning storm. "
        "Birds the size of clouds circle overhead, and a silver crown of lightning flickers far to "
        "the north.",
        {"s": "air_gate", "w": "air_vortex", "e": "air_spires", "n": "air_throne"},
        spawns=[("storm_elemental", 1), ("thunderbird", 1)], level=(55, 56)),
    "air_vortex": R(
        "Plane of Air: The Howling Vortex", "Plane of Air",
        "A whirlpool of wind spins down into nothing, dragging lightning with it. The storm elementals "
        "ride its walls like children on a swing.",
        {"e": "air_cyclone"},
        spawns=[("storm_elemental", 2)], level=(55, 56)),
    "air_spires": R(
        "Plane of Air: The Cloud Spires", "Plane of Air",
        "Spires of solid cloud rise from nowhere into nowhere, and thunderbirds nest on their tops. "
        "The sound of their wings is the sound of a storm breaking.",
        {"w": "air_cyclone", "n": "air_heights"},
        spawns=[("thunderbird", 2)], level=(56, 57)),
    "air_heights": R(
        "Plane of Air: The Highest Heights", "Plane of Air",
        "Above the spires, the air grows so thin that it glitters. Lightning walks here on legs of "
        "light, and the thunderbirds circle in a great ring.",
        {"s": "air_spires"},
        spawns=[("thunderbird", 2), ("storm_elemental", 1)], level=(56, 57)),
    "air_throne": R(
        "Plane of Air: The Court of the Winds", "Plane of Air",
        "Four winds meet in a court with no floor and no walls, and in the middle of them stands a "
        "shape of silver storm with a crown of lightning. 'Never still,' says Zephyrion, 'never "
        "caught. Catch me, and the king will hear of it.'",
        {"s": "air_cyclone"},
        spawns=[("lord_air", 1)], level=(58, 58)),

    # ================================================================= PLANE OF ETERNITY (57-60)
    "eternity_door": R(
        "The Door of Eternity", "Plane of Eternity",
        "At the top of the stair of light, beyond the bronze door, lies a hall of silence where every "
        "clock that was ever made hangs on the walls, each telling a different hour. The door shuts "
        "behind you without a sound. South, the Plane of Eternity turns like a great wheel.",
        {"d": "threshold_court", "s": "eternity_hourglass"}, safe=True,
        gate={"kills": ELEMENTAL_LORDS,
              "msg": "The bronze door is carved with four sigils: a flame, a wave, a mountain and a "
                     "whirlwind. It will not open until the four elemental lords have fallen to you."}),
    "eternity_hourglass": R(
        "Plane of Eternity: The Great Hourglass", "Plane of Eternity",
        "You stand inside an hourglass the size of a mountain, on a floor of golden sand that pours "
        "upward toward a sky of stars. Knights of brass and crystal march through the falling sand, "
        "leaving afterimages behind them.",
        {"n": "eternity_door", "w": "eternity_past", "e": "eternity_future", "s": "eternity_stair"},
        spawns=[("chronal_sentinel", 2)], level=(57, 58)),
    "eternity_past": R(
        "Plane of Eternity: The Halls of the Past", "Plane of Eternity",
        "Every moment that has ever happened is kept here, frozen in glass, in halls that go on "
        "forever. You see Elandor whole and Pyraxis young. Golems of glass and bronze guard the "
        "moments jealously.",
        {"e": "eternity_hourglass"},
        spawns=[("hourglass_golem", 2)], level=(58, 58)),
    "eternity_future": R(
        "Plane of Eternity: The Shores of Tomorrow", "Plane of Eternity",
        "A grey shore at the edge of everything that has not happened yet. Figures walk out of the "
        "mist toward you, and every one of them is you, older, or stranger, or worse.",
        {"w": "eternity_hourglass"},
        spawns=[("paradox", 2)], level=(59, 59)),
    "eternity_stair": R(
        "Plane of Eternity: The Stair of Ages", "Plane of Eternity",
        "A stair climbs through every age of the world at once: you pass the first dawn, the fall of "
        "Elandor, and a Brightwater that has not been built yet. At its top stands a door of white "
        "gold, carved with a crown.",
        {"n": "eternity_hourglass", "s": "trepth_throne"},
        spawns=[("chronal_sentinel", 1), ("hourglass_golem", 1), ("paradox", 1)], level=(58, 59)),
    "trepth_throne": R(
        "The Throne of Trepth", "Plane of Eternity",
        "A hall at the end of time, its walls the night sky as it will be on the last day. On a throne "
        "carved from the first moment sits the king of the gods. His face is every face, and his "
        "eyes hold every dawn. Lord Trepth rises, and lifts the sword called Eternity. 'You have walked "
        "every path,' he says. 'Now walk the last.'",
        {"n": "eternity_stair"},
        spawns=[("lord_trepth", 1)], level=(60, 60),
        gate={"all_classes": True,
              "msg": "The white-gold door does not move. A voice older than the stars speaks from beyond "
                     "it: 'Only one who has walked every path to its end may stand before the throne.'"}),
}
