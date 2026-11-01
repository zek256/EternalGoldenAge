"""The Chancery of the Dead, south of the Dustway's Gnoll Scrub (30-38). A court that hears the
cases of the dead with unfinished business. Its clerks and petitioners ignore the living; only the
bailiffs and wardens attack on sight. The inner chambers open only to those carrying a writ of
audience from the Office of Forms and Writs."""
from data.rooms.common import R

AREA = "The Chancery of the Dead"

ROOMS = {
    # ------------------------------------------------- the Gallows Road (30-32)
    "gallows_road": R(
        "The Gallows Road", AREA,
        "South of the scrub, a road of grey dust runs down from the foot of Gallows Hill into a valley "
        "where no birds sing. The colour drains from everything as you walk. Pale figures with ropes "
        "still around their necks trudge south beside you, clutching rolls of paper.",
        {"n": "gnoll_scrub", "s": "hanged_queue"},
        spawns=[("hanged_petitioner", 2)], level=(30, 31)),
    "hanged_queue": R(
        "The Line of the Hanged", AREA,
        "The road ends in a queue that stretches out of sight: the dead of Gallows Hill and a hundred "
        "other gallows, waiting their turn in silence. A wooden sign reads TAKE A NUMBER. The number "
        "you take is four hundred thousand and six.",
        {"n": "gallows_road", "w": "headsmans_block", "s": "grey_gate"},
        spawns=[("hanged_petitioner", 2), ("queue_warden", 1)], level=(30, 31)),
    "headsmans_block": R(
        "The Headsman's Block", AREA,
        "Off to the side of the queue stands a scaffold with a block of black wood, worn hollow in the "
        "middle. A hooded headsman sits beside it, sharpening his axe and waiting, as he has waited for "
        "three hundred years, for the court to send him someone.",
        {"e": "hanged_queue"},
        spawns=[("the_headsman", 1)], level=(32, 32)),
    "grey_gate": R(
        "The Grey Gate", AREA,
        "A gate of grey stone, carved with scales and quills, stands at the head of the queue. Above it "
        "runs an inscription: ALL SHALL BE HEARD IN THEIR TURN. Bailiffs in grey tabards check each "
        "petitioner's papers, and they are not pleased to see someone who is still breathing.",
        {"n": "hanged_queue", "s": "hall_of_waiting"},
        spawns=[("court_bailiff", 2)], level=(31, 32)),

    # ------------------------------------------------- the outer offices (31-34)
    "hall_of_waiting": R(
        "The Hall of Waiting", AREA,
        "A vast hall of grey benches, row upon row, where the dead sit with their papers on their knees "
        "and wait. Some have been waiting so long that they have faded to outlines. A clerk at a high "
        "desk calls a number every hour, and no one ever stands up.",
        {"n": "grey_gate", "w": "registry_of_deaths", "e": "office_of_forms", "s": "petition_corridor"},
        spawns=[("waiting_shade", 2), ("court_bailiff", 1)], level=(31, 32)),
    "registry_of_deaths": R(
        "The Registry of Deaths", AREA,
        "Ledgers as tall as a man line the walls of this office, listing every death in the world in "
        "tiny, crabbed writing that is still being added to as you watch. Spectral clerks stamp, blot, "
        "file and refile, and the thump of their seals never stops.",
        {"e": "hall_of_waiting", "w": "room_of_lost_names"},
        spawns=[("registry_clerk", 3)], level=(32, 33)),
    "room_of_lost_names": R(
        "The Room of Lost Names", AREA,
        "A small, cold room for the dead whose names have been lost, misspelled or filed under the "
        "wrong letter. They drift about the shelves, searching and muttering half-names to "
        "themselves, and grow angry when anyone gets in the way.",
        {"e": "registry_of_deaths"},
        spawns=[("nameless_shade", 2)], level=(33, 33)),
    "office_of_forms": R(
        "The Office of Forms and Writs", AREA,
        "A tidy office behind a grille, with pigeonholes of forms rising to the ceiling, every one "
        "labelled in a neat hand. A small, precise ghost in spectacles sits behind the grille. A "
        "notice on the wall says that the living may be heard only with a writ of audience, and that "
        "no exceptions will be made, and that this includes you.",
        {"w": "hall_of_waiting"},
        npcs=["clerk_quillon"], safe=True),
    "petition_corridor": R(
        "The Corridor of Petitions", AREA,
        "A long corridor whose walls are papered, layer on layer, with petitions nailed up and never "
        "answered. Ghostly petitioners pace it, reading their own petitions aloud to anyone who will "
        "listen. Doors lead to the scriveners and to the court of small claims.",
        {"n": "hall_of_waiting", "w": "scriveners_hall", "e": "small_claims", "s": "hall_of_seals"},
        spawns=[("waiting_shade", 1), ("restless_petitioner", 2)], level=(33, 33)),
    "scriveners_hall": R(
        "The Scriveners' Hall", AREA,
        "Rows of slanted desks fill a long hall where spectral scriveners copy out wills, deeds and "
        "judgements by the light of grey candles. Their quills never stop. Here and there a page "
        "rustles and rewrites itself, and a scrivener sighs and starts again.",
        {"e": "petition_corridor"},
        spawns=[("spectral_scrivener", 3)], level=(33, 34)),
    "small_claims": R(
        "The Court of Small Claims", AREA,
        "A cramped little courtroom where the dead argue over borrowed spoons, unpaid debts of three "
        "coppers, and a goat that went missing two hundred years ago. A minor magistrate presides, "
        "visibly bored, and the bailiff is asleep.",
        {"w": "petition_corridor"},
        spawns=[("restless_petitioner", 2), ("minor_magistrate", 1)], level=(33, 34)),

    # ------------------------------------------------- the courts and archives (34-36)
    "hall_of_seals": R(
        "The Hall of Seals", AREA,
        "A round hall where every seal the court has ever used hangs on the walls, from tiny signets "
        "to a stamp the size of a cartwheel. Wardens of the court stand under them in grey plate. "
        "East, through tall doors, lie the great courts.",
        {"n": "petition_corridor", "e": "probate_court"},
        spawns=[("chancery_warden", 1), ("court_bailiff", 1)], level=(34, 34)),
    "probate_court": R(
        "The Court of Probate", AREA,
        "Here the court hears disputes over wills. Heirs living and dead shout across the aisle, and a "
        "will on the bench keeps rewriting itself in front of everyone, to gasps from the gallery. "
        "Below, a stair leads down to the archives.",
        {"w": "hall_of_seals", "e": "property_court", "s": "archive_of_wills"},
        spawns=[("wrathful_heir", 2), ("spectral_scrivener", 1)], level=(34, 35)),
    "property_court": R(
        "The Court of Property", AREA,
        "A court for disputes between the living and the dead over houses, fields and graves. Today "
        "a family of ghosts refuses to leave a manor sold sixty years ago, and the buyer's hired "
        "swords, very much alive, have given up waiting for a verdict.",
        {"w": "probate_court", "e": "court_of_appeals"},
        spawns=[("ghostly_squatter", 2), ("hired_sword", 1)], level=(35, 35)),
    "court_of_appeals": R(
        "The Court of Appeals", AREA,
        "A high, echoing court where judgements are appealed, and the appeals are appealed, and the "
        "appeals of the appeals fill a hall of shelves behind the bench. A tired advocate is still "
        "arguing a case whose client has long since faded. North, a pair of black doors is closed.",
        {"w": "property_court", "n": "door_of_audience", "s": "sealed_archive"},
        spawns=[("dead_advocate", 2), ("chancery_warden", 1)], level=(35, 36)),
    "archive_of_wills": R(
        "The Archive of Wills", AREA,
        "Below the court of probate, shelves of wills run off into the dark, each tied with a black "
        "ribbon. Some of the scrolls are twitching. A will slips from its shelf, unrolls itself on the "
        "floor and begins, in a thin voice, to read itself aloud.",
        {"n": "probate_court", "e": "archive_stacks"},
        spawns=[("living_will", 2), ("archive_keeper", 1)], level=(34, 35)),
    "archive_stacks": R(
        "The Archive Stacks", AREA,
        "The stacks go on and on, every aisle the same, and the ladders lean into darkness above. "
        "Keepers of the archive glide between the shelves with lanterns of grey flame, and every so "
        "often one of them stops and looks at you for a long time.",
        {"w": "archive_of_wills", "e": "sealed_archive"},
        spawns=[("archive_keeper", 2), ("living_will", 1)], level=(35, 36)),
    "sealed_archive": R(
        "The Sealed Archive", AREA,
        "Behind a grille of black iron lie the court's sealed records: evidence never heard, verdicts "
        "never read, and the confessions of people who were hanged anyway. The air is heavy with old "
        "wax and older secrets.",
        {"w": "archive_stacks", "n": "court_of_appeals"},
        spawns=[("archive_keeper", 1), ("chancery_warden", 1)], level=(36, 36)),

    # ------------------------------------------------- the inner chambers (36-38)
    "door_of_audience": R(
        "The Door of Audience", AREA,
        "Beyond the black doors, a quiet antechamber is lined with portraits of judges, every face worn "
        "smooth and blank. A warden at the far door holds out a gauntleted hand for your writ, and does "
        "not lower it until he has read every word.",
        {"s": "court_of_appeals", "n": "robing_room"},
        spawns=[("chancery_warden", 2)], level=(36, 36),
        gate={"item": "writ_of_audience",
              "msg": "The black doors do not open. A voice from behind them intones: 'The living may be "
                     "heard only with a writ of audience. Apply to the Office of Forms and Writs.'"}),
    "robing_room": R(
        "The Robing Room", AREA,
        "Black robes and grey wigs hang on pegs around a dim room, empty, swaying as if worn by "
        "invisible judges. A rack of gavels stands by the door. The judges of the high court are "
        "dressing for a session that has lasted four hundred years.",
        {"s": "door_of_audience", "n": "judges_chambers", "w": "hall_of_old_verdicts"},
        spawns=[("robed_judge", 1), ("court_bailiff", 1)], level=(36, 37)),
    "hall_of_old_verdicts": R(
        "The Hall of Old Verdicts", AREA,
        "Every verdict the high court has ever given is carved on the walls of this long hall, and "
        "the oldest are so worn that only the word GUILTY can still be read. The ghosts of the "
        "condemned stand before their verdicts, reading them over and over.",
        {"e": "robing_room"},
        spawns=[("condemned_shade", 2), ("robed_judge", 1)], level=(37, 37)),
    "judges_chambers": R(
        "The Judges' Chambers", AREA,
        "Leather chairs, cold hearths and decanters of something grey surround a long table where the "
        "judges of the high court confer. Two of them are arguing about the meaning of a comma. "
        "Beyond a door of black oak, someone is banging a gavel slowly, over and over.",
        {"s": "robing_room", "n": "high_bench"},
        spawns=[("robed_judge", 2)], level=(37, 37)),
    "high_bench": R(
        "The High Bench", AREA,
        "A courtroom of black stone with a bench raised so high that you must crane your neck to see "
        "it. On the bench sits the High Justice, a husk of a man in robes gone grey with dust, beating "
        "his gavel on nothing. He peers down at you. 'Guilty,' he says. 'Of what, I no longer recall.'",
        {"s": "judges_chambers"},
        spawns=[("high_justice", 1), ("court_bailiff", 1)], level=(38, 38)),
}
