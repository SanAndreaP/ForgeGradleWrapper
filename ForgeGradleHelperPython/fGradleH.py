# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
from __future__ import print_function

import os
import random

from colorama import init
from colorama import Fore, Back, Style

from consoleHelper import ConsoleHelper
from setupForge import setupForge
from buildMod import buildMod
from setupBuild import setupBuild
	
init()
clrs = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]
menuItm = {"1" : setupForge, "2" : buildMod, "3" : setupBuild}


def mainMenu():
	ConsoleHelper.clearScr()
	titleClr = clrs[random.randrange(len(clrs))]
	print(Style.BRIGHT + titleClr, end='')
	print("=" * 79)
	print("|" + " " * 23 + "SanAndreasPs ForgeGradle Helper" + " " * 23 + "|")
	print("=" * 79, end='\n\n')
	
	print(Style.NORMAL + Fore.WHITE, end='')
	print(" [" + Style.BRIGHT + "1" + Style.NORMAL + "] setup forge")
	print(" [" + Style.BRIGHT + "2" + Style.NORMAL + "] build mod")
	print(" [" + Style.BRIGHT + "3" + Style.NORMAL + "] setup / edit build.gradle for mod")
	print(" [" + Style.BRIGHT + "0" + Style.NORMAL + "] exit", end='\n\n')
	
	choice = raw_input("Please enter a number from above: " + Style.BRIGHT + Fore.YELLOW)
	
	if choice in menuItm:
		menuItm[choice]()
	else:
		exit()

mainMenu()
ConsoleHelper.pause()