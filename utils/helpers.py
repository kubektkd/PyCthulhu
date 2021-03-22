import os
import sys
import time
import json
import textwrap
import utils.config as config
from utils.constants import *


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
clear = lambda: os.system('clear')
logo_file = os.path.join(SCRIPT_DIR, '../assets/game-logo.txt')


# ! HELPER FUNCTIONS ! #
def input_number(input_message):
    while True:
        try:
            user_input = int(input(input_message))
        except ValueError:
            print("Wprowadź liczbę.")
            continue
        else:
            return user_input


def input_float(input_message):
    while True:
        try:
            user_input = float(input(input_message))
        except ValueError:
            print("Wprowadź liczbę.")
            continue
        else:
            return user_input


def input_text(input_message):
    user_input = input(input_message).lower().strip()
    return user_input


def print_text(message):
    wrapped_message = textwrap.wrap(message, width=80)
    if config.settings_print_messages:
        print()
        for idx, text in enumerate(wrapped_message):
            if idx == 0:
                print("    ", end="")
            else:
                print("  ", end="")
            for character in text:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            print()
    else:
        print()
        for idx, text in enumerate(wrapped_message):
            if idx == 0:
                print(f"    {text}")
            else:
                print(f"  {text}")


def show_game_logo_alt():
    with open(logo_file, 'r') as fin:
        print(fin.read())


def show_game_logo():
    os_cmd = f'lolcat {SCRIPT_DIR}/../assets/game-logo.txt'
    if os.system(os_cmd) != 0:
        show_game_logo_alt()
    time.sleep(config.logoSleepTime)
    print(f"\n  Wykonał - {ORANGE}Jakub Michniewicz{NC}                   Wersja - {BRED}{config.APP_VER_NO}{NC}\n")
    time.sleep(config.logoSleepTime)


def read_locale_file(lang):
    with open(f'locale/{lang}.json') as f:
        config.locale = json.load(f)


def _(translate_key):
    key_list = translate_key.split('.')

    def json_extract(data, lists):
        if len(lists) > 1:
            return json_extract(data[lists[0]], lists[1:])
        return data[lists[0]]

    return json_extract(config.locale, key_list)
