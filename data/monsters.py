"""Monster templates.

aggro: attacks on sight. Kept rare, in the Aardwolf tradition: only undead, demons, elementals,
guards, cultists and bosses are aggressive. Animals and roaming humanoids only fight when attacked,
one at a time.

Base statistics are derived from level in world.MonsterInstance; the per-monster
multipliers (hp, dmg, armor, xp, gold) adjust that baseline.

specials: special attacks used with `chance` each round instead of a basic attack.
  big    - a heavy blow dealing `mult` x normal damage
  dot    - damage-over-time on the player (`mult` x normal damage per round for `turns`)
  stun   - stuns the player for `turns` rounds
  drain  - damage that heals the monster
  heal   - heals the monster for `mult` x its max hp
"""

MONSTERS = {}


def M(mid, name, level, desc, hp=1.0, dmg=1.0, armor=1.0, aggro=False, specials=None,
      loot=None, xp=1.0, gold=1.0, boss=False, element="physical"):
    MONSTERS[mid] = {
        "id": mid, "name": name, "level": level, "desc": desc, "hp": hp, "dmg": dmg,
        "armor": armor, "aggro": aggro, "specials": specials or [], "loot": loot or [],
        "xp": xp, "gold": gold, "boss": boss, "element": element,
    }


def big(name, chance, mult, msg):
    return {"type": "big", "name": name, "chance": chance, "mult": mult, "msg": msg}


def dot(name, chance, mult, turns, element, msg):
    return {"type": "dot", "name": name, "chance": chance, "mult": mult, "turns": turns,
            "element": element, "msg": msg}


def drain(name, chance, mult, msg):
    return {"type": "drain", "name": name, "chance": chance, "mult": mult, "msg": msg}


def heal(name, chance, mult, msg):
    return {"type": "heal", "name": name, "chance": chance, "mult": mult, "msg": msg}


# ------------------------------------------------------------- Cellar & Meadow (1-5)
M("giant_rat", "a giant rat", 1, "A rat the size of a small dog, with yellow teeth and a hairless tail.",
  hp=0.6, dmg=0.7, loot=[("rat_tail", 0.5)], gold=0.3)
M("cellar_spider", "a bloated cellar spider", 2, "A pale, bloated spider that drops from the rafters.",
  hp=0.7, dmg=0.8, specials=[dot("Venomous Bite", 0.2, 0.3, 3, "poison", "sinks its fangs into you!")],
  loot=[("spider_silk", 0.3)], gold=0.3)
M("field_snake", "a field adder", 2, "A brown-and-gold adder coiled in the tall grass.",
  hp=0.7, dmg=0.8, specials=[dot("Venom", 0.25, 0.3, 3, "poison", "strikes, and venom burns in your veins!")])
M("wild_boar", "a wild boar", 3, "A bristling boar with wicked curved tusks and a foul temper.",
  hp=1.0, dmg=0.9, specials=[big("Gore", 0.2, 1.6, "lowers its head and gores you!")], gold=0.2)
M("kobold_scavenger", "a kobold scavenger", 3, "A yapping, dog-faced kobold clutching a rusty knife.",
  hp=0.9, dmg=0.9, loot=[("leather_gloves", 0.08), ("leather_leggings", 0.08)], gold=1.2)
M("kobold_trapper", "a kobold trapper", 4, "A wiry kobold draped in snares and smelling of wet dog.",
  hp=0.9, dmg=1.0, specials=[big("Net Toss", 0.15, 1.6, "hurls a weighted net over you!")],
  loot=[("leather_jerkin", 0.08), ("iron_buckler", 0.06)], gold=1.3)

# ------------------------------------------------------------- Whispering Woods (4-10)
M("grey_wolf", "a grey wolf", 4, "A lean grey wolf with hungry amber eyes.",
  hp=0.9, dmg=1.0, loot=[("wolf_pelt", 0.65)], gold=0.2)
M("giant_spider", "a giant forest spider", 5, "A hairy black spider as large as a pony, its fangs dripping.",
  hp=1.0, dmg=1.0, specials=[dot("Venomous Bite", 0.25, 0.35, 3, "poison", "sinks its dripping fangs into you!")],
  loot=[("spider_silk", 0.6)], gold=0.3)
M("dire_wolf", "a dire wolf", 7, "A massive black wolf, its shoulders as high as a man's chest.",
  hp=1.1, dmg=1.1, specials=[big("Savage Maul", 0.2, 1.7, "seizes you in its jaws and shakes you savagely!")],
  loot=[("wolf_pelt", 0.5), ("wolfhide_boots", 0.06)], gold=0.3)
M("brown_bear", "a brown bear", 9, "A big shaggy bear with a scarred muzzle, standing up on its hind legs to get a better look at you.",
  hp=1.4, dmg=1.05, specials=[big("Bear Hug", 0.2, 1.7, "seizes you in a crushing bear hug!")], gold=0.2, xp=1.2)
M("bandit_scout", "a bandit scout", 6, "A hooded bandit with a short bow and a shifty gaze.",
  hp=0.9, dmg=1.0, loot=[("steel_dagger", 0.06), ("wolfhide_boots", 0.06), ("studded_gloves", 0.06)], gold=1.5)
M("bandit_cutthroat", "a bandit cutthroat", 8, "A scarred brigand in mismatched leathers, twin knives in hand.",
  hp=1.0, dmg=1.1, specials=[dot("Bleeding Cut", 0.2, 0.35, 3, "bleed", "opens a deep, bleeding gash across your arm!")],
  loot=[("iron_longsword", 0.05), ("iron_helm", 0.05), ("chain_shirt", 0.04)], gold=1.6)
M("bandit_archer", "a bandit archer", 8, "A bandit perched behind a barricade, arrow nocked.",
  hp=0.9, dmg=1.15, aggro=True, loot=[("yew_longbow", 0.06), ("iron_helm", 0.05)], gold=1.6)
M("bandit_chieftain", "Rask the Bandit Chieftain", 10,
  "A towering, one-eyed brute in a stolen noble's coat, his cutlass dark with old blood.",
  hp=2.4, dmg=1.15, armor=1.3, aggro=True, boss=True, xp=2.0, gold=4.0,
  specials=[big("Brutal Slash", 0.25, 1.8, "swings his cutlass in a brutal, two-handed slash!"),
            big("Pommel Strike", 0.12, 1.6, "cracks you across the skull with his pommel!")],
  loot=[("bandit_cutlass", 1.0), ("chain_shirt", 0.5), ("ring_of_vigor", 0.4)])

# ------------------------------------------------------------- The Underhedge (5-10)
# The hedgerow behind the Willow Mill, seen at the size of a mouse. Its creatures go about their business;
# only the soldier ants, the mole guards and the wasps attack on sight.
M("garden_ant", "a garden ant", 5, "A red-brown ant as big as a dog, hurrying along with a crumb held high in its jaws.",
  hp=0.9, dmg=0.95, loot=[("wheat_grain", 0.35), ("honeydew", 0.3)], gold=0.2)
M("water_beetle", "a water beetle", 5, "A glossy black beetle the size of a rowing boat, its legs fringed like oars.",
  hp=1.0, dmg=0.95, armor=1.5, loot=[("beetle_chitin", 0.4), ("acorn_helm", 0.05)], gold=0.2)
M("pond_frog", "a pond frog", 6, "A mottled green frog as big as a house, with golden eyes and a throat that pulses slowly.",
  hp=1.2, dmg=1.0, specials=[big("Tongue Lash", 0.15, 1.6, "lashes out its tongue, snatches you up and spits you out, dazed!")],
  loot=[("petal_slippers", 0.05), ("minor_healing_potion", 0.08)], gold=0.2)
M("soldier_ant", "a soldier ant", 7, "A big-headed ant with jaws like curved swords, guarding the road and the grain that rolls along it.",
  hp=1.0, dmg=1.1, armor=1.4, aggro=True, specials=[big("Mandible Crush", 0.2, 1.7, "seizes you in its great jaws and squeezes!")],
  loot=[("wheat_grain", 0.5), ("beetleshell_jerkin", 0.04), ("acorn_helm", 0.04)], gold=0.4)
M("garden_snail", "a garden snail", 7, "A snail the size of a cottage, its striped shell rising like a spiral tower, leaving a road of slime.",
  hp=1.5, dmg=0.85, armor=2.0, specials=[dot("Corrosive Slime", 0.2, 0.3, 3, "poison", "rears up and slimes you, and your skin burns!")],
  loot=[("snailskin_leggings", 0.06)], gold=0.2, xp=1.2)
M("mouse_knight", "a mouse knight", 8, "A grey mouse in a walnut-shell helm and armour of beetle shell, with a darning needle for a lance.",
  hp=1.0, dmg=1.1, specials=[big("Needle Lance", 0.2, 1.7, "levels its darning needle and charges!")],
  loot=[("needle_sword", 0.06), ("beetleshell_shield", 0.05), ("minor_healing_potion", 0.1)], gold=1.4)
M("stag_beetle", "a stag beetle", 8, "A huge beetle with antlers like a stag's, saddled with thread and bridled for the mouse cavalry.",
  hp=1.4, dmg=1.05, armor=1.6, specials=[big("Antler Toss", 0.2, 1.7, "catches you in its antlers and flings you through the grass!")],
  loot=[("beetleshell_jerkin", 0.06), ("beetle_chitin", 0.5)], gold=0.3, xp=1.3)
M("mole_digger", "a mole digger", 8, "A velvet-black mole in a leather apron, with spade-like hands and tiny squinting eyes.",
  hp=1.2, dmg=1.0, loot=[("dandelion_trousers", 0.05), ("hawthorn_wand", 0.04)], gold=1.0)
M("mole_guard", "a mole guard", 9, "A burly mole in a coat of overlapping beetle shell, gripping a pick and sniffing the air.",
  hp=1.1, dmg=1.1, armor=1.4, aggro=True, specials=[big("Pick Haft", 0.12, 1.6, "cracks you across the head with the haft of its pick!")],
  loot=[("mole_claw_gloves", 0.03), ("healing_potion", 0.08)], gold=1.4)
M("mole_king", "Grubbin, the Mole King", 9, "A fat old mole in a crown of bottle-tin and a cloak of sewn-together moth wings, lord of every tunnel under the hedge.",
  hp=1.7, dmg=1.1, armor=1.2, xp=1.6, gold=3.0,
  specials=[big("Royal Burrow", 0.2, 1.8, "dives into the floor and bursts up beneath your feet!"),
            heal("A Royal Snack", 0.1, 0.12, "pulls a worm from the wall and gulps it down, looking much refreshed!")],
  loot=[("mole_claw_gloves", 0.25), ("hawthorn_wand", 0.2)])
M("garden_cat", "Old Tom, the gardener's cat", 9, "A grey tomcat as big as a church, with a torn ear and green eyes like lanterns. He has not yet decided whether you are worth the bother.",
  hp=1.75, dmg=1.12, xp=1.6, gold=0.1,
  specials=[big("Pounce", 0.22, 1.9, "crouches, wiggles, and pounces on you!"),
            big("Pinned", 0.1, 1.6, "pins you under one enormous paw!")],
  loot=[("whisker_bow", 0.25)])
M("wasp_drone", "a wasp drone", 9, "A striped wasp as big as a hound, its wings a blur and its sting dripping.",
  hp=0.9, dmg=1.1, armor=0.6, aggro=True, specials=[dot("Sting", 0.22, 0.35, 3, "poison", "darts in and stings you!")],
  loot=[("wasp_sting_dagger", 0.05), ("thistledown_robe", 0.04)], gold=0.6)
M("wasp_guard", "a wasp guard", 10, "A heavy wasp of the queen's guard, with a sting as long as a spear and armour-hard stripes.",
  hp=1.2, dmg=1.15, armor=1.3, aggro=True, specials=[dot("Spear Sting", 0.2, 0.35, 3, "poison", "drives its sting into you like a spear!"),
                                                     big("Paralysing Venom", 0.1, 1.6, "stings you, and your limbs go numb!")],
  loot=[("wasp_sting_dagger", 0.06), ("healing_potion", 0.1)], gold=0.8)
M("wasp_queen", "Vesperine, the Wasp Queen", 10,
  "The queen of the Wasp Keep, longer than a horse, her striped body swollen and her wings humming like a storm. "
  "Her great black eyes see everything in the apple.",
  hp=2.4, dmg=1.15, armor=1.3, aggro=True, boss=True, xp=2.0, gold=4.0,
  specials=[dot("Royal Sting", 0.2, 0.4, 4, "poison", "curls her body and drives her great sting into you!"),
            big("Paralysing Venom", 0.12, 1.6, "stings you, and you cannot move a muscle!"),
            heal("Royal Jelly", 0.1, 0.12, "feeds from the comb, and her wounds close!")],
  loot=[("queens_stinger", 0.6), ("amber_pendant", 0.6), ("thistledown_robe", 0.4)])

# ------------------------------------------------------------- Westmarch (3-10)
M("goblin_sneak", "a goblin sneak", 5, "A skinny green goblin with a sack over one shoulder and someone else's chicken in it.",
  hp=0.9, dmg=1.0, specials=[dot("Dirty Knife", 0.15, 0.3, 3, "bleed", "darts in and nicks you with a filthy knife!")],
  loot=[("leather_gloves", 0.06), ("wolfhide_boots", 0.05), ("minor_healing_potion", 0.1)], gold=1.4)
M("hill_goblin", "a hill goblin", 7, "A goblin in a dented pot helm, waving a quarry pick with more enthusiasm than skill.",
  hp=1.0, dmg=1.05, loot=[("iron_buckler", 0.06), ("studded_gloves", 0.06), ("iron_helm", 0.04)], gold=1.5)
M("goblin_shaman", "a goblin shaman", 8, "A wizened goblin in a cloak of crow feathers, muttering to a rattle made from a skull.",
  hp=0.9, dmg=1.05, specials=[heal("Grubby Mending", 0.15, 0.2, "smears something green on its cuts, and they close!"),
                              dot("Crow Curse", 0.15, 0.3, 3, "shadow", "shakes its rattle at you and screeches a curse!")],
  loot=[("wand_of_sparks", 0.05), ("minor_mana_potion", 0.2)], gold=1.6)
M("goblin_brute", "a goblin brute", 9, "A goblin half again as big as its kin, all knotted muscle and a club studded with nails.",
  hp=1.3, dmg=1.1, specials=[big("Nail-Club Swing", 0.2, 1.7, "swings its nail-studded club into your ribs!")],
  loot=[("chain_shirt", 0.04), ("iron_longsword", 0.05)], gold=1.6, xp=1.2)

# ------------------------------------------------------------- Dustway (8-15)
M("dust_hyena", "a dust hyena", 9, "A mangy spotted hyena that giggles horribly as it circles you.",
  hp=1.0, dmg=1.05, specials=[dot("Ragged Bite", 0.2, 0.3, 3, "bleed", "darts in and tears a ragged bite from your leg!")],
  loot=[("hyena_hide", 0.5)], gold=0.2)
M("highwayman", "a highwayman", 10, "A masked rider in a long coat, with a crossbow across his saddle and a cudgel at his belt.",
  hp=1.0, dmg=1.1, specials=[big("Cudgel Blow", 0.12, 1.6, "clubs you behind the ear!")],
  loot=[("chain_leggings", 0.05), ("iron_longsword", 0.05), ("healing_potion", 0.1)], gold=2.0)
M("gnoll_scavenger", "a gnoll scavenger", 12, "A hunched, hyena-headed gnoll in rags, gnawing on something it would rather you did not see.",
  hp=1.1, dmg=1.05, loot=[("hyena_hide", 0.3), ("iron_boots", 0.05)], gold=1.2)
M("gnoll_raider", "a gnoll raider", 14, "A tall gnoll in a patchwork of stolen armour, howling as it swings a notched axe.",
  hp=1.1, dmg=1.15, specials=[big("Rending Axe", 0.2, 1.7, "howls and brings its notched axe down on you!")],
  loot=[("dwarven_war_axe", 0.04), ("knights_blade", 0.03)], gold=1.6)

# ------------------------------------------------------------- Barrowfield & Crypt (9-17)
M("restless_zombie", "a restless zombie", 9, "A shambling corpse in a rotted burial shroud, moaning softly.",
  hp=1.2, dmg=0.95, aggro=True, specials=[dot("Grave Rot", 0.2, 0.3, 4, "disease", "claws you with filthy, rotting nails!")],
  loot=[("bone_dust", 0.3)], gold=0.8)
M("carrion_ghoul", "a carrion ghoul", 10, "A grey-skinned ghoul crouched over an opened grave, its claws long and black.",
  hp=1.0, dmg=1.1, specials=[big("Paralysing Claw", 0.15, 1.6, "rakes you with paralysing claws!")],
  loot=[("bone_dust", 0.4), ("chain_leggings", 0.05)], gold=1.0)
M("crypt_bat", "a swarm of crypt bats", 11, "A shrieking cloud of red-eyed bats.",
  hp=0.7, dmg=0.9, gold=0.2)
M("skeleton_warrior", "a skeleton warrior", 12, "A skeleton in corroded mail, still clutching its ancient sword.",
  hp=1.1, dmg=1.05, armor=1.5, aggro=True, loot=[("bone_dust", 0.4), ("iron_boots", 0.05), ("bonecleaver", 0.04)], gold=1.0)
