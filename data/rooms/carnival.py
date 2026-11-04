"""The Carnival That Never Closes, south of the Badlands' Howling Pit (24-30). A fairground that has
run for centuries. The midway is bright and cheerful, the attractions are strange, and behind the
tents it is always midnight. The carnival itself is the thing that is alive; the Ringmaster in the
big top was its first prisoner."""
from data.rooms.common import R

AREA = "The Carnival That Never Closes"

ROOMS = {
    # ------------------------------------------------- the midway (24-26)
    "carnival_gates": R(
        "The Carnival Gates", AREA,
        "South of the gnolls' pit, the badlands give way to trampled grass and a painted arch strung "
        "with lanterns: THE CARNIVAL THAT NEVER CLOSES. Music drifts out, and the smell of toffee and "
        "sawdust. The paint on the arch is fresh, though the lanterns look three hundred years old.",
        {"n": "howling_pit", "s": "midway"},
        spawns=[("carnival_barker", 1), ("roustabout", 1)], level=(24, 24)),
    "midway": R(
        "The Midway", AREA,
        "A wide avenue of striped tents and booths runs through the fair, packed with laughing crowds "
        "who never seem to leave. Barkers bellow from every stall. Nobody here looks older or younger "
        "than they did yesterday, and nobody can remember arriving.",
        {"n": "carnival_gates", "w": "sweet_stalls", "e": "games_of_skill", "s": "strongman_stage"},
        spawns=[("carnival_barker", 2), ("carnival_pickpocket", 1)], level=(24, 25)),
    "sweet_stalls": R(
        "The Sweet Stalls", AREA,
        "Stalls of toffee apples, spun sugar and candied nuts crowd together in a haze of sweet smoke. "
        "The sweet-sellers stir copper pans of bubbling sugar and smile very wide. The toffee apples "
        "are delicious, and you are not sure what is inside them.",
        {"e": "midway"},
        spawns=[("sweet_seller", 2), ("carnival_pickpocket", 1)], level=(24, 25)),
    "games_of_skill": R(
        "The Games of Skill", AREA,
        "Ring tosses, coconut shies, knife boards and shooting galleries line a crooked lane. The "
        "prizes on the top shelves are magnificent, and nobody has ever won one. A barker waves you "
        "over: 'Three throws for a copper! Everybody's a winner, sooner or later!'",
        {"w": "midway", "e": "prize_booth"},
        spawns=[("carnival_barker", 1), ("carnival_pickpocket", 2)], level=(25, 25)),
    "prize_booth": R(
        "The Prize Booth", AREA,
        "A booth stacked to the canvas roof with prizes, and none of them are cheap trinkets: swords, "
        "helms, lutes, boots and rings, each with a paper tag giving a name and a date. They are the "
        "things lost by everyone who ever came to the carnival. A cheerful ghost in a striped "
        "waistcoat minds the booth.",
        {"w": "games_of_skill"},
        npcs=["pip"], safe=True),
    "strongman_stage": R(
        "The Strongman's Stage", AREA,
        "A wooden stage hung with bunting holds iron weights, a test-your-strength machine with a "
        "great brass bell, and a man with arms like tree trunks and a waxed moustache. He has been "
        "lifting the same anvil over his head since before your grandmother was born.",
        {"n": "midway", "s": "carousel"},
        spawns=[("the_strongman", 1), ("roustabout", 1)], level=(25, 26)),

    # ------------------------------------------------- the attractions (26-28)
    "carousel": R(
        "The Carousel", AREA,
        "A great carousel turns to a wheezing organ tune, its painted horses rising and falling on "
        "brass poles. Grey, laughing spirits ride them round and round, and wave each time they pass. "
        "You are fairly sure that yesterday it had a swan, and that the swan had a rider.",
        {"n": "strongman_stage", "w": "hall_of_mirrors", "e": "menagerie", "s": "ghost_train"},
        spawns=[("carousel_spirit", 2), ("painted_horse", 1)], level=(26, 26)),
    "hall_of_mirrors": R(
        "The Hall of Mirrors", AREA,
        "A maze of mirrors throws a thousand of you back at yourself, tall, thin, squat and swollen. "
        "Some of the reflections are a moment late. One of them is not moving at all, and is smiling "
        "in a way that you are not.",
        {"e": "carousel"},
        spawns=[("mirror_double", 2)], level=(26, 27)),
    "menagerie": R(
        "The Menagerie", AREA,
        "Painted wagons with barred sides form a ring around a muddy yard, each holding a beast from "
        "some far country: a striped cat the size of a horse, a bear in a ruff and a little hat. The "
        "cages are all open. The animals have chosen to stay, and they are watching you.",
        {"w": "carousel", "e": "great_wheel"},
        spawns=[("menagerie_tiger", 1), ("dancing_bear", 1)], level=(27, 27)),
    "great_wheel": R(
        "The Great Wheel", AREA,
        "A wheel of iron and painted wood stands taller than any tower in Brightwater, hung with "
        "swinging gondolas. It is turned from inside by spirits running in a treadmill, singing a "
        "marching song and waving cheerfully whenever anyone looks. North, a small purple tent "
        "promises your fortune.",
        {"w": "menagerie", "n": "fortune_tent"},
        spawns=[("wheel_spirit", 2), ("roustabout", 1)], level=(27, 28)),
    "fortune_tent": R(
        "The Fortune Teller's Tent", AREA,
        "Inside a tent of purple velvet, a crystal ball glows on a table covered with cards. A woman "
        "in shawls and coins looks up as you enter. 'Sit,' she says. 'I already know what you came "
        "to ask, and the answer is no. Nobody ever leaves.'",
        {"s": "great_wheel"},
        spawns=[("madame_vesna", 1)], level=(28, 28)),
    "ghost_train": R(
        "The Ghost Train", AREA,
        "A little painted train rattles into a black tunnel decorated with paper skeletons and cotton "
        "cobwebs. The skeletons are not paper. The passengers are see-through and wave from the "
        "carriages, delighted, as they go round for the ten-thousandth time.",
        {"n": "carousel", "e": "tent_of_wonders", "s": "behind_the_tents"},
        spawns=[("ghost_passenger", 2), ("roustabout", 1)], level=(27, 28)),
    "tent_of_wonders": R(
        "The Tent of Wonders", AREA,
        "A long tent of curiosities: a mermaid in a jar, a two-headed calf, a waxwork of every king of "
        "Brightwater. The waxworks are warm to the touch, and their eyes are wet. Some of them, you "
        "notice, are wearing adventurers' boots.",
        {"w": "ghost_train"},
        spawns=[("waxwork", 2)], level=(28, 28)),

    # ------------------------------------------------- behind the tents (28-30)
    "behind_the_tents": R(
        "Behind the Tents", AREA,
        "Behind the midway, the lights go out. Guy ropes and stacked crates make a maze of shadows, "
        "and the music from the front sounds very far away. Here it is always midnight, and the "
        "barkers who work the back lots no longer bother to lie.",
        {"n": "ghost_train", "w": "performers_wagons", "e": "cage_wagons", "s": "back_lot"},
        spawns=[("night_barker", 1), ("carnival_acrobat", 1)], level=(28, 28)),
    "performers_wagons": R(
        "The Performers' Wagons", AREA,
        "A circle of painted living-wagons, their windows lit and their doors open. Acrobats stretch on "
        "the steps, and a juggler keeps seven knives in the air without looking at them. They have all "
        "performed every night for longer than they can remember, and they are very, very tired.",
        {"e": "behind_the_tents", "s": "knife_wagon"},
        spawns=[("carnival_acrobat", 2)], level=(28, 29)),
    "knife_wagon": R(
        "The Knife-Thrower's Wagon", AREA,
        "A red wagon with a spinning target board leaning against it, the board studded with knives "
        "around a person-shaped gap. A woman with a bandolier of blades is cleaning them one by one. "
        "'Stand against the board,' she says. 'I never miss. Not any more.'",
        {"n": "performers_wagons"},
        spawns=[("mirela", 1)], level=(29, 29)),
    "cage_wagons": R(
        "The Cage Wagons", AREA,
        "Wagons with heavy black bars stand in a row under a sign reading THE CARNIVAL'S OWN. Whatever "
        "is inside them has been made by the carnival out of what it kept: too many arms, a face in "
        "the wrong place, a voice that whispers your name. These cages are locked.",
        {"w": "behind_the_tents"},
        spawns=[("caged_horror", 2)], level=(29, 29)),
    "back_lot": R(
        "The Back Lot", AREA,
        "A muddy field of broken rides and rotting tents, where the carnival puts the attractions it "
        "has finished with. A carousel horse lies on its side, still slowly kicking. Ahead, the great "
        "striped dome of the big top rises against a sky with no stars.",
        {"n": "behind_the_tents", "e": "clown_alley", "s": "big_top_doors"},
        spawns=[("night_barker", 1), ("painted_horse", 1)], level=(29, 29)),
    "clown_alley": R(
        "Clown Alley", AREA,
        "The clowns' wagons stand in a crooked row, their doors painted with grinning faces. Greasepaint "
        "and seltzer bottles litter the steps. The clowns sit in the doorways and do not laugh, and when "
        "they stand up, all at once, they do not stop smiling.",
        {"w": "back_lot"},
        spawns=[("carnival_clown", 2)], level=(29, 30)),
    "big_top_doors": R(
        "The Big Top Doors", AREA,
        "The canvas flaps of the big top hang open, and a roar of applause rolls out from inside, though "
        "the seats you can see are empty. Ticket stubs drift about your feet, each one stamped with a "
        "name. The roustabouts on the door wave you in.",
        {"n": "back_lot", "s": "big_top"},
        spawns=[("roustabout", 2), ("night_barker", 1)], level=(29, 30)),
    "big_top": R(
        "The Big Top", AREA,
        "Under the great dome, a sawdust ring lies in a single spotlight, and ten thousand empty seats "
        "rise into the dark, applauding. In the ring stands the Ringmaster in a scarlet coat and a tall "
        "hat, whip in hand, smiling with every tooth. Thin threads, like puppet strings, run from his "
        "wrists up into the canvas. 'Welcome,' he says, 'to the show that never ends.'",
        {"n": "big_top_doors"},
        spawns=[("the_ringmaster", 1)], level=(30, 30)),
}
