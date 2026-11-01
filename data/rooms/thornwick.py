"""Thornwick Hall, seat of the Vane family, west of the Stag Walk (40-50). Every soul in the house
can be fought, and Lord Aldric Vane waits at the top of it. The grounds and ground floor are one
area; the upper floor is its own area so the map can tell the floors apart."""
from data.rooms.common import R

HALL = "Thornwick Hall"
UPPER = "Thornwick Hall, Upper Floor"

ROOMS = {
    # ------------------------------------------------- the deer park and grounds (40-43)
    "vane_chase": R(
        "The Vane Chase", HALL,
        "West of the Stag Walk, the wild forest ends at a ditch and a fence of sharpened oak, and the "
        "trees beyond have been thinned for riding. Bones of white stags lie bleaching in the ditch. "
        "A carved board on the fence reads: THE CHASE OF THE HOUSE OF VANE. TRESPASSERS WILL BE HUNTED.",
        {"e": "stag_walk", "w": "deer_park"},
        spawns=[("vane_huntsman", 1), ("vane_boarhound", 2)], level=(40, 41)),
    "deer_park": R(
        "The Deer Park", HALL,
        "Rolling parkland dotted with great oaks, where the grass is cropped short by deer kept for the "
        "Vanes' table and their sport. Huntsmen in green and silver ride the rides with spears across "
        "their saddles. West, beyond a stone wall, the roofs of a great house rise above the trees.",
        {"e": "vane_chase", "n": "hunting_lodge", "s": "poachers_camp", "w": "vane_gatehouse"},
        spawns=[("vane_huntsman", 2), ("vane_boarhound", 1)], level=(40, 41)),
    "hunting_lodge": R(
        "The Hunting Lodge", HALL,
        "A long timber lodge hung with antlers, boar tusks and the stiff hides of wolves. Hounds sprawl "
        "by a fire big enough to roast an ox, and a broad man in a leather apron is skinning a stag on "
        "a trestle, whistling through his teeth.",
        {"s": "deer_park"},
        spawns=[("hobb_gamekeeper", 1), ("vane_boarhound", 2)], level=(42, 42)),
    "poachers_camp": R(
        "The Poacher's Camp", HALL,
        "A hollow under the roots of a fallen oak, hidden from the rides by bracken and brambles. A "
        "small, smokeless fire burns in a ring of stones, and snares, sacks and a set of very fine "
        "silver spoons lie about it. Nobody from the house comes here, and nobody here asks questions.",
        {"n": "deer_park"},
        npcs=["nell_rook"], safe=True),
    "vane_gatehouse": R(
        "The Gatehouse", HALL,
        "A square gatehouse of grey stone straddles the drive, its gates standing open and a portcullis "
        "raised above them. The arms of the Vanes, a silver stag on a field of green, are carved over "
        "the arch. The wardens on the gate look at every stranger as though measuring them for a grave.",
        {"e": "deer_park", "w": "long_drive"},
        spawns=[("gate_warden", 2)], level=(41, 41)),
    "long_drive": R(
        "The Long Drive", HALL,
        "An avenue of ancient lime trees runs west toward the house, its gravel raked smooth every "
        "morning. Gardeners clip the verges on their knees. To the north lie formal gardens, and to the "
        "south, the smell of horses drifts from the stable yard.",
        {"e": "vane_gatehouse", "w": "forecourt", "n": "topiary_garden", "s": "vane_stables"},
        spawns=[("under_gardener", 2), ("gate_warden", 1)], level=(41, 42)),
    "topiary_garden": R(
        "The Topiary Garden", HALL,
        "Yew and box have been clipped into the shapes of stags, hounds and knights on horseback, and "
        "gravel paths run between them in perfect squares. A groundskeeper with shears as long as a "
        "sword is trimming a hedge-knight's lance. North, a gap in a tall green wall leads into a maze.",
        {"s": "long_drive", "n": "hedge_maze"},
        spawns=[("vane_groundskeeper", 1), ("under_gardener", 2)], level=(41, 42)),
    "hedge_maze": R(
        "The Hedge Maze", HALL,
        "Walls of yew twice the height of a man close in on every side, and every turn looks like the "
        "last. Somewhere ahead, a hound is baying, and someone is laughing. At the centre, a fountain "
        "of a stag and hunter plays into a pool full of fat golden fish.",
        {"s": "topiary_garden"},
        spawns=[("vane_groundskeeper", 1), ("vane_boarhound", 2)], level=(42, 43)),
    "vane_stables": R(
        "The Stable Yard", HALL,
        "A cobbled yard ringed by stables, with a clock tower over the arch and a pump in the middle. "
        "Fine horses look out over their half-doors. Grooms in green livery muck out and polish tack, "
        "while a big man with a whip shouts at all of them.",
        {"n": "long_drive"},
        spawns=[("vane_groom", 2), ("vane_stablemaster", 1)], level=(42, 43)),
    "forecourt": R(
        "The Forecourt", HALL,
        "The drive ends in a great forecourt before the house. Thornwick Hall is three storeys of "
        "honey-coloured stone, its hundred windows glittering, with a flight of steps up to doors of "
        "carved oak. Carriages stand waiting, and liveried footmen hurry up and down the steps.",
        {"e": "long_drive", "w": "entrance_hall", "s": "vane_chapel"},
        spawns=[("vane_footman", 2), ("gate_warden", 1)], level=(42, 43)),
    "vane_chapel": R(
        "The Family Chapel", HALL,
        "A small chapel of pale stone stands beside the house, its windows of coloured glass showing "
        "the Vanes kneeling before the Dawnfather. The family's tombs line the walls, each lord in "
        "marble with a stag at his feet. The house chaplain is polishing the altar silver.",
        {"n": "forecourt"},
        spawns=[("house_chaplain", 1)], level=(43, 43)),

    # ------------------------------------------------- the ground floor (44-46)
    "entrance_hall": R(
        "The Entrance Hall", HALL,
        "A soaring hall of chequered marble, lit by a lantern of gilded glass hanging on a chain from "
        "the ceiling far above. Knights of the household stand by the doors in green-enamelled plate. "
        "Corridors lead off in every direction, and the din of a feast rolls in from the west.",
        {"e": "forecourt", "w": "great_hall", "n": "portrait_gallery", "s": "servants_passage"},
        spawns=[("household_knight", 1), ("vane_footman", 1)], level=(44, 45)),
    "portrait_gallery": R(
        "The Portrait Gallery", HALL,
        "Generations of Vanes glare down from gilded frames along a long, quiet gallery: lords in "
        "armour, ladies in pearls, children with hounds. The painted eyes are all the same cold grey. "
        "At the far end, a grand staircase rises to the floor above.",
        {"s": "entrance_hall", "w": "grand_staircase"},
        spawns=[("household_knight", 1), ("noble_guest", 1)], level=(44, 45)),
    "great_hall": R(
        "The Great Hall", HALL,
        "A hall with a hammer-beam roof and a hearth as wide as a cottage, where a feast is in full "
        "flow. Long tables groan under roast swans, boars' heads and towers of sugared fruit. Noble "
        "guests in silk and velvet drink, quarrel and laugh far too loudly.",
        {"e": "entrance_hall", "w": "minstrels_gallery", "n": "grand_staircase"},
        spawns=[("noble_guest", 3), ("visiting_knight", 1)], level=(44, 46)),
    "minstrels_gallery": R(
        "The Minstrels' Gallery", HALL,
        "A carved wooden gallery at the end of the great hall, where the household musicians play for "
        "the feast below. Lutes, viols and a set of silver trumpets hang on the walls. The minstrels "
        "play on, though their eyes follow you.",
        {"e": "great_hall", "n": "stewards_office"},
        spawns=[("household_minstrel", 2)], level=(45, 46)),
    "stewards_office": R(
        "The Steward's Office", HALL,
        "A panelled room full of ledgers, tally sticks and iron-bound chests, smelling of ink and "
        "candle wax. Clerks scratch away at the rents of every farm in the valley, and a thin man with "
        "a ring of keys at his belt watches over them all.",
        {"s": "minstrels_gallery", "e": "grand_staircase"},
        spawns=[("vane_steward", 1), ("estate_clerk", 2)], level=(45, 46)),
    "grand_staircase": R(
        "The Grand Staircase", HALL,
        "A staircase of white marble sweeps up in two great curves to the family's rooms on the floor "
        "above, its banisters carved with leaping stags. A knight of the household stands at its foot, "
        "and no servant climbs it without being sent for.",
        {"s": "great_hall", "w": "stewards_office", "e": "portrait_gallery", "u": "upper_landing"},
        spawns=[("household_knight", 1)], level=(45, 46)),

    # ------------------------------------------------- the servants' wing (42-44)
    "servants_passage": R(
        "The Servants' Passage", HALL,
        "Behind a door covered in green baize, the marble ends and the bare stone begins. A narrow, "
        "busy passage runs between the kitchens and the rest of the house, full of footmen carrying "
        "trays and maids carrying coal. Bells on springs jangle above the doors.",
        {"n": "entrance_hall", "w": "vane_kitchens", "s": "butlers_pantry"},
        spawns=[("vane_footman", 1), ("vane_housemaid", 2)], level=(42, 43)),
    "vane_kitchens": R(
        "The Kitchens", HALL,
        "A vaulted kitchen roaring with heat, where whole oxen turn on spits and copper pots bubble on "
        "three great ranges. Kitchen hands run in every direction. In the middle of it all stands the "
        "cook, a vast woman with a cleaver in one hand and a ladle in the other, bellowing orders.",
        {"e": "servants_passage", "s": "scullery", "w": "wine_store"},
        spawns=[("mistress_hollin", 1), ("kitchen_hand", 2)], level=(43, 44)),
    "scullery": R(
        "The Scullery and Laundry", HALL,
        "Steam rolls from the coppers where the household's linen is boiled, and the sinks are piled "
        "with greasy pans from the feast. Laundresses with arms red to the elbow wring out sheets, and "
        "scullery maids scrub away by the light of a single high window.",
        {"n": "vane_kitchens", "w": "servants_hall"},
        spawns=[("vane_laundress", 2), ("vane_housemaid", 1)], level=(42, 43)),
    "wine_store": R(
        "The Buttery and Wine Store", HALL,
        "Rows of barrels and racks of dusty bottles fill a cool stone room behind the kitchens. Hams "
        "and cheeses hang from the beams. The cellarer, red-nosed and suspicious, is tapping a fresh "
        "cask and tasting it rather often.",
        {"e": "vane_kitchens", "s": "servants_hall"},
        spawns=[("vane_cellarer", 1), ("vane_footman", 1)], level=(43, 44)),
    "servants_hall": R(
        "The Servants' Hall", HALL,
        "A long, plain room with a scrubbed table where the servants eat in shifts, ranked by "
        "position from the head of the table to the foot. Bread, beer and cold meat are laid out. A "
        "board on the wall lists every servant's duties in a stern copperplate hand.",
        {"e": "scullery", "n": "wine_store"},
        spawns=[("vane_footman", 1), ("vane_housemaid", 1), ("vane_groom", 1)], level=(42, 43)),
    "butlers_pantry": R(
        "The Butler's Pantry", HALL,
        "A locked room of glass-fronted cupboards full of the family's silver: plates, ewers, salvers "
        "and candlesticks, all polished to a mirror shine. A tall, grave man in black is counting the "
        "spoons, and he looks up at you as though you are a stain on the tablecloth.",
        {"n": "servants_passage"},
        spawns=[("mr_graves", 1)], level=(44, 44)),

    # ------------------------------------------------- the upper floor (46-50)
    "upper_landing": R(
        "The Upper Landing", UPPER,
        "The grand staircase ends at a wide landing hung with tapestries of the hunt. The noise of the "
        "feast is muffled up here, and the carpets are so thick that footsteps make no sound. Doors "
        "lead west to the ladies' rooms, and a long gallery runs north.",
        {"d": "grand_staircase", "w": "ladies_solar", "n": "long_gallery"},
        spawns=[("household_knight", 1), ("lady_in_waiting", 1)], level=(46, 46)),
    "ladies_solar": R(
        "The Ladies' Solar", UPPER,
        "A bright room with tall windows, full of embroidery frames, lap dogs and gossip. The ladies-in-"
        "waiting sit in a ring of chairs, their needles flashing, their eyes flicking up at you and "
        "away. One of them has a dagger in her sewing basket, and she is not the only one.",
        {"e": "upper_landing", "w": "seraphine_chamber"},
        spawns=[("lady_in_waiting", 3)], level=(46, 47)),
    "seraphine_chamber": R(
        "Lady Seraphine's Bedchamber", UPPER,
        "A chamber of rose-coloured silk, with a great curtained bed and a dressing table crowded with "
        "scent bottles and jewel cases. Lady Seraphine, the young wife of the lord, sits before the "
        "mirror with a long golden pin in her hair. She smiles at your reflection.",
        {"e": "ladies_solar"},
        spawns=[("lady_seraphine", 1), ("lady_in_waiting", 1)], level=(47, 47)),
    "long_gallery": R(
        "The Long Gallery", UPPER,
        "A gallery running the length of the house, panelled in oak and lit by a row of windows over "
        "the gardens. Card tables and decanters stand along it. Sir Corwin Vane, the lord's cousin, is "
        "duelling a suit of armour with a rapier, very drunk and very good.",
        {"s": "upper_landing", "w": "vane_library", "n": "lords_antechamber"},
        spawns=[("sir_corwin", 1), ("noble_guest", 1)], level=(47, 47)),
    "vane_library": R(
        "The Library", UPPER,
        "Shelves climb to the ceiling, reached by ladders on brass rails, and a globe of the world "
        "stands in the window. Books lie open on every table. A pale young man is hunched over a heavy "
        "black book that he plainly should not have, muttering the words under his breath.",
        {"e": "long_gallery", "w": "dowager_chambers"},
        spawns=[("master_tobias", 1)], level=(47, 47)),
    "dowager_chambers": R(
        "The Dowager's Chambers", UPPER,
        "A cold, dark room of black oak and grey velvet, where the clocks tick very loudly. The Dowager "
        "Lady Isolde, the lord's mother, sits straight-backed in a high chair with an ebony cane across "
        "her knees, her attendants silent at her side. She has ruled this house for forty years.",
        {"e": "vane_library", "w": "mathilde_rooms"},
        spawns=[("dowager_isolde", 1), ("dowager_attendant", 2)], level=(47, 48)),
    "mathilde_rooms": R(
        "Great-aunt Mathilde's Rooms", UPPER,
        "A stuffy little room crammed with knick-knacks, cushions, sleeping cats and a century of "
        "letters tied in ribbon. A tiny old lady in an enormous lace cap dozes by the fire, wearing "
        "more jewels than the rest of the family put together.",
        {"e": "dowager_chambers"},
        spawns=[("great_aunt_mathilde", 1)], level=(46, 46)),
    "lords_antechamber": R(
        "The Lord's Antechamber", UPPER,
        "A guardroom before the lord's own rooms, its walls hung with swords, shields and the banners "
        "of old wars. The lord's sworn swords stand guard in full plate, their visors down. Beyond a "
        "pair of doors carved with a silver stag, someone is pacing.",
        {"s": "long_gallery", "w": "lords_chambers"},
        spawns=[("vane_sworn_sword", 2)], level=(48, 49)),
    "lords_chambers": R(
        "The Lord's Chambers", UPPER,
        "The great chamber of the Lord of Thornwick, its walls hung with green and silver and its "
        "windows looking out over all his lands. A war-axe and a hunting horn hang above the hearth. "
        "Lord Aldric Vane turns from the window in his family's ancient armour and draws his sword. "
        "'Whoever sent you,' he says, 'they did not pay you enough.'",
        {"e": "lords_antechamber"},
        spawns=[("lord_aldric_vane", 1), ("vane_sworn_sword", 1)], level=(50, 50)),
}