M("bone_guardian", "a bone guardian", 13, "A hulking construct of fused skeletons that guards the deeper halls.",
  hp=1.5, dmg=1.1, armor=2.0, specials=[big("Crushing Blow", 0.2, 1.7, "brings its bone-fists down upon you!")],
  loot=[("bonecleaver", 0.1), ("bone_helm", 0.1), ("bone_dust", 0.5)], gold=1.2, xp=1.3)
M("wailing_spirit", "a wailing spirit", 14, "The translucent shade of a weeping woman, drifting just above the floor.",
  hp=0.9, dmg=1.1, armor=0.5, aggro=True, specials=[drain("Life Drain", 0.25, 1.0, "passes through you, and your life drains away!")],
  loot=[("grave_shroud", 0.05)], gold=0.8)
M("crypt_cultist", "a cultist of Varnoth", 14, "A gaunt man in black robes, his face painted like a skull.",
  hp=1.0, dmg=1.05, aggro=True, specials=[heal("Dark Mending", 0.15, 0.25, "chants, and dark energy mends his wounds."),
                                          dot("Curse of Decay", 0.15, 0.35, 3, "shadow", "points at you and hisses a curse of decay!")],
  loot=[("grave_shroud", 0.08), ("healing_potion", 0.2)], gold=1.8)
M("varnoth", "Varnoth the Bone King", 17,
  "A towering lich-lord in a crown of rusted iron, green witchfire burning in his empty eye sockets.",
  hp=2.3, dmg=1.15, armor=1.6, aggro=True, boss=True, xp=2.0, gold=5.0,
  specials=[drain("Soul Rend", 0.2, 1.0, "tears at your very soul with a skeletal hand!"),
            dot("Grave Curse", 0.15, 0.4, 4, "shadow", "curses you with the chill of the grave!"),
            heal("Phylactery Pulse", 0.08, 0.15, "draws power from his hidden phylactery and his bones knit together!")],
  loot=[("varnoth_scepter", 0.6), ("grave_shroud", 0.5), ("bone_helm", 0.5), ("knights_blade", 0.4)])

# ------------------------------------------------------------- Mirefen (15-22)
M("bog_lurker", "a bog lurker", 15, "A scaly green thing that rises dripping from the black water.",
  hp=1.1, dmg=1.05, loot=[("mirescale_vest", 0.04), ("bog_pearl", 0.15)], gold=0.5)
M("lizardman_warrior", "a lizardman warrior", 16, "A hissing lizardman with a bone-tipped spear and a shield of turtle shell.",
  hp=1.1, dmg=1.1, armor=1.4, loot=[("steel_kite_shield", 0.05), ("bog_pearl", 0.15)], gold=1.4)
M("swamp_troll", "a swamp troll", 17, "A hulking, moss-covered troll whose wounds close as you watch.",
  hp=1.5, dmg=1.15, specials=[heal("Regenerate", 0.15, 0.15, "regenerates, its wounds bubbling closed!")],
  loot=[("plate_gauntlets", 0.05), ("bog_pearl", 0.2)], gold=1.3, xp=1.3)
M("will_o_wisp", "a will-o'-the-wisp", 18, "A drifting, flickering ball of pale light that hums an eerie tune.",
  hp=0.7, dmg=1.2, armor=0.3, specials=[big("Bewitching Glow", 0.2, 1.6, "flares brightly, and you stand transfixed!")],
  loot=[("bog_pearl", 0.3), ("mana_potion", 0.2)], gold=0.6)
M("lizardman_shaman", "a lizardman shaman", 18, "A lizardman hung with shells and dried frogs, rattling a staff topped with a heron's skull.",
  hp=1.0, dmg=1.1, specials=[heal("Swamp Blessing", 0.15, 0.2, "croaks a prayer to the swamp, and its wounds close!"),
                             dot("Spit Venom", 0.2, 0.35, 3, "poison", "spits a stream of burning venom into your eyes!")],
  loot=[("bog_pearl", 0.25), ("bogwood_staff", 0.04), ("mana_potion", 0.15)], gold=1.4)
M("mire_serpent", "a mire serpent", 19, "A huge olive-green serpent, thick as a tree trunk, sliding through the reeds.",
  hp=1.3, dmg=1.15, specials=[dot("Venomous Fangs", 0.25, 0.4, 4, "poison", "strikes like lightning, venom searing through you!")],
  loot=[("serpentfang", 0.06), ("bogwood_staff", 0.05)], gold=0.8)
M("giant_leech", "a giant leech", 20, "A glistening black leech as long as a rowing boat, its round mouth ringed with teeth.",
  hp=1.3, dmg=1.05, armor=0.6, specials=[drain("Bloodsuck", 0.25, 1.0, "fastens onto you and drinks deep!")],
  loot=[("bog_pearl", 0.2)], gold=0.3)
M("fen_crocodile", "a fen crocodile", 21, "A crocodile longer than a cart, its back crusted with moss so that it looks like a log.",
  hp=1.4, dmg=1.2, armor=1.4, specials=[big("Death Roll", 0.2, 1.8, "clamps its jaws on you and rolls, dragging you under!"),
                                        big("Tail Lash", 0.1, 1.6, "knocks you sprawling with a lash of its tail!")],
  loot=[("mirescale_vest", 0.04), ("bog_pearl", 0.2)], gold=0.5, xp=1.3)
M("bog_hag", "Old Mother Gristle", 22,
  "A hunched, warty crone in a shawl of rotting moss, her eyes like lanterns and her teeth like needles.",
  hp=2.6, dmg=1.2, armor=1.3, aggro=True, boss=True, xp=2.0, gold=5.0,
  specials=[dot("Hex of Withering", 0.2, 0.45, 4, "shadow", "cackles and hurls a hex of withering at you!"),
            big("Evil Eye", 0.12, 1.6, "fixes you with her evil eye, and your limbs lock!"),
            heal("Drink from the Cauldron", 0.1, 0.12, "slurps from a ladle of bubbling broth and cackles with renewed vigour!")],
  loot=[("gristles_hexrod", 0.6), ("hag_charm", 0.6), ("mirescale_vest", 0.4), ("bogwood_staff", 0.4)])

# ------------------------------------------------------------- Rimefells (10-20)
M("snow_wolf", "a snow wolf", 10, "A rangy grey-white wolf, almost invisible against the drifts until it moves.",
  hp=1.0, dmg=1.05, loot=[("wolf_pelt", 0.3)], gold=0.3)
M("frost_goblin", "a frost goblin", 12, "A blue-lipped goblin bundled in stolen furs, with icicles in its scraggly beard.",
  hp=1.0, dmg=1.1, specials=[dot("Frozen Spear", 0.15, 0.3, 3, "frost", "jabs you with a spear tipped in black ice!")],
  loot=[("dwarven_chainmail", 0.03), ("iron_boots", 0.05), ("healing_potion", 0.1)], gold=1.5)
M("ice_spider", "an ice spider", 14, "A spider of glassy blue chitin that spins webs of frozen silk across the cave mouths.",
  hp=1.0, dmg=1.1, specials=[dot("Frost Venom", 0.2, 0.35, 3, "frost", "bites you, and cold spreads through your veins!")],
  loot=[("spider_silk", 0.5), ("runestone_ring", 0.03)], gold=0.4)
M("yeti", "a yeti", 16, "A great shaggy ape-beast with white fur and a blue-black face, beating its chest as it rises.",
  hp=1.5, dmg=1.15, specials=[big("Avalanche Slam", 0.2, 1.8, "raises both fists and brings them down like an avalanche!")],
  loot=[("yeti_fur", 0.6), ("dwarven_helm", 0.04)], gold=0.6, xp=1.3)
M("frost_wisp", "a frost wisp", 17, "A drifting mote of blue-white cold, ringed by a halo of whirling snowflakes.",
  hp=0.8, dmg=1.15, armor=0.4, aggro=True, specials=[big("Flash Freeze", 0.15, 1.6, "flares, and ice locks your limbs in place!")],
  loot=[("frost_shard", 0.1), ("mana_potion", 0.2)], gold=0.6)
M("snow_troll", "a snow troll", 19, "A towering troll with a mane of frozen hair, gnawing on the leg of something it caught.",
  hp=1.5, dmg=1.15, specials=[heal("Regenerate", 0.15, 0.15, "regenerates, frost knitting its wounds shut!")],
  loot=[("dwarven_greaves", 0.04), ("yeti_fur", 0.2)], gold=1.2, xp=1.3)

# ------------------------------------------------------------- The Mycelial Wards (12-20)
# The capfolk share a partial hive mind and mostly ignore the living. Only the spore wardens, the
# bone-blooms of the Rot Ward and the thought-spores of the deep network attack on sight.
M("myconid_drudge", "a myconid drudge", 12, "A squat, shuffling capfolk labourer with a cap like a dinner plate, hauling baskets of moss.",
  hp=1.1, dmg=1.05, specials=[dot("Spore Puff", 0.2, 0.3, 3, "poison", "puffs a cloud of choking spores into your face!")],
  loot=[("spore_sac", 0.3)], gold=0.6)
M("spore_warden", "a spore warden", 13, "A tall capfolk in armour of hardened shelf-fungus, with a club of the same, swaying in time with the other wardens.",
  hp=1.2, dmg=1.1, armor=1.6, aggro=True, specials=[big("Shelf Club", 0.2, 1.7, "swings a club of stone-hard fungus into you!")],
  loot=[("shelf_shield", 0.04), ("shelfcap_breastplate", 0.03)], gold=1.0)
M("capfolk_citizen", "a capfolk citizen", 13, "A pale, soft-footed citizen of the Wards with a gilled cap for a head, murmuring to its neighbours without moving its lips.",
  hp=1.0, dmg=1.05, specials=[big("Murmuring Chorus", 0.12, 1.6, "and every capfolk nearby murmur at once, and your thoughts scatter!")],
  loot=[("spore_sac", 0.3)], gold=0.8)
M("gill_tender", "a gill-tender", 14, "A stooped capfolk gardener who tends the moss in the doorways, with a hooked knife for trimming gills.",
  hp=1.1, dmg=1.1, specials=[big("Hooked Knife", 0.2, 1.7, "hooks you with its trimming knife!")],
  loot=[("spore_sac", 0.25), ("mossfelt_boots", 0.03)], gold=0.8)
M("puffball_hawker", "a puffball hawker", 14, "A round capfolk market-keeper, swollen like a puffball, who breathes out a glittering cloud when it is startled.",
  hp=1.0, dmg=1.1, specials=[big("Spore Cloud", 0.14, 1.6, "bursts in a glittering cloud, and you choke and stagger!")],
  loot=[("spore_sac", 0.35)], gold=1.0)
M("capfolk_porter", "a capfolk porter", 15, "A broad capfolk with a cap like a shield and shoulders made for hauling, carrying a load of woven root.",
  hp=1.4, dmg=1.1, xp=1.2, specials=[big("Shoulder Barge", 0.2, 1.7, "lowers its broad cap and barges you over!")],
  loot=[("mossfelt_boots", 0.04)], gold=0.8)
M("spore_drift", "a drift of spores", 15, "A slow, glittering cloud of spores that moves against the wind and gathers around anyone who stands still.",
  hp=0.7, dmg=1.15, armor=0.3, specials=[dot("Settling Spores", 0.22, 0.35, 3, "poison", "settles over you, and the spores take root in your lungs!")],
  gold=0.3)
M("glowcap_scholar", "a glowcap scholar", 16, "A slow, thoughtful capfolk whose cap glows soft blue. It speaks only as 'we', and has been considering you.",
  hp=0.9, dmg=1.15, specials=[big("Slow Thought", 0.14, 1.6, "shares a thought so slow and vast that you stop to follow it!"),
                              drain("Borrowed Memory", 0.15, 0.9, "touches your brow and reads a memory, and some of your life goes with it!")],
  loot=[("glowcap_pendant", 0.04), ("mana_potion", 0.1)], gold=1.0)
M("lantern_cap", "a lantern-cap", 16, "A capfolk lamplighter whose own cap burns with cold blue light, carrying a crook hung with glowing caps.",
  hp=1.0, dmg=1.15, specials=[dot("Cold Light", 0.2, 0.35, 3, "fire", "flares, and its cold light burns like frost!")],
  loot=[("glowcap_pendant", 0.03)], gold=0.8)
M("dreaming_sage", "the Dreaming Sage", 17, "An ancient capfolk grown into the floor of its dome, dreaming so deeply that the dream spills out and takes others in.",
  hp=1.7, dmg=1.15, xp=1.6, gold=2.0,
  specials=[big("Pulled Into the Dream", 0.14, 1.6, "dreams you into its dream, and for a while you cannot find your way out!"),
            drain("The Dream Feeds", 0.15, 1.0, "dreams of you, and grows stronger as you grow faint!")],
  loot=[("glowcap_pendant", 0.2), ("healing_potion", 0.3)])
M("rot_tender", "a rot-tender", 17, "A dark, glistening capfolk of the Rot Ward, polite, patient and hungry, with hands that leave black marks.",
  hp=1.3, dmg=1.15, specials=[dot("Rotting Touch", 0.2, 0.4, 3, "poison", "lays a black hand on you, and your skin begins to rot!")],
  loot=[("capshell_hauberk", 0.03)], gold=0.8)
M("compost_crawler", "a compost crawler", 18, "A long, pale crawling thing of the compost halls, many-legged and fungus-backed, that turns the heaps.",
  hp=1.5, dmg=1.15, xp=1.3, specials=[big("Rolling Crush", 0.2, 1.7, "rolls over you like a cartwheel of rot!")],
  loot=[("rootweave_chausses", 0.04)], gold=0.4)
M("bone_bloom", "a bone-bloom", 18, "A skeleton held upright by the fungus growing through it, white fans sprouting from its ribs and skull.",
  hp=1.2, dmg=1.15, armor=1.4, aggro=True, specials=[drain("Rooting", 0.2, 1.0, "drives threads of fungus into you and drinks!")],
  loot=[("sporethorn_knife", 0.03)], gold=0.8)
M("whispering_host", "a whispering host", 18, "A capfolk so deep in the network that it has forgotten it was ever separate. It speaks in a thousand voices.",
  hp=1.1, dmg=1.15, specials=[big("A Thousand Voices", 0.14, 1.6, "speaks with a thousand voices at once, and yours is drowned out!")],
  loot=[("glowcap_pendant", 0.03)], gold=0.8)
M("rot_renderer", "a rot-ward renderer", 19, "A huge, silent capfolk of the rendering pits with a hook for dragging things into the rot.",
  hp=1.4, dmg=1.2, xp=1.2, specials=[big("Rendering Hook", 0.22, 1.8, "drags you toward the pit with its great hook!")],
  loot=[("rootmaul", 0.04), ("sporethorn_knife", 0.03)], gold=1.0)
M("the_rotmother", "the Rotmother", 19, "A vast, motherly mound of rot that tends the ossuary beds, humming to the bones as they bloom.",
  hp=1.7, dmg=1.15, xp=1.6, gold=1.5,
  specials=[dot("Mother's Embrace", 0.2, 0.4, 4, "poison", "folds you into her soft, rotting bulk!"),
            heal("Fresh Mulch", 0.12, 0.12, "draws the rot of her beds into herself and swells!")],
  loot=[("capshell_hauberk", 0.2), ("healing_potion", 0.3)])
M("root_crawler", "a root-crawler", 19, "A pale, eyeless thing that crawls along the network's great threads like blood along a vein.",
  hp=1.5, dmg=1.2, xp=1.3, specials=[big("Lashing Thread", 0.2, 1.7, "lashes you with a thread as thick as a rope!"),
                                     big("Entangle", 0.1, 1.6, "wraps you in sticky threads!")],
  loot=[("rootmaul", 0.03)], gold=0.4)
M("thought_spore", "a thought-spore", 20, "A drifting, glowing spore the size of a head, carrying one of the network's thoughts. This one is about you.",
  hp=0.9, dmg=1.2, armor=0.5, aggro=True, specials=[drain("We Remember You", 0.22, 1.0, "settles on you and remembers you, and you feel yourself being forgotten!")],
  gold=0.6)
M("the_first_spore", "the First Spore", 20,
  "The oldest growth in the Wards, from which every thread and cap has grown: a vast mushroom whose cap is lost in the dark and whose gills "
  "glow with every colour of every ward. It does not hate you. It simply has a use for you.",
  hp=2.3, dmg=1.2, armor=1.6, aggro=True, boss=True, xp=2.0, gold=4.0,
  specials=[dot("Spore Storm", 0.18, 0.45, 4, "poison", "breathes out a storm of spores that take root in your flesh!"),
            drain("Absorption", 0.15, 1.1, "draws you into its threads and begins to digest you!"),
            big("The Chorus", 0.12, 1.6, "speaks with the voice of every capfolk in the Wards, and you cannot move!"),
            heal("Regrowth", 0.08, 0.1, "draws strength up from every thread in the city!")],
  loot=[("heartspore_staff", 0.5), ("mycelial_crown", 0.4), ("rootbound_ring", 0.5)])

# ------------------------------------------------------------- Deepdelve Mine (18-21)
M("rockgnasher", "a rockgnasher", 19, "A blind, armour-plated burrower the size of a pony, with a mouth full of grinding stone teeth.",
  hp=1.4, dmg=1.1, armor=1.8, specials=[big("Grinding Bite", 0.2, 1.7, "clamps you in a mouth full of grinding stone!")],
  loot=[("deep_crystal", 0.3), ("dwarven_boots", 0.04)], gold=0.6, xp=1.3)
M("deepkin_delver", "a deepkin delver", 20, "A dwarf who dug too deep, grey-skinned and hollow-eyed, still swinging a pick at whatever it is told.",
  hp=1.1, dmg=1.15, armor=1.4, aggro=True, specials=[big("Pick-Haft Blow", 0.12, 1.6, "cracks you across the head with the haft of its pick!")],
  loot=[("deep_crystal", 0.3), ("dwarven_greataxe", 0.04), ("dwarven_plate", 0.02)], gold=1.6)
M("crystal_golem", "a crystal golem", 21, "A hulking figure of cloudy crystal that grew rather than was built, glowing from within.",
  hp=1.8, dmg=1.15, armor=2.2, specials=[big("Shard Fist", 0.2, 1.8, "smashes you with a fist of jagged crystal!")],
  loot=[("deep_crystal", 0.6), ("rune_amulet", 0.04)], gold=1.0, xp=1.5)
M("ghaldrek", "Ghaldrek the Stonewake", 21,
  "A colossus of living granite that slept beneath the mountain since before the dwarves came. Veins of glowing crystal "
  "run through it like blood, and its voice is the grinding of the earth itself.",
  hp=2.5, dmg=1.2, armor=1.8, aggro=True, boss=True, xp=2.0, gold=5.0,
  specials=[big("Mountain's Weight", 0.25, 1.9, "brings a fist of solid granite down on you!"),
            big("Tremor", 0.12, 1.6, "stamps, and the cavern floor heaves beneath you!"),
            heal("Draw from the Deep", 0.08, 0.12, "sinks its feet into the stone and draws strength from the mountain!")],
  loot=[("stonewake_hammer", 0.6), ("deepheart_amulet", 0.6), ("dwarven_plate", 0.4), ("deep_crystal", 1.0)])

# ------------------------------------------------------------- Eldergrove (20-34)
M("thornback_boar", "a thornback boar", 20, "A boar as big as a cart horse, its bristles grown into a mane of woody thorns.",
  hp=1.2, dmg=1.1, specials=[big("Thorned Charge", 0.2, 1.7, "charges, driving its thorny back into you!")],
  loot=[("greater_healing_potion", 0.05)], gold=0.3)
M("centaur_outrider", "a centaur outrider", 22, "A wild centaur of the deep woods, painted with ochre and carrying a short bow and a long knife.",
  hp=1.1, dmg=1.15, specials=[dot("Barbed Arrow", 0.2, 0.35, 3, "bleed", "wheels and looses a barbed arrow into you!")],
  loot=[("hunters_recurve", 0.03), ("elven_saber", 0.02)], gold=1.4)
M("dusk_owl", "a dusk owl", 23, "An owl as big as a man, grey as dusk, that hunts on silent wings beneath the canopy.",
  hp=1.0, dmg=1.15, specials=[big("Silent Swoop", 0.12, 1.6, "drops out of nowhere and bowls you over!")], gold=0.3)
M("wood_troll", "a wood troll", 24, "A gangling green troll with bark-rough skin and moss in its hair, which heals as fast as you can cut it.",
  hp=1.5, dmg=1.15, specials=[heal("Regenerate", 0.15, 0.15, "regenerates, its bark-skin knitting together!")],
  loot=[("leafsteel_helm", 0.03), ("greater_healing_potion", 0.1)], gold=1.2, xp=1.3)
M("thorn_sprite", "a thorn sprite", 25, "A tiny, spiteful fey no bigger than your hand, with wings of thorn and a laugh like breaking twigs.",
  hp=0.7, dmg=1.2, armor=0.3, specials=[big("Bewildering Dust", 0.18, 1.6, "flings a pinch of glittering dust in your eyes!")],
  loot=[("greater_mana_potion", 0.15), ("moonweave_gloves", 0.03)], gold=0.8)
M("greatstag", "a greatstag", 26, "A white stag taller than a horse, with antlers like the branches of a winter oak.",
  hp=1.4, dmg=1.15, specials=[big("Antler Rake", 0.2, 1.7, "lowers its great antlers and rakes you!")],
  loot=[("stag_antler", 0.5)], gold=0.2, xp=1.2)
M("blighted_treant", "a blighted treant", 27, "A walking oak gone black and weeping with rot, its branches clutching like fingers.",
  hp=1.8, dmg=1.2, armor=1.6, specials=[dot("Rotting Grasp", 0.2, 0.4, 3, "nature", "wraps you in rotting, oozing branches!")],
  loot=[("blight_heartwood", 0.3), ("dawnwood_staff", 0.03)], gold=0.6, xp=1.5)
M("rotwood_druid", "a rotwood druid", 29, "A druid who has given himself to the blight, his skin grey and his beard grown through with fungus.",
  hp=1.1, dmg=1.2, aggro=True, specials=[heal("Fungal Mending", 0.15, 0.2, "breathes in a cloud of spores, and his wounds close!"),
                                         dot("Blight Curse", 0.2, 0.4, 3, "nature", "points a twisted staff at you, and rot spreads over your skin!")],
  loot=[("blight_heartwood", 0.2), ("moonweave_robe", 0.03), ("greater_mana_potion", 0.15)], gold=1.8)
M("blight_wolf", "a blight wolf", 31, "A wolf whose fur has fallen away in patches to show bark and fungus beneath, its eyes glowing sickly green.",
  hp=1.2, dmg=1.25, specials=[dot("Blighted Bite", 0.2, 0.4, 3, "nature", "sinks rotten teeth into you!")],
  loot=[("wardens_boots", 0.03)], gold=0.4)
M("gloom_dryad", "a gloom dryad", 33, "A dryad bound to a dying tree, beautiful and terrible, with eyes like holes into dark water.",
  hp=1.1, dmg=1.3, armor=0.8, specials=[drain("Wither", 0.22, 1.0, "touches your cheek, and you feel your life drain into her!"),
                                        big("Entangle", 0.12, 1.6, "sings, and roots burst from the ground to bind you!")],
  loot=[("silverleaf_pendant", 0.03), ("moonstone_ring", 0.02), ("blight_heartwood", 0.2)], gold=1.2)
M("rotheart", "Rotheart, the Blighted Oak", 33,
  "The oldest tree in the Eldergrove, older than Elandor, gone black and hollow with blight. Its trunk splits open "
  "around a heart of green fire, and its roots move through the earth like serpents.",
  hp=2.7, dmg=1.25, armor=1.6, aggro=True, boss=True, xp=2.0, gold=5.0,
  specials=[big("Crushing Bough", 0.22, 1.9, "brings a bough as thick as a tower down on you!"),
            dot("Blightbloom", 0.18, 0.45, 4, "nature", "bursts with a cloud of rotting spores!"),
            big("Grasping Roots", 0.12, 1.6, "drives its roots up through the ground and pins you!"),
            heal("Drink the Earth", 0.08, 0.1, "sinks its roots deep and drinks the life of the grove!")],
  loot=[("thornheart", 0.6), ("crown_of_thorns", 0.6), ("eldergrove_amulet", 0.5), ("blight_heartwood", 1.0)])

# ------------------------------------------------------------- Redrock Badlands (18-27)
M("gnoll_warrior", "a gnoll warrior", 18, "A broad gnoll in a coat of rusted scales, its spear hung with the tails of its kills.",
  hp=1.2, dmg=1.15, armor=1.3, specials=[big("Spear Thrust", 0.2, 1.7, "lunges and drives its spear into you!")],
  loot=[("hyena_hide", 0.3), ("dwarven_chainmail", 0.04)], gold=1.5)
M("giant_scorpion", "a giant scorpion", 20, "A red-brown scorpion the size of a cart, its stinger poised high over its back.",
  hp=1.3, dmg=1.15, armor=1.8, specials=[dot("Venomous Sting", 0.22, 0.4, 3, "poison", "lashes down with its stinger, and venom burns through you!")],
  loot=[("scorpion_stinger", 0.4)], gold=0.4, xp=1.2)
M("gnoll_bonecaller", "a gnoll bonecaller", 22, "A gnoll shaman draped in hyena skulls, who calls the spirits of the pack with a whistle of human bone.",
  hp=1.0, dmg=1.15, aggro=True, specials=[heal("Pack Spirits", 0.15, 0.2, "whistles, and ghostly hyenas lick its wounds closed!"),
                                          dot("Bone Curse", 0.2, 0.35, 3, "shadow", "rattles its skulls and howls a curse at you!")],
  loot=[("rune_amulet", 0.03), ("greater_mana_potion", 0.1)], gold=1.8)
M("canyon_wyvern", "a canyon wyvern", 23, "A rust-red wyvern with leathery wings and a barbed tail, shrieking from the canyon ledges.",
  hp=1.3, dmg=1.15, specials=[dot("Barbed Tail", 0.2, 0.4, 3, "poison", "whips its barbed tail into you!"),
                              big("Diving Talons", 0.15, 1.7, "dives out of the sun, talons first!")],
  loot=[("dragon_scale", 0.05), ("hunters_recurve", 0.03)], gold=0.6, xp=1.3)
M("dust_devil", "a dust devil", 25, "A whirling column of red sand and grit with a pair of burning eyes in its heart.",
  hp=1.0, dmg=1.2, armor=0.6, aggro=True, specials=[big("Blinding Sand", 0.15, 1.6, "whips stinging sand into your eyes!")],
  loot=[("greater_mana_potion", 0.1)], gold=0.6)
M("yellowtooth", "Yellowtooth, Gnoll Warlord", 26,
  "The biggest gnoll in the Badlands, grey-muzzled and one-eared, in a coat of overlapping shields and a crown of human teeth. "
  "He laughs constantly, and it is the worst sound you have ever heard.",
  hp=2.6, dmg=1.25, armor=1.5, aggro=True, boss=True, xp=2.0, gold=5.0,
  specials=[big("Teeth-Flail", 0.25, 1.9, "swings his flail of tooth-crusted iron balls into you!"),
            dot("Hyena's Grin", 0.15, 0.4, 4, "bleed", "laughs and tears at you with his own yellowed fangs!"),
            heal("Feast", 0.08, 0.12, "tears a chunk from a carcass and gulps it down, laughing!")],
  loot=[("yellowtooth_flail", 0.6), ("gnoll_bone_necklace", 0.6), ("dwarven_plate", 0.3), ("scorpion_stinger", 0.5)])

# ------------------------------------------------------------- The Carnival That Never Closes (24-30)
# Cheerful and passive on the midway; the roustabouts (the carnival's guards), the night barkers and
# the clowns behind the tents attack on sight. The trapped spirits are happy, and passive.
M("carnival_barker", "a carnival barker", 24, "A barker in a striped jacket and a straw boater, who has been calling the same patter for two hundred years.",
  hp=1.0, dmg=1.15, specials=[big("Patter", 0.12, 1.6, "talks so fast and so loud that your head spins!")],
  loot=[("lost_trinket", 0.25)], gold=1.5)
M("roustabout", "a carnival roustabout", 25, "A huge, silent tent-hand in a leather apron, carrying a mallet for driving stakes.",
  hp=1.3, dmg=1.25, armor=1.5, aggro=True, specials=[big("Tent Mallet", 0.2, 1.7, "drives you into the ground like a tent stake!")],
  loot=[("tent_mallet", 0.03), ("roustabouts_chausses", 0.03)], gold=1.2)
M("sweet_seller", "a sweet-seller", 24, "A smiling woman with a copper pan of bubbling sugar and arms scarred by a century of spills.",
  hp=0.9, dmg=1.1, specials=[dot("Molten Sugar", 0.2, 0.35, 3, "fire", "flings a ladle of molten sugar over you!")],
  loot=[("lost_trinket", 0.2)], gold=1.0, xp=0.9)
M("carnival_pickpocket", "a carnival pickpocket", 25, "A quick, grinning cutpurse of the fair with nimble fingers and a pocketful of other people's things.",
  hp=0.9, dmg=1.2, specials=[big("Knife in the Crowd", 0.2, 1.7, "slips a knife between your ribs in the crush!")],
  loot=[("lost_trinket", 0.4)], gold=2.5)
M("the_strongman", "the Strongman", 26, "A giant of a man in a leopard skin with a waxed moustache, who has lifted the same anvil every night for two centuries.",
  hp=1.9, dmg=1.3, xp=1.6, gold=2.0,
  specials=[big("Anvil Press", 0.22, 1.9, "heaves his anvil over his head and brings it down on you!"),
            big("Bear Hug", 0.12, 1.6, "crushes you in a bear hug until your ribs creak!")],
  loot=[("strongmans_breastplate", 0.2), ("greater_healing_potion", 0.15)])
M("carousel_spirit", "a carousel spirit", 26, "A grey, laughing ghost who has ridden the carousel for three hundred years and would love you to join.",
  hp=0.9, dmg=1.2, specials=[drain("Round and Round", 0.2, 0.9, "takes your hands and spins you, and your strength spins out of you!")],
  loot=[("brass_ring", 0.03)], gold=0.4)
M("painted_horse", "a painted carousel horse", 26, "A wooden carousel horse with flaring nostrils and gilded mane, which has slipped its pole.",
  hp=1.3, dmg=1.2, armor=1.4, specials=[big("Trample", 0.2, 1.7, "rears up and tramples you with painted hooves!")],
  loot=[("brass_ring", 0.03)], gold=0.3)
M("mirror_double", "a mirror double", 27, "Your own reflection, stepped out of the glass, a moment late and smiling a smile you are not smiling.",
  hp=1.0, dmg=1.3, specials=[big("Mirror Strike", 0.22, 1.8, "strikes exactly as you would, and exactly where you are weakest!")],
  loot=[("lost_trinket", 0.2)], gold=0.8)
M("menagerie_tiger", "a menagerie tiger", 27, "A striped cat the size of a horse, its cage long since open, its ribbon collar still around its neck.",
  hp=1.2, dmg=1.25, specials=[big("Pounce", 0.22, 1.8, "pounces and bears you to the ground!")], gold=0.3)
M("dancing_bear", "a dancing bear", 27, "A great brown bear in a ruff and a little hat, which dances when the music plays and does other things when it stops.",
  hp=1.6, dmg=1.2, xp=1.3, specials=[big("Waltz", 0.12, 1.6, "seizes you and whirls you round in a dreadful waltz!")],
  loot=[("acrobats_grips", 0.03)], gold=0.3)
M("wheel_spirit", "a wheel spirit", 27, "A cheerful ghost in the great wheel's treadmill, singing a marching song and very pleased to see you.",
  hp=0.9, dmg=1.2, specials=[drain("All Together Now", 0.2, 0.9, "links arms with you, and your breath goes into the song!")],
  loot=[("brass_ring", 0.03)], gold=0.4)
M("ghost_passenger", "a ghost-train passenger", 27, "A see-through passenger who has ridden the ghost train ten thousand times and screams with delight at every corner.",
  hp=1.0, dmg=1.2, specials=[big("Boo!", 0.12, 1.6, "leaps out at you with a shriek, and you freeze!")],
  loot=[("lost_trinket", 0.25)], gold=0.6)
M("waxwork", "a waxwork", 28, "A warm, waxen figure with wet glass eyes, wearing the clothes and boots of someone who came to the carnival and stayed.",
  hp=1.4, dmg=1.25, armor=1.2, specials=[big("Waxen Grip", 0.12, 1.6, "grips you with soft, warm fingers that will not let go!"),
                                       big("Heavy Fist", 0.18, 1.7, "swings a fist as heavy as a candle-mould!")],
  loot=[("lost_trinket", 0.35), ("dancing_slippers", 0.03)], gold=1.0)
M("madame_vesna", "Madame Vesna, the fortune teller", 28, "A woman in shawls and jangling coins, whose crystal ball shows the future clearly, and only ever one ending.",
  hp=1.9, dmg=1.3, xp=1.6, gold=2.5,
  specials=[dot("Ill Fortune", 0.2, 0.45, 4, "shadow", "turns over a card, and misfortune settles on you like a shroud!"),
            big("Glimpse of Your Death", 0.12, 1.6, "holds up the crystal ball, and you see your own death in it!")],
  loot=[("fortune_tellers_orb", 0.2), ("greater_mana_potion", 0.2)])
M("night_barker", "a night barker", 28, "A barker of the back lots in a moth-eaten tailcoat, who tells the truth: 'Come in, come in, and never leave.'",
  hp=1.2, dmg=1.3, aggro=True, specials=[dot("The Honest Pitch", 0.2, 0.4, 3, "shadow", "tells you exactly what the carnival will do to you, and the words cut!")],
  loot=[("lost_trinket", 0.3), ("greater_healing_potion", 0.08)], gold=1.5)
M("carnival_acrobat", "a carnival acrobat", 28, "A lean, tired acrobat in faded spangles, who moves faster than anyone that tired should.",
  hp=1.0, dmg=1.3, specials=[big("Flying Kick", 0.22, 1.8, "somersaults over you and kicks you in the back of the head!")],
  loot=[("acrobats_grips", 0.04), ("dancing_slippers", 0.03)], gold=1.0)
M("mirela", "Mirela, the knife-thrower", 29, "A knife-thrower with a bandolier of blades and eyes like a hawk's. She never misses any more, and she wishes she would.",
  hp=1.9, dmg=1.35, xp=1.6, gold=2.5,
  specials=[big("Seven Knives", 0.22, 1.9, "throws seven knives in a single breath, and every one finds you!"),
            dot("Bleeding Edge", 0.15, 0.45, 3, "bleed", "nicks an artery with a thrown blade!")],
  loot=[("knife_throwers_blade", 0.2), ("greater_healing_potion", 0.2)])
M("caged_horror", "a caged horror", 29, "Something the carnival made from what it kept: too many arms, a face in the wrong place, and a voice that whispers your name.",
  hp=1.4, dmg=1.3, specials=[drain("Hungry Hands", 0.22, 1.0, "reaches through the bars with too many hands and feeds!")],
  loot=[("lost_trinket", 0.3)], gold=0.6, xp=1.2)
M("carnival_clown", "a carnival clown", 29, "A clown in a ruff and greasepaint, whose painted smile is wider than its face and does not move when it speaks.",
  hp=1.1, dmg=1.3, aggro=True, specials=[big("The Grin", 0.12, 1.6, "leans close and grins, and you cannot look away!"),
                                       dot("Seltzer", 0.18, 0.4, 3, "poison", "sprays you with seltzer that burns like acid!")],
  loot=[("lost_trinket", 0.25)], gold=1.2)
M("the_ringmaster", "the Ringmaster", 30,
  "The master of the carnival in a scarlet coat and tall hat, with a whip in his hand and every tooth in his smile. "
  "Threads like puppet strings run from his wrists into the canvas above. He was the carnival's first prisoner, and he no longer remembers being anything else.",
  hp=2.8, dmg=1.3, armor=1.4, aggro=True, boss=True, xp=2.0, gold=5.0,
  specials=[big("Whipcrack", 0.22, 1.9, "cracks his whip, and it opens you like a knife!"),
            big("Showstopper", 0.12, 1.6, "throws up his arms, the spotlight swings onto you, and you cannot move!"),
            dot("Under the Spotlight", 0.15, 0.45, 4, "fire", "turns the burning spotlight full on you!"),
            heal("The Show Must Go On", 0.08, 0.1, "is jerked upright by his strings, smiling, his wounds closing!")],
  loot=[("ringmasters_baton", 0.4), ("ringmasters_coat", 0.5), ("brass_ring", 0.3)])

# ------------------------------------------------------------- Ironspine Mountains (20-31)
M("mountain_lion", "a mountain lion", 21, "A tawny great cat crouched on a ledge, tail twitching.",
  hp=1.0, dmg=1.15, specials=[dot("Rending Claws", 0.2, 0.35, 3, "bleed", "rakes you with rending claws!")], gold=0.4)
M("harpy", "a shrieking harpy", 22, "A filthy winged hag with talons of black iron.",
  hp=0.9, dmg=1.15, specials=[big("Deafening Shriek", 0.15, 1.6, "lets loose a deafening shriek!")],
  loot=[("hunters_recurve", 0.04)], gold=1.0)
M("griffon", "a mountain griffon", 23, "A great eagle-headed beast with a lion's tawny haunches, nesting on the high crags.",
  hp=1.1, dmg=1.2, specials=[big("Diving Strike", 0.2, 1.7, "folds its wings and plummets onto you, talons first!")],
  loot=[("griffon_feather", 0.5), ("hunters_recurve", 0.04)], gold=0.4)
M("hill_giant", "a hill giant", 24, "A dull-eyed giant twice the height of a man, carrying a tree trunk as a club.",
  hp=1.7, dmg=1.25, specials=[big("Tree-Trunk Smash", 0.25, 1.8, "brings his tree-trunk club smashing down!")],
  loot=[("tower_shield", 0.05), ("greater_healing_potion", 0.15)], gold=1.5, xp=1.5)
M("orc_raider", "an orc raider", 24, "A grey-skinned orc in spiked leathers, hungry for loot and glory.",
  hp=1.1, dmg=1.1, loot=[("orc_tusk", 0.3), ("mithril_sword", 0.04), ("mithril_hauberk", 0.03)], gold=1.5)
M("mountain_ogre", "a mountain ogre", 25, "A warty grey ogre in a bearskin, hefting a slab of quarried stone as a club.",
  hp=1.6, dmg=1.2, specials=[big("Stone Slab", 0.2, 1.8, "swings its slab of stone into you with a sickening crunch!"),
                             big("Bellow", 0.1, 1.6, "bellows in your face, and its foul breath leaves you reeling!")],
  loot=[("tower_shield", 0.04), ("greater_healing_potion", 0.12)], gold=1.6, xp=1.4)
M("orc_berserker", "an orc berserker", 26, "A foaming, tattooed orc wielding an axe in each hand.",
  hp=1.2, dmg=1.25, specials=[big("Frenzied Chop", 0.25, 1.7, "screams and chops at you in a frenzy!")],
  loot=[("orc_tusk", 0.3), ("orcish_greataxe", 0.06), ("orcish_helm", 0.05)], gold=1.5)
M("orc_shaman", "an orc shaman", 27, "A wizened orc draped in bones and feathers, chanting to the storm.",
  hp=1.0, dmg=1.15, specials=[heal("Spirit Mending", 0.15, 0.2, "chants to the spirits, and his wounds mend!"),
                                          dot("Searing Totem", 0.2, 0.4, 3, "fire", "calls down searing spirit-fire upon you!")],
  loot=[("orc_tusk", 0.3), ("greater_mana_potion", 0.2), ("frostweave_staff", 0.04)], gold=1.8)
M("orc_warbeast", "an orc warbeast", 28, "A massive armoured boar-beast ridden into battle by the orc clans.",
  hp=1.6, dmg=1.2, armor=1.5, specials=[big("Trample", 0.15, 1.6, "tramples you underfoot!")],
  loot=[("orc_tusk", 0.5)], gold=0.8, xp=1.4)
M("orc_bloodguard", "an orc bloodguard", 29, "One of the warlord's sworn guards, in blackened plate daubed with red handprints.",
  hp=1.3, dmg=1.25, armor=1.6, specials=[big("Execution Swing", 0.2, 1.8, "raises a heavy cleaver and swings for your neck!"),
                                         big("Shield Bash", 0.12, 1.6, "slams a spiked shield into your face!")],
  loot=[("orc_tusk", 0.4), ("orcish_helm", 0.05), ("warlord_gauntlets", 0.02)], gold=1.8, xp=1.3)
M("warlord_gorrak", "Warlord Gorrak Skullsplitter", 31,
  "A mountain of scarred green muscle in blackened plate, wearing a cloak of human scalps.",
  hp=2.7, dmg=1.25, armor=1.6, aggro=True, boss=True, xp=2.0, gold=5.0,
  specials=[big("Skullsplitter", 0.25, 2.0, "brings his warhammer down in a skull-splitting overhead blow!"),
            big("War Stomp", 0.12, 1.6, "stomps, and the ground shakes you off your feet!"),
            heal("Bloodlust", 0.08, 0.1, "roars with bloodlust, his wounds forgotten!")],
  loot=[("gorraks_warhammer", 0.6), ("warlord_gauntlets", 0.6), ("orcish_helm", 0.5), ("tower_shield", 0.3)])

# ------------------------------------------------------------- Frost Caverns (29-35)
M("winter_wolf", "a winter wolf", 29, "A huge white wolf whose breath hangs in glittering clouds of frost.",
  hp=1.1, dmg=1.2, specials=[dot("Frostbite", 0.2, 0.4, 3, "frost", "clamps its freezing jaws on your arm!")],
  loot=[("winter_wolf_pelt", 0.5), ("frost_shard", 0.15)], gold=0.4)
M("ice_wraith", "an ice wraith", 30, "A shrieking spectre of blue frost, its touch colder than death.",
  hp=1.0, dmg=1.2, armor=0.6, aggro=True, specials=[drain("Frozen Touch", 0.25, 1.0, "passes a frozen hand through your chest!")],
  loot=[("frost_shard", 0.3), ("frost_ring", 0.03)], gold=0.8)
M("rime_drake", "a rime drake", 31, "A lean, pale-blue drake with frost-rimed scales, coiled on the glacier ice.",
  hp=1.4, dmg=1.25, armor=1.4, specials=[big("Frost Breath", 0.22, 1.8, "exhales a howling blast of frost over you!")],
  loot=[("frost_shard", 0.4), ("frost_ring", 0.03), ("frostbrand", 0.03)], gold=1.2, xp=1.4)
M("frost_troll", "a frost troll", 32, "A white-furred troll with icicles hanging from its tusks.",
  hp=1.5, dmg=1.2, specials=[heal("Regenerate", 0.15, 0.12, "regenerates, frost sealing its wounds!")],
  loot=[("frost_shard", 0.3), ("frostgiant_greaves", 0.04)], gold=1.2, xp=1.3)
M("frost_giant", "a frost giant", 34, "A blue-skinned giant in rime-crusted mail, wielding a sword of ice.",
  hp=1.8, dmg=1.3, armor=1.5, specials=[big("Glacial Cleave", 0.25, 1.8, "cleaves at you with a sword of solid ice!"),
                                        big("Frost Nova", 0.1, 1.6, "exhales a blast of frost that freezes you in place!")],
  loot=[("frostbrand", 0.06), ("frostgiant_greaves", 0.08), ("frost_shard", 0.5)], gold=2.0, xp=1.7)

# ------------------------------------------------------------- Ruins of Elandor (32-41)
M("phantom_sentinel", "a phantom sentinel", 33, "The ghost of an elven guardsman, still at his post after a thousand years.",
  hp=1.1, dmg=1.2, armor=1.2, aggro=True, loot=[("elven_relic", 0.2), ("elandor_runeblade", 0.03)], gold=1.0)
M("ruin_stalker", "a ruin stalker", 34, "A sleek, six-legged predator with chitinous plates and mirror-bright eyes.",
  hp=1.2, dmg=1.25, specials=[dot("Barbed Tail", 0.2, 0.4, 3, "poison", "lashes you with its barbed tail!")],
  loot=[("elven_relic", 0.1)], gold=0.8)
M("spectral_mage", "a spectral mage", 36, "A translucent elven sorcerer in flowing robes, endlessly reading a book of light.",
  hp=0.9, dmg=1.3, armor=0.5, specials=[dot("Arcane Burn", 0.25, 0.45, 3, "arcane", "hurls a bolt of searing arcane fire!"),
                                        big("Time Lock", 0.12, 1.6, "gestures, and time freezes around you!")],
  loot=[("elven_relic", 0.25), ("elandor_robes", 0.04), ("staff_of_stars", 0.03), ("starlight_circlet", 0.03)], gold=1.5)
M("living_statue", "a living statue", 37, "A marble statue of an elven hero that grinds slowly to life.",
  hp=2.0, dmg=1.25, armor=2.5, specials=[big("Marble Fist", 0.25, 1.8, "smashes you with a fist of solid marble!")],
  loot=[("elandor_plate", 0.05), ("elven_relic", 0.3)], gold=1.0, xp=1.6)
M("moonblade_revenant", "a moonblade revenant", 38, "The risen husk of an elven knight of the Moon Court, its silver blade still bright after a thousand years.",
  hp=1.2, dmg=1.3, armor=1.4, aggro=True, specials=[drain("Moonblade", 0.22, 1.0, "draws its pale blade across you, and your strength flows into it!")],
  loot=[("elven_relic", 0.25), ("elandor_runeblade", 0.04), ("starlight_circlet", 0.03)], gold=1.4)
M("arcane_sentinel", "an arcane sentinel", 39, "A tall guardian of white stone and silver runes, its hollow face lit by a cold blue glow.",
  hp=1.8, dmg=1.25, armor=2.2, specials=[big("Runic Hammer", 0.22, 1.8, "brings down a fist blazing with silver runes!"),
                                         big("Binding Glyph", 0.1, 1.6, "flashes a glyph that binds your limbs!")],
  loot=[("elven_relic", 0.3), ("staff_of_stars", 0.04), ("elandor_plate", 0.03)], gold=1.2, xp=1.5)
M("seluvar", "Seluvar the Hollow Archmage", 41,
  "An elven archmage whose body is long gone. Only robes, a crown of stars and two burning eyes remain.",
  hp=2.7, dmg=1.25, armor=1.0, aggro=True, boss=True, xp=2.0, gold=5.0,
  specials=[dot("Starfire", 0.22, 0.45, 4, "arcane", "calls down a column of starfire upon you!"),
            big("Temporal Prison", 0.12, 1.6, "traps you in a prison of frozen time!"),
            drain("Hollowing", 0.15, 1.2, "hollows you out, drinking your essence!")],
  loot=[("seluvars_wand", 0.6), ("archmage_ring", 0.6), ("elandor_robes", 0.4), ("starlight_circlet", 0.4), ("elven_longbow", 0.3)])

# ------------------------------------------------------------- The Painted Gallery (36-42)
# Ithilmir's gallery north of the Moon Court, and the worlds inside his paintings. The painted people go
# about their painted lives; only the frame-wardens and other guards, the elementals of paint and flame,
# the skull and the painter's sketches attack on sight. Each painting has a named champion (not a boss);
# only Ithilmir himself is one.
M("frame_warden", "a gilded frame-warden", 38, "A tall figure of gilt and plaster with an empty picture frame for a chest, through which you can see the wall behind it.",
  hp=1.5, dmg=1.25, armor=2.0, aggro=True, specials=[big("Framing Blow", 0.2, 1.8, "brings its gilded fists down on you!")],
  loot=[("gilt_frame_shield", 0.04), ("living_pigment", 0.2)], gold=1.4, xp=1.3)
M("painted_sailor", "a painted sailor", 36, "A drowned sailor brushed in greys and greens, dripping paint, his mouth open in a shout that never ends.",
  hp=1.1, dmg=1.25, specials=[dot("Boathook", 0.2, 0.4, 3, "bleed", "swings a boathook into you!")],
  loot=[("living_pigment", 0.3), ("greater_healing_potion", 0.08)], gold=1.0)
M("painted_breaker", "a painted breaker", 36, "A wave of green and white brushstrokes that has risen out of the sea with a face in its foam.",
  hp=1.0, dmg=1.3, armor=0.6, aggro=True, element="frost",
  specials=[big("Undertow", 0.12, 1.6, "crashes over you, and the undertow drags you off your feet!")],
  loot=[("living_pigment", 0.3)], gold=0.8)
M("saltmere_serpent", "the Saltmere Serpent", 37, "A sea serpent of glistening blue-green paint, coiled around the lighthouse, with eyes the painter took a great deal of care over.",
  hp=1.9, dmg=1.3, armor=1.3, xp=1.7, gold=2.0,
  specials=[big("Crushing Coils", 0.22, 1.9, "wraps you in its painted coils and squeezes!"),
            dot("Venom of Varnish", 0.18, 0.45, 3, "poison", "bites you, and varnish burns in your veins!")],
  loot=[("sea_varnish_greaves", 0.25), ("living_pigment", 1.0)])
M("painted_hound", "a painted hound", 37, "A lean scarlet-collared hound brushed in a few swift strokes, running in full cry after a quarry it never reaches.",
  hp=1.0, dmg=1.25, specials=[big("Pull Down", 0.2, 1.6, "leaps and drags you down into the painted snow!")],
  loot=[("living_pigment", 0.25)], gold=0.2)
M("painted_huntsman", "a painted huntsman", 37, "A rider in scarlet and fur, his horse's hooves never touching the snow, a spear across his saddle.",
  hp=1.1, dmg=1.3, specials=[big("Boar Spear", 0.2, 1.7, "wheels his horse and drives his spear into you!")],
  loot=[("frost_varnished_bow", 0.04), ("living_pigment", 0.3)], gold=1.2)
M("frost_glaze", "a frost glaze", 38, "A skimming shape of cold white light, the varnish of the winter scene come alive, leaving trails of frost on the ice.",
  hp=0.9, dmg=1.3, armor=0.5, aggro=True, element="frost",
  specials=[big("Hoarfrost", 0.14, 1.6, "flashes over you, and frost locks your joints!"),
            dot("Glaze", 0.18, 0.4, 3, "frost", "coats you in a skin of freezing varnish!")],
  loot=[("living_pigment", 0.3), ("greater_mana_potion", 0.12)], gold=0.8)
M("white_stag", "the White Stag", 38, "The quarry of the Winter Hunt, a white stag as big as a horse, with antlers like winter trees and breath that smokes.",
  hp=1.9, dmg=1.3, armor=1.2, xp=1.7, gold=0.5,
  specials=[big("Antler Charge", 0.22, 1.9, "lowers its antlers and charges!"),
            big("Trampling Hooves", 0.1, 1.6, "rears and strikes you down with its hooves!")],
  loot=[("antler_maul", 0.3), ("living_pigment", 1.0)])
M("fly_swarm", "a swarm of painted flies", 38, "A droning cloud of black flies as big as hawks, each one a perfect dot of paint with wings.",
  hp=0.8, dmg=1.25, armor=0.4, specials=[dot("Biting Swarm", 0.25, 0.4, 3, "bleed", "descends on you, biting everywhere at once!")],
  loot=[("living_pigment", 0.25)], gold=0.2)
