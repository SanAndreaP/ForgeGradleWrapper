from __future__ import print_function

import zipfile
import os.path
import urllib2
import json
import time
import os
import io

from colorama import Fore, Back, Style

def downloadGradle():
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
	
	print("Downloading Forge... ", end='')
	forgeBuild = jsonData["number"][input]["mcversion"] + "-" + jsonData["number"][input]["version"]
	response = urllib2.urlopen(jsonData["webpath"] + "/" + forgeBuild + "/forge-" + forgeBuild + "-src.zip")
	zipData = zipfile.ZipFile(io.BytesIO(response.read()))
	print("[Done]")
	
	for name in zipData.namelist():
		(dirname, filename) = os.path.split(name)
		dirname = "./forge/" + dirname
		print("\rExtracting Zip: " + (filename[:30] + "..." + filename[:-30] if len(filename) > 63 else filename + " " * (63 - len(filename))), end='')
		if not os.path.exists(dirname):
			os.makedirs(dirname)
		zipData.extract(name, dirname)
	print("\rExtracting Zip: [Done]" + " " * 57)

def checkForGradlew():
	if not os.path.isfile("gradlew"):
		input = raw_input(Style.BRIGHT + Fore.YELLOW + "gradlew could not be found! Do you want to setup Forge here? [Y/N] > " + Fore.WHITE + Style.NORMAL)
		if input.lower() == "y":
			downloadGradle()

def setupForge():
	checkForGradlew()