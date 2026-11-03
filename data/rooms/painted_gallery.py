"""The Painted Gallery, north of the Ruins of Elandor's Hall of the Moon Court (36-42). As Elandor fell,
its court painter Ithilmir sealed pieces of the world into his canvases to save them, and then sealed
himself into an unfinished self-portrait. The gallery itself is three rooms; each painting is a world
of its own, entered with ENTER <painting> (hidden exits) and drawn on the map as its own inset. The
self-portrait opens only to someone carrying the painter's palette, the curator's reward for bringing
her living pigment. In the paintings, only elementals, guards, the dead and the painter's sketches
attack on sight; the painted people go about their painted lives."""
from data.rooms.common import R

GALLERY = "The Painted Gallery"
WRECK = "The Wreck at Saltmere"
WINTER = "The Winter Hunt"
STILL_LIFE = "Still Life with Rot"
SALON = "The Salon of Sitters"
CITY = "Elandor Before the Fall"
PORTRAIT = "The Unfinished Self-Portrait"


def painting(word, extra, title, prompt_verb="step into"):
    """A hidden exit into a painting: ENTER <word> (or any of `extra`)."""
    return {"words": [word] + extra,
            "prompt": "Type ENTER {} to {} {}.".format(word.upper(), prompt_verb, title),
            "hint": "You can't walk into a painting. (Type ENTER {}.)".format(word.upper()),
            "msg": "You step up to {} and lean close. The smell of oil paint and varnish fills your head, the "
                   "frame swings wide around you, and you are inside it.".format(title)}