M("candle_flame", "a living candle-flame", 38, "The flame of the still life's candle, grown as tall as a man and dancing on the wick of its own will.",
  hp=1.0, dmg=1.3, armor=0.6, aggro=True, element="fire",
  specials=[dot("Tallow Fire", 0.25, 0.45, 3, "fire", "wraps you in burning tallow!")],
  loot=[("candle_of_stillness", 0.04), ("living_pigment", 0.3)], gold=0.8)
M("rotfruit_horror", "a rotfruit horror", 39, "A heaving mass of blackened pears and burst grapes, furred with mould, dragging itself across the tablecloth.",
  hp=1.6, dmg=1.25, armor=0.8, xp=1.3, specials=[dot("Spores of Rot", 0.2, 0.4, 4, "disease", "bursts, showering you in rot!")],
  loot=[("living_pigment", 0.35)], gold=0.4)
M("memento_skull", "the Memento Skull", 39, "The skull of the still life, as big as a cottage, its jaw grinding and its sockets lit. It is very tired of lying still.",
  hp=1.9, dmg=1.3, armor=1.4, aggro=True, xp=1.7, gold=2.0,
  specials=[drain("Memento Mori", 0.18, 1.1, "reminds you that you will die, and you feel it happening!"),
            big("The Hollow Stare", 0.12, 1.6, "fixes you with its empty sockets, and you cannot move!")],
  loot=[("candle_of_stillness", 0.25), ("living_pigment", 1.0)])
M("portrait_sitter", "a portrait sitter", 39, "A noble stepped out of a portrait, exactly as beautiful as the painter was paid to make them, and very bored.",
  hp=1.0, dmg=1.25, specials=[big("Withering Snub", 0.12, 1.6, "looks you up and down, and you are too mortified to move!")],
  loot=[("painted_silk_slippers", 0.04), ("living_pigment", 0.3)], gold=2.0)
M("painted_duellist", "a painted duellist", 40, "A painted gallant in lace and velvet, rapier in hand, fighting the same duel for the hundredth time and glad of a new opponent.",
  hp=1.2, dmg=1.35, specials=[dot("Flickering Rapier", 0.2, 0.45, 3, "bleed", "flicks his rapier across you in a dozen fine cuts!")],
  loot=[("palette_knife", 0.05), ("living_pigment", 0.3)], gold=1.8)
M("gilt_footman", "a gilt footman", 40, "A footman in gilded livery with a perfect painted smile, and a silver tray he swings like a mace.",
  hp=1.4, dmg=1.3, armor=1.8, aggro=True, specials=[big("Silver Tray", 0.2, 1.7, "swings his silver tray into your head!")],
  loot=[("gilt_sabatons", 0.04), ("living_pigment", 0.25)], gold=1.6)
M("countess_isaura", "Countess Isaura, the Host", 40, "The host of the salon, in silver and pearl, fanning herself before her own empty frame. She thinks you would look very fine in it.",
  hp=1.9, dmg=1.3, armor=1.2, xp=1.7, gold=4.0,
  specials=[big("Sit for Me", 0.12, 1.6, "raises her lorgnette, and you find yourself frozen in a pose!"),
            drain("Framed", 0.15, 1.1, "traces a frame in the air around you, and your colour drains into it!")],
  loot=[("countess_gloves", 0.25), ("living_pigment", 1.0)])
M("painted_citizen", "a painted citizen of Elandor", 40, "An elf of the living city in bright silks, who knows, somewhere behind the eyes, that the city fell a thousand years ago.",
  hp=1.0, dmg=1.25, loot=[("living_pigment", 0.3), ("elven_relic", 0.15)], gold=1.5)
M("painted_moonguard", "a painted moonguard", 41, "A knight of the Moon Court in silver mail and a crescent helm, as the revenants in the ruins once were.",
  hp=1.4, dmg=1.3, armor=1.8, aggro=True, specials=[drain("Moonblade", 0.2, 1.0, "draws a pale blade across you, and your strength flows into it!")],
  loot=[("moonsteel_gauntlets", 0.04), ("living_pigment", 0.25)], gold=1.6)
M("painted_king", "the Painted King of Elandor", 41, "The last king of Elandor as the painter saw him, crowned, young and proud. He alone knows his city has fallen.",
  hp=2.0, dmg=1.3, armor=1.5, xp=1.8, gold=4.0,
  specials=[big("Blade of the Moon Court", 0.22, 1.9, "strikes with the silver blade of the Moon Court!"),
            big("Royal Command", 0.12, 1.6, "commands you to kneel, and you do!"),
            heal("The City Remembers", 0.1, 0.12, "draws on the painted city, and his wounds fill in like fresh paint!")],
  loot=[("painted_king_gauntlets", 0.25), ("living_pigment", 1.0)])
M("charcoal_sketch", "a charcoal sketch", 41, "A half-drawn figure of smudged charcoal lines with no face, stepping out of the margins of the self-portrait.",
  hp=1.0, dmg=1.3, armor=0.6, aggro=True, specials=[dot("Smudge", 0.2, 0.45, 3, "shadow", "smears across you, and you start to fade!")],
  loot=[("living_pigment", 0.3)], gold=0.6)
M("ithilmir", "Ithilmir, the Court Painter", 42,
  "The court painter of Elandor, who sealed his city into canvas as it fell and then himself. He wears a smock stiff "
  "with a thousand years of paint, and where his face should be there is only smooth, blank skin.",
  hp=2.8, dmg=1.3, armor=1.1, aggro=True, boss=True, xp=2.0, gold=6.0,
  specials=[big("Hold Still", 0.12, 1.6, "raises his brush, and you cannot move a muscle!"),
            dot("Turpentine", 0.2, 0.45, 4, "arcane", "flicks a brushful of burning spirit across you!"),
            drain("Taking Your Likeness", 0.15, 1.2, "studies you, and your face begins to come away onto his canvas!"),
            heal("A Fresh Coat", 0.08, 0.12, "paints over his wounds with a single stroke!")],
  loot=[("ithilmirs_brush", 0.5), ("ithilmirs_maulstick", 0.5), ("smock_of_living_paint", 0.5)])

# ------------------------------------------------------------- The Chancery of the Dead (30-38)
# The dead here are busy with their cases and ignore the living, so only the court's bailiffs,
# wardens and the High Justice attack on sight (a deliberate exception to the undead rule).
M("hanged_petitioner", "a hanged petitioner", 30, "A grey ghost with a noose still knotted around its neck, clutching a petition to its chest.",
  hp=1.0, dmg=1.2, specials=[big("Strangling Grip", 0.12, 1.6, "seizes your throat with cold, choking fingers!")],
  gold=0.6)
M("queue_warden", "a queue warden", 31, "A spectral warden in a grey tabard who keeps the line of the hanged in order with a heavy staff.",
  hp=1.2, dmg=1.25, armor=1.6, aggro=True, specials=[big("Keep the Line", 0.2, 1.7, "cracks his staff across you to keep the line!")],
  loot=[("greater_healing_potion", 0.1)], gold=1.0)
M("the_headsman", "the Headsman", 32, "A hooded executioner, dead for three hundred years, with an axe whose edge has never dulled.",
  hp=2.0, dmg=1.35, xp=1.7, gold=2.0,
  specials=[big("Headsman's Stroke", 0.22, 2.0, "raises his axe high and brings it down on your neck!"),
            big("The Block", 0.1, 1.6, "forces your head down onto the block!")],
  loot=[("headsmans_axe", 0.2), ("greater_healing_potion", 0.2)])
M("court_bailiff", "a court bailiff", 32, "A dead bailiff in grey tabard and mail, a halberd in his hands and a ring of keys at his belt.",
  hp=1.3, dmg=1.25, armor=1.6, aggro=True,
  specials=[big("Halberd", 0.18, 1.7, "swings his halberd at you!"),
            big("Seize", 0.1, 1.6, "grabs you by the collar and holds you fast!")],
  loot=[("bailiffs_halberd", 0.03), ("bailiffs_hauberk", 0.03)], gold=1.2)
M("waiting_shade", "a waiting shade", 31, "A ghost faded nearly to nothing from waiting, still holding a numbered ticket.",
  hp=0.9, dmg=1.2, specials=[drain("Weary Touch", 0.2, 0.9, "lays a weary hand on you and drinks your strength!")],
  gold=0.5, xp=0.9)
M("registry_clerk", "a registry clerk", 32, "An ink-stained spectral clerk with a seal in one hand and a stack of forms in the other.",
  hp=1.0, dmg=1.2, specials=[big("Seal of Record", 0.12, 1.6, "stamps a seal of record on your forehead, and you freeze!")],
  loot=[("stamped_form", 0.4)], gold=1.0)
M("nameless_shade", "a nameless shade", 33, "A ghost whose name has been lost, searching the shelves and muttering half-names.",
  hp=1.1, dmg=1.3, specials=[drain("Who Am I?", 0.22, 1.0, "clutches at you, trying to take your name, and your life comes with it!")],
  gold=0.6)
M("restless_petitioner", "a restless petitioner", 33, "A ghost pacing with a petition, reading it aloud to anyone who will listen, and to anyone who won't.",
  hp=1.0, dmg=1.25, specials=[dot("Endless Grievance", 0.2, 0.4, 3, "shadow", "reads you its grievance, and the words burn like cold fire!")],
  gold=0.8)
M("spectral_scrivener", "a spectral scrivener", 33, "A hunched ghost with an ink-blackened quill and a penknife for trimming it.",
  hp=0.9, dmg=1.25, specials=[dot("Ink Blot", 0.2, 0.4, 3, "shadow", "flicks a blot of black ink that eats into your skin!")],
  loot=[("will_page", 0.4), ("scriveners_penknife", 0.03)], gold=0.8)
M("minor_magistrate", "a minor magistrate", 34, "A bored ghost in a grey wig who has heard ten thousand cases about spoons.",
  hp=1.4, dmg=1.25, xp=1.3, gold=1.5, specials=[big("Order!", 0.14, 1.6, "bangs his gavel and roars 'ORDER!', and you freeze!")],
  loot=[("notarys_rod", 0.05)])
M("wrathful_heir", "a wrathful heir", 34, "The ghost of a disinherited son, still furious about it a hundred years later.",
  hp=1.2, dmg=1.3, specials=[big("Disinherited Fury", 0.2, 1.8, "flies at you in a fury of wounded pride!")],
  loot=[("will_page", 0.3)], gold=1.2)
M("living_will", "a living will", 34, "A will of yellow parchment that has come loose from its ribbon and keeps rewriting itself, edges sharp as razors.",
  hp=0.8, dmg=1.25, specials=[dot("Paper Cuts", 0.22, 0.4, 3, "bleed", "whips around you in a storm of razor-edged pages!")],
  loot=[("will_page", 0.5)], gold=0.3, xp=0.9)
M("ghostly_squatter", "a ghostly squatter", 35, "The ghost of a farmer who refuses to leave a house sold out from under his grave, and says so.",
  hp=1.1, dmg=1.25, specials=[drain("Get Off My Land", 0.2, 1.0, "grips you with cold hands and roars 'GET OFF MY LAND!'")],
  gold=0.8)
M("hired_sword", "a hired sword", 35, "A living mercenary in a leather coat, hired to evict the dead and long out of patience.",
  hp=1.2, dmg=1.3, specials=[big("Dirty Cut", 0.2, 1.8, "feints high and cuts you low!")],
  loot=[("bailiffs_hauberk", 0.03), ("greater_healing_potion", 0.1)], gold=2.0)
M("dead_advocate", "a dead advocate", 35, "A gaunt ghost in an advocate's black gown, still arguing a case whose client faded long ago.",
  hp=1.0, dmg=1.3, specials=[big("Objection!", 0.12, 1.6, "shouts 'OBJECTION!' so loudly that you stagger!"),
                            dot("Long-Winded Argument", 0.15, 0.4, 3, "shadow", "begins a speech that drains the will to live!")],
  loot=[("sealed_record", 0.15), ("notarys_rod", 0.03)], gold=1.5)
M("archive_keeper", "a keeper of the archive", 35, "A tall, silent ghost with a lantern of grey flame, who has kept the archive for six hundred years.",
  hp=1.3, dmg=1.25, specials=[big("Silence", 0.14, 1.6, "raises a finger to its lips, and you cannot move or speak!")],
  loot=[("sealed_record", 0.35), ("greater_mana_potion", 0.1)], gold=1.0)
M("chancery_warden", "a warden of the Chancery", 35, "A towering dead knight in grey plate, sworn to guard the courts until the last case is heard.",
  hp=1.4, dmg=1.3, armor=2.0, aggro=True, specials=[big("Sentence Carried Out", 0.2, 1.8, "carries out the sentence with a great two-handed sword!")],
  loot=[("wardens_greathelm", 0.04), ("wardens_sabatons", 0.04), ("chancery_shield", 0.03)], gold=1.5)
M("robed_judge", "a judge of the high court", 37, "A dead judge in black robes and a grey wig, who long ago stopped telling cases apart.",
  hp=1.5, dmg=1.3, xp=1.4, gold=2.0,
  specials=[big("Sentence", 0.12, 1.6, "pronounces sentence, and the words hold you fast!"),
            dot("Contempt of Court", 0.18, 0.45, 3, "shadow", "holds you in contempt, and the contempt burns!")],
  loot=[("seal_of_office", 0.04), ("greater_mana_potion", 0.12)])
M("condemned_shade", "a condemned shade", 37, "The ghost of someone the court condemned, reading its own verdict over and over.",
  hp=1.2, dmg=1.3, specials=[drain("Last Appeal", 0.22, 1.0, "clutches you, begging, and your life drains into its cold hands!")],
  gold=1.0)
M("high_justice", "the High Justice", 38,
  "The highest judge of the Chancery, dead so long that he no longer remembers what justice is supposed to mean. "
  "His robes are grey with dust, his wig has rotted to cobweb, and his gavel never stops.",
  hp=2.8, dmg=1.3, armor=1.4, aggro=True, boss=True, xp=2.0, gold=6.0,
  specials=[big("The Gavel Falls", 0.22, 1.9, "brings his great gavel down on you like a verdict!"),
            dot("Contempt of Court", 0.15, 0.45, 4, "shadow", "holds you in contempt, and the cold of the grave seeps into you!"),
            big("Order in the Court", 0.12, 1.6, "roars 'ORDER!', and the whole court falls still around you!"),
            drain("Sentence of Death", 0.12, 1.1, "pronounces a sentence of death, and your life flows up to the bench!")],
  loot=[("gavel_of_the_high_justice", 0.5), ("chain_of_office", 0.5), ("seal_of_office", 0.4)])

# ------------------------------------------------------------- The Clockwork Orchard (38-44)
# Orrin Gearwhistle's creations tend the orchard and ignore visitors; only his sentries, hounds and
# escapement guardians (guards) and the foundry's molten springs (elementals) attack on sight. The
# cuckoo, the hostess and the master automaton are named champions; only Orrin is a boss.
M("brass_sparrow", "a clockwork sparrow", 38, "A sparrow of brass and enamel with jewelled eyes, ticking as it hops, and quite fearless.",
  hp=0.9, dmg=1.25, armor=1.0, specials=[dot("Brass Beak", 0.22, 0.4, 3, "bleed", "darts at you and pecks with a beak like a chisel!")],
  loot=[("brass_gear", 0.4)], gold=0.3)
M("orchard_tender", "a clockwork gardener", 38, "A gardener of brass and green enamel with an oilcan for one hand and pruning shears for the other.",
  hp=1.2, dmg=1.25, armor=1.6, specials=[big("Pruning Shears", 0.2, 1.7, "snaps its great shears shut on you!")],
  loot=[("wound_mainspring", 0.3), ("clockwork_pruning_axe", 0.04)], gold=1.2)
M("rust_crawler", "a rust crawler", 39, "A flaking, many-legged thing the size of a dog, made of rust and hunger, that eats iron and leaves red dust.",
  hp=1.3, dmg=1.25, specials=[dot("Corrode", 0.22, 0.4, 3, "poison", "bites you, and rust spreads across your armour and skin!")],
  loot=[("brass_gear", 0.3)], gold=0.3)
M("brass_bees", "a swarm of brass bees", 39, "A humming cloud of jewelled mechanical bees on wings of gold leaf, each with a sting like a sewing needle.",
  hp=0.9, dmg=1.3, armor=0.8, specials=[dot("Needle Stings", 0.25, 0.4, 3, "poison", "swarms over you, stinging!")],
  loot=[("tinker_gloves", 0.03), ("brass_gear", 0.3)], gold=0.2)
M("clockwork_sentry", "a clockwork sentry", 40, "A sentry of polished steel with a halberd and a face like a clock, which turns its hands to point at intruders.",
  hp=1.5, dmg=1.3, armor=2.2, aggro=True, specials=[big("Halberd Sweep", 0.2, 1.8, "sweeps its halberd through you!")],
  loot=[("brass_gear_helm", 0.04), ("wound_mainspring", 0.3)], gold=1.4)
M("clockwork_pike", "a clockwork pike", 40, "A pike of steel as long as a rowing boat, with rows of filed teeth, swimming in circles until something better comes along.",
  hp=1.3, dmg=1.3, armor=1.5, specials=[big("Steel Jaws", 0.2, 1.8, "lunges from the water and clamps its steel jaws on you!")],
  loot=[("brass_gear", 0.4), ("piston_sabatons", 0.03)], gold=0.4)
M("winding_automaton", "a winding automaton", 40, "A huge automaton with arms like cranes, built to carry the orchard's keys, slow and patient and very strong.",
  hp=1.8, dmg=1.25, armor=2.5, xp=1.5, specials=[big("Crane Arm", 0.22, 1.8, "swings a crane-like arm into you!")],
  loot=[("wound_mainspring", 0.4), ("brass_scale_hauberk", 0.03)], gold=1.0)
M("great_cuckoo", "the Great Cuckoo", 40, "The cuckoo of the great clock tower, a bird of brass and painted feathers as big as a horse, which shrieks the hour and hates to be interrupted.",
  hp=1.9, dmg=1.3, armor=1.4, xp=1.7, gold=2.0,
  specials=[big("Shriek the Hour", 0.12, 1.6, "throws back its head and shrieks the hour, and your ears ring!"),
            big("Spring-Loaded Strike", 0.22, 1.9, "shoots out of its doors on a great spring and strikes you!")],
  loot=[("jewellers_circlet", 0.25), ("wound_mainspring", 1.0)])
M("tea_guest", "a clockwork tea guest", 41, "A clockwork lady or gentleman in painted silks, pouring tea and laughing at a joke three hundred years old.",
  hp=1.1, dmg=1.3, specials=[big("Another Cup?", 0.12, 1.6, "insists you have another cup, and you find you cannot refuse!")],
  loot=[("wound_mainspring", 0.3), ("supreme_healing_potion", 0.06)], gold=1.8)
M("clockwork_hostess", "the Clockwork Hostess", 41, "The hostess of the unending tea party, in a gown of silver plate and a lace cap, who has never once let a guest leave early.",
  hp=1.9, dmg=1.3, armor=1.2, xp=1.7, gold=4.0,
  specials=[big("Do Sit Down", 0.12, 1.6, "presses you firmly into a chair!"),
            dot("Scalding Tea", 0.2, 0.45, 3, "fire", "pours a pot of boiling tea over you!")],
  loot=[("tinker_gloves", 0.25), ("wound_mainspring", 1.0)])
M("spring_hound", "a spring-loaded hound", 41, "A hound of steel coils and plates that bounds along the hedge paths, every leap powered by a great spring.",
  hp=1.2, dmg=1.3, armor=1.4, aggro=True, specials=[big("Coiled Leap", 0.22, 1.8, "compresses its springs and leaps on you!")],
  loot=[("piston_sabatons", 0.04)], gold=0.6)
M("unfinished_automaton", "an unfinished automaton", 42, "A half-built automaton missing a hand or a face, shuffling between the benches, trying to finish itself.",
  hp=1.4, dmg=1.3, armor=1.6, specials=[big("Grasping Clamp", 0.12, 1.6, "grips you in a clamp where a hand should be!")],
  loot=[("wound_mainspring", 0.35), ("clockwork_warhelm", 0.03)], gold=1.2)
M("molten_spring", "a molten spring", 42, "A coil of white-hot steel that has escaped the crucible and writhes across the foundry floor like a snake.",
  hp=1.0, dmg=1.35, armor=0.8, aggro=True, element="fire",
  specials=[dot("White Heat", 0.25, 0.5, 3, "fire", "coils around you, white-hot!")],
  loot=[("supreme_mana_potion", 0.1)], gold=0.8)
M("master_automaton", "the Master Automaton", 42, "Orrin's first and finest creation, a towering automaton in a leather apron who has kept the workshop running for three hundred years.",
  hp=2.0, dmg=1.3, armor=2.0, xp=1.8, gold=3.0,
  specials=[big("Hammer and Anvil", 0.22, 1.9, "brings a smith's hammer down on you as if you were an anvil!"),
            heal("Self-Repair", 0.1, 0.12, "tightens a few bolts in its own chest, and its damage is mended!")],
  loot=[("gearwork_blade", 0.25), ("wound_mainspring", 1.0)])
M("escapement_guardian", "an escapement guardian", 43, "A guardian of black iron that moves in time with the great escapement, one lurching step at every tick.",
  hp=1.6, dmg=1.3, armor=2.2, aggro=True,
  specials=[big("Toothed Wheel", 0.2, 1.8, "swings a toothed iron wheel into you!"),
            big("On the Tick", 0.1, 1.6, "strikes exactly on the tick, and you lose a beat!")],
  loot=[("cog_shield", 0.04), ("clockwork_warhelm", 0.03), ("brass_scale_hauberk", 0.03)], gold=1.6)
M("orrin_gearwhistle", "Orrin Gearwhistle, Wound into the Clock", 44,
  "The gnome inventor of the Clockwork Orchard, three hundred years old, wired into the golden sun of the great orrery "
  "with a key turning slowly in his back. The planets of brass swing around him at his command.",
  hp=2.9, dmg=1.3, armor=1.6, aggro=True, boss=True, xp=2.0, gold=7.0,
  specials=[big("Swing of the Planets", 0.2, 2.0, "sends a planet of brass sweeping through you!"),
            big("Stopped Clock", 0.12, 1.6, "stops the clock, and for a moment you cannot move!"),
            dot("Steam Vent", 0.18, 0.5, 4, "fire", "opens a valve, and scalding steam pours over you!"),
            heal("Rewind", 0.1, 0.12, "winds himself back a few seconds, and his wounds unhappen!")],
  loot=[("orrins_wrench", 0.5), ("pendulum_staff", 0.5), ("orrery_amulet", 0.6)])

# ------------------------------------------------------------- Scorchsands (35-49)
M("desert_raider", "a desert raider", 36, "A veiled rider of the deep desert, all in black, with a scimitar and eyes that never blink.",
  hp=1.1, dmg=1.25, specials=[dot("Curved Cut", 0.2, 0.4, 3, "bleed", "wheels and slashes you with a curved blade!")],
  loot=[("sunsteel_scimitar", 0.03), ("sand_strider_boots", 0.02)], gold=2.0)
M("dune_scorpion", "a dune scorpion", 38, "A pale scorpion longer than a camel, buried in the sand until it strikes.",
  hp=1.4, dmg=1.25, armor=1.8, specials=[dot("Deathstalker Venom", 0.22, 0.45, 3, "poison", "erupts from the sand and stings you!")],
  loot=[("scorpion_stinger", 0.5), ("desert_glass", 0.15)], gold=0.5, xp=1.3)
M("salt_wraith", "a salt wraith", 40, "The dried, white husk of a traveller who died on the salt flats, drifting on the hot wind.",
  hp=1.0, dmg=1.3, armor=0.6, aggro=True, specials=[drain("Thirst", 0.25, 1.0, "touches you, and the water is drawn from your body!")],
  loot=[("supreme_healing_potion", 0.08), ("desert_glass", 0.1)], gold=0.8)
M("mirage_stalker", "a mirage stalker", 42, "A lean desert cat whose hide bends the light, so that you only see it when it moves.",
  hp=1.2, dmg=1.3, specials=[big("Ambush", 0.22, 1.8, "appears out of a shimmer of heat and pounces!")],
  loot=[("desert_glass", 0.25), ("silkwind_gloves", 0.03)], gold=0.6)
M("wild_djinn", "a wild djinn", 44, "A towering figure of smoke and fire with burning eyes, bound to no lamp and no master.",
  hp=1.2, dmg=1.3, armor=0.9, aggro=True, specials=[dot("Sirocco", 0.22, 0.5, 3, "fire", "spins into a howling wind of burning sand!"),
                                                    big("Bewitch", 0.1, 1.6, "laughs, and the desert spins around you!")],
  loot=[("obelisk_amulet", 0.03), ("sunfire_staff", 0.03), ("supreme_mana_potion", 0.15)], gold=1.5)
M("sand_giant", "a sand giant", 46, "A giant with skin like sandstone and a beard of dried grass, carrying a pillar from some ruined temple.",
  hp=1.9, dmg=1.3, armor=1.6, specials=[big("Pillar Smash", 0.25, 1.9, "swings a stone pillar into you like a club!")],
  loot=[("sunsteel_greaves", 0.04), ("crescent_greatsword", 0.03), ("ancient_scarab", 0.1)], gold=2.0, xp=1.6)
M("great_sandworm", "a great sandworm", 49, "A worm as wide as a house, ringed with plates of yellow chitin, its round mouth lined with teeth.",
  hp=2.2, dmg=1.35, armor=1.8, specials=[big("Engulf", 0.22, 2.0, "rises from the sand beneath you and engulfs you!"),
                                         big("Quake", 0.1, 1.6, "thrashes, and the sand heaves you off your feet!")],
  loot=[("desert_glass", 0.4), ("sunstone_ring", 0.04)], gold=1.5, xp=1.8)

# ------------------------------------------------------------- The Sugarwold (44-49)
# Madame Marchpane's country of sweets beneath the Salt Pans. Its creatures are content to be left
# alone; only her gingerbread soldiers, her oven imps and the witch herself attack on sight.
M("gumdrop_ooze", "a gumdrop ooze", 44, "A wobbling green gumdrop the size of a wagon, sugar-crusted and glistening, with something dark suspended in its middle.",
  hp=1.3, dmg=1.25, armor=0.8, specials=[big("Sticky Engulf", 0.12, 1.6, "rolls over you, and you are stuck fast in sugar!")],
  loot=[("gumdrop", 0.5), ("supreme_healing_potion", 0.06)], gold=0.6)
M("sugar_sprite", "a sugar sprite", 45, "A tiny winged figure of spun sugar, giggling, carrying a lollipop like a sceptre.",
  hp=1.0, dmg=1.3, armor=0.6, specials=[big("Sugar Rush", 0.14, 1.6, "blows a cloud of glittering sugar into your eyes, and the world spins!")],
  loot=[("spun_sugar_cowl", 0.04), ("rock_candy_dagger", 0.03), ("supreme_mana_potion", 0.12)], gold=1.2)
M("peppermint_hog", "a peppermint hog", 45, "A hog as big as an ox, striped red and white like a peppermint stick, with tusks of boiled sugar.",
  hp=1.4, dmg=1.25, specials=[big("Candied Tusks", 0.2, 1.7, "lowers its head and gores you with its sugar tusks!")],
  loot=[("peppermint_hide", 0.5), ("peppermint_boots", 0.04)], gold=0.4)
M("licorice_serpent", "a licorice serpent", 46, "A long black serpent of twisted licorice, thick as a man, gleaming wetly, with a forked tongue of red sugar.",
  hp=1.2, dmg=1.3, specials=[dot("Bitter Bite", 0.22, 0.45, 3, "poison", "bites you, and a bitter black poison burns in your blood!")],
  loot=[("licorice_hood", 0.04), ("taffy_gloves", 0.03)], gold=0.6)
M("toffee_lurker", "a toffee lurker", 46, "A heap of hot golden toffee that rises from the pits in the rough shape of a man, dripping and cooling as it comes.",
  hp=1.6, dmg=1.25, armor=1.2, specials=[big("Sticky Grip", 0.12, 1.6, "wraps you in cooling toffee, and you cannot move!"),
                                         dot("Scalding Sugar", 0.15, 0.4, 3, "fire", "splashes you with scalding toffee!")],
  loot=[("toffee_greaves", 0.04), ("striped_trousers", 0.04)], gold=0.8, xp=1.3)
M("candied_raven", "a candied raven", 47, "A raven as big as an eagle, its feathers glazed in hard, glittering sugar. It caws in a voice like a child's.",
  hp=1.1, dmg=1.35, specials=[dot("Glass Beak", 0.2, 0.45, 3, "bleed", "pecks you with a beak as sharp as broken sugar-glass!")],
  loot=[("gumdrop_slippers", 0.04), ("peppermint_amulet", 0.03)], gold=0.8)
M("gingerbread_man", "a gingerbread man", 47, "A man-sized figure of gingerbread with gumdrop buttons and a smile of white icing. Its currant eyes look as if they are trying to tell you something.",
  hp=1.4, dmg=1.3, specials=[big("Hard-Baked Fist", 0.2, 1.8, "swings a fist baked as hard as brick!")],
  loot=[("gumdrop_button", 0.6), ("gingerbread_gauntlets", 0.03)], gold=1.5)
M("gingerbread_soldier", "a gingerbread soldier", 48, "A gingerbread soldier in a coat of red and white frosting, with raisin eyes and a candy-cane bayonet.",
  hp=1.5, dmg=1.35, armor=2.0, aggro=True, specials=[big("Bayonet Thrust", 0.2, 1.8, "lunges and drives its candy-cane bayonet into you!")],
  loot=[("candy_cane_mace", 0.04), ("gingerbread_shield", 0.04), ("supreme_healing_potion", 0.08)], gold=2.2)
M("sugarloaf_golem", "a sugarloaf golem", 48, "A hulking giant of crusted sugar, shaped roughly like a man by enormous hands, with lumps of rock candy for eyes.",
  hp=2.0, dmg=1.3, armor=2.5, specials=[big("Sugarloaf Slam", 0.22, 1.9, "raises both crusted fists and brings them crashing down!")],
  loot=[("rock_candy_dagger", 0.04), ("peppermint_amulet", 0.04)], gold=1.5, xp=1.6)
M("oven_imp", "an oven imp", 48, "A little red imp with a coal-black tail and a toasting fork, sooty from the witch's stoves and grinning with sharp teeth.",
  hp=1.2, dmg=1.4, aggro=True, element="fire", specials=[dot("Toasting Fork", 0.22, 0.5, 3, "fire", "jabs you with a red-hot toasting fork!")],
  loot=[("supreme_mana_potion", 0.12), ("taffy_gloves", 0.03)], gold=1.8)
M("madame_marchpane", "Madame Marchpane", 49,
  "A plump, rosy old woman in a flour-white apron, with sugar in her grey curls and a smile as sweet as honey. "
  "Her eyes are as red as the oven behind her, and she has been baking for a thousand years.",
  hp=3.1, dmg=1.35, armor=1.7, aggro=True, boss=True, xp=2.0, gold=8.0,
  specials=[big("Have a Sweet, Dearie", 0.12, 1.6, "holds out a sugared plum, and before you know it you have eaten it, and your limbs grow heavy!"),
            dot("Boiling Syrup", 0.18, 0.5, 4, "fire", "flings a ladle of boiling syrup over you!"),
            big("The Rolling Pin", 0.18, 1.9, "brings her great black rolling pin down on you!"),
            heal("A Nibble of Gingerbread", 0.1, 0.12, "breaks a gingerbread figure in half and nibbles it, and her wounds close!")],
  loot=[("marchpane_rolling_pin", 0.5), ("sugarglass_wand", 0.5), ("spun_sugar_ring", 0.6), ("spun_sugar_cowl", 0.4)])

# ------------------------------------------------------------- Tomb of the Sand Kings (45-48)
M("scarab_swarm", "a scarab swarm", 45, "A clicking, glittering tide of black and gold beetles that pours across the floor.",
  hp=1.1, dmg=1.3, armor=1.0, specials=[dot("Devour", 0.25, 0.45, 3, "bleed", "pours over you, biting everywhere at once!")],
  loot=[("ancient_scarab", 0.3)], gold=0.4)
M("tomb_guardian", "a tomb guardian", 46, "A jackal-headed statue of black basalt, ten feet tall, that steps down from its plinth.",
  hp=2.0, dmg=1.3, armor=2.5, aggro=True, specials=[big("Basalt Halberd", 0.22, 1.9, "sweeps a halberd of black stone into you!")],
  loot=[("ancient_scarab", 0.3), ("sunsteel_mail", 0.03)], gold=1.5, xp=1.6)
M("mummy_priest", "a mummy priest", 47, "A withered priest in rotting linen and a collar of gold, still chanting the funeral rites of a dead empire.",
  hp=1.3, dmg=1.3, aggro=True, specials=[dot("Curse of the Tomb", 0.22, 0.5, 4, "shadow", "points at you and speaks a curse in a dead tongue!"),
                                         heal("Embalming Rite", 0.12, 0.15, "chants, and its wrappings draw tight over its wounds!")],
  loot=[("ancient_scarab", 0.4), ("scepter_of_the_sand_kings", 0.01), ("silkwind_slippers", 0.04)], gold=2.0)
M("ussreth", "Ussreth, the Last Sand King", 48,
  "The last king of the sand-empire, three thousand years dead, in a burial mask of gold and robes of rotted purple. "
  "Sand pours from the joints of his armour, and his eyes are two points of blue fire.",
  hp=3.0, dmg=1.35, armor=1.8, aggro=True, boss=True, xp=2.0, gold=8.0,
  specials=[big("Khopesh of the Kings", 0.22, 2.0, "sweeps his bronze khopesh through you!"),
            dot("Plague of Ages", 0.18, 0.5, 4, "shadow", "breathes a cloud of ancient dust that rots your flesh!"),
            big("Command", 0.12, 1.6, "speaks a word of command, and you kneel!"),
            drain("Eternity's Thirst", 0.12, 1.2, "seizes you, and three thousand years of hunger drink your life!")],
  loot=[("khopesh_of_ussreth", 0.5), ("scepter_of_the_sand_kings", 0.5), ("burial_mask", 0.6), ("ancient_scarab", 1.0)])

