from __future__ import print_function

import os
import sys

import title
import buildMod
import landscape
import setupForge
import setupBuild
import pythonHelper
import nothingToSeeHereReallyNopeSoEmptyAndNothingness

from colorama import init, Fore, Back, Style

init()

menuItm = {
        "0" : exit,
        "1" : setupForge,
        "2" : buildMod,
        "3" : setupBuild,
        "4" : landscape,
        "5" : nothingToSeeHereReallyNopeSoEmptyAndNothingness
    }
    
def mainMenu():
    title.show()
    
    print(" [" + Style.BRIGHT + "1" + Style.NORMAL + "] setup forge")
    print(" [" + Style.BRIGHT + "2" + Style.NORMAL + "] build mod")
    print(" [" + Style.BRIGHT + "3" + Style.NORMAL + "] setup / edit build.gradle for mod")
    print(" [" + Style.BRIGHT + "0" + Style.NORMAL + "] exit", end='\n\n')
    
    choice = raw_input("Please enter a number from above > " + Style.BRIGHT + Fore.WHITE)
    print(Fore.RESET + Style.NORMAL, end="")
    if choice in menuItm:
        menuItm[choice].call()
    else:
        print(Fore.YELLOW + "Invalid input! Try again.")
        pythonHelper.pause()
        mainMenu()

while True:
    mainMenu()
    input = raw_input("Continue working? [Y/N] > " + Fore.WHITE)
    print(Fore.RESET + Style.NORMAL, end="")
    if input.lower() != "y":
        break

os.system("PAUSE")