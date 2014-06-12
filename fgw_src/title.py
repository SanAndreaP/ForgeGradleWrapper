from __future__ import print_function

import random

from colorama import Fore, Style
from fgw_src import pythonHelper

clrs = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]
currClr = None


def show(subtitle=""):
    pythonHelper.clear_scr()
    global currClr
    if currClr is None:
        currClr = clrs[random.randrange(len(clrs))]
    st_len = len(subtitle)
    space_len_l = (77 - st_len) / 2 + 1
    space_len_r = (77 - st_len) / 2 - st_len % 2

    print(Style.BRIGHT + currClr, end="")
    print(u"\u2591" * 79)
    print(u"\u2591" + " " * 77 + u"\u2591")
    print(u"\u2591" + " " * 23 + u"SanAndreasPs ForgeGradle Helper" + u" " * 23 + u"\u2591")
    print(
        u"\u2591" + " " * space_len_l + Fore.WHITE + Style.NORMAL + subtitle + Style.BRIGHT + currClr + " " * space_len_r + u"\u2591")
    if st_len > 0:
        print(u"\u2591" + " " * 77 + u"\u2591")
    print(u"\u2591" * 79, end='\n\n')
    print(Style.NORMAL + Fore.WHITE, end='')