import entities.Investigator as Investigator
from gameEngine.settings import *
from gameEngine.interface import *
from utils.constants import *
import story.dayOne as story


def reset_flags():
    global selectedProblems, handgunRounds, rifleRounds, ownedNotes
    global GirlHitByCar, CarChecked, CalledForMechanic, GirlHysteria
    # * reset Game Vars
    selectedProblems = []
    handgunRounds = 0
    rifleRounds = 0
    ownedNotes = []
    # * reset Game Flags
    GirlHitByCar = 0
    CarChecked = 0
    CalledForMechanic = 0
    GirlHysteria = 0


# TODO: add save game functionality
def save_game():
    """
    to save:
    - character stats
    - game flags
    - equipment and found items
    save this data to save file in ~/pythulhu folder
    """
    pass


# TODO: add load game functionality
def load_game():
    print("Niedostępne w wersji DEMO")
    time.sleep(config.sleepTime)
    helpers.clear()


# TODO: add this functionality by reading last modified 'save' file in ~/pythulhu/ folder
def continue_game():
    print("Niedostępne w wersji DEMO")
    time.sleep(config.sleepTime)
    helpers.clear()


def about_game():
    while config.choice != 0:
        print("╒════════════════╕")
        print("│     O GRZE     │")
        print("╘════════════════╛")
        print(f"{ORANGE}Wykonawca gry:{NC}	Jakub Michniewicz")
        print(f"{ORANGE}Scenariusz:{NC}	Asia Wiewiórska")
        print(f'''\n{ORANGE}'DRUGA'{NC}
  Scenariusz ten inspirowany jest ponurymi skandynawskimi powieściami i serialami,
  w których główne role odgrywają tajemnica, społeczność i śledztwo. Konwencja ta
  znana jest pod nazwą nordic-noir, lecz scenariusz nawiązuje również do znanych baśni
  ludowych i Lovecraftowskiej Krainy Snów. Akcja gry rozpoczyna się w lutym 2020 r.
  gdzieś w Skandynawii. Oniryczny nastrój buduje tu odosobnione miasteczko otoczone przez
  wzgórza i ciemne lasy oraz surowa, choć urokliwa zimowa aura. To bardzo subtelna historia,
  która nie jest opowieścią akcji.''')

        print(f"\n0) Powrót")
        config.choice = helpers.input_number("Wybór > ")
        helpers.clear()


def new_game():
    reset_flags()
    player.create_character()
    helpers.clear()
    player.show_character_stats()

    while config.choice != 0:
        print("╒════════════════╕")
        print("│    NOWA GRA    │")
        print("╘════════════════╛")
        print("1) Graj tą postacią")
        print("2) Utwórz nową postać")
        print("9) Pokaż statystyki mojej postaci")
        print("0) Powrót")
        config.choice = helpers.input_number("Wybór > ")
        helpers.clear()

        if config.choice == 9:
            player.show_character_stats()

        if config.choice == 2:
            player.create_caracter()
            player.show_character_stats()

        if config.choice == 1:
            story.initiate_history()


def main_menu():
    helpers.clear()
    while config.choice != 'q' and config.choice != 'Q':
        helpers.show_game_logo()
        print("╒═════════════════╕")
        print("│   MENU GŁÓWNE   │")
        print("╘═════════════════╛")
        print(f"1) {DGRAY}Kontynuuj grę{NC}")
        print("2) Rozpocznij grę")
        print(f"3) {DGRAY}Wczytaj grę{NC}")
        print("4) O grze")
        print("5) Ustawienia")
        print("Q) Wyjście")
        config.choice = helpers.input_text("Wybór > ")
        helpers.clear()

        if config.choice == '1':
            continue_game()

        if config.choice == '2':
            new_game()

        if config.choice == '3':
            load_game()

        if config.choice == '4':
            about_game()

        if config.choice == '5':
            game_settings()
