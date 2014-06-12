from __future__ import print_function

import os
import random
import locale

from colorama import Fore, Back, Style


def call():
    encoding = locale.getdefaultlocale()[1]
    tree_chars = [u"\u2591", u"\u2591"]
    if encoding == "cp1252":
        tree_chars = [u"\x05", u"\x06"]
    elif encoding == "utf-8":
        tree_chars = [u"\u2663", u"\u2660"]

    trees = []
    for i in range(0, 200):
        trees.extend([[random.randrange(25), random.randrange(79)]])
    print(Fore.GREEN + Style.BRIGHT, end="")
    os.system("CLS")
    for y in range(0, 25):
        for x in range(0, 79):
            if [y, x] in trees:
                print(Back.GREEN + Fore.RED + Style.NORMAL + tree_chars[random.randrange(2)] + Back.RESET
                      + Fore.GREEN + Style.BRIGHT, end='')
            else:
                print(u"\u2591", end='')
        if y < 24:
            print("")
    raw_input()