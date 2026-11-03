"""The world, one file per region.

Each room: name, area, desc, exits {dir: room_id}, spawns [(monster_id, count)],
npcs [npc_id], safe (no combat / free resting), items [item_id] lying on the ground.
Add a new region by writing a module with a ROOMS dict and listing it in REGIONS below.
"""
from data.rooms import (ashen_peaks, badlands, barrowfield, brightwater, carnival, chancery, clockwork_orchard, deepdelve,
                        dustway, elandor, eldergrove, greenmeadow, hearthdeep, ironspine, mirefen, mycelial,
                        northlands, painted_gallery, planes, rimefells, sand_tomb, scorchsands, silverbough, sugarwold, sunspire,
                        thornwick, underhedge, westmarch, whispering_woods)
from data.rooms.npcs import NPCS  # noqa: F401

START_ROOM = "town_square"
RESPAWN_ROOM = "temple"

REGIONS = [brightwater, greenmeadow, underhedge, whispering_woods, northlands, barrowfield, mirefen, ironspine,
           elandor, painted_gallery, ashen_peaks, westmarch, rimefells, hearthdeep, deepdelve, eldergrove, silverbough,
           dustway, chancery, clockwork_orchard, badlands, carnival, scorchsands, sunspire, sand_tomb, thornwick, mycelial, sugarwold, planes]

ROOMS = {}
for _region in REGIONS:
    for _rid, _room in _region.ROOMS.items():
        if _rid in ROOMS:
            raise ValueError("room id '%s' is defined twice" % _rid)
        ROOMS[_rid] = _room