ROOMS = {
    # ------------------------------------------------- the gallery (on the surface)
    "gallery_entrance": R(
        "The Gallery Entrance", GALLERY,
        "Beyond a door of silvered wood at the back of the Moon Court, a hall of white marble has "
        "survived the fall of Elandor untouched, its air still and smelling of linseed oil. Two great "
        "paintings face each other across it: a storm at sea, and a hunt across a winter field. Both "
        "move, very slightly, when you are not looking straight at them.",
        {"s": "moon_court", "n": "gallery_long_hall", "e": "wreck_shore", "w": "winter_edge"},
        npcs=["sylwen_curator"], safe=True,
        hidden={"e": painting("seascape", ["sea", "storm", "wreck"], "The Wreck at Saltmere"),
                "w": painting("winter", ["hunt", "winter hunt"], "The Winter Hunt")}),
    "gallery_long_hall": R(
        "The Long Gallery", GALLERY,
        "A long hall hung with paintings in frames of gilt and silver, lit by tall windows of moonstone. "
        "Three canvases are larger than the rest: a still life of fruit and a skull, a salon of elegant "
        "sitters, and, high on the end wall, Elandor itself, whole and golden. Gilded frame-wardens "
        "stand between them, and the empty frames on their chests turn towards you.",
        {"s": "gallery_entrance", "n": "painters_studio", "e": "tabletop_edge", "w": "salon_door",
         "u": "painted_gate"},
        spawns=[("frame_warden", 2)], level=(38, 38),
        hidden={"e": painting("still life", ["still", "life", "fruit"], "Still Life with Rot"),
                "w": painting("salon", ["sitters"], "The Salon of Sitters"),
                "u": painting("city", ["elandor", "golden city"], "Elandor Before the Fall", "climb up into")}),
    "painters_studio": R(
        "The Painter's Studio", GALLERY,
        "A round studio under a dome of clear crystal, cluttered with easels, jars of brushes and "
        "pots of pigment long dried. On the largest easel stands an unfinished self-portrait of an elf "
        "with a brush in his hand: the face is only charcoal lines, and the eyes follow you. A frame-"
        "warden guards it, and the canvas will not let you near unless you carry the painter's palette.",
        {"s": "gallery_long_hall", "w": "sketch_lines"},
        spawns=[("frame_warden", 1)], level=(39, 39),
        hidden={"w": painting("self-portrait", ["portrait", "self portrait", "selfportrait"],
                              "the unfinished self-portrait")}),

    # ------------------------------------------------- The Wreck at Saltmere (36-37)
    "wreck_shore": R(
        "The Shore of Wet Oils", WRECK,
        "You stand on a beach of thick, glistening paint under a storm that never breaks. The waves "
        "are brushstrokes of green and white, frozen at their crest and then, suddenly, crashing. "
        "Behind you hangs the inside of the frame, an archway of gilt back into the gallery to the "
        "west. A wrecked ship lies broken on the rocks to the north.",
        {"w": "gallery_entrance", "n": "the_wreck"},
        spawns=[("painted_sailor", 2)], level=(36, 36)),
    "the_wreck": R(
        "The Wreck", WRECK,
        "The deck of a great ship tilts beneath you, its masts snapped and its sails in painted rags. "
        "Sailors cling to the rigging, mouths open in a shout that never ends. Painted waves break over "
        "the rail, and some of them have faces.",
        {"s": "wreck_shore", "e": "flooded_hold", "n": "painted_lighthouse"},
        spawns=[("painted_sailor", 1), ("painted_breaker", 1)], level=(36, 37)),
    "flooded_hold": R(
        "The Flooded Hold", WRECK,
        "Below decks, dark paint has pooled waist-deep, thick and cold as the sea. Barrels and crates "
        "float in it, and the dim shapes of drowned men drift between them, brushed in shades of grey.",
        {"w": "the_wreck"},
        spawns=[("painted_breaker", 2)], level=(37, 37)),
    "painted_lighthouse": R(
        "The Lighthouse on the Rocks", WRECK,
        "A lighthouse stands on a crag above the wreck, its lamp a single bright dab of yellow that "
        "never reaches the ship. Coiled around its tower, scales of blue-green paint glistening, a sea "
        "serpent raises its head and looks at you with eyes the painter took a great deal of care over.",
        {"s": "the_wreck"},
        spawns=[("saltmere_serpent", 1)], level=(37, 37)),

    # ------------------------------------------------- The Winter Hunt (37-38)
    "winter_edge": R(
        "The Snowbound Edge", WINTER,
        "Snow of thick white impasto crunches underfoot, and the sky is a pale wash of grey. Bare black "
        "trees are drawn with a single stroke each. Behind you, to the east, the frame stands open on "
        "the warm gallery. Far off, a horn sounds, and keeps sounding.",
        {"e": "gallery_entrance", "n": "hunters_ride"},
        spawns=[("painted_hound", 2)], level=(37, 37)),
    "hunters_ride": R(
        "The Hunters' Ride", WINTER,
        "Riders in scarlet and fur gallop across the snowfield beside you, their horses' hooves never "
        "quite touching the ground, their hounds strung out ahead in full cry. They have been riding "
        "for a thousand years, and they have not noticed.",
        {"s": "winter_edge", "n": "frozen_mere"},
        spawns=[("painted_huntsman", 2), ("painted_hound", 1)], level=(37, 38)),
    "frozen_mere": R(
        "The Frozen Mere", WINTER,
        "A lake of blue-white ice spreads out under the trees, so smooth it reflects the painted sky. "
        "Shapes of cold light skim across it, leaving trails of frost. On the far shore, a white shape "
        "stands among the trees, watching.",
        {"s": "hunters_ride", "e": "stags_clearing"},
        spawns=[("frost_glaze", 2)], level=(38, 38)),
    "stags_clearing": R(
        "The Stag's Clearing", WINTER,
        "In a clearing ringed with black trees stands the quarry of the hunt: a white stag as big as a "
        "horse, its antlers branching like winter trees, its breath smoking. It has outrun every hunter "
        "for a thousand years, and it does not mean to be caught now.",
        {"w": "frozen_mere"},
        spawns=[("white_stag", 1)], level=(38, 38)),

    # ------------------------------------------------- Still Life with Rot (38-39)
    "tabletop_edge": R(
        "The Edge of the Table", STILL_LIFE,
        "You stand on a tablecloth of white linen at the size of a beetle, at the edge of a table that "
        "drops away into painted dark. Behind you, to the west, the frame opens on the gallery. Ahead, "
        "the painted fruit rises like hills, and the sweet stench of rot is everywhere.",
        {"w": "gallery_long_hall", "n": "bottle_tower"},
        spawns=[("fly_swarm", 2)], level=(38, 38)),
    "bottle_tower": R(
        "The Wine-Bottle Tower", STILL_LIFE,
        "A green glass bottle rises like a tower, light glowing through it, beside a candle whose flame "
        "is a living thing. The fruit around it has gone soft and black, and some of it has begun to "
        "move. At the far end of the table, a skull grins at you.",
        {"s": "tabletop_edge", "e": "rotting_fruit", "n": "the_skull"},
        spawns=[("candle_flame", 1), ("rotfruit_horror", 1)], level=(38, 39)),
    "rotting_fruit": R(
        "The Rotting Fruit", STILL_LIFE,
        "Pears and grapes the size of houses slump into each other, oozing and furred with mould. Flies "
        "as big as hawks drone over them, and things made of fruit and rot heave themselves up out of "
        "the heap.",
        {"w": "bottle_tower"},
        spawns=[("rotfruit_horror", 2), ("fly_swarm", 1)], level=(39, 39)),
    "the_skull": R(
        "The Skull", STILL_LIFE,
        "At the end of the table rests a human skull, yellow with age and as big as a cottage, the "
        "painter's reminder that all things die. Its jaw moves. Its sockets light. It has been the only "
        "thing in this painting that knew what it was, and it is very tired of lying still.",
        {"s": "bottle_tower"},
        spawns=[("memento_skull", 1)], level=(39, 39)),

    # ------------------------------------------------- The Salon of Sitters (39-40)
    "salon_door": R(
        "The Salon Door", SALON,
        "A painted hallway of gilt and rose leads to a pair of tall doors, and behind you, to the east, "
        "the frame opens back on the gallery. Footmen in gilded livery stand at the doors, faces "
        "painted on with perfect, empty smiles. Music and laughter drift out.",
        {"e": "gallery_long_hall", "n": "ballroom"},
        spawns=[("gilt_footman", 1), ("portrait_sitter", 1)], level=(39, 39)),
    "ballroom": R(
        "The Ballroom", SALON,
        "A ballroom of mirrors and chandeliers, where the subjects of a hundred portraits dance and "
        "gossip, each one stepped out of a frame on the walls and each one exactly as beautiful as the "
        "painter was paid to make them. A pair of duellists fence in a corner, for the hundredth time.",
        {"s": "salon_door", "n": "hosts_portrait"},
        spawns=[("portrait_sitter", 2), ("painted_duellist", 1)], level=(39, 40)),
    "hosts_portrait": R(
        "The Host's Portrait", SALON,
        "At the head of the ballroom hangs the largest portrait of all, and its frame is empty. Its "
        "subject stands before it: a countess in silver and pearl, fanning herself. She has decided that "
        "you would look very fine in a frame, and she has a great many empty frames.",
        {"s": "ballroom"},
        spawns=[("countess_isaura", 1), ("gilt_footman", 1)], level=(40, 40)),

    # ------------------------------------------------- Elandor Before the Fall (40-41)
    "painted_gate": R(
        "The Painted Gate", CITY,
        "You climb through the frame onto the road before the gates of Elandor, and the city is whole: "
        "white towers, silver roofs, banners, gardens. The air is golden with a sunset that never ends. "
        "Below you, the frame opens down into the gallery.",
        {"d": "gallery_long_hall", "n": "golden_market"},
        spawns=[("painted_citizen", 2)], level=(40, 40)),
    "golden_market": R(
        "The Golden Market", CITY,
        "A market square full of elves in bright silks, buying and selling and laughing. They stop when "
        "they see you, and for a moment every face turns, and every one of them is afraid. Then they go "
        "back to their painted lives. Moonguards in silver patrol between the stalls.",
        {"s": "painted_gate", "e": "whole_moon_court", "n": "living_palace"},
        spawns=[("painted_citizen", 1), ("painted_moonguard", 1)], level=(40, 41)),
    "whole_moon_court": R(
        "The Moon Court, Whole", CITY,
        "The Hall of the Moon Court as it was: roofed in silver, its crescent thrones filled with elven "
        "lords in judgement. You know the place; you walked its ruins to get here. The lords fall silent "
        "and look at you as if they know exactly where you came from.",
        {"w": "golden_market"},
        spawns=[("painted_moonguard", 2)], level=(41, 41)),
    "living_palace": R(
        "The Living Palace", CITY,
        "The palace of Elandor, all white stone and moonlight, its throne room hung with banners of "
        "silver stars. On the throne sits the painted king, crowned and young and proud, and he alone "
        "seems to understand that his city fell a thousand years ago. He does not mean to let you leave "
        "and tell anyone.",
        {"s": "golden_market"},
        spawns=[("painted_king", 1), ("painted_moonguard", 1)], level=(41, 41)),

    # ------------------------------------------------- The Unfinished Self-Portrait (42)
    "sketch_lines": R(
        "The Charcoal Lines", PORTRAIT,
        "Inside the self-portrait, the world is not finished. Charcoal lines sketch a studio, a window, "
        "an easel, and stop in mid-air. Half-drawn figures stir in the margins, smudged and faceless. "
        "Behind you, to the east, the frame opens on the studio.",
        {"e": "painters_studio", "n": "blank_canvas"},
        spawns=[("charcoal_sketch", 2)], level=(41, 42),
        gate={"item": "painters_palette",
              "msg": "The canvas is as hard as stone under your hand. It will only open to someone who carries "
                     "the painter's own palette."}),
    "blank_canvas": R(
        "The Blank Canvas", PORTRAIT,
        "Beyond the lines lies nothing but white: a blank canvas stretching in every direction. In the "
        "middle of it stands an elf in a paint-stained smock, a brush in his hand and no face at all, "
        "only smooth pale skin where his face should be. 'At last,' he says, without a mouth. 'Hold "
        "still. This will only take a moment.'",
        {"s": "sketch_lines"},
        spawns=[("ithilmir", 1), ("charcoal_sketch", 1)], level=(42, 42)),
}
