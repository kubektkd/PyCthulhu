import time
import textwrap
import utils.config as config
import utils.helpers as helpers
import entities.Investigator as Investigator


player = Investigator.Investigator("Brida Fox", 30, "K", "Komendant")


def standard_menu_options():
    print("")
    if player.ownedNotes:
        print("8) Sprawdź posiadane notatki")
    print("9) Pokaż statystyki mojej postaci")
    print("0) Powrót do menu")


def generate_title_box(text):
    text = text.upper()
    lines = textwrap.wrap(text, width=14)
    print("╒═════════════════╕")
    for line in lines:
        length = len(line)
        req_spaces = 16 - length
        spaces = req_spaces // 2
        if req_spaces % 2 == 0:
            print(f"│{spaces*' '}{line}{spaces*' '} │")
        else:
            print(f"│ {spaces * ' '}{line}{spaces * ' '} │")
    print("╘═════════════════╛")


def the_end():
    time.sleep(config.sleepTime)
    print(f"\n  ### KONIEC WERSJI DEMO ###\n")
    config.choice = input("Wciśnij Enter aby wrócić do menu głównego... ")
    config.choice = 0
    helpers.clear()