# ------------------------------------------------------------- Ashen Peaks & Dragon's Lair (37-52)
M("steam_wraith", "a steam wraith", 38, "A writhing column of scalding vapour where meltwater meets the mountain's fire.",
  hp=1.0, dmg=1.25, armor=0.6, aggro=True, specials=[dot("Scald", 0.25, 0.45, 3, "fire", "wraps around you in a cloud of scalding steam!")],
  loot=[("frost_shard", 0.2), ("supreme_mana_potion", 0.05)], gold=0.8)
M("cinder_hound", "a cinder hound", 39, "A lean black hound with coals for eyes, its hide cracked to show the fire beneath.",
  hp=1.1, dmg=1.25, specials=[dot("Burning Bite", 0.22, 0.4, 3, "fire", "sinks its smouldering teeth into your leg!")],
  loot=[("ember_ring", 0.02)], gold=0.4)
M("lava_troll", "a lava troll", 40, "A hunched troll with skin like cooling basalt, magma oozing from every wound.",
  hp=1.6, dmg=1.25, specials=[heal("Magma Blood", 0.15, 0.12, "regenerates, molten rock sealing its wounds!"),
                              big("Basalt Fist", 0.2, 1.7, "slams you with a fist of glowing rock!")],
  loot=[("supreme_healing_potion", 0.12), ("dragon_scale", 0.1)], gold=1.3, xp=1.3)
M("fire_elemental", "a fire elemental", 41, "A roaring pillar of living flame, vaguely human in shape.",
  hp=1.1, dmg=1.25, armor=0.8, aggro=True, specials=[dot("Immolate", 0.25, 0.45, 3, "fire", "engulfs you in roaring flames!")],
  loot=[("supreme_mana_potion", 0.1)], gold=0.8)
M("salamander", "a magma salamander", 42, "A huge red lizard whose skin glows like coals.",
  hp=1.2, dmg=1.25, specials=[dot("Burning Bite", 0.2, 0.4, 3, "fire", "bites you with searing jaws!")],
  loot=[("drakehide_boots", 0.03)], gold=0.8)
M("ash_drake", "an ash drake", 44, "A wingless young dragon, grey as cinders, smoke curling from its nostrils.",
  hp=1.5, dmg=1.3, armor=1.5, specials=[big("Cinder Breath", 0.25, 1.8, "breathes a gout of burning cinders over you!")],
  loot=[("dragon_scale", 0.2), ("drakehide_boots", 0.06), ("ember_ring", 0.03)], gold=1.5, xp=1.4)
M("dragonkin_guard", "a dragonkin guard", 45, "A scaled warrior of the dragon cult, wielding an obsidian glaive.",
  hp=1.3, dmg=1.3, armor=1.8, aggro=True, loot=[("obsidian_greaves", 0.05), ("obsidian_blade", 0.04), ("sunforged_mace", 0.03)], gold=2.0)
M("obsidian_golem", "an obsidian golem", 46, "A towering construct of black volcanic glass, magma glowing in its cracks.",
  hp=2.0, dmg=1.3, armor=3.0, specials=[big("Shattering Fist", 0.25, 1.9, "smashes you with a fist of volcanic glass!")],
  loot=[("obsidian_greaves", 0.08), ("obsidian_blade", 0.06)], gold=1.5, xp=1.7)
M("cult_flamecaller", "a dragon cult flamecaller", 47, "A robed priest of Pyraxis with a mask of red scales, fire coiling around his hands.",
  hp=1.3, dmg=1.4, aggro=True, specials=[dot("Dragon's Breath", 0.22, 0.5, 3, "fire", "spreads his hands and breathes fire like his master!"),
                                         heal("Scales of Devotion", 0.12, 0.2, "chants the name of Pyraxis, and his burns fade!")],
  loot=[("dragonbone_staff", 0.04), ("ashen_crown", 0.03), ("supreme_mana_potion", 0.15)], gold=2.2)
M("flame_demon", "a flame demon", 48, "A horned demon of fire and shadow with a whip of living flame.",
  hp=1.4, dmg=1.35, armor=1.5, aggro=True, specials=[dot("Hellfire Lash", 0.25, 0.5, 3, "fire", "lashes you with a whip of hellfire!"),
                                                     big("Terrify", 0.1, 1.6, "roars, and terror roots you to the spot!")],
  loot=[("ashen_crown", 0.04), ("dragonbone_staff", 0.04), ("supreme_healing_potion", 0.15)], gold=2.0, xp=1.3)
M("magma_titan", "a magma titan", 50, "A colossus of molten rock, each footstep leaving a pool of fire.",
  hp=2.2, dmg=1.35, armor=2.0, specials=[big("Eruption", 0.25, 1.9, "erupts in a fountain of molten rock!")],
  loot=[("ember_ring", 0.08), ("dragon_scale", 0.4), ("ashen_crown", 0.05)], gold=2.5, xp=1.8)
M("pyraxis", "Pyraxis the Eternal Flame", 52,
  "An ancient red dragon, vast beyond belief, its scales like molten rubies and its eyes like twin suns.",
  hp=3.5, dmg=1.4, armor=2.0, aggro=True, boss=True, xp=2.0, gold=10.0,
  specials=[big("Dragonfire", 0.25, 2.2, "rears back and engulfs you in a torrent of dragonfire!"),
            dot("Searing Wounds", 0.15, 0.5, 4, "fire", "rakes you with claws that leave searing wounds!"),
            big("Wing Buffet", 0.12, 1.6, "buffets you to the ground with a mighty wing!")],
  loot=[("pyraxis_fang", 0.7), ("dragonscale_mail", 0.7), ("heart_of_flame", 0.5), ("dragon_scale", 1.0)])

# ------------------------------------------------------------- Thornwick Hall (40-50)
# The Vane household. Only the wardens, knights and sworn swords attack on sight; everyone else
# fights when attacked. The named servants and family are tougher, but only the lord is a boss.
M("vane_huntsman", "a Vane huntsman", 40, "A lean huntsman in green and silver livery, a boar spear in his hands and a horn at his hip.",
  hp=1.1, dmg=1.25, specials=[big("Boar Spear", 0.2, 1.7, "drives his boar spear into you!")],
  loot=[("huntsmans_jerkin", 0.03), ("huntsmans_breeches", 0.03)], gold=1.0)
M("vane_boarhound", "a Vane boarhound", 40, "A huge brindled hound in a spiked collar, bred to pull down boar and stag.",
  hp=1.0, dmg=1.25, specials=[big("Pull Down", 0.2, 1.6, "leaps, seizes you by the arm and drags you down!")],
  gold=0.2)
M("hobb_gamekeeper", "Hobb the gamekeeper", 42, "The Vanes' gamekeeper, broad as a door, with a skinning knife, a longbow and a sack of snares.",
  hp=1.9, dmg=1.3, xp=1.6, gold=1.5,
  specials=[big("Broadhead", 0.2, 1.8, "looses a broadhead arrow into you at point-blank range!"),
            big("Snare", 0.12, 1.6, "flicks a snare around your ankle and yanks you off your feet!")],
  loot=[("vane_hunting_bow", 0.15), ("huntsmans_jerkin", 0.1), ("huntsmans_breeches", 0.1)])
M("gate_warden", "a gate warden", 41, "A grim warden of the Vane gate in a mail coat and a green surcoat, a halberd in his fists.",
  hp=1.3, dmg=1.3, armor=1.8, aggro=True, specials=[big("Halberd", 0.18, 1.7, "swings his halberd down on you!")],
  loot=[("vane_gauntlets", 0.03), ("supreme_healing_potion", 0.06)], gold=1.5)
M("under_gardener", "an under-gardener", 40, "A sunburnt gardener in a straw hat, a pruning hook in his hand.",
  hp=0.9, dmg=1.2, loot=[("huntsmans_breeches", 0.02)], gold=0.8, xp=0.9)
M("vane_groundskeeper", "the groundskeeper", 42, "A gnarled old man with shears as long as a sword, who has kept the Vanes' hedges for fifty years.",
  hp=1.3, dmg=1.3, specials=[big("Hedge Shears", 0.22, 1.8, "snips at you with his great shears!")],
  loot=[("supreme_healing_potion", 0.08)], gold=1.2, xp=1.1)
M("vane_groom", "a Vane groom", 41, "A wiry groom in green livery, smelling of horse and saddle soap.",
  hp=0.9, dmg=1.2, gold=0.8, xp=0.9)
M("vane_stablemaster", "the stablemaster", 43, "A big, red-faced man with a coachman's whip and a voice that carries across three fields.",
  hp=1.6, dmg=1.3, xp=1.3, gold=1.5,
  specials=[big("Whip Crack", 0.15, 1.6, "cracks his whip around your neck and jerks you off balance!"),
            big("Hobnailed Kick", 0.18, 1.7, "kicks you like a carthorse!")],
  loot=[("huntsmans_breeches", 0.06)])
M("house_chaplain", "the house chaplain", 43, "A plump priest of the Dawnfather in white and gold, who preaches obedience to the Vanes every morning.",
  hp=1.3, dmg=1.25, gold=2.0,
  specials=[heal("Blessing of the House", 0.15, 0.15, "prays, and light knits his wounds!"),
            big("Rebuke", 0.12, 1.6, "raises his sun-disc and speaks a word of rebuke that roots you in place!")],
  loot=[("supreme_healing_potion", 0.15), ("supreme_mana_potion", 0.1)])
M("vane_footman", "a Vane footman", 42, "A tall footman in a powdered wig and green-and-silver livery, chosen for his height and his calves.",
  hp=1.0, dmg=1.25, loot=[("vane_silver", 0.3)], gold=1.2)
M("vane_housemaid", "a housemaid", 41, "A housemaid in a black dress and white apron, carrying a coal scuttle she is ready to swing.",
  hp=0.8, dmg=1.15, loot=[("vane_silver", 0.15)], gold=0.8, xp=0.8)
M("kitchen_hand", "a kitchen hand", 42, "A sweating kitchen hand, scarred from spits and ovens, with a carving knife in his fist.",
  hp=0.9, dmg=1.2, specials=[dot("Scalding Water", 0.18, 0.35, 3, "fire", "dashes a pan of boiling water over you!")],
  gold=0.6, xp=0.9)
M("vane_laundress", "a laundress", 42, "A broad laundress with forearms like hams and a paddle for beating linen.",
  hp=0.9, dmg=1.2, specials=[big("Wet Sheet", 0.12, 1.6, "throws a sodden sheet over your head!")],
  gold=0.6, xp=0.9)
M("vane_cellarer", "the cellarer", 43, "A red-nosed, barrel-chested man with a mallet for driving taps, and a strong smell of wine.",
  hp=1.5, dmg=1.3, xp=1.2, gold=1.5, specials=[big("Cask Mallet", 0.2, 1.8, "swings his heavy mallet at your head!")],
  loot=[("supreme_mana_potion", 0.12)])
M("mistress_hollin", "Mistress Hollin, the cook", 44, "A vast, floury woman who rules the kitchens of Thornwick like a warlord, a cleaver in one hand and a ladle in the other.",
  hp=2.0, dmg=1.35, xp=1.7, gold=2.0,
  specials=[big("Cleaver", 0.22, 1.9, "brings her cleaver down like an executioner!"),
            dot("Boiling Pot", 0.15, 0.45, 3, "fire", "flings a pot of boiling stock over you!")],
  loot=[("cooks_cleaver", 0.2), ("supreme_healing_potion", 0.2)])
M("mr_graves", "Mr. Graves, the butler", 44, "The butler of Thornwick Hall, tall and grave in perfect black, who has never once raised his voice.",
  hp=2.0, dmg=1.3, armor=1.5, xp=1.7, gold=3.0,
  specials=[big("Silver Salver", 0.15, 1.6, "strikes you across the temple with a silver salver!"),
            big("Corkscrew", 0.18, 1.8, "drives a corkscrew into you with a flick of his wrist!")],
  loot=[("silver_salver", 0.2), ("vane_silver", 1.0)])
M("household_knight", "a knight of the household", 45, "A knight of the Vane household in plate enamelled green, a silver stag on his shield.",
  hp=1.4, dmg=1.3, armor=2.0, aggro=True, specials=[big("Shield Bash", 0.18, 1.7, "slams his shield into you!")],
  loot=[("vane_warhelm", 0.03), ("vane_gauntlets", 0.03), ("vane_heirloom_plate", 0.01)], gold=2.0)
M("noble_guest", "a noble guest", 44, "A guest of the house in silk and velvet, flushed with wine, wearing a jewelled court sword.",
  hp=1.0, dmg=1.25, loot=[("vane_silver", 0.2), ("silk_evening_gloves", 0.02)], gold=2.5)
M("visiting_knight", "a visiting knight", 46, "A knight from a neighbouring house, here for the feast and the tourney, in polished steel.",
  hp=1.4, dmg=1.3, armor=1.6, specials=[big("Overhand Blow", 0.2, 1.8, "brings his longsword down in a great overhand blow!")],
  loot=[("vane_warhelm", 0.03), ("supreme_healing_potion", 0.08)], gold=2.0)
M("household_minstrel", "a household minstrel", 45, "A minstrel in particoloured hose with a lute on his back and a knife in his boot.",
  hp=1.0, dmg=1.25, specials=[big("Dizzying Air", 0.12, 1.6, "plays a whirling air that sets your head spinning!")],
  loot=[("minstrels_lute", 0.05)], gold=1.5)
M("vane_steward", "Master Aldous, the steward", 46, "The steward of Thornwick, thin and grey, with a ring of keys at his belt and the rents of the valley in his head.",
  hp=1.5, dmg=1.3, xp=1.3, gold=4.0, specials=[big("Ring of Keys", 0.12, 1.6, "lashes you across the face with his heavy ring of keys!")],
  loot=[("vane_ledger", 0.6), ("supreme_mana_potion", 0.1)])
M("estate_clerk", "an estate clerk", 45, "An ink-stained clerk in a black gown, with a quill behind his ear and a penknife in his hand.",
  hp=0.9, dmg=1.2, loot=[("vane_ledger", 0.4)], gold=1.5, xp=0.9)
M("lady_in_waiting", "a lady-in-waiting", 46, "A noblewoman in attendance on Lady Seraphine, in a gown of green brocade, with a long jewelled pin in her hair.",
  hp=1.0, dmg=1.3, specials=[dot("Hatpin", 0.2, 0.4, 3, "poison", "stabs you with a long jewelled pin dipped in something!")],
  loot=[("vane_brooch", 0.45), ("silk_evening_gloves", 0.03)], gold=2.0)
M("lady_seraphine", "Lady Seraphine Vane", 47, "The lord's young wife, golden-haired and lovely, with a long golden pin in her hair and a smile that never reaches her eyes.",
  hp=2.0, dmg=1.35, xp=1.7, gold=4.0,
  specials=[dot("Poisoned Hairpin", 0.22, 0.5, 4, "poison", "draws the golden pin from her hair and stabs it into your neck!"),
            big("Faint", 0.1, 1.6, "swoons into your arms, and the knife in her sleeve finds your ribs!")],
  loot=[("seraphines_hairpin", 0.2), ("brocade_gown", 0.1), ("vane_brooch", 1.0)])
M("sir_corwin", "Sir Corwin Vane", 47, "The lord's cousin and heir, handsome, drunk and dangerous, the finest duellist in the valley.",
  hp=2.1, dmg=1.4, xp=1.7, gold=4.0,
  specials=[big("Riposte", 0.22, 1.9, "turns your attack aside and ripostes straight through your guard!"),
            dot("Flickering Cuts", 0.15, 0.45, 3, "bleed", "flicks his rapier across you in a dozen tiny cuts!")],
  loot=[("corwins_rapier", 0.2), ("supreme_healing_potion", 0.2)])
M("master_tobias", "Master Tobias Vane", 47, "The lord's younger brother, a pale scholar of twenty with ink on his fingers and a forbidden book under his arm.",
  hp=1.8, dmg=1.35, xp=1.7, gold=3.0,
  specials=[dot("Half-Learned Curse", 0.2, 0.5, 3, "shadow", "reads a curse from his black book, and your skin blisters!"),
            big("Word of Binding", 0.12, 1.6, "speaks a word of binding, and your limbs lock!")],
  loot=[("tobias_grimoire", 0.2), ("supreme_mana_potion", 0.2)])
M("dowager_attendant", "a dowager's attendant", 47, "A silent woman in grey who has served the Dowager for thirty years, a stiletto at her girdle.",
  hp=1.2, dmg=1.3, loot=[("vane_brooch", 0.25)], gold=2.0)
M("dowager_isolde", "Lady Isolde, the Dowager", 48, "The lord's mother, iron-grey and straight as a blade, who has ruled Thornwick for forty years. Her ebony cane hides a sword.",
  hp=2.2, dmg=1.35, armor=1.3, xp=1.8, gold=5.0,
  specials=[big("Cane Sword", 0.22, 1.9, "draws the blade from her ebony cane and runs you through!"),
            big("Withering Glare", 0.12, 1.6, "fixes you with a glare that has cowed lords, and you falter!")],
  loot=[("dowagers_pearls", 0.25), ("supreme_healing_potion", 0.2)])
M("great_aunt_mathilde", "Great-aunt Mathilde", 46, "A tiny, ancient lady in an enormous lace cap, wearing a fortune in jewels and brandishing a knitting needle.",
  hp=0.7, dmg=1.0, xp=0.8, gold=8.0, specials=[dot("Knitting Needle", 0.2, 0.3, 3, "bleed", "jabs you smartly with a knitting needle!")],
  loot=[("mathildes_cameo", 0.3), ("vane_brooch", 1.0)])
M("vane_sworn_sword", "a Vane sworn sword", 49, "One of the lord's own sworn swords, in full plate of green and silver with a stag-crested helm.",
  hp=1.5, dmg=1.35, armor=2.2, aggro=True, specials=[big("Greatsword", 0.2, 1.8, "cleaves into you with a two-handed greatsword!")],
  loot=[("vane_warhelm", 0.04), ("vane_gauntlets", 0.04), ("vane_heirloom_plate", 0.02)], gold=2.5)
M("lord_aldric_vane", "Lord Aldric Vane", 50,
  "The Lord of Thornwick, in the ancient green-and-silver plate of his house, with the Vane longsword in his hand. "
  "A veteran of three wars and a hundred hunts, proud, cold and very, very good with a blade.",
  hp=3.4, dmg=1.4, armor=2.0, aggro=True, boss=True, xp=2.0, gold=9.0,
  specials=[big("The Vane Longsword", 0.22, 2.0, "brings the ancestral longsword of his house down on you!"),
            dot("Rending Cut", 0.15, 0.5, 4, "bleed", "opens a long, deep wound with a drawing cut!"),
            big("Shield Bash", 0.12, 1.6, "smashes his shield into your face!"),
            heal("Second Wind", 0.1, 0.12, "steps back, breathes, and comes on again as fresh as ever!")],
  loot=[("vane_longsword", 0.5), ("vane_heirloom_plate", 0.5), ("vane_signet", 0.6), ("vane_silver", 1.0)])

# ------------------------------------------------------------- The Planes of the Gods (51-60)
# Tuned for reborn characters, whose stats are the best of every class they have lived (not a sum):
# first-tier monsters are a coin flip for one life and easy with six; champions ~80-95% with six lives;
# the elemental lords need nearly every class (~95% with all 11); Lord Trepth ~70% with all 11.
# Check with `python tools/balance_sim.py endgame`.

# First tier (51-55): the Planes of Stars, Dreams, Death and Law
M("star_eagle", "a star eagle", 51, "An eagle with a wingspan wider than a ship, its feathers dark as the night sky and pricked with stars.",
  hp=3.8, dmg=2.9, armor=2.0, specials=[big("Falling Star", 0.2, 1.8, "folds its wings and strikes like a falling star!")],
  loot=[("planar_shard", 0.1)], gold=2.0)
M("celestial_sentinel", "a celestial sentinel", 53, "A towering knight of silver and white starlight, set to guard the roads between the stars for all time.",
  hp=3.8, dmg=2.6, armor=2.5, aggro=True, specials=[big("Starburst", 0.12, 1.6, "raises its gauntlets, and a burst of starlight leaves you senseless!")],
  loot=[("planar_shard", 0.15)], gold=2.5)
M("dreamstalker", "a dreamstalker", 52, "A long, pale hunter that slips from one dream to the next, wearing the shape of something you were afraid of as a child.",
  hp=3.6, dmg=2.9, armor=2.0, specials=[dot("Waking Nightmare", 0.2, 0.5, 3, "bleed", "steps out of nowhere and its claws find you!")],
  loot=[("planar_shard", 0.1)], gold=2.0)
M("sleepwalker", "a sleepwalking giant", 54, "A giant as tall as a tower who walks with its eyes shut, lost in a dream older than the mountains.",
  hp=4.2, dmg=2.6, armor=2.5, specials=[heal("Deeper Sleep", 0.12, 0.12, "sinks into a deeper sleep, and its wounds fade like a dream!"),
                                        big("Dreaming Blow", 0.2, 1.9, "swings at something only it can see, and hits you!")],
  loot=[("planar_shard", 0.15)], gold=2.0, xp=1.3)
M("pale_horse", "a pale horse", 52, "A horse the colour of bone, with no rider and no shadow, that carries the dead to where they are going.",
  hp=3.6, dmg=2.9, armor=2.0, aggro=True, specials=[big("Chill of the Grave", 0.14, 1.6, "breathes on you, and the cold of the grave holds you still!")],
  loot=[("planar_shard", 0.1)], gold=2.0)
M("reaper", "a reaper", 54, "A hooded figure of bone and grey smoke with a scythe of black iron, who gathers the souls of the dead.",
  hp=3.6, dmg=2.8, armor=1.5, aggro=True, specials=[drain("Harvest", 0.22, 1.2, "draws its scythe through you, and reaps a little of your life!")],
  loot=[("planar_shard", 0.15)], gold=2.5)
M("caelestra", "Caelestra, the Star-Warden", 55,
  "The guardian of the Plane of Stars, a woman of silver and night with wings of starlight, and a bow strung with a thread of light in her hand.",
  hp=6.6, dmg=2.9, armor=2.0, aggro=True, boss=True, xp=2.0, gold=12.0,
  specials=[big("Shooting Star", 0.22, 2.0, "draws her bow, and a shooting star strikes you!"),
            big("Eclipse", 0.12, 1.6, "folds her wings over the stars, and you stagger blind in the dark!"),
            heal("Starlight", 0.08, 0.1, "bathes in starlight, and her wounds close!")],
  loot=[("stormcaller_bow", 0.4), ("starweave_robes", 0.4), ("starstep_slippers", 0.4), ("planar_shard", 1.0)])
M("somnara", "Somnara, the Dreamweaver", 55,
  "The guardian of the Plane of Dreams, a tall woman of moonlight and grey silk crowned with sleeping moths, who weaves "
  "the dreams of every living thing on a loom of silver.",
  hp=6.3, dmg=2.45, armor=2.0, aggro=True, boss=True, xp=2.0, gold=12.0,
  specials=[dot("Smothering Dream", 0.2, 0.6, 4, "arcane", "wraps you in a dream that will not let you breathe!"),
            big("Endless Sleep", 0.12, 1.6, "sings a single note, and you fall asleep where you stand!"),
            heal("Lucid Mending", 0.1, 0.12, "dreams herself whole again!")],
  loot=[("dreamweaver_staff", 0.4), ("dreamsilver_greaves", 0.4), ("dreamsilk_trousers", 0.4), ("planar_shard", 1.0)])
M("morthis", "Morthis, Keeper of the Dead", 55,
  "The guardian of the Plane of Death, a gaunt giant in a robe of grey ash with a lantern of cold blue fire, who has "
  "counted every soul that ever died and has a place ready for yours.",
  hp=4.85, dmg=2.3, armor=1.8, aggro=True, boss=True, xp=2.0, gold=12.0,
  specials=[drain("Toll of the Dead", 0.2, 1.4, "names the hour of your death, and your life drains toward it!"),
            big("Grave Cold", 0.14, 1.6, "lifts his lantern, and the cold of the grave stops your heart for a moment!"),
            big("Last Rites", 0.18, 2.0, "brings down his staff of bone like a closing coffin lid!")],
  loot=[("gravesong", 0.4), ("death_mask", 0.4), ("ferrymans_gloves", 0.4), ("planar_shard", 1.0)])

M("chained_penitent", "a chained penitent", 52, "A giant prisoner bound in chains of light, serving a sentence a thousand years long, who swings those chains at anyone who comes near.",
  hp=3.6, dmg=2.9, armor=2.0, specials=[big("Flail of Chains", 0.2, 1.8, "whirls its chains and brings them crashing down on you!")],
  loot=[("planar_shard", 0.1)], gold=2.0)
M("iron_warden", "an iron warden", 53, "A gaoler of the gods in a full suit of black iron, with a ring of keys at its belt and no face behind its visor.",
  hp=3.8, dmg=2.7, armor=2.6, aggro=True, specials=[big("Shackle", 0.14, 1.6, "snaps a shackle of light around your wrists!")],
  loot=[("planar_shard", 0.15)], gold=2.5)
M("stalworth", "Stalworth Lightbearer", 55,
  "The warden of the Plane of Law, a paladin in white plate who was the first mortal ever judged worthy to serve "
  "Lord Trepth. His sword is engraved with every law of the gods, and his eyes see every crime you have ever committed.",
  hp=6.55, dmg=2.8, armor=2.4, aggro=True, boss=True, xp=2.0, gold=12.0,
  specials=[big("Smite the Guilty", 0.22, 2.0, "raises his blazing sword and smites you with the full weight of the law!"),
            big("Sentence Passed", 0.12, 1.6, "pronounces your sentence, and chains of light bind you where you stand!"),
            heal("Lay on Hands", 0.1, 0.12, "lays a hand on his own wounds, and holy light closes them!")],
  loot=[("lightbearers_oath", 0.4), ("shield_of_judgement", 0.4), ("planar_shard", 1.0)])

# Second tier (54-58): the elemental planes
M("efreet", "an efreet", 55, "A towering spirit of fire with brass bracers and a scimitar of white flame.",
  hp=4.3, dmg=3.0, armor=2.0, aggro=True, specials=[dot("Immolation", 0.22, 0.6, 3, "fire", "engulfs you in roaring white flame!")],
  loot=[("planar_shard", 0.2)], gold=3.0)
M("pyre_phoenix", "a pyre phoenix", 57, "A bird of living fire whose every wingbeat scatters burning feathers.",
  hp=5.04, dmg=3.2, armor=1.8, specials=[big("Phoenix Dive", 0.2, 1.9, "dives at you in a blaze of fire!"),
                                        heal("Rebirth Flame", 0.1, 0.15, "bursts into flame and rises renewed!")],
  loot=[("planar_shard", 0.25)], gold=3.0, xp=1.3)
M("tide_elemental", "a tide elemental", 55, "A towering wave that never breaks, with two cold eyes deep in its heart.",
  hp=4.5, dmg=2.9, armor=2.0, aggro=True, specials=[big("Undertow", 0.14, 1.6, "crashes over you and drags you under!")],
  loot=[("planar_shard", 0.2)], gold=3.0)
M("abyssal_kraken", "an abyssal kraken", 57, "A kraken from the lightless deeps, its tentacles as thick as towers.",
  hp=5.6, dmg=3.1, armor=2.2, specials=[big("Crushing Coils", 0.22, 1.9, "wraps you in its coils and squeezes!")],
  loot=[("planar_shard", 0.25)], gold=3.0, xp=1.3)
M("granite_elemental", "a granite elemental", 55, "A hulking shape of grey stone that walks through rock as if it were water.",
  hp=5.0, dmg=2.9, armor=3.0, aggro=True, specials=[big("Landslide", 0.2, 1.9, "becomes a landslide that rolls over you!")],
  loot=[("planar_shard", 0.2)], gold=3.0)
M("crystal_basilisk", "a crystal basilisk", 57, "An eight-legged lizard of living crystal whose gaze turns flesh to glass.",
  hp=5.15, dmg=3.1, armor=2.5, specials=[big("Petrifying Gaze", 0.15, 1.6, "meets your eyes, and your limbs turn to stone!"),
                                        dot("Shard Bite", 0.15, 0.5, 3, "bleed", "bites you with teeth of jagged crystal!")],
  loot=[("planar_shard", 0.25)], gold=3.0, xp=1.3)
M("storm_elemental", "a storm elemental", 55, "A spinning column of black cloud and lightning that howls like a hurricane.",
  hp=4.2, dmg=3.1, armor=1.6, aggro=True, specials=[dot("Static", 0.2, 0.5, 3, "lightning", "crackles, and lightning arcs through you!")],
  loot=[("planar_shard", 0.2)], gold=3.0)
M("thunderbird", "a thunderbird", 57, "A bird the size of a cloud, whose wingbeats are thunder and whose eyes are lightning.",
  hp=5.15, dmg=3.2, armor=1.8, specials=[big("Thunderstrike", 0.22, 1.9, "screams, and lightning falls from its eyes!")],
  loot=[("planar_shard", 0.25)], gold=3.0, xp=1.3)
M("lord_fire", "Rekkn, Lord of Flame", 58,
  "The lord of the Plane of Fire, a giant of white-hot stone with a crown of flame and a hammer that is a captive star.",
  hp=7.22, dmg=2.87, armor=2.2, aggro=True, boss=True, xp=2.0, gold=15.0,
  specials=[big("Starfall Hammer", 0.22, 2.1, "brings down a hammer that burns like a falling star!"),
            dot("Inferno", 0.18, 0.7, 4, "fire", "breathes, and the world becomes fire!"),
            big("Heatstroke", 0.1, 1.6, "flares so brightly that you reel, blinded!")],
  loot=[("flameheart_hammer", 0.4), ("gauntlets_of_the_pyre", 0.4), ("planar_shard", 1.0)])
M("lord_water", "Nerevos, Lord of the Tides", 58,
  "The lord of the Plane of Water, a crowned giant of green sea-glass with a trident of coral, whose voice is the roar of surf.",
  hp=10.53, dmg=3.49, armor=2.2, aggro=True, boss=True, xp=2.0, gold=15.0,
  specials=[big("Drowning Wave", 0.14, 1.6, "raises a wave that crashes down and drowns you!"),
            big("Trident Thrust", 0.2, 2.0, "drives his coral trident into you!"),
            heal("Tidal Renewal", 0.1, 0.1, "draws in the tide, and his wounds wash away!")],
  loot=[("tidecaller", 0.4), ("pearl_of_the_deep", 0.4), ("tidescale_legguards", 0.4), ("planar_shard", 1.0)])
M("lord_earth", "Ulmathra, Lord of Stone", 58,
  "The lord of the Plane of Earth, a mountain that stands and walks, with crystal eyes and a voice like the grinding of continents.",
  hp=9.97, dmg=3.37, armor=3.0, aggro=True, boss=True, xp=2.0, gold=15.0,
  specials=[big("Mountainfall", 0.22, 2.1, "falls on you like a mountain!"),
            big("Earthquake", 0.14, 1.6, "stamps, and the plane itself shakes you off your feet!"),
            heal("Stone Skin", 0.08, 0.1, "draws the plane's stone over his wounds!")],
  loot=[("mountainheart_shield", 0.4), ("stonestride_boots", 0.4), ("planar_shard", 1.0)])
M("lord_air", "Zephyrion, Lord of the Winds", 58,
  "The lord of the Plane of Air, a shape of silver wind and storm with a crown of lightning, never still and never solid.",
  hp=6.44, dmg=3.05, armor=1.8, aggro=True, boss=True, xp=2.0, gold=15.0,
  specials=[big("Hurricane", 0.22, 2.0, "becomes a hurricane that tears at you!"),
            dot("Lightning Storm", 0.18, 0.6, 4, "lightning", "calls down a storm of lightning on you!"),
            big("Breathless", 0.12, 1.6, "steals the air from your lungs!")],
  loot=[("windwalker_boots", 0.4), ("band_of_four_winds", 0.4), ("planar_shard", 1.0)])

# Third tier (57-60): the Plane of Eternity
M("chronal_sentinel", "a chronal sentinel", 57, "A knight of brass and crystal whose every movement leaves a trail of afterimages.",
  hp=5.6, dmg=3.4, armor=2.5, aggro=True, specials=[big("Time Lock", 0.15, 1.6, "touches you, and time stops for you alone!")],
  loot=[("planar_shard", 0.3)], gold=3.5)
M("hourglass_golem", "an hourglass golem", 58, "A colossus of glass and bronze with a storm of golden sand turning in its chest.",
  hp=5.6, dmg=3.1, armor=3.0, specials=[big("Sands of Ages", 0.22, 2.0, "pours a torrent of ageing sand over you!")],
  loot=[("planar_shard", 0.3)], gold=3.5, xp=1.3)
M("paradox", "a paradox", 59, "A figure that is you, from a moment that has not happened yet, wearing a smile you have never worn.",
  hp=3.92, dmg=2.65, armor=2.0, aggro=True, specials=[drain("Unmaking", 0.22, 1.3, "unmakes a moment of your past, and you feel yourself fade!"),
                                                    dot("Entropy", 0.15, 0.6, 3, "arcane", "touches you, and you begin to come undone!")],
  loot=[("planar_shard", 0.4)], gold=3.5)
M("lord_trepth", "Lord Trepth", 60,
  "The king of the gods, older than the stars, seated on a throne carved from the first moment of time. His face is every "
  "face, his eyes hold every dawn, and his sword is named Eternity.",
  hp=7.39, dmg=2.59, armor=3.0, aggro=True, boss=True, xp=2.0, gold=40.0,
  specials=[big("Eternity", 0.22, 2.2, "swings Eternity, and you feel every moment of your life at once!"),
            dot("The Long Night", 0.15, 0.8, 4, "shadow", "unmakes the dawn, and cold darkness eats at you!"),
            big("Stop Time", 0.12, 1.6, "raises a hand, and time stops for everyone but him!"),
            drain("Tithe of Ages", 0.12, 1.3, "takes the years from you as tribute!"),
            heal("The First Dawn", 0.06, 0.08, "calls the first dawn of the world, and it heals him!")],
  loot=[("eternity", 0.5), ("crown_of_trepth", 0.5), ("hourglass_amulet", 0.5), ("planar_shard", 1.0)])
