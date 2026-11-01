"""The Mycelial Wards, west of Westmarch's Old Watchtower (12-20). A city grown from one vast fungal
network, whose capfolk share a partial hive mind: the deeper the ward, the more 'we' and the less
'I'. Most citizens ignore the living; only the spore wardens and the things of the Rot Ward and the
deep network attack on sight. A quiet path leads south from the Gilled Houses into the Vanes'
neglected garden and the Hedge Maze of Thornwick Hall."""
from data.rooms.common import R

AREA = "The Mycelial Wards"

ROOMS = {
    # ------------------------------------------------- the approach (12-13)
    "mouldering_path": R(
        "The Mouldering Path", AREA,
        "West of the watchtower, the path drops into a damp hollow where the grass turns grey and soft "
        "underfoot. Toadstools line the way, each larger than the last, until they stand taller than "
        "you. Pale threads lace the soil, and when you step on them, something far off seems to notice.",
        {"e": "old_watchtower", "w": "ward_gate"},
        spawns=[("myconid_drudge", 2)], level=(12, 12)),
    "ward_gate": R(
        "The Ward Gate", AREA,
        "Two great shelf-fungi have grown together across the path into an arch, gilled like a "
        "cathedral roof. Beyond it lies a city of hollowed mushrooms, lit by a soft green glow. Spore "
        "wardens in armour of hardened cap stand beneath the arch, swaying gently in unison.",
        {"e": "mouldering_path", "w": "gill_street"},
        spawns=[("spore_warden", 1), ("myconid_drudge", 1)], level=(12, 13)),

    # ------------------------------------------------- the Gilled Quarter (13-15)
    "gill_street": R(
        "Gill Street", AREA,
        "A street of houses grown from giant mushrooms, their doors cut into the stalks and their "
        "windows glowing between the gills. Capfolk go about their business, pale and soft-footed, "
        "and murmur to each other without moving their lips. Each one turns its head toward you, and "
        "then, all together, they turn away.",
        {"e": "ward_gate", "w": "spore_square", "n": "hall_of_voices", "s": "gilled_houses"},
        spawns=[("capfolk_citizen", 2), ("spore_warden", 1)], level=(13, 14)),
    "gilled_houses": R(
        "The Gilled Houses", AREA,
        "The poorer end of the quarter, where the houses grow close and lopsided and the gills drip "
        "onto the street. Capfolk tend little gardens of moss in the doorways. To the south, the "
        "mushrooms thin out, and a faint scent of cut grass comes from somewhere beyond them.",
        {"n": "gill_street", "s": "thinning_caps"},
        spawns=[("capfolk_citizen", 2), ("gill_tender", 1)], level=(13, 14)),
    "hall_of_voices": R(
        "The Hall of Many Voices", AREA,
        "A vast, hollow cap forms a domed hall, its ceiling ribbed with gills that glow softly green. "
        "Threads of the network hang down like the strings of a harp and hum when anyone speaks. This "
        "is where the network talks to visitors, and it is very patient with them.",
        {"s": "gill_street"},
        npcs=["many_voiced_speaker"], safe=True),

    # ------------------------------------------------- the garden path to Thornwick (no monsters)
    "thinning_caps": R(
        "The Thinning Caps", AREA,
        "The mushrooms grow smaller and farther apart here, and green grass pushes up between them for "
        "the first time. The pale threads in the soil grow thin and sparse, and the hum of the network "
        "fades to a whisper. To the south, through the last of the caps, you can see the dark line of a "
        "tall, clipped hedge.",
        {"n": "gilled_houses", "s": "old_garden_wall"}),
    "old_garden_wall": R(
        "The Old Garden Wall", AREA,
        "A wall of old red brick crosses the hollow, half-swallowed by moss and shelf-fungus, with a "
        "rotten wooden door hanging open in it. A painted sign over the door, almost worn away, shows a "
        "silver stag. Scratched beneath it, in a far rougher hand: TURN BACK. THE VANES HUNT MORE THAN "
        "DEER. The grass beyond is mown.",
        {"n": "thinning_caps", "s": "overgrown_arbour"}),
    "overgrown_arbour": R(
        "The Overgrown Arbour", AREA,
        "A long arbour of iron hoops, once a rose walk in some great house's garden, has gone wild. "
        "Climbing roses and yew shoots twist through it, and the last few pale toadstools cling to its "
        "roots. South, the arbour opens into a maze of clipped yew, and you can hear hounds baying and "
        "a hunting horn. Whoever keeps this garden is far stronger than anything in the Wards.",
        {"n": "old_garden_wall", "s": "hedge_maze"}),

    # ------------------------------------------------- the Puffball Market (14-16)
    "spore_square": R(
        "Spore Square", AREA,
        "The heart of the city is a wide square around a single giant puffball, which breathes out a "
        "slow cloud of glittering spores every few minutes. The capfolk stop whatever they are doing "
        "and breathe it in together. Streets lead off toward the market, the glowing ward to the north "
        "and a darker way west.",
        {"e": "gill_street", "w": "threadway", "n": "glowcap_lane", "s": "puffball_market"},
        spawns=[("capfolk_citizen", 2), ("puffball_hawker", 1)], level=(14, 15)),
    "puffball_market": R(
        "The Puffball Market", AREA,
        "Stalls of woven root sell things you cannot name: jellies that glow, dried caps that whisper, "
        "jars of spores sorted by colour. There is no haggling and no money. Each capfolk simply knows "
        "what every other one needs, and hands it over, and you are the only one in the market who has "
        "to ask.",
        {"n": "spore_square", "w": "sporedrift_stalls"},
        spawns=[("puffball_hawker", 2), ("capfolk_porter", 1)], level=(14, 15)),
    "sporedrift_stalls": R(
        "The Sporedrift Stalls", AREA,
        "At the windy end of the market, spores drift in slow, glittering clouds between the stalls, "
        "thick enough to hide a person. The clouds move against the wind, and gather around anyone who "
        "stands still for too long.",
        {"e": "puffball_market"},
        spawns=[("spore_drift", 2), ("capfolk_porter", 1)], level=(15, 16)),

    # ------------------------------------------------- the Glowcap Ward (15-17)
    "glowcap_lane": R(
        "Glowcap Lane", AREA,
        "North of the square, the mushrooms glow blue instead of green, and the capfolk move slowly, "
        "as if thinking very hard about every step. Their speech is all 'we' here. A scholar pauses as "
        "you pass and says, 'We have been considering you,' and then walks on.",
        {"s": "spore_square", "n": "lantern_halls"},
        spawns=[("glowcap_scholar", 2), ("lantern_cap", 1)], level=(15, 16)),
    "lantern_halls": R(
        "The Lantern Halls", AREA,
        "Hall after hall of luminous caps light the ward like a city of paper lanterns. The light is "
        "cold and beautiful, and it hums faintly with the network's thoughts. Stand still and you can "
        "almost hear them: slow, enormous, and not unkind.",
        {"s": "glowcap_lane", "w": "slow_library", "n": "dreaming_dome"},
        spawns=[("lantern_cap", 2), ("glowcap_scholar", 1)], level=(16, 16)),
    "slow_library": R(
        "The Slow Library", AREA,
        "The network keeps its memory here, in shelf upon shelf of dried caps, each holding a single "
        "thought that took a hundred years to think. Scholars press their foreheads to the caps and "
        "stand motionless for days. One of them has been reading the same cap since before Brightwater "
        "was founded.",
        {"e": "lantern_halls"},
        spawns=[("glowcap_scholar", 2)], level=(16, 17)),
    "dreaming_dome": R(
        "The Dreaming Dome", AREA,
        "Under a dome of translucent blue cap, a single ancient capfolk sits in a bed of moss, so deeply "
        "joined to the network that its body has grown into the floor. It dreams, and the dream leaks "
        "out: the walls show forests that never grew and cities that never fell, and for a moment you "
        "see yourself among them.",
        {"s": "lantern_halls"},
        spawns=[("dreaming_sage", 1)], level=(17, 17)),

    # ------------------------------------------------- the Rot Ward (17-19)
    "threadway": R(
        "The Threadway", AREA,
        "West of the square, the street becomes a tunnel of white threads, thick as rope and woven "
        "tight overhead. The glow fades to a sickly yellow and the air turns warm and sweet. The capfolk "
        "here are fewer and quieter, and they watch you with something like appetite.",
        {"e": "spore_square", "w": "rot_gate"},
        spawns=[("rot_tender", 1), ("capfolk_porter", 1)], level=(16, 17)),
    "rot_gate": R(
        "The Rot Gate", AREA,
        "A gate of black, oozing fungus marks the edge of the Rot Ward, where the strain that breaks "
        "down the dead holds sway. The rot-folk are polite, patient and hungry. A carving on the gate, "
        "older than the rest, shows the network sending a single dark thread east, toward the elves' "
        "forest, with a mark beside it that means 'lost'.",
        {"e": "threadway", "w": "rendering_pits", "s": "compost_halls", "n": "whispering_grove"},
        spawns=[("rot_tender", 2), ("bone_bloom", 1)], level=(17, 18)),
    "compost_halls": R(
        "The Compost Halls", AREA,
        "Long, steaming halls where the Rot Ward breaks down everything the city no longer needs: "
        "leaves, wood, animals, and things that were once capfolk. Great crawling things turn the heaps. "
        "It smells of earth and endings, and it is very warm.",
        {"n": "rot_gate", "w": "ossuary_gardens"},
        spawns=[("compost_crawler", 2), ("rot_tender", 1)], level=(17, 18)),
    "ossuary_gardens": R(
        "The Ossuary Gardens", AREA,
        "Bones are planted here in neat rows like seed potatoes, and fungus grows from them in fans "
        "of white and ivory. Some of the bones are old animals. Some are not. At the centre, a vast, "
        "motherly mound of rot tends the beds, humming to them.",
        {"e": "compost_halls"},
        spawns=[("the_rotmother", 1), ("bone_bloom", 1)], level=(18, 19)),
    "whispering_grove": R(
        "The Whispering Grove", AREA,
        "A grove of tall, thin stalks that whisper constantly in a voice made of a thousand voices. "
        "Capfolk stand among them with their eyes closed, swaying, so far into the network that they "
        "have forgotten they were ever separate. When you speak, the grove repeats your words, slightly "
        "wrong.",
        {"s": "rot_gate"},
        spawns=[("whispering_host", 2)], level=(18, 18)),
    "rendering_pits": R(
        "The Rendering Pits", AREA,
        "Deep pits of bubbling black rot where the Rot Ward renders down what the compost halls cannot. "
        "Things float to the surface and sink again. The renderers who work the pits are huge and "
        "silent, and they look at you the way a cook looks at a joint of meat.",
        {"e": "rot_gate", "w": "root_hollows"},
        spawns=[("rot_renderer", 2)], level=(18, 19)),

    # ------------------------------------------------- the deep network (19-20)
    "root_hollows": R(
        "The Root Hollows", AREA,
        "Below the city, the ground opens into hollows laced with threads as thick as tree trunks, "
        "pulsing slowly with a pale light. This is the network itself, and you are inside it. Things "
        "crawl along the threads like blood along a vein.",
        {"e": "rendering_pits", "n": "thinking_dark"},
        spawns=[("root_crawler", 2), ("thought_spore", 1)], level=(19, 19)),
    "thinking_dark": R(
        "The Thinking Dark", AREA,
        "A cavern of absolute dark, except for the threads, which flicker with thoughts too large to "
        "understand. You feel them brush against your mind: curiosity, then hunger, then a vast, "
        "patient indifference. Something to the west is thinking about you.",
        {"s": "root_hollows", "w": "heart_of_network"},
        spawns=[("thought_spore", 2), ("root_crawler", 1)], level=(19, 20)),
    "heart_of_network": R(
        "The Heart of the Network", AREA,
        "Every thread in the Wards runs here, into a single vast growth that fills the cavern: a "
        "mushroom older than any city, its cap lost in the dark above and its gills glowing with every "
        "colour of every ward. This is the First Spore, from which all the rest have grown. It does not "
        "hate you. It simply has a use for you.",
        {"e": "thinking_dark"},
        spawns=[("the_first_spore", 1), ("thought_spore", 1)], level=(20, 20)),
}
