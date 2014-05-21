from __future__ import print_function

from colorama import deinit, reinit, Fore, Back, Style
import os
import random

def landscape():
    trees = []
    for i in range(0, 25):
        trees.extend([[random.randrange(25), random.randrange(79)]])
    print(Fore.GREEN + Style.BRIGHT, end="")
    os.system("CLS")
    for y in range(0, 25):
        for x in range(0, 79):
            if [y, x] in trees:
                print(u"♣",end='')
            else:
                print(u"\u2591",end='')
        if y < 24:
            print("")
    raw_input()