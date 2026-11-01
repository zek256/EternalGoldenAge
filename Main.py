"""Eternal Golden Age - an offline, single-player fantasy MUD.

Run:  python main.py
"""
import sys

import ui
from game import ask, create_character, list_saves, load_game_interactive

TITLE = r"""
  +==================================================+
  |                                                  |
  |       E T E R N A L   G O L D E N   A G E        |
  |                                                  |
  |      ~ swords, sorcery, and lives beyond ~       |
  |                                                  |
  +==================================================+
"""


def main():
    ui.init()
    ui.start_input()

    ui.out(ui.c(TITLE, "byellow"))
    ui.say("A tale of swords and sorcery, of crypts and dragons, of heroes who live, and live again.", "grey")
    ui.out("")
    game = None
    while game is None:
        ui.out("  1. New game")
        ui.out("  2. Load game" + ("" if list_saves() else ui.c("  (no saves yet)", "grey")))
        ui.out("  3. Quit")
        sel = ask("> ").strip().lower()
        if sel in ("1", "n", "new"):
            game = create_character()
        elif sel in ("2", "l", "load"):
            game = load_game_interactive()
            if game:
                ui.say("Welcome back, {}.".format(game.player.name), "bgreen")
        elif sel in ("3", "q", "quit"):
            return
    game.run()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print()
        sys.exit(0)
