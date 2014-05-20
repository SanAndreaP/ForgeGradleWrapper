from __future__ import print_function

import os.path
import urllib2
import json

from colorama import Fore, Back, Style

def checkForGradlew():
	if not os.path.isfile("gradlew"):
		input = raw_input(Style.BRIGHT + Fore.YELLOW + "gradlew could not be found! Do you want to setup Forge here? [Y/N] > " + Fore.WHITE + Style.NORMAL)
		if input.lower() == "y":
			print("Reading JSON data... ", end='')
			response = urllib2.urlopen("http://files.minecraftforge.net/maven/net/minecraftforge/forge/json")
			jsonData = json.loads(response.read())
			packages = {}
			for pkg in jsonData["promos"]:
				id = jsonData["promos"][pkg]
				if not id in packages:
					packages[id] = pkg
			print("[Done]")
			print("Following packages are available:", end="\n\n")
			for id in packages:
				print(" [" + Style.BRIGHT + str(id) + Style.NORMAL + "] " + packages[id])
			print
			input = raw_input("\nPlease enter one of the listed build numbers to continue > ")
			# print(jsonData["promos"])
			
			# print(jsonData)
			print("Downloading Forge...")

def setupForge():
	checkForGradlew()