from __future__ import print_function

import math
import os

from colorama import Style


def pause():
    if os.system("PAUSE") != 0:
        os.system("read -p \"Press [Enter] key to continue...\"")


def clear_scr():
    if os.system("CLS") != 0:
        os.system("clear")


def is_integer(s):
    try:
        return int(s)
    except ValueError:
        return math.isnan


def get_yesno_input(s):
    usr_input = raw_input(Style.NORMAL + s + " [Y/N] > " + Style.BRIGHT)
    while len(usr_input) == 0 or not usr_input.lower() in "yn":
        usr_input = raw_input(Style.NORMAL + " "*len(s + " [Y/N]") + " > " + Style.BRIGHT)
    print(Style.NORMAL, end="")
    return usr_input.lower() == "y"


def printmenu_and_getchoice(menu_title, menu_items, menu_choice):
    print(Style.NORMAL + menu_title)
    for k in menu_items:
        val = menu_items[k]
        if isinstance(val, tuple):
            val = val[0]
        print(" [" + Style.BRIGHT + k + Style.NORMAL + "] " + val)
    usr_input = raw_input(menu_choice + " > " + Style.BRIGHT)
    while not usr_input in menu_items:
        usr_input = raw_input(Style.NORMAL + " "*len(menu_choice) + " > " + Style.BRIGHT)
    print(Style.NORMAL, end="")
    return usr_input