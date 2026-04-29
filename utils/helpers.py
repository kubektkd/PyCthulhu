import os
import sys
import time
import json
import math
import textwrap
import utils.config as config
from utils.constants import *


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
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


def _rainbow_print(text, freq=0.1, spread=3.0):
    for i, line in enumerate(text.splitlines()):
        colored = []
        for j, char in enumerate(line):
            if char.strip():
                phase = freq * (i * spread + j)
                r = int(math.sin(phase + 0) * 127 + 128)
                g = int(math.sin(phase + 2 * math.pi / 3) * 127 + 128)
                b = int(math.sin(phase + 4 * math.pi / 3) * 127 + 128)
                colored.append(f'\033[38;2;{r};{g};{b}m{char}\033[0m')
            else:
                colored.append(char)
        print(''.join(colored))


def show_game_logo_alt():
    with open(logo_file, 'r') as fin:
        print(fin.read())


def show_game_logo():
    try:
        with open(logo_file, 'r') as fin:
            _rainbow_print(fin.read())
    except Exception:
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
