from __future__ import print_function

import random

from colorama import init, Fore, Back, Style
import pythonHelper

clrs = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]
currClr = None

def show(subtitle=""):
    pythonHelper.clearScr()
    global currClr
    if currClr is None:
        currClr = clrs[random.randrange(len(clrs))]
    stLen = len(subtitle)
    spaceLenL = (77 - stLen) / 2 + 1
    spaceLenR = (77 - stLen) / 2 - stLen % 2
    
    print(Style.BRIGHT + currClr, end="")
    print(u"\u2591"*79)
    print(u"\u2591" + " " * 77 + u"\u2591")
    print(u"\u2591" + " "*23 + u"SanAndreasPs ForgeGradle Helper" + u" "*23 + u"\u2591")
    print(u"\u2591" + " " * spaceLenL + Fore.WHITE + Style.NORMAL + subtitle + Style.BRIGHT + currClr + " " * spaceLenR + u"\u2591")
    if stLen > 0:
        print(u"\u2591" + " " * 77 + u"\u2591")
    print(u"\u2591"*79, end='\n\n')
    print(Style.NORMAL + Fore.WHITE, end='')