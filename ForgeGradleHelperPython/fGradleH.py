from __future__ import print_function

import os
import sys

import buildMod
import landscape
import setupForge
import setupBuild
import title
import pythonHelper

from colorama import init, Fore, Back, Style

init()

menuItm = {
        "0" : exit,
        "1" : setupForge.call,
        "2" : buildMod.call,
        "3" : setupBuild.call,
        "4" : landscape.call
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
        menuItm[choice]()
    else:
        print(Fore.YELLOW + "Invalid input! Try again.")
        pythonHelper.pause()
        mainMenu()

mainMenu()
pythonHelper.pause()