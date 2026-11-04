"""The Sugarwold, north of the Salt Pans of the Scorchsands (44-49). A country of sweets that the witch
Madame Marchpane baked at the edge of the salt, where travellers dying of thirst find a pan of crystals
that taste of sugar. Everything in it is good to eat, and those who eat too much of it become part of
it: the gingerbread folk of her village were heroes and wanderers once. Its eastern dunes run down into
the Scorchsands' Valley of the Kings, and a coal road behind the witch's cottage climbs west to the
Forge of the Dragon Cult in the Ashen Peaks, which keeps her ovens burning. Only her gingerbread
soldiers, the imps of her ovens and the witch herself attack on sight."""
from data.rooms.common import R

AREA = "The Sugarwold"

ROOMS = {
    # ------------------------------------------------- the way in (safe)
    "sugar_pan": R(
        "The Sugar Pan", AREA,
        "At the northern edge of the salt, the last pan is filled not with brine but with crystals of "
        "pink and white sugar, and the air turns cool and sweet. Someone has made a little camp of "
        "shortbread crates beside it. To the north, the white crust gives way to a land of sweets.",
        {"s": "salt_pans", "n": "sugar_gate"},
        npcs=["edric_hale"], safe=True),

    # ------------------------------------------------- the gumdrop meadows (44-45)
    "sugar_gate": R(
        "The Spun-Sugar Gate", AREA,
        "Beyond the sugar pan, the sky turns the colour of strawberry cream above a gate of spun sugar "
        "that glitters like frost. After the salt, the air is so sweet it makes your teeth ache. Something "
        "round and glistening wobbles across the path, leaving a sticky trail.",
        {"s": "sugar_pan", "n": "gumdrop_meadow"},
        spawns=[("gumdrop_ooze", 2)], level=(44, 44)),
    "gumdrop_meadow": R(
        "The Gumdrop Meadow", AREA,
        "Hills of green sugar grass are studded with gumdrops as big as boulders, some of which roll "
        "slowly about on their own. Striped hogs root among them, grunting happily. The meadow is "
        "lovely, and very quiet, with no birdsong at all.",
        {"s": "sugar_gate", "w": "lollipop_grove", "e": "peppermint_fields", "n": "chocolate_ford"},
        spawns=[("gumdrop_ooze", 1), ("peppermint_hog", 2)], level=(44, 45)),
    "lollipop_grove": R(
        "The Lollipop Grove", AREA,
        "Lollipops grow here like trees, their great swirled discs taller than a house and their sticks "
        "rooted in the sugar grass. Tiny winged figures flit between them, giggling. The swirls turn "
        "slowly when you are not looking straight at them.",
        {"e": "gumdrop_meadow", "n": "licorice_thicket"},
        spawns=[("sugar_sprite", 2)], level=(45, 45)),
    "peppermint_fields": R(
        "The Peppermint Fields", AREA,
        "Rows of red and white peppermint plants stand in neat furrows, each leaf a striped boiled "
        "sweet. The cold, sharp smell of mint stings your eyes. Nobody tends the rows, yet every one "
        "of them is perfectly weeded. East, the furrows give way to dunes of brown sugar.",
        {"w": "gumdrop_meadow", "e": "brown_sugar_dunes"},
        spawns=[("peppermint_hog", 2), ("sugar_sprite", 1)], level=(45, 45)),

    # ------------------------------------------------- the eastern dunes, down to the Valley of the Kings (46-47)
    "brown_sugar_dunes": R(
        "The Brown-Sugar Dunes", AREA,
        "Dunes of soft brown sugar roll eastward, crusted on top where the sun has melted and hardened "
        "them. Your boots sink to the ankle, and the sand that blows in from the desert sticks to "
        "everything. A raven glazed in sugar picks at something half-buried in a dune.",
        {"w": "peppermint_fields", "e": "toffee_tarpits"},
        spawns=[("candied_raven", 1), ("toffee_lurker", 1)], level=(46, 46)),
    "toffee_tarpits": R(
        "The Toffee Tarpits", AREA,
        "Pools of hot golden toffee bubble and pop between crusts of burnt sugar, kept molten by the "
        "desert sun. Bones lie glazed and shining at the edges of the pools, licked clean. Now and then "
        "a shape rises out of the toffee, looks around and sinks again.",
        {"w": "brown_sugar_dunes", "e": "sugar_line"},
        spawns=[("toffee_lurker", 2)], level=(46, 47)),
    "sugar_line": R(
        "The Sugar Line", AREA,
        "Here the sugar ends and the desert begins, in a line as sharp as a blade drawn across the dunes. "
        "On one side lies sand, on the other brown sugar, and licorice serpents bask along the border. "
        "South, sandstone cliffs carved with tomb doors fall away into the Valley of the Kings.",
        {"w": "toffee_tarpits", "s": "valley_of_kings"},
        spawns=[("licorice_serpent", 2)], level=(46, 47)),

    # ------------------------------------------------- the chocolate river (46-47)
    "licorice_thicket": R(
        "The Licorice Thicket", AREA,
        "Black licorice grows in coils and twisted ropes here, dense as a bramble and taller than "
        "your head. The tangle rustles, and you see that some of the coils are moving. A gap in the "
        "thicket leads east towards the sound of slow, heavy water.",
        {"s": "lollipop_grove", "e": "chocolate_ford"},
        spawns=[("licorice_serpent", 2)], level=(46, 46)),
    "chocolate_ford": R(
        "The Chocolate Ford", AREA,
        "A broad river of melted chocolate oozes past, too thick to flow, too warm to be safe. Stepping "
        "stones of brittle toffee cross it. Things lie half-sunk in the chocolate along the banks, and "
        "some of them wear armour.",
        {"s": "gumdrop_meadow", "w": "licorice_thicket", "n": "candied_orchard"},
        spawns=[("licorice_serpent", 1), ("toffee_lurker", 1)], level=(46, 46)),
    "candied_orchard": R(
        "The Candied Orchard", AREA,
        "Trees of barley sugar hang heavy with toffee apples and candied pears that tinkle like glass "
        "in the breeze. Sugar-glazed ravens watch from the boughs. Beneath one tree stands a figure of "
        "gingerbread, holding an apple to its icing mouth and never taking a bite.",
        {"s": "chocolate_ford", "n": "gingerbread_row"},
        spawns=[("candied_raven", 2), ("gingerbread_man", 1)], level=(47, 47)),

    # ------------------------------------------------- the gingerbread village (47-48)
    "gingerbread_row": R(
        "Gingerbread Row", AREA,
        "A village street of gingerbread cottages with sugar-glass windows and roofs tiled in chocolate. "
        "Gingerbread folk shuffle between the doors, smiling iced smiles. One of them wears a sword "
        "belt of licorice and a helm of gingerbread, as if it was once a warrior and has forgotten how.",
        {"s": "candied_orchard", "w": "sugarglass_chapel", "e": "peppermint_barracks", "n": "frosting_road"},
        spawns=[("gingerbread_man", 2), ("gingerbread_soldier", 1)], level=(47, 48)),
    "sugarglass_chapel": R(
        "The Sugarglass Chapel", AREA,
        "A little chapel with windows of coloured sugar-glass, its pews of shortbread and its altar a "
        "great iced cake. Gingerbread folk sit in rows, facing the altar, quite still. Scratched into "
        "the back of one pew, in a hand that shakes, are the words: IT WAS ONLY ONE TASTE.",
        {"e": "gingerbread_row"},
        spawns=[("gingerbread_man", 2)], level=(47, 47)),
    "peppermint_barracks": R(
        "The Peppermint Barracks", AREA,
        "A long hall of red and white striped candy, where racks of candy-cane bayonets line the walls. "
        "Gingerbread soldiers in sugar-frosted coats drill in perfect step on the parade ground. "
        "Their eyes are raisins, and every one of them turns to look at you.",
        {"w": "gingerbread_row"},
        spawns=[("gingerbread_soldier", 2)], level=(48, 48)),
    "frosting_road": R(
        "The Frosting Road", AREA,
        "A road of thick white frosting runs north out of the village between hedges of marzipan. A "
        "great lumbering shape of crusted sugar stands guard where the hedges end. Ahead, a chimney "
        "puffs smoke that smells of cinnamon and something burnt.",
        {"s": "gingerbread_row", "n": "witch_garden"},
        spawns=[("gingerbread_soldier", 1), ("sugarloaf_golem", 1)], level=(48, 48)),

    # ------------------------------------------------- the witch's cottage (48-49)
    "witch_garden": R(
        "The Witch's Garden", AREA,
        "A garden of sugared roses and caramel pumpkins surrounds a cottage built all of gingerbread, "
        "its walls studded with sweets and its eaves dripping icing. It is the most inviting house you "
        "have ever seen, and its door stands open to the west. The candied ravens on its roof have "
        "stopped watching you and started waiting.",
        {"s": "frosting_road", "w": "witch_kitchen"},
        spawns=[("sugarloaf_golem", 1), ("candied_raven", 1)], level=(48, 48)),
    "witch_kitchen": R(
        "The Witch's Kitchen", AREA,
        "Copper pans hang over a long table dusted with flour and sugar, beside rolling pins, cutters "
        "shaped like people, and a bowl of gumdrop buttons. Little red imps scuttle between the stoves, "
        "stoking them with coal carried in through a sooty back door. The heat comes from a great iron "
        "door to the north.",
        {"e": "witch_garden", "s": "fattening_pantry", "w": "coal_road", "n": "great_oven"},
        spawns=[("oven_imp", 2)], level=(48, 49)),
    "fattening_pantry": R(
        "The Fattening Pantry", AREA,
        "Shelves of jars and sacks of sugar line the walls, and at the back stand cages of iron bars "
        "dipped in caramel. The cages are empty, but each one holds a plate of half-eaten cake and a "
        "battered helm or a sword in its scabbard. A sugarloaf hulk stands at the door like a gaoler.",
        {"n": "witch_kitchen"},
        spawns=[("sugarloaf_golem", 1), ("oven_imp", 1)], level=(49, 49)),
    "great_oven": R(
        "The Great Oven", AREA,
        "The iron door opens on an oven as big as a chapel, its brick walls glowing red and its floor "
        "laid with trays of gingerbread figures, half-baked, some of them still moving. In the heat "
        "stands a plump old woman in a flour-white apron, smiling sweetly, holding out a gingerbread "
        "biscuit for you.",
        {"s": "witch_kitchen"},
        spawns=[("madame_marchpane", 1)], level=(49, 49)),

    # ------------------------------------------------- the coal road, up to the Forge of the Dragon Cult (47-48)
    "coal_road": R(
        "The Witch's Coal Road", AREA,
        "Behind the cottage, a track of crushed cinder toffee climbs west between heaps of black coal, "
        "rutted by the wheels of little iron carts. Imps haul the carts down from the mountains, "
        "squabbling, and the sugar grass on either side is grey with soot.",
        {"e": "witch_kitchen", "w": "cinder_steps"},
        spawns=[("oven_imp", 2)], level=(48, 48)),
    "cinder_steps": R(
        "The Cinder Steps", AREA,
        "Steps of cinder toffee climb into the flanks of the Ashen Peaks, where the sweet air of the "
        "Sugarwold turns to smoke and sulphur. Ash falls like icing sugar. To the west, the ring of "
        "hammers and a red glow come from the forge of the dragon cult, who sell the witch her fire.",
        {"e": "coal_road", "w": "cult_forge"},
        spawns=[("oven_imp", 1), ("sugarloaf_golem", 1)], level=(47, 48)),
}
