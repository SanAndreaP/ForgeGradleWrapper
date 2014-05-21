from __future__ import print_function

import os
import sys
import random

import buildMod
import landscape
import setupForge
import setupBuild

from colorama import init, Fore, Back, Style
from consoleHelper import ConsoleHelper

# if sys.stdout.encoding != 'cp850':
    # sys.stdout = codecs.getwriter('cp850')(sys.stdout, 'strict')
# if sys.stderr.encoding != 'cp850':
    # sys.stderr = codecs.getwriter('cp850')(sys.stderr, 'strict')

init()

clrs = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]
menuItm = {"0" : exit, "1" : setupForge.setupForge, "2" : buildMod.buildMod, "3" : setupBuild.setupBuild, "4" : landscape.landscape}

def mainMenu():
    ConsoleHelper.clearScr()
    titleClr = clrs[random.randrange(len(clrs))]
    print(Style.BRIGHT + titleClr, end='')
    print(u"\u2591"*79)
    print(u"\u2591" + " " * 77 + u"\u2591")
    print(u"\u2591" + " "*23 + u"SanAndreasPs ForgeGradle Helper" + u" "*23 + u"\u2591")
    print(u"\u2591" + " " * 77 + u"\u2591")
    print(u"\u2591"*79, end='\n\n')
    
    print(Style.NORMAL + Fore.WHITE, end='')
    print(" [" + Style.BRIGHT + "1" + Style.NORMAL + "] setup forge")
    print(" [" + Style.BRIGHT + "2" + Style.NORMAL + "] build mod")
    print(" [" + Style.BRIGHT + "3" + Style.NORMAL + "] setup / edit build.gradle for mod")
    print(" [" + Style.BRIGHT + "0" + Style.NORMAL + "] exit", end='\n\n')
    
    choice = raw_input("Please enter a number from above: " + Style.BRIGHT + Fore.WHITE)
    
    if choice in menuItm:
        menuItm[choice]()
    else:
        print(Fore.YELLOW + "Invalid input! Try again.")
        ConsoleHelper.pause()
        mainMenu()

mainMenu()
ConsoleHelper.pause()