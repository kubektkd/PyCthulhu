#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import os

if os.name == 'nt':
    sys.stdout.reconfigure(encoding='utf-8')

from gameEngine.mainMenu import *
import utils.helpers as helpers
import utils.config as config


# ! START GAME ! #
# * MAIN LOOP * #
def main():
    if '--dev' in sys.argv:
        config.sleepTime = 0.5
        config.logoSleepTime = 0.5
    else:
        config.logoSleepTime = config.defaults_settings[0]
        config.sleepTime = config.defaults_settings[1]
        config.settings_print_messages = config.defaults_settings[2]

    helpers.read_locale_file('pl')
    main_menu()


# ? Let this file to be imported as module
if __name__ == "__main__":
    main()

# TODO: Add and import further days as a modules
