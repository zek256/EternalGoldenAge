"""Draw an SVG map of every room. Run from anywhere: python tools/draw_map.py [out.svg]

Writes map.svg in the game folder by default; open it in any web browser.
Rooms are placed on a grid by following exits from the town square (north is up,
up/down are drawn diagonally). Areas listed in mapview.INSETS (dungeons below the surface, realms
above it) would sit on top of surface rooms, so each is laid out on its own grid and drawn
in a framed box to the right of the surface map. Each area's name is written inside the area.
"""
import os
import sys
import textwrap
from html import escape

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, ROOT)

import mapview  # noqa: E402  (the grid layout and INSETS list, shared with the in-game map)
from data.monsters import MONSTERS  # noqa: E402
from data.rooms import ROOMS  # noqa: E402

COLORS = {  # area: (fill, border)
    "Brightwater": ("#3a3a46", "#c9b67a"), "Greenmeadow": ("#2f4a2a", "#8fc46a"),
    "Whispering Woods": ("#1f3d2c", "#5fae7a"), "The Northlands": ("#3b3f47", "#a7b0bd"),
    "Barrowfield": ("#3d3530", "#a89380"), "Crypt of Varnoth": ("#33293d", "#a98bd0"),
    "The Mirefen": ("#2e3b33", "#7fa58c"), "Ironspine Mountains": ("#363c45", "#8fb3d9"),
    "Ruins of Elandor": ("#2c3445", "#9fb0e8"), "Ashen Peaks": ("#47271f", "#e88a5a"),
    "Westmarch": ("#3d3a26", "#d2b55b"), "Rimefells": ("#3a4048", "#dde6ee"),
    "Hearthdeep": ("#45332a", "#e0a070"), "Deepdelve Mine": ("#243a3a", "#6fc7c0"),
    "Eldergrove": ("#1b3324", "#6fcf86"), "Silverbough": ("#38362a", "#f0e2a0"),
    "Dustway": ("#3f3a33", "#c8b89a"), "Redrock Badlands": ("#4a2a22", "#e07a5a"),
    "Scorchsands": ("#463c22", "#f2c45a"), "Sunspire": ("#40372a", "#ffe08a"),
    "Tomb of the Sand Kings": ("#2a2630", "#c9a0e0"),
    "The Chancery of the Dead": ("#2b2d3f", "#b9bdf2"), "The Carnival That Never Closes": ("#3a1f3a", "#ff8ad8"),
    "The Mycelial Wards": ("#1f3333", "#7fe0d0"), "The Sugarwold": ("#4a2a3d", "#f2a0c8"),
    "The Underhedge": ("#2a3d1f", "#b8e06a"), "The Clockwork Orchard": ("#3d3320", "#e0b04a"),
    "The Painted Gallery": ("#3d3528", "#e8d29a"), "The Wreck at Saltmere": ("#1e3340", "#6fb7d8"),
    "The Winter Hunt": ("#333b45", "#dfe8f2"), "Still Life with Rot": ("#3a2f1c", "#c9a24a"),
    "The Salon of Sitters": ("#40263a", "#e6a6cf"), "Elandor Before the Fall": ("#3d3a24", "#f2e27a"),
    "The Unfinished Self-Portrait": ("#2e2e2e", "#d0d0d0"),
    "Thornwick Hall": ("#42262e", "#e4a0b4"), "Thornwick Hall, Upper Floor": ("#58343f", "#f6cad6"),
    "Threshold of the Gods": ("#3a3a40", "#fff4c8"), "Plane of Stars": ("#22284a", "#b8c8ff"),
    "Plane of Dreams": ("#2e2a44", "#d8c0ff"), "Plane of Death": ("#2a2a2a", "#b0c0c8"),
    "Plane of Fire": ("#4a1e14", "#ff8050"), "Plane of Water": ("#14304a", "#60b0ff"),
    "Plane of Earth": ("#3a3020", "#c8a060"), "Plane of Air": ("#30384a", "#e0f0ff"),
    "Plane of Eternity": ("#3a3424", "#ffd870"), "Plane of Law": ("#2e2e34", "#f4f4ff"),
}
BOSS_RED = "#ff5a4a"
CW, CH = 170, 92           # grid cell size
BW, BH = 140, 60           # room box size
PAD = 40


def layout():
    try:
        return mapview.layout()
    except ValueError as exc:
        sys.exit(str(exc))


def draw(pos, insets):
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    minx, miny = min(xs), min(ys)
    W = (max(xs) - minx + 1) * CW + 2 * PAD
    H = (max(ys) - miny + 1) * CH + 2 * PAD + 40
    taken = {p: r for r, p in pos.items()}

    def ctr(r):
        x, y = pos[r]
        return PAD + (x - minx) * CW + CW / 2, PAD + 40 + (y - miny) * CH + CH / 2

    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="{0}" height="{1}" viewBox="0 0 {0} {1}" '
           'font-family="Georgia, serif">'.format(W, H),
           '<rect width="100%" height="100%" fill="#16161c"/>',
           '<text x="{}" y="34" fill="#e8d9a8" font-size="24">Eternal Golden Age</text>'.format(PAD)]

    # exits, each drawn once
    done = set()
    for r, v in ROOMS.items():
        for d, t in v["exits"].items():
            if frozenset((r, t)) in done:
                continue
            done.add(frozenset((r, t)))
            (x1, y1), (x2, y2) = ctr(r), ctr(t)
            dash = ' stroke-dasharray="6 5"' if d in "ud" else ""
            if abs(pos[r][0] - pos[t][0]) <= 1 and abs(pos[r][1] - pos[t][1]) <= 1:
                out.append('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#77736a" stroke-width="2"{}/>'
                           .format(x1, y1, x2, y2, dash))
                if d in "ud":
                    out.append('<text x="{}" y="{}" fill="#b8b3a6" font-size="11" text-anchor="middle">stairs</text>'
                               .format((x1 + x2) / 2 + 22, (y1 + y2) / 2 - 4))
            # the way into an inset is drawn below as a faint leader line, and the surface room gets a note
    for label, rooms, entry, outside in insets:
        # down into the gap under the row, across, and up into the entry, so it never looks like an exit
        (x1, y1), (x2, y2) = ctr(outside), ctr(entry)
        x1, x2, gap = x1 + BW / 4, x2 - BW / 4, max(y1, y2) + CH / 2
        color = COLORS.get(ROOMS[entry]["area"], ("", "#999999"))[1]
        out.append('<polyline points="{},{} {},{} {},{} {},{}" fill="none" stroke="{}" stroke-width="2" '
                   'stroke-opacity="0.7" stroke-dasharray="2 7" stroke-linecap="round"/>'
                   .format(x1, y1 + BH / 2, x1, gap, x2, gap, x2, y2 + BH / 2, color))
    portal = {}  # surface room -> (text, colour) naming the inset below or above it
    for label, rooms, entry, outside in insets:
        way = next(d for d, t in ROOMS[outside]["exits"].items() if t == entry)
        arrow = {"d": "↓ ", "u": "↑ "}.get(way, "")
        portal[outside] = (arrow + label, COLORS.get(ROOMS[entry]["area"], ("", "#999999"))[1])

    # inset frames
    for label, rooms, entry, outside in insets:
        ix = [ctr(r)[0] for r in rooms]
        iy = [ctr(r)[1] for r in rooms]
        color = COLORS.get(ROOMS[entry]["area"], ("", "#999999"))[1]
        way = next(d for d, t in ROOMS[entry]["exits"].items() if t == outside)
        where = {"u": "below", "d": "above"}.get(way, "beside")
        out.append('<rect x="{}" y="{}" width="{}" height="{}" rx="12" fill="none" stroke="{}" stroke-dasharray="4 4"/>'
                   .format(min(ix) - BW / 2 - 14, min(iy) - BH / 2 - 30, max(ix) - min(ix) + BW + 28,
                           max(iy) - min(iy) + BH + 44, color))
        out.append('<text x="{}" y="{}" fill="{}" font-size="13">{} ({} {})</text>'
                   .format(min(ix) - BW / 2 - 4, min(iy) - BH / 2 - 12, color, escape(label), where,
                           escape(ROOMS[outside]["name"].replace("The ", ""))))

    # rooms
    for r, v in ROOMS.items():
        cx, cy = ctr(r)
        fill, border = COLORS.get(v["area"], ("#333333", "#999999"))
        bosses = [MONSTERS[m] for m, _ in v["spawns"] if MONSTERS[m]["boss"]]
        out.append('<rect x="{}" y="{}" width="{}" height="{}" rx="6" fill="{}" stroke="{}" stroke-width="{}"/>'
                   .format(cx - BW / 2, cy - BH / 2, BW, BH, fill,
                           BOSS_RED if bosses else border, 3 if bosses else 1.2))
        lines = textwrap.wrap(v["name"], 20)[:2]
        if bosses:
            sub = "Boss Lv {}".format(bosses[0]["level"])
        elif v["level"]:
            lo, hi = v["level"]
            sub = "Lv {}-{}".format(lo, hi) if lo != hi else "Lv {}".format(lo)
        else:
            sub = "safe" if v["safe"] else ""
        notes = [(sub, "#ff8a7a" if bosses else border)] if sub else []
        if r in portal:
            notes.append(portal[r])
        top = cy - (len(lines) + len(notes)) * 14 / 2 + 11
        for i, ln in enumerate(lines):
            out.append('<text x="{}" y="{}" fill="#f1ead6" font-size="12.5" text-anchor="middle">{}</text>'
                       .format(cx, top + i * 14, escape(ln)))
        for i, (text, color) in enumerate(notes):
            out.append('<text x="{}" y="{}" fill="{}" font-size="11" text-anchor="middle">{}</text>'
                       .format(cx, top + (len(lines) + i) * 14 + 1, color, escape(text)))

    # area names, each in the empty grid square nearest the middle of its area
    used = set()
    for area in dict.fromkeys(v["area"] for v in ROOMS.values()):
        cells = [pos[r] for r in ROOMS if ROOMS[r]["area"] == area]
        mx = sum(x for x, _ in cells) / len(cells)
        my = sum(y for _, y in cells) / len(cells)
        best = None
        for (cx0, cy0) in cells:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    c = (cx0 + dx, cy0 + dy)
                    if c in taken or c in used:
                        continue
                    near = [taken[(c[0] + i, c[1] + j)] for i in (-1, 0, 1) for j in (-1, 0, 1)
                            if (c[0] + i, c[1] + j) in taken]
                    own = sum(ROOMS[r]["area"] == area for r in near)
                    score = (len(near) - own) * 3 - own * 1.5 + ((c[0] - mx) ** 2 + (c[1] - my) ** 2) ** 0.5
                    if best is None or score < best[0]:
                        best = (score, c, own, len(near) - own)
        border = COLORS.get(area, ("", "#999999"))[1]
        if best and best[2] <= best[3]:
            # no square mostly of this area: a banner in the gap just above one of its own rooms instead
            def cost(r):
                x0, y0 = pos[r]
                above = taken.get((x0, y0 - 1))
                return (("n" in ROOMS[r]["exits"]) + 2 * (above is not None and ROOMS[above]["area"] != area)
                        + ((x0 - mx) ** 2 + (y0 - my) ** 2) ** 0.5)
            r = min((r for r in ROOMS if ROOMS[r]["area"] == area), key=cost)
            x, y = ctr(r)
            y -= BH / 2 + (CH - BH) / 2
            w = len(area) * 7.6 + 12
            out.append('<rect x="{}" y="{}" width="{}" height="20" rx="4" fill="#16161c" fill-opacity="0.9"/>'
                       .format(x - w / 2, y - 10, w))
            out.append('<text x="{}" y="{}" fill="{}" font-size="14" font-weight="bold" font-style="italic" '
                       'text-anchor="middle">{}</text>'.format(x, y + 5, border, escape(area)))
            continue
        if best:
            used.add(best[1])
            x = PAD + (best[1][0] - minx) * CW + CW / 2
            y = PAD + 40 + (best[1][1] - miny) * CH + CH / 2
            lines = textwrap.wrap(area, 16)
            top = y - (len(lines) - 1) * 18 / 2 + 6
            for i, ln in enumerate(lines):
                out.append('<text x="{}" y="{}" fill="{}" font-size="16" font-weight="bold" font-style="italic" '
                           'text-anchor="middle" opacity="0.9">{}</text>'.format(x, top + i * 18, border, escape(ln)))
        else:
            print("no free square for " + area, file=sys.stderr)

    # a one-line key under the title
    kx, ky = PAD + 300, 28
    out.append('<rect x="{}" y="{}" width="22" height="16" rx="3" fill="none" stroke="{}" stroke-width="3"/>'
               .format(kx, ky - 12, BOSS_RED))
    out.append('<text x="{}" y="{}" fill="#ddd6c4" font-size="12">Boss room</text>'.format(kx + 30, ky))
    kx += 120
    out.append('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#77736a" stroke-width="2" stroke-dasharray="6 5"/>'
               .format(kx, ky - 4, kx + 22, ky - 4))
    out.append('<text x="{}" y="{}" fill="#ddd6c4" font-size="12">Up / down</text>'.format(kx + 30, ky))
    kx += 120
    out.append('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#c9b67a" stroke-width="2" stroke-opacity="0.6" '
               'stroke-dasharray="2 7" stroke-linecap="round"/>'.format(kx, ky - 4, kx + 22, ky - 4))
    out.append('<text x="{}" y="{}" fill="#ddd6c4" font-size="12">Way to a boxed area</text>'.format(kx + 30, ky))
    kx += 190
    out.append('<text x="{}" y="{}" fill="#9a958a" font-size="11">North is up. Lv = monster levels.</text>'
               .format(kx, ky))
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "map.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(draw(*layout()))
    print("Wrote " + os.path.abspath(path))
