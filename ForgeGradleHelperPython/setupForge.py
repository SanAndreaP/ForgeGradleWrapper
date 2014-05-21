from __future__ import print_function

import subprocess
import webbrowser
import zipfile
import os.path
import urllib2
import json
import time
import os
import io

from colorama import deinit, reinit, Fore, Back, Style

gradlePath = r"."

def downloadGradle():
    print("Reading JSON data... ", end='')
    response = urllib2.urlopen("http://files.minecraftforge.net/maven/net/minecraftforge/forge/json")
    jsonData = json.loads(response.read())
    packages = {}
    for pkg in jsonData["promos"]:
        id = jsonData["promos"][pkg]
        if not id in packages and id != 965:        # build 965 is NOT recommended! It ships with no gradle!
            packages[id] = pkg
    print("[Done]")

    print("Following packages are recommended:", end="\n\n")
    for id in packages:
        print(" [" + Style.BRIGHT + str(id) + Style.NORMAL + "] " + packages[id])
    print
    input = raw_input("\nPlease enter a preferred build number to continue > ")
    
    print("Downloading Forge... ", end='')
    forgeBuild = jsonData["number"][input]["mcversion"] + "-" + jsonData["number"][input]["version"]
    response = urllib2.urlopen(jsonData["webpath"] + "/" + forgeBuild + "/forge-" + forgeBuild + "-src.zip")
    zipData = zipfile.ZipFile(io.BytesIO(response.read()))
    print("[Done]")
    
    print("Extracting Zip... ", end='')
    zipData.extractall(r"forge")
    print("[Done]")
    
    print("Forge successfully downloaded to /forge/")

def runGradleTask(percent, callList, baseWPath):
    output = 0
    print("\rSetup ForgeGradle... " + str(percent) + "%", end='')
    try:
        execData = ["gradlew"]
        execData.extend(callList)
        output = subprocess.call(execData, creationflags=subprocess.CREATE_NEW_CONSOLE)
    except Exception:
        try:
            execData = ["gradlew.bat"]
            execData.extend(callList)
            output = subprocess.call(execData, creationflags=subprocess.CREATE_NEW_CONSOLE)
        except Exception as ex:
            print(ex)

    if output != 0:
        reinit()
        input = raw_input(Fore.RED + Style.BRIGHT + "\nThere was something wrong with the setup! Do you want to show the log file? [Y/N] > ")
        if input.lower() == "y":
            webbrowser.open("file://" + os.getcwd() + "/.gradle/gradle.log")
        os.chdir(baseWPath)
        return False
    return True
 
def setupGradle():
    print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    deinit()
    baseWPath = os.getcwd()
    os.chdir(gradlePath)
    if not runGradleTask(00, ["clean"], baseWPath):
        return
    if not runGradleTask(25, ["cleanCache"], baseWPath):
        return
    if not runGradleTask(50, ["setupDecompWorkspace", "--refresh-dependencies", "--stacktrace"], baseWPath):
        return
    if not runGradleTask(75, ["eclipse"], baseWPath):
        return
    print("\rSetup ForgeGradle... [Done]")
    os.chdir(baseWPath)
    reinit()

def checkForGradlew():
    hasGradle = False
    if not os.path.isfile("gradlew") and not os.path.isfile("forge/gradlew"):
        input = raw_input(Style.BRIGHT + Fore.YELLOW + "gradlew could not be found! Do you want to setup Forge here? [Y/N] > " + Fore.WHITE + Style.NORMAL)
        if input.lower() == "y":
            downloadGradle()
            global gradlePath
            gradlePath = r"forge"
            hasGradle = True
    else:
        if os.path.isfile("forge/gradlew"):
            global gradlePath
            gradlePath = r"forge"
        hasGradle = True
    
    if hasGradle:
        setupGradle()

def setupForge():
    checkForGradlew()