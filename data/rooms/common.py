"""The room constructor shared by every region file."""


def R(name, area, desc, exits, spawns=None, npcs=None, safe=False, items=None, level=None, max_aggro=None,
      gate=None, hidden=None):
    """max_aggro: how many monsters here may attack on sight (default 1); the rest wait until you
    attack them. Rooms with a boss ignore it: everything in a boss room attacks.

    gate: a condition for entering the room, checked by Game.gate_block, with a "msg" shown on refusal:
      {"kills": [boss ids], "msg": ...}       - the character must have killed every listed boss
      {"item": item id, "msg": ...}           - the character must be carrying the item (it is not used up)
      {"all_classes": True, "msg": ...}       - every class lived to level 50 (past lives + current)

    hidden: exits taken only with 'enter <word>', not by walking. {dir: {"words": [...], "prompt": the
    command, printed in colour under the room description (e.g. "Type ENTER MOUSEHOLE to squeeze
    inside."), "hint": shown when the player tries to walk that way, "msg": shown on entering}}. The
    exit itself stays in `exits` (so maps, find and the data check treat it normally), but it is left
    out of the Exits line, speedwalks and fleeing.
    """
    return {"name": name, "area": area, "desc": desc, "exits": exits, "spawns": spawns or [],
            "npcs": npcs or [], "safe": safe, "items": items or [], "level": level, "max_aggro": max_aggro,
            "gate": gate, "hidden": hidden or {}}
