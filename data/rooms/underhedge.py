"""The Underhedge, through a mousehole in Greenmeadow's Willow Mill (5-10). A fairy ring under the floor
shrinks anyone who steps into it to the size of a mouse, and the hedgerow behind the mill becomes a
country: a meadow of dewdrops, a roaring millrace, an ant road, a beetle cavalry, the mole kings'
tunnels and the garden wall where the gardener's cat prowls. A windfall apple rotting in the grass has
become the Wasp Keep. Only the soldier ants, the mole guards and the wasps attack on sight. The
entrance is a hidden exit, taken with ENTER MOUSEHOLE."""
from data.rooms.common import R

AREA = "The Underhedge"

ROOMS = {
    # ------------------------------------------------- the way in (safe)
    "fairy_ring": R(
        "The Fairy Ring", AREA,
        "You stand in a ring of toadstools as tall as towers, beneath floorboards that stretch away "
        "like a wooden sky. The mousehole you squeezed through is a vast arch far above, reached by a "
        "stalk of dry grass you could climb back up. A tiny woman in a flour-dusted apron has set up "
        "camp in the ring, and she waves.",
        {"u": "willow_mill", "n": "dewdrop_meadow"},
        npcs=["wenna_furrow"], safe=True),

    # ------------------------------------------------- the grass (5-7)
    "dewdrop_meadow": R(
        "The Dewdrop Meadow", AREA,
        "Blades of grass tower over you like a green forest, and dewdrops as big as boulders hang "
        "from them, each holding a tiny upside-down sun. Ants hurry along the stems in lines, "
        "carrying crumbs larger than themselves. Somewhere to the west, water roars.",
        {"s": "fairy_ring", "w": "millrace", "n": "clover_forest"},
        spawns=[("garden_ant", 3)], level=(5, 5)),
    "millrace": R(
        "The Millrace", AREA,
        "The little brook that turns the mill wheel is a thundering river at this size, white with "
        "foam where it pours over a pebble the size of a hill. Water beetles row along its edges, and "
        "something with goggling golden eyes watches from a lily pad.",
        {"e": "dewdrop_meadow", "s": "leaf_landing"},
        spawns=[("water_beetle", 2), ("pond_frog", 1)], level=(5, 6)),
    "leaf_landing": R(
        "The Leaf-Boat Landing", AREA,
        "A sandbar where fallen willow leaves lie beached like boats, some lashed together with "
        "spider thread into rafts. Somebody has been trying to build a fleet here, and given up. A "
        "frog as big as a house sits on the largest raft, throat pulsing.",
        {"n": "millrace"},
        spawns=[("pond_frog", 2)], level=(6, 6)),
    "clover_forest": R(
        "The Clover Forest", AREA,
        "Clover leaves spread overhead like green parasols, and the air is heavy with the scent of "
        "its flowers. Bees as big as oxen drone between the blossoms, paying you no mind. Paths "
        "trodden by countless small feet lead off in every direction.",
        {"s": "dewdrop_meadow", "e": "ant_road", "n": "snail_trail"},
        spawns=[("garden_ant", 2), ("water_beetle", 1)], level=(6, 7)),

    # ------------------------------------------------- the ant road and the beetle cavalry (7-8)
    "ant_road": R(
        "The Ant Road", AREA,
        "A highway of packed earth runs through the grass, worn smooth by a million marching feet. "
        "Columns of ants march along it carrying grain from the mill, and soldiers with great curved "
        "jaws stand guard at the verges, antennae twitching at your scent.",
        {"w": "clover_forest", "s": "anthill_mouth", "n": "beetle_stables"},
        spawns=[("garden_ant", 2), ("soldier_ant", 1)], level=(7, 7)),
    "anthill_mouth": R(
        "The Anthill Mouth", AREA,
        "A hill of crumbled earth rises like a mountain, its slopes riddled with tunnels. Grains of "
        "wheat from the mill, each as big as a barrel, are being rolled down into the dark. The "
        "soldiers here do not wait to see what you want.",
        {"n": "ant_road"},
        spawns=[("soldier_ant", 2), ("garden_ant", 1)], level=(7, 8)),
    "snail_trail": R(
        "The Snail Trail", AREA,
        "A silver road of dried slime winds between the stems, glittering in the light. A snail the "
        "size of a cottage grinds along it, its shell rising like a spiral tower. To the north, the "
        "air turns sweet and rotten and full of a low, angry humming.",
        {"s": "clover_forest", "e": "beetle_stables", "n": "windfall_apple"},
        spawns=[("garden_snail", 2)], level=(7, 7)),
    "beetle_stables": R(
        "The Beetle Stables", AREA,
        "Under the shelter of a dock leaf, great shining beetles stand in stalls of twig, saddled and "
        "bridled with thread. Mice in walnut-shell helms and armour of beetle shell tend them, and "
        "practise with lances made from darning needles. They watch you warily, but do not draw.",
        {"w": "snail_trail", "s": "ant_road"},
        spawns=[("mouse_knight", 2), ("stag_beetle", 1)], level=(8, 8)),

    # ------------------------------------------------- the mole kings' tunnels (8-9)
    "tunnel_hall": R(
        "The Tunnel Hall", AREA,
        "A great tunnel opens out of the earth beneath the garden wall, its roof held up by roots "
        "as thick as pillars. Pale worms coil in the walls. Moles in leather aprons dig and haul, "
        "squinting at you with tiny eyes, and a carved gate stands to the west.",
        {"n": "cats_walk", "w": "mole_gate"},
        spawns=[("mole_digger", 2)], level=(8, 8)),
    "mole_gate": R(
        "The Mole Gate", AREA,
        "Two vast doors of carved root bar the way into the mole kingdom, set with polished pebbles "
        "for jewels. Mole guards in coats of overlapping beetle shell stand before them, armed with "
        "picks, and they sniff the air and growl as you come near.",
        {"e": "tunnel_hall", "s": "mole_court"},
        spawns=[("mole_guard", 2)], level=(8, 9)),
    "mole_court": R(
        "The Mole Kings' Court", AREA,
        "A round hall dug deep beneath the hedge, lit by glow-worms in jars. Its walls are lined with "
        "treasures dug from the garden: buttons, bent pins, a lost thimble, a single silver spoon. On "
        "a throne made of a broken teacup sits a fat old mole in a crown of bottle-tin.",
        {"n": "mole_gate"},
        spawns=[("mole_king", 1), ("mole_guard", 1)], level=(9, 9)),

    # ------------------------------------------------- the garden wall and the Wasp Keep (9-10)
    "cats_walk": R(
        "The Cat's Walk", AREA,
        "The foot of the garden wall rises like a cliff of red brick, and the grass beneath it is "
        "flattened into a broad path. Tufts of grey fur as big as haystacks catch on the stems. "
        "Above you, two green eyes the size of windows open slowly, and a vast shape stretches.",
        {"e": "windfall_apple", "s": "tunnel_hall"},
        spawns=[("garden_cat", 1)], level=(9, 9)),
    "windfall_apple": R(
        "The Windfall Apple", AREA,
        "A fallen apple lies in the grass like a red hill, rotting and soft, its sweet stink so strong "
        "it makes you dizzy. Its flesh has been tunnelled and walled with grey paper. Wasps crawl in "
        "and out of the holes, and the whole apple hums.",
        {"s": "snail_trail", "w": "cats_walk", "e": "wasp_keep"},
        spawns=[("wasp_drone", 2)], level=(9, 9)),
    "wasp_keep": R(
        "The Wasp Keep", AREA,
        "Inside the apple, the wasps have built a fortress of grey paper, chamber upon chamber, its "
        "walls rustling. Wasp guards stand in the doorways with stings like spears. Hanging from the "
        "ceiling in paper cocoons are shapes that are not wasps, and some of them are moving.",
        {"w": "windfall_apple", "n": "queens_comb"},
        spawns=[("wasp_guard", 2), ("wasp_drone", 1)], level=(9, 10)),
    "queens_comb": R(
        "The Queen's Comb", AREA,
        "At the heart of the apple lies a chamber of golden comb, sticky with honey and rot. Grubs "
        "squirm in the cells. Above them hangs the queen, longer than a horse, her striped body "
        "swollen and her wings humming like a storm, and she turns her great black eyes on you.",
        {"s": "wasp_keep"},
        spawns=[("wasp_queen", 1), ("wasp_guard", 1)], level=(10, 10)),
}
