"""The Clockwork Orchard, south of the Chancery of the Dead's Archive of Wills (38-44). The estate of the
gnome inventor Orrin Gearwhistle, where brass trees bear clockwork fruit and everything is wound by
hand. When Orrin grew old he wound himself into the great orrery at its heart so that he would never
die, and the Chancery, which has held his will for three hundred years, would very much like him to.
His creations mostly tend the orchard and ignore visitors; only his sentries, hounds, escapement
guardians and the molten springs of the foundry attack on sight."""
from data.rooms.common import R

AREA = "The Clockwork Orchard"

ROOMS = {
    # ------------------------------------------------- the way in (safe)
    "ticking_passage": R(
        "The Ticking Passage", AREA,
        "Behind the last shelf of the Archive of Wills, a passage of grey stone slopes down and out of "
        "the valley of the dead, and the silence of the Chancery gives way to a steady ticking, like a "
        "thousand clocks in the walls. A grey ghost with a satchel of papers waits here, as far as the "
        "court's writ allows it to go.",
        {"n": "archive_of_wills", "s": "brass_gate"},
        npcs=["assessor_morrow"], safe=True),

    # ------------------------------------------------- the orchard (38-40)
    "brass_gate": R(
        "The Brass Gate", AREA,
        "The passage opens on a gate of brass wrought into the shape of interlocking gears, which turn "
        "slowly as you watch. Beyond it rows of metal trees glitter under a clear sky. A brass sign on "
        "the gate reads: ORCHARD OF O. GEARWHISTLE. PLEASE DO NOT WIND THE TREES.",
        {"n": "ticking_passage", "s": "clockwork_orchard"},
        spawns=[("orchard_tender", 1), ("brass_sparrow", 2)], level=(38, 38)),
    "clockwork_orchard": R(
        "The Clockwork Orchard", AREA,
        "Trees of brass and copper stand in perfect rows, their leaves of hammered foil chiming in the "
        "breeze. Clockwork apples hang from the branches, ticking as they ripen. Gardeners of brass "
        "and enamel move between the trees with oilcans and keys, winding them one by one.",
        {"n": "brass_gate", "w": "copper_grove", "e": "silver_pear_walk", "s": "winding_house"},
        spawns=[("orchard_tender", 2), ("brass_sparrow", 1)], level=(38, 39)),
    "copper_grove": R(
        "The Copper Grove", AREA,
        "Here the trees are copper, gone green at the edges, and their fruit has stopped ticking. "
        "Patches of orange rust creep up the trunks from the roots. To the west the rust is worse, and "
        "something is eating the trees.",
        {"w": "rusting_corner", "e": "clockwork_orchard", "s": "brass_apiary"},
        spawns=[("orchard_tender", 1), ("rust_crawler", 1)], level=(39, 39)),
    "rusting_corner": R(
        "The Rusting Corner", AREA,
        "The farthest corner of the orchard has rusted almost away. Trees stand as orange skeletons, "
        "their fruit fallen and split, and flaking crawlers the size of dogs gnaw at the trunks, "
        "leaving trails of red dust.",
        {"e": "copper_grove"},
        spawns=[("rust_crawler", 2)], level=(39, 39)),
    "brass_apiary": R(
        "The Brass Apiary", AREA,
        "Rows of beehives built like little brass houses hum with mechanical bees, each one a jewelled "
        "body on wings of gold leaf. They carry a sweet, dark oil back to the hives, and they do not "
        "like to be disturbed.",
        {"n": "copper_grove", "e": "winding_house"},
        spawns=[("brass_bees", 2)], level=(39, 40)),
    "silver_pear_walk": R(
        "The Silver Pear Walk", AREA,
        "An avenue of silver pear trees runs east, espaliered against frames of iron, their pears so "
        "finely made that they open like lockets to show a tiny ticking heart. Clockwork sparrows "
        "squabble in the branches. To the east rises a tall tower with a great clock face.",
        {"w": "clockwork_orchard", "e": "cuckoo_tower", "s": "mechanical_pond"},
        spawns=[("brass_sparrow", 2), ("orchard_tender", 1)], level=(39, 39)),
    "cuckoo_tower": R(
        "The Cuckoo-Clock Tower", AREA,
        "A tower of carved and painted wood stands at the end of the walk, an enormous cuckoo clock "
        "taller than a castle keep. As you arrive, the little doors at its top fly open and something "
        "huge and feathered and made of brass leans out, shrieking the hour.",
        {"w": "silver_pear_walk"},
        spawns=[("great_cuckoo", 1), ("brass_sparrow", 1)], level=(40, 40)),
    "mechanical_pond": R(
        "The Mechanical Pond", AREA,
        "A round pond of clear water is full of clockwork fish, carp of gold and pike of steel, "
        "wound to swim in endless circles. Lily pads of green enamel float on the surface. Some of the "
        "pike have stopped circling, and are looking at you.",
        {"n": "silver_pear_walk", "w": "winding_house"},
        spawns=[("clockwork_pike", 2)], level=(40, 40)),
    "winding_house": R(
        "The Winding House", AREA,
        "A great wooden shed full of keys: brass keys as long as oars hang on every wall, one for every "
        "tree in the orchard. A huge automaton with arms like cranes takes them down and carries them "
        "out, one by one, and a sentry of polished steel stands at the door.",
        {"n": "clockwork_orchard", "w": "brass_apiary", "e": "mechanical_pond", "s": "hedge_of_springs"},
        spawns=[("winding_automaton", 1), ("clockwork_sentry", 1)], level=(40, 40)),

    # ------------------------------------------------- the gardens and the workshop (41-42)
    "hedge_of_springs": R(
        "The Hedge of Springs", AREA,
        "A hedge maze of coiled steel springs, trimmed into neat green-painted walls, opens onto three "
        "paths. West comes the clink of teacups, east the ring of hammers, and south a great humming "
        "like a vast clock thinking. Spring-loaded hounds patrol the paths.",
        {"n": "winding_house", "w": "unending_tea", "e": "inventors_workshop", "s": "orrery_steps"},
        spawns=[("spring_hound", 2)], level=(41, 41)),
    "unending_tea": R(
        "The Unending Tea Party", AREA,
        "A long table set for a tea party stands on a lawn of enamel grass, laid with silver and china "
        "and cakes that never go stale. Clockwork guests sit at it, pouring and sipping and laughing at "
        "the same joke they were laughing at three hundred years ago, and at the head of the table their "
        "hostess turns to see who has arrived late.",
        {"e": "hedge_of_springs"},
        spawns=[("tea_guest", 2), ("clockwork_hostess", 1)], level=(41, 41)),
    "inventors_workshop": R(
        "The Inventor's Workshop", AREA,
        "A cavernous workshop cluttered with lathes, vices, half-built creatures and drawings pinned to "
        "every wall. Unfinished automatons shuffle between the benches, missing hands or faces. At the "
        "largest bench, a towering automaton in a leather apron works on, perfectly, endlessly.",
        {"w": "hedge_of_springs", "e": "spring_foundry", "s": "escapement_hall"},
        spawns=[("unfinished_automaton", 2), ("master_automaton", 1)], level=(42, 42)),
    "spring_foundry": R(
        "The Spring Foundry", AREA,
        "A foundry where steel is drawn into wire and wound into springs, glowing in the heat of a "
        "great furnace. The molten metal has got loose: coils of white-hot steel writhe out of the "
        "crucibles and slither across the floor of their own accord.",
        {"w": "inventors_workshop"},
        spawns=[("molten_spring", 2)], level=(42, 42)),

    # ------------------------------------------------- the heart of the clock (43-44)
    "escapement_hall": R(
        "The Escapement Hall", AREA,
        "A hall built around a single enormous escapement, a toothed wheel as tall as a house that "
        "lurches forward one tooth at every tick, shaking the floor. Guardians of black iron stand "
        "between its teeth, moving with it, and turn as one to face you.",
        {"n": "inventors_workshop", "w": "orrery_steps"},
        spawns=[("escapement_guardian", 2)], level=(43, 43)),
    "orrery_steps": R(
        "The Orrery Steps", AREA,
        "Steps of polished brass lead down into a vast round chamber, and the humming grows into a "
        "roar of gears. Below, planets of brass and crystal swing on great arms around a sun of glowing "
        "gold. A guardian stands at the head of the stair.",
        {"n": "hedge_of_springs", "e": "escapement_hall", "s": "great_orrery"},
        spawns=[("escapement_guardian", 1), ("unfinished_automaton", 1)], level=(43, 43)),
    "great_orrery": R(
        "The Great Orrery", AREA,
        "At the heart of the orchard turns the great orrery, every planet and moon of the heavens in "
        "brass and crystal, sweeping around you on arms longer than ships' masts. In the golden sun at "
        "its centre sits a tiny old gnome, wired into the gears, a key turning slowly in his back. 'Is "
        "it the court?' he asks. 'Tell them I'm not finished yet.'",
        {"n": "orrery_steps"},
        spawns=[("orrin_gearwhistle", 1)], level=(44, 44)),
}
