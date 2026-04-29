#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import os

if os.name == 'nt':
    sys.stdout.reconfigure(encoding='utf-8')

from gameEngine.mainMenu import *
import utils.helpers as helpers


# ! START GAME ! #
# * MAIN LOOP * #
def main():
    helpers.read_locale_file('pl')
    main_menu()


# ? Let this file to be imported as module
if __name__ == "__main__":
    main()

# TODO: Add and import further days as a modules
