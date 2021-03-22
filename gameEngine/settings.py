from gameEngine.interface import *
from utils.helpers import _, read_locale_file


# TODO: add game settings functionality
def game_settings():
    while config.choice != 0:
        print("")
        generate_title_box(_('settings.title'))
        print(f"1) {_('settings.option_1')}")
        print(f"2) {_('settings.option_2')}")
        print(f"9) {_('settings.option_9')}")
        print(f"0) {_('back')}")
        config.choice = helpers.input_number(f"{_('choice')}")
        helpers.clear()

        if config.choice == 1:
            print(f"Aktualna wartość: {'%g' % config.sleepTime}s")
            print("(Wprowadź '0' aby nie zmieniać)")
            new_time = helpers.input_float("Podaj nowy czas w sekundach: ")
            if new_time != 0:
                config.sleepTime = new_time

        if config.choice == 2:
            selected_language = 0
            while selected_language != 1 and selected_language != 2:
                print("Wybierz język:")
                print("1) Polski")
                print("2) Angielski")
                selected_language = helpers.input_number("Wybór > ")
                if selected_language == 1:
                    read_locale_file('pl')
                if selected_language == 2:
                    read_locale_file('en')
                helpers.clear()

        if config.choice == 9:
            config.sleepTime = 2
            read_locale_file('pl')
            print("Przywrócono ustawienia domyślne")