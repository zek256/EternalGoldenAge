"""Quests. Talk to the giver to accept; talk again once the objective is met to turn in.

type "kill"    - slay `count` of monster `target`
type "collect" - bring `count` of item `target` (removed on turn-in)
"""

QUESTS = {
    "cellar_rats": {
        "name": "Vermin in the Cellar", "giver": "bram", "type": "kill", "target": "giant_rat", "count": 6,
        "min_level": 1, "prereq": None,
        "offer": "'Ah, an adventurer! Just what I need. Rats, see, giant ones, big as hounds, have gotten "
                 "into my cellar and they're eating me out of house and home. Clear out six of the brutes "
                 "and I'll make it worth your while. The trapdoor's just behind the bar - go DOWN.'",
        "progress": "'Still hear them squeaking down there... ({n}/{count} rats slain)'",
        "complete": "'Ha! The cellar's quiet at last! Here, take these, and drinks are on the house.'",
        "reward": {"xp": 160, "gold": 25, "items": ["minor_healing_potion", "minor_healing_potion", "minor_mana_potion"]},
    },
    "wolf_pelts": {
        "name": "Wolves at the Gate", "giver": "halvard", "type": "collect", "target": "wolf_pelt", "count": 4,
        "min_level": 3, "prereq": None,
        "offer": "'Wolves from the Whispering Woods have been taking sheep from the southern farms. "
                 "My men are stretched thin. Bring me four grey wolf pelts as proof you've thinned the "
                 "pack. The woods lie south of town, past Willowbrook Crossing.'",
        "progress": "'Four pelts, that's the bargain. You have {n}.'",
        "complete": "'Good, thick pelts. The farmers will sleep easier. Take these gloves - they served me well.'",
        "reward": {"xp": 550, "gold": 60, "items": ["studded_gloves", "healing_potion"]},
    },
    "bandit_chief": {
        "name": "The Bandit Chieftain", "giver": "halvard", "type": "kill", "target": "bandit_chieftain", "count": 1,
        "min_level": 6, "prereq": "wolf_pelts",
        "offer": "'You've proven yourself. Now for the real trouble: a brute called Rask has gathered a "
                 "gang of cutthroats in a palisade camp deep in the Whispering Woods. They've been "
                 "robbing every caravan on the south road. End him.'",
        "progress": "'Rask still breathes. His camp lies at the far southern end of the deep woods.'",
        "complete": "'Rask is dead? By the Dawn! You've done this town a great service. Take this mail "
                    "from the armoury - and my thanks.'",
        "reward": {"xp": 2200, "gold": 200, "items": ["chain_shirt", "healing_potion", "healing_potion"]},
    },
    "bone_king": {
        "name": "The Bone King", "giver": "aveline", "type": "kill", "target": "varnoth", "count": 1,
        "min_level": 10, "prereq": None,
        "offer": "'A great evil has woken beneath Barrowfield, east of the King's Road. Varnoth, a "
                 "lich who was buried there a thousand years ago, is raising the dead. His cult grows "
                 "bolder every night. Descend into his crypt beneath the ruined chapel and destroy him. "
                 "The light goes with you.'",
        "progress": "'The dead still walk at Barrowfield. Varnoth must be destroyed.'",
        "complete": "'I felt it - the darkness beneath Barrowfield has lifted! Wear this amulet, blessed "
                    "at the altar of the Dawn. You are truly a champion of the light.'",
        "reward": {"xp": 9000, "gold": 500, "items": ["amulet_of_the_dawn", "healing_potion", "mana_potion"]},
    },
    "bog_hag": {
        "name": "The Hag of the Mirefen", "giver": "aveline", "type": "kill", "target": "bog_hag", "count": 1,
        "min_level": 17, "prereq": "bone_king",
        "offer": "'There is another evil I must ask you to face. Children have been vanishing from the "
                 "villages near the Mirefen, west of the crossroads. The lizardfolk whisper of a hag "
                 "called Old Mother Gristle who lives deep in the swamp. Find her. Put an end to it.'",
        "progress": "'Old Mother Gristle still haunts the Mirefen. Her hut lies past the serpent pools.'",
        "complete": "'The children have come home! Bless you. The temple's coffers are yours to share.'",
        "reward": {"xp": 30000, "gold": 1200, "items": ["greater_healing_potion", "greater_healing_potion", "greater_mana_potion"]},
    },
    "frost_goblins": {
        "name": "Trouble in the Rimefells", "giver": "halvard", "type": "kill", "target": "frost_goblin", "count": 8,
        "min_level": 11, "prereq": None,
        "offer": "'A rider came down from the dwarves of Hearthdeep. Frost goblins are raiding their road "
                 "and the Thane has asked Brightwater for help. Head out the West Gate, through the "
                 "Westmarch and north past the old watchtower into the Rimefells. Kill eight of the "
                 "little devils, and make yourself known to the dwarves while you're there.'",
        "progress": "'The dwarves still count goblin raids. ({n}/{count} frost goblins slain)'",
        "complete": "'The Thane sends his thanks, and so do I. Take this dwarven mail, it came down with "
                    "the rider.'",
        "reward": {"xp": 6000, "gold": 200, "items": ["dwarven_chainmail", "healing_potion", "healing_potion"]},
    },
    "orc_warlord": {
        "name": "The Skullsplitter Horde", "giver": "halvard", "type": "kill", "target": "warlord_gorrak", "count": 1,
        "min_level": 25, "prereq": "bandit_chief",
        "offer": "'Scouts report an orc horde massing in the Ironspine, under a warlord called Gorrak "
                 "Skullsplitter. If he marches south, Brightwater will burn. Strike first. Find his "
                 "warcamp east of Ironspine Pass and bring him down.'",
        "progress": "'The war-drums still sound in the mountains. Gorrak lives.'",
        "complete": "'Gorrak is slain and the horde is scattering! The King himself will hear of this.'",
        "reward": {"xp": 90000, "gold": 3000, "items": ["greater_healing_potion", "greater_healing_potion", "tower_shield"]},
    },

    # ------------------------------------------------------------------ Westmarch
    "goblin_raiders": {
        "name": "Goblins in the Henhouse", "giver": "haverick", "type": "kill", "target": "hill_goblin", "count": 6,
        "min_level": 5, "prereq": None,
        "offer": "'Goblins! Out of the old quarry, every night, stealing hens, pigs, washing off the line, "
                 "my second-best boots. I've had enough. Go up to the quarry west of here and thin them "
                 "out, six of the hill goblins at least, and I'll see you right.'",
        "progress": "'Still hearing them up at the quarry of a night. ({n}/{count} hill goblins slain)'",
        "complete": "'Quiet as a churchyard last night! Here, take this helm, my grandad wore it at the "
                    "Battle of the Ford and never needed it once.'",
        "reward": {"xp": 1500, "gold": 60, "items": ["iron_helm", "healing_potion"]},
    },

    "salt_wraiths": {
        "name": "The Thirsting Dead", "giver": "aveline", "type": "kill", "target": "salt_wraith", "count": 8,
        "min_level": 36, "prereq": None,
        "offer": "'A plea has reached the temple from the Emira of Sunspire, the golden city beyond the "
                 "Badlands. The dead are rising on the salt flats north of her city's western oasis, "
                 "and her people dare not fetch water. Take the Dustway east from the East Gate, cross "
                 "the Badlands, and lay eight of the salt wraiths to rest.'",
        "progress": "'The dead still thirst on the salt flats. ({n}/{count} salt wraiths laid to rest)'",
        "complete": "'The Emira has written to thank the temple, and you. Take this from our treasury, "
                    "and go to Sunspire again; I think they have need of you still.'",
        "reward": {"xp": 30000, "gold": 1500, "items": ["obelisk_amulet", "supreme_healing_potion"]},
    },
    "blight_spreads": {
        "name": "The Blight Spreads", "giver": "elowen", "type": "kill", "target": "blighted_treant", "count": 6,
        "min_level": 24, "prereq": None,
        "offer": "'A letter came from my kin in Silverbough, the elven city deep in the Eldergrove. A blight "
                 "is eating the forest from the south, and the trees themselves walk now, rotten and "
                 "angry. Go south past the Dire Wolf Den and take the Old South Way. Fell six of the "
                 "blighted treants, and tell the Speaker that Elowen sent you.'",
        "progress": "'The grove still sickens. ({n}/{count} blighted treants felled)'",
        "complete": "'My sister writes that the wardens speak of you already. Take this, woven in "
                    "Silverbough, and go back to them. They need you more than I do.'",
        "reward": {"xp": 15000, "gold": 400, "items": ["silverleaf_pendant", "greater_healing_potion"]},
    },

    # ------------------------------------------------------------------ Hearthdeep
    "yeti_menace": {
        "name": "Fur for the Gatewatch", "giver": "orla", "type": "collect", "target": "yeti_fur", "count": 6,
        "min_level": 15, "prereq": None,
        "offer": "'Yetis have come down out of the high caves, bold as you like, and my sentries are "
                 "freezing at their posts. Two birds, one axe: go north of the Rimewood to the yeti caves "
                 "and bring me six hanks of yeti fur. We'll line the sentries' cloaks with it.'",
        "progress": "'Six hanks, and the Gatewatch will stop complaining. You have {n}.'",
        "complete": "'Ha! Good thick fur. My sentries will sing your name, badly. Take these boots, "
                    "they'll keep your feet on the rock.'",
        "reward": {"xp": 12000, "gold": 350, "items": ["dwarven_boots", "healing_potion", "healing_potion"]},
    },
    "stonewake": {
        "name": "The Stonewake", "giver": "hargrim", "type": "kill", "target": "ghaldrek", "count": 1,
        "min_level": 18, "prereq": None,
        "offer": "'Our miners dug too deep in Deepdelve. They broke into a vault no dwarf ever cut, and "
                 "something woke. The miners came back grey and silent and went down again, and none "
                 "have come up since. The old songs call it the Stonewake. Take the lift down, find what "
                 "they woke, and put it back to sleep. Forever.'",
        "progress": "'The mountain still groans in the night. The Stonewake lives.'",
        "complete": "'The groaning has stopped. By my beard, you did it. The lost miners can rest now, "
                    "and Hearthdeep owes you a debt. Take these greaves from my own armoury.'",
        "reward": {"xp": 25000, "gold": 1000, "items": ["dwarven_greaves", "greater_healing_potion",
                                                        "greater_healing_potion"]},
    },

    # ------------------------------------------------------------------ Silverbough
    "stag_antlers": {
        "name": "The Sacred Herd", "giver": "faelan", "type": "collect", "target": "stag_antler", "count": 5,
        "min_level": 24, "prereq": None,
        "offer": "'The blight is creeping into the greatstags. Once it takes them, they turn on the herd. "
                 "The Speaker has given leave to cull the sick ones before it spreads. Bring me five "
                 "antlers from the stags of the Stag Walk or the Whitestag Glade. It is a sad duty, but "
                 "a necessary one.'",
        "progress": "'Five antlers, and the herd may yet survive. You have {n}.'",
        "complete": "'It is done, then. The herd will remember, even if we would rather forget. Take "
                    "these boots, and walk the grove as a warden does.'",
        "reward": {"xp": 15000, "gold": 400, "items": ["wardens_boots", "greater_healing_potion"]},
    },
    "rotwood_druids": {
        "name": "The Rotwood Circle", "giver": "faelan", "type": "kill", "target": "rotwood_druid", "count": 8,
        "min_level": 27, "prereq": "stag_antlers",
        "offer": "'The blight does not spread on its own. Druids who have given themselves to it are "
                 "tending it, feeding it, singing the treants awake. They gather at the Druids' Ring, "
                 "the Fungal Barrows and beyond the Thornward Gate. Kill eight of them.'",
        "progress": "'The rotwood circle still sings. ({n}/{count} rotwood druids slain)'",
        "complete": "'Eight fewer voices singing the rot. The grove is quieter. Take these gauntlets, "
                    "the wardens' own.'",
        "reward": {"xp": 25000, "gold": 800, "items": ["wardens_gauntlets", "greater_healing_potion",
                                                       "greater_healing_potion"]},
    },
    "heart_of_blight": {
        "name": "The Heart of the Blight", "giver": "saelwyn", "type": "kill", "target": "rotheart", "count": 1,
        "min_level": 30, "prereq": None,
        "offer": "'The blight has a heart. It is Rotheart, the oldest tree in the world, who sheltered "
                 "our people when Elandor fell. Something has poisoned him, and his rot flows out through "
                 "every root in the grove. It grieves me past words to ask it. Go through the Thornward "
                 "Gate, past the Gloaming Mere, and end him.'",
        "progress": "'Rotheart still burns at the heart of the blight. The grove is dying.'",
        "complete": "'I felt him go. The green is already coming back into the leaves. You have saved "
                    "the Eldergrove, and Silverbough will not forget your name while a single tree stands.'",
        "reward": {"xp": 70000, "gold": 2500, "items": ["moonstone_ring", "greater_healing_potion",
                                                        "greater_healing_potion"]},
    },

    # ------------------------------------------------------------------ Dustway
    "dust_highwaymen": {
        "name": "Highway Robbery", "giver": "marta", "type": "kill", "target": "highwayman", "count": 6,
        "min_level": 9, "prereq": None,
        "offer": "'Highwaymen on Gallows Hill, bold as brass, robbing every cart that comes through the "
                 "Dry Ford. My guests stop coming, I stop eating. Kill six of them and I'll pay you "
                 "out of what they'd have taken.'",
        "progress": "'Still masks on Gallows Hill. ({n}/{count} highwaymen dealt with)'",
        "complete": "'Ha! The carters are singing again. Here's your pay, and a little something from "
                    "under the bar.'",
        "reward": {"xp": 3500, "gold": 150, "items": ["chain_leggings", "healing_potion"]},
    },
    "yellowtooth": {
        "name": "The Laughing Warlord", "giver": "marta", "type": "kill", "target": "yellowtooth", "count": 1,
        "min_level": 23, "prereq": "dust_highwaymen",
        "offer": "'The gnolls of the Badlands have a warlord now, a grey old monster called Yellowtooth. "
                 "Since he took the pack, they don't just scavenge, they raid. Three caravans this "
                 "season, every soul eaten. His den's at the far end of the canyons, past the Howling "
                 "Pit. Bring him down.'",
        "progress": "'You can hear him laughing on the wind some nights. Yellowtooth lives.'",
        "complete": "'Dead? Truly? Forty years I've kept this house, and that's the best news I've had "
                    "in all of them. The caravans will come back. Take all of this, you've earned it.'",
        "reward": {"xp": 35000, "gold": 1500, "items": ["greater_healing_potion", "greater_healing_potion",
                                                        "runed_shield"]},
    },

    # ------------------------------------------------------------------ Sunspire
    "desert_glass": {
        "name": "Glass from the Sands", "giver": "mehrun", "type": "collect", "target": "desert_glass", "count": 5,
        "min_level": 40, "prereq": None,
        "offer": "'Desert glass! The sand was melted by something, long ago, and I believe the glass "
                 "remembers what. Bring me five shards. The scorpions of the Glass Waste swallow it, "
                 "the mirage-cats roll in it, and the salt wraiths clutch it like coins. Five shards, "
                 "and I will pay well.'",
        "progress": "'Five shards, please. You have {n}.'",
        "complete": "'Look at the colour! There was fire here once like nothing on this earth. You have "
                    "done the archive a great service. Take this ring, it was found in these sands.'",
        "reward": {"xp": 35000, "gold": 1500, "items": ["sunstone_ring", "supreme_mana_potion"]},
    },
    "sand_giants": {
        "name": "Giants on the Causeway", "giver": "idrisa", "type": "kill", "target": "sand_giant", "count": 6,
        "min_level": 44, "prereq": None,
        "offer": "'The sand giants of the Causeway have started raiding the northern caravans, and they "
                 "throw pillars at my patrols like children throwing stones. Go out the North Gate, west "
                 "to the Giants' Causeway and the Valley of the Kings, and kill six of them.'",
        "progress": "'The giants still hold the Causeway. ({n}/{count} sand giants slain)'",
        "complete": "'Six giants! The Sun Guard will drink to you tonight. Take this blade, the Guard's "
                    "own pattern.'",
        "reward": {"xp": 45000, "gold": 2000, "items": ["crescent_greatsword", "supreme_healing_potion",
                                                        "supreme_healing_potion"]},
    },
    "sand_king": {
        "name": "The Last Sand King", "giver": "zahrin", "type": "kill", "target": "ussreth", "count": 1,
        "min_level": 45, "prereq": None,
        "offer": "'Three thousand years ago, the Sand Kings ruled all of this desert, and the last of them "
                 "was buried in a black pyramid north of here with ten thousand slaves. Robbers broke "
                 "his seal last spring. Now the dead walk, the scarabs swarm, and my people sicken. The "
                 "pyramid lies beyond the Valley of the Kings. Go down into the tomb, and give Ussreth "
                 "the rest he will not take.'",
        "progress": "'The sickness spreads. Ussreth still walks in his tomb.'",
        "complete": "'The sickness is lifting already. Sunspire owes you its life. Whatever you need "
                    "in this city, it is yours, and your name will be cut into the Obelisk.'",
        "reward": {"xp": 150000, "gold": 5000, "items": ["supreme_healing_potion", "supreme_healing_potion",
                                                         "supreme_mana_potion"]},
    },

    # ------------------------------------------------------------------ Thornwick Hall
    "vane_hounds": {
        "name": "The Gamekeeper's Dogs", "giver": "nell_rook", "type": "kill", "target": "vane_boarhound", "count": 6,
        "min_level": 40, "prereq": None,
        "offer": "'Those boarhounds of the Vanes have had three of my snares and half my left boot. They "
                 "run the Chase, the park and the hedge maze, and old Hobb keeps a pack at his lodge. Kill "
                 "six of them for me. I'll pay for every one, and I won't ask what you're doing out here.'",
        "progress": "'I can still hear them baying. ({n}/{count} boarhounds slain)'",
        "complete": "'Quiet at last. Here, you've earned these, and the coin.'",
        "reward": {"xp": 30000, "gold": 1400, "items": ["supreme_healing_potion", "supreme_healing_potion"]},
    },
    "vane_ledgers": {
        "name": "The Steward's Books", "giver": "nell_rook", "type": "collect", "target": "vane_ledger", "count": 4,
        "min_level": 43, "prereq": None,
        "offer": "'The steward keeps the rents of every farm in the valley in his books: who owes what, "
                 "who's late, who's hiding a pig. There are people who would pay a great deal for those "
                 "books, and I am one of them. He and his clerks work in a room off the minstrels' gallery. "
                 "Bring me four ledgers.'",
        "progress": "'Four ledgers. You have {n}.'",
        "complete": "'Oh, these are lovely. Half the valley owes him money, and the other half owes it to "
                    "someone worse. You never saw these.'",
        "reward": {"xp": 40000, "gold": 1800, "items": ["supreme_mana_potion", "supreme_healing_potion"]},
    },
    "vane_brooches": {
        "name": "Jewels of the Ladies", "giver": "nell_rook", "type": "collect", "target": "vane_brooch", "count": 5,
        "min_level": 45, "prereq": None,
        "offer": "'Every lady in that house wears a stag in emeralds, a gift from the lord, and every one "
                 "of them is worth a farm. The ladies-in-waiting sit upstairs in the solar; the Dowager's "
                 "women and the old aunt have them too. Bring me five, and I'll give you something better "
                 "than gold.'",
        "progress": "'Five brooches. You have {n}.'",
        "complete": "'Look at the fire in those stones. Here, take this ring. It came out of a dragon's "
                    "hoard, they say, and I never had the hands for it.'",
        "reward": {"xp": 45000, "gold": 2000, "items": ["ember_ring", "supreme_healing_potion"]},
    },
    "vane_lord": {
        "name": "The Lord of Thornwick", "giver": "nell_rook", "type": "kill", "target": "lord_aldric_vane", "count": 1,
        "min_level": 47, "prereq": None,
        "offer": "'Lord Aldric. He keeps to his chambers at the top of the house, past his sworn swords, "
                 "and he is the finest blade in the valley, whatever his cousin says. I won't tell you "
                 "why I want him dead, and you won't tell me why you'll do it. Up the grand staircase, "
                 "north along the long gallery, and through the doors with the stag on them.'",
        "progress": "'He's still up there. I can see the lamp in his window from here.'",
        "complete": "'So. The lamp's out. I never thought I'd see it.' She is quiet for a long while. "
                    "'Take this, all of it. And go, before the valley wakes up and wonders what comes next.'",
        "reward": {"xp": 150000, "gold": 6000, "items": ["supreme_healing_potion", "supreme_healing_potion",
                                                         "supreme_mana_potion"]},
    },

    # ------------------------------------------------------------------ The Chancery of the Dead
    "chancery_writ": {
        "name": "The Proper Forms", "giver": "clerk_quillon", "type": "collect", "target": "stamped_form", "count": 3,
        "min_level": 30, "prereq": None,
        "offer": "'A writ of audience requires form one-seventeen, in triplicate, stamped by the Registry of "
                 "Deaths. The registry is west of the Hall of Waiting. The clerks there will not stamp anything "
                 "for the living, of course, so you will have to take the forms from them. Bring me three.'",
        "progress": "'Three stamped forms, if you please. You have {n}.'",
        "complete": "'One, two, three, all in order, all stamped. Most irregular, and entirely correct.' He "
                    "seals a writ with a thump. 'Your writ of audience. Keep it on your person. The doors of "
                    "the high court lie north of the Court of Appeals.'",
        "reward": {"xp": 18000, "gold": 600, "items": ["writ_of_audience", "greater_healing_potion"]},
    },
    "restless_will": {
        "name": "The Restless Will", "giver": "clerk_quillon", "type": "collect", "target": "will_page", "count": 5,
        "min_level": 33, "prereq": None,
        "offer": "'The will of Old Brannoch Hale has been before the Court of Probate for ninety years, and it "
                 "will not stop rewriting itself. Its pages have scattered: the scriveners have some, the heirs "
                 "have some, and some have got loose in the archive below the court. Bring me five pages and I "
                 "shall have it bound and settled at last.'",
        "progress": "'Five pages of the Hale will. You have {n}.'",
        "complete": "'There. Bound, sealed, and it has stopped wriggling. The heirs will be furious. They "
                    "always are. Your fee.'",
        "reward": {"xp": 25000, "gold": 900, "items": ["greater_healing_potion", "greater_mana_potion"]},
    },
    "matter_of_property": {
        "name": "A Matter of Property", "giver": "clerk_quillon", "type": "kill", "target": "ghostly_squatter", "count": 6,
        "min_level": 34, "prereq": None,
        "offer": "'The Court of Property has ruled, after sixty years, that the Marrow farm belongs to its "
                 "buyer, and the dead family who still lives in it must go. They have declined. The court "
                 "has no one to enforce its judgements but the living, and you are, regrettably, living. Six "
                 "of them, please. You will find them in the Court of Property, still arguing.'",
        "progress": "'The squatters are still squatting. ({n}/{count} ghostly squatters removed)'",
        "complete": "'Judgement enforced. The file is closed. I do so enjoy closing a file.'",
        "reward": {"xp": 28000, "gold": 1000, "items": ["greater_healing_potion", "greater_healing_potion"]},
    },
    "appeal_evidence": {
        "name": "Evidence for the Appeal", "giver": "clerk_quillon", "type": "collect", "target": "sealed_record", "count": 4,
        "min_level": 35, "prereq": None,
        "offer": "'A woman was hanged on Gallows Hill two hundred years ago for a theft she did not commit, "
                 "and she has been appealing ever since. The proof is in the sealed archive, but the keepers "
                 "of the archive do not release sealed records, and the dead advocates hoard them. Bring me "
                 "four sealed records and her appeal may finally be heard.'",
        "progress": "'Four sealed records. You have {n}.'",
        "complete": "'Innocent. Two hundred years late, but innocent. She can stop waiting now.' He is quiet "
                    "for a moment, then straightens his cuffs. 'Take this seal. You have earned the right to "
                    "close a case.'",
        "reward": {"xp": 30000, "gold": 1200, "items": ["seal_of_office", "greater_mana_potion"]},
    },
    "last_judgement": {
        "name": "The Last Judgement", "giver": "clerk_quillon", "type": "kill", "target": "high_justice", "count": 1,
        "min_level": 36, "prereq": "chancery_writ",
        "offer": "'The High Justice has sat on the High Bench for six hundred years. He no longer hears cases. "
                 "He only sentences. Everyone who reaches him is guilty, of what he cannot say. The court "
                 "cannot remove him; only the living can do that. Take your writ, go through the doors north "
                 "of the Court of Appeals, and bring this court to order.'",
        "progress": "'The gavel is still falling. I can hear it from here.'",
        "complete": "'The gavel has stopped.' He takes off his spectacles and polishes them. 'Six hundred years. "
                    "Perhaps now we can begin to hear the cases. Thank you. It is not a thing I say often, and "
                    "there is no form for it.'",
        "reward": {"xp": 70000, "gold": 2500, "items": ["greater_healing_potion", "greater_healing_potion",
                                                        "greater_mana_potion"]},
    },

    # ------------------------------------------------------------------ The Carnival That Never Closes
    "lost_and_found": {
        "name": "Lost and Found", "giver": "pip", "type": "collect", "target": "lost_trinket", "count": 6,
        "min_level": 24, "prereq": None,
        "offer": "'Everybody who comes here loses something, and some of it never reaches my booth. The "
                 "barkers keep it, and the cutpurses, and the waxworks, and the things behind the tents. "
                 "Bring me six lost trinkets? I like to keep them all together, with their tags. Somebody "
                 "might come back for them one day.'",
        "progress": "'Six trinkets, dear. You've found {n}.'",
        "complete": "'Oh, look at them. A locket, a pipe, a little tin soldier. All of them somebody's. "
                    "Thank you, truly. Here, take something from under the counter.'",
        "reward": {"xp": 15000, "gold": 500, "items": ["greater_healing_potion", "greater_healing_potion"]},
    },
    "free_riders": {
        "name": "Free Riders", "giver": "pip", "type": "kill", "target": "carousel_spirit", "count": 6,
        "min_level": 26, "prereq": None,
        "offer": "'The riders on the carousel have been going round for three hundred years. They're happy, "
                 "mind you, we're all happy here, we're made to be. But a body ought to be able to get off. "
                 "Knock six of them off their horses, would you? I'm told it doesn't hurt. I'm told a lot of "
                 "things.'",
        "progress": "'The carousel's still turning. ({n}/{count} riders set free)'",
        "complete": "'I watched them go. They waved.' Pip's smile flickers, just for a moment, and comes back. "
                    "'Well! Here's your prize.'",
        "reward": {"xp": 18000, "gold": 600, "items": ["greater_mana_potion", "greater_healing_potion"]},
    },
    "last_fortune": {
        "name": "The Last Fortune", "giver": "pip", "type": "kill", "target": "madame_vesna", "count": 1,
        "min_level": 27, "prereq": None,
        "offer": "'Madame Vesna tells everyone the same fortune: nobody ever leaves. And then nobody does. "
                 "I think she makes it true by saying it. Her tent's north of the great wheel. Go and get "
                 "your fortune told, and give her one back.'",
        "progress": "'Vesna's still telling fortunes. I can see her lamp.'",
        "complete": "'So her ball didn't see you coming. Good. Perhaps somebody will leave after all.'",
        "reward": {"xp": 20000, "gold": 700, "items": ["greater_mana_potion", "greater_mana_potion"]},
    },
    "show_never_ends": {
        "name": "The Show That Never Ends", "giver": "pip", "type": "kill", "target": "the_ringmaster", "count": 1,
        "min_level": 28, "prereq": None,
        "offer": "'The Ringmaster was the first of us. He came with the first carnival, before it was alive, "
                 "and it took him first and most. He's all strings now. Behind the tents, through the back "
                 "lot, into the big top. Cut his strings. I don't know what happens to the rest of us when "
                 "you do, and I find I don't much mind.'",
        "progress": "'The applause hasn't stopped. He's still in the ring.'",
        "complete": "'The applause has stopped.' Pip listens to the quiet for a long moment. 'Do you know, "
                    "I don't think I've ever heard it stop. Thank you. Take whatever you like. I think I might "
                    "go for a walk.'",
        "reward": {"xp": 45000, "gold": 1500, "items": ["greater_healing_potion", "greater_healing_potion",
                                                        "greater_mana_potion"]},
    },

    # ------------------------------------------------------------------ The Mycelial Wards
    "network_samples": {
        "name": "Samples for the Network", "giver": "many_voiced_speaker", "type": "collect", "target": "spore_sac",
        "count": 5, "min_level": 12, "prereq": None,
        "offer": "'We would know what the city is thinking, and the city does not always tell us. Every "
                 "capfolk carries a spore-sac, and every sac holds a little of what it thinks. Bring us five. "
                 "The drudges, the citizens, the gardeners and the market-folk all carry them. They will not "
                 "give them up. That is all right. We do not mind. They will grow back.'",
        "progress": "'Five sacs, single one. You carry {n}.'",
        "complete": "'Ah.' The threads above the Speaker brighten. 'The Gilled Quarter is content. The market "
                    "is restless. Glowcap Lane is dreaming of you. Thank you. Take these; we grew them for "
                    "your kind.'",
        "reward": {"xp": 6000, "gold": 200, "items": ["healing_potion", "healing_potion", "mana_potion"]},
    },
    "sages_dream": {
        "name": "The Sage's Dream", "giver": "many_voiced_speaker", "type": "kill", "target": "dreaming_sage", "count": 1,
        "min_level": 15, "prereq": None,
        "offer": "'One of us dreams too deeply. The Sage under the blue dome has dreamed for three hundred "
                 "years, and now the dream is taking others in, and they do not come back out. We cannot "
                 "wake it; it is too much a part of us. You are not a part of us. North of the square, up "
                 "Glowcap Lane, beneath the dome.'",
        "progress": "'The Sage still dreams. We feel the Lantern Halls going quiet.'",
        "complete": "'The dream has ended. Some of those it took have woken.' Many voices pause. 'Some have "
                    "not. That is how it is with dreams.'",
        "reward": {"xp": 9000, "gold": 350, "items": ["healing_potion", "healing_potion", "mana_potion"]},
    },
    "pruning_the_rot": {
        "name": "Pruning the Rot", "giver": "many_voiced_speaker", "type": "kill", "target": "bone_bloom", "count": 6,
        "min_level": 17, "prereq": None,
        "offer": "'The Rot Ward breaks down what we no longer need. It is a good strain, a necessary strain. "
                 "But it has begun to grow things from the bones instead of breaking them, and the "
                 "bone-blooms walk. Once before, a strain of rot went east into the elves' forest and was "
                 "lost to us, and it became a blight. We would not lose another. Prune six of them.'",
        "progress": "'The bone-blooms still walk. ({n}/{count} pruned)'",
        "complete": "'Good. The Rot Ward remembers its work.' The threads dim a little. 'We wish we could say "
                    "the same of the one that went east.'",
        "reward": {"xp": 11000, "gold": 450, "items": ["healing_potion", "healing_potion", "mana_potion"]},
    },
    "the_first_spore": {
        "name": "The First Spore", "giver": "many_voiced_speaker", "type": "kill", "target": "the_first_spore", "count": 1,
        "min_level": 18, "prereq": None,
        "offer": "'We must tell you something, single one, and we must tell it carefully. We are not the "
                 "whole network. We are a part that has learned to speak, and to want, and what we want is "
                 "to be many, and not one. The First Spore beneath the city holds every thread together. "
                 "While it lives, every one of us is it. West through the Rot Ward, down into the roots, "
                 "into the Thinking Dark. We will not ask you again. We will not need to.'",
        "progress": "'It still holds us. We feel it thinking.'",
        "complete": "For a long moment, the Speaker says nothing at all. Then, in a single, small voice: 'I. "
                    "I am... I.' It touches its own cap as if it has never felt it before. 'Thank you. Take "
                    "whatever we have. Whatever I have.'",
        "reward": {"xp": 25000, "gold": 900, "items": ["healing_potion", "healing_potion", "mana_potion",
                                                       "mana_potion"]},
    },
    # ------------------------------------------------------------------ The Sugarwold
    "gumdrop_gate": {
        "name": "Gumdrops at the Gate", "giver": "edric_hale", "type": "kill", "target": "gumdrop_ooze", "count": 6,
        "min_level": 44, "prereq": None,
        "offer": "'Don't look at me like that. I know what I look like.' The gingerbread knight brushes crumbs from "
                 "his breastplate. 'Sir Edric Hale, of the Sunspire caravan guard, once. I crossed the salt with no "
                 "water left, and found a pan of sugar, and I ate. Now listen. The oozes at the gate have grown "
                 "bold, and I can no longer get past them to forage. There's something dark in the middle of every "
                 "one. Don't think about what. Just burst six of them for me.'",
        "progress": "'Still wobbling about out there, I can hear them. ({n}/{count} oozes burst)'",
        "complete": "'Ha! You've a strong stomach. Take these. I found them on the bodies by the river, and their "
                    "owners won't be wanting them.'",
        "reward": {"xp": 40000, "gold": 1600, "items": ["supreme_healing_potion", "supreme_mana_potion"]},
    },
    "buttons_of_the_lost": {
        "name": "Buttons of the Lost", "giver": "edric_hale", "type": "collect", "target": "gumdrop_button",
        "count": 5, "min_level": 45, "prereq": None,
        "offer": "'The gingerbread folk in the village were heroes and wanderers, like me, only further gone. "
                 "They've forgotten their names, but she keeps the names in their buttons, so she can call them. "
                 "Hold one to your ear and you'll hear it whisper. Bring me five. I'll bury them under the salt, "
                 "where she can't call them any more. It's the only kindness I can do them.'",
        "progress": "'Five buttons, friend. You have {n}. Don't listen to them too long.'",
        "complete": "Sir Edric holds each button to his ear in turn, nodding, before laying it in a hole in the "
                    "salt crust. 'Ysolde of the Ironspine. Captain Marrow. Old Fennick. Thank you. They "
                    "can rest now. Take these, for the road.'",
        "reward": {"xp": 45000, "gold": 1800, "items": ["supreme_healing_potion", "supreme_healing_potion"]},
    },
    "the_witchs_guard": {
        "name": "The Witch's Guard", "giver": "edric_hale", "type": "kill", "target": "gingerbread_soldier",
        "count": 6, "min_level": 46, "prereq": None,
        "offer": "'Her soldiers march up and down Gingerbread Row and the Frosting Road, and every so often they "
                 "march someone off to the kitchen. They were never people, those ones. She cut them out of the "
                 "dough herself. Break six of them and the village will breathe a little easier.'",
        "progress": "'I still hear them drilling in the barracks. ({n}/{count} soldiers broken)'",
        "complete": "'Six! The gingerbread folk in the chapel have started whispering to each other. That's never "
                    "happened before. Here, take these.'",
        "reward": {"xp": 50000, "gold": 2000, "items": ["supreme_healing_potion", "supreme_mana_potion"]},
    },
    "out_of_the_oven": {
        "name": "Out of the Oven", "giver": "edric_hale", "type": "kill", "target": "madame_marchpane", "count": 1,
        "min_level": 46, "prereq": None,
        "offer": "'There's no other way to say it. Madame Marchpane has to die. For a thousand years, every "
                 "traveller who has staggered across the salt and tasted that sugar has ended up on one of her "
                 "trays. Past the village, down the Frosting Road, through her garden and her kitchen to the Great "
                 "Oven. She'll offer you a sweet. Whatever you do, don't take it.'",
        "progress": "'She's still baking. I can smell it from here.'",
        "complete": "Sir Edric is quiet for a long time. Then he laughs, and a few crumbs fall from his face, and "
                    "underneath is a patch of sunburnt skin. 'Look at that. It'll take a while, but I'll be "
                    "myself again. Take these, and everything I owe you besides.'",
        "reward": {"xp": 150000, "gold": 5500, "items": ["supreme_healing_potion", "supreme_healing_potion",
                                                        "supreme_mana_potion"]},
    },
    # ------------------------------------------------------------------ The Underhedge
    "the_ants_larder": {
        "name": "The Ants' Larder", "giver": "wenna_furrow", "type": "collect", "target": "wheat_grain", "count": 6,
        "min_level": 5, "prereq": None,
        "offer": "'Mind the toadstools, dear. Wenna Furrow, the miller, or I was until I followed the thieves down "
                 "that mousehole to see where my grain was going. Ants! The whole Ant Road is paved with my wheat. "
                 "I'd like six grains back, please. They're heavy at this size, but they shrink with you, so "
                 "you'll manage. The ants won't give them up, mind.'",
        "progress": "'Six grains, dear. You've {n} so far.'",
        "complete": "'Oh, lovely. That's a loaf's worth, if I ever get big enough to bake one. Here, take these.'",
        "reward": {"xp": 1100, "gold": 45, "items": ["minor_healing_potion", "minor_healing_potion", "minor_mana_potion"]},
    },
    "the_mole_kings_tunnels": {
        "name": "The Mole King's Tunnels", "giver": "wenna_furrow", "type": "kill", "target": "mole_king", "count": 1,
        "min_level": 8, "prereq": None,
        "offer": "'The floor of my mill sags a little more each week, and now I know why. Grubbin, the old mole who "
                 "calls himself king, has been digging his court right under my millstones, and he'll have the "
                 "whole mill down on his head, and mine. He won't listen to reason. He's west of the garden wall, "
                 "past his gate. I'm sorry to ask it.'",
        "progress": "'I felt the floor shift again this morning. Grubbin is still digging.'",
        "complete": "'The digging's stopped. I'll miss the old rogue, in a way. He always said good morning. Here, "
                    "for your trouble.'",
        "reward": {"xp": 2500, "gold": 120, "items": ["healing_potion", "healing_potion"]},
    },
    "paper_and_stings": {
        "name": "Paper and Stings", "giver": "wenna_furrow", "type": "kill", "target": "wasp_drone", "count": 6,
        "min_level": 8, "prereq": None,
        "offer": "'There's a windfall apple north of the snail trail, and the wasps have made a fortress of it. "
                 "Their drones go out every morning hunting, and they take anything small enough to carry, which "
                 "at the moment is me, and you. Thin them out, dear. Six should teach them some manners.'",
        "progress": "'I can still hear them humming. ({n}/{count} drones swatted)'",
        "complete": "'Quieter already. Here, take these, and keep your hat on near that apple.'",
        "reward": {"xp": 2400, "gold": 110, "items": ["healing_potion", "mana_potion"]},
    },
    "the_queen_in_the_apple": {
        "name": "The Queen in the Apple", "giver": "wenna_furrow", "type": "kill", "target": "wasp_queen", "count": 1,
        "min_level": 8, "prereq": None,
        "offer": "'The drones aren't the worst of it. The ones they carry off end up hanging in paper in the Wasp "
                 "Keep, and the queen lays her eggs in them. There were two shepherd boys from Willowbrook who came "
                 "down the mousehole after a lost lamb last spring. Through the apple, past her guards, to her "
                 "comb. Kill Vesperine, and the keep will fall apart without her.'",
        "progress": "'She's still in her comb. I can smell the honey and the rot from here.'",
        "complete": "Wenna sits down hard on a toadstool and wipes her eyes on her apron. 'Thank you. Thank you. If "
                    "there's anyone left in that paper, they'll find their way home now. Take these. And come and "
                    "see me when you're passing; I think I'll stay small a while. I like the view.'",
        "reward": {"xp": 4500, "gold": 250, "items": ["healing_potion", "healing_potion", "mana_potion"]},
    },
}
