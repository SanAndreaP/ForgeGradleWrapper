from __future__ import print_function

import subprocess
import webbrowser
import zipfile
import os.path
import urllib2
import shutil
import title
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
    input = raw_input("\nPlease enter a preferred build number to continue > " + Style.BRIGHT)
    
    print(Style.NORMAL + "Downloading Forge... ", end='')
    forgeBuild = jsonData["number"][input]["mcversion"] + "-" + jsonData["number"][input]["version"]
    response = urllib2.urlopen(jsonData["webpath"] + "/" + forgeBuild + "/forge-" + forgeBuild + "-src.zip")
    zipData = zipfile.ZipFile(io.BytesIO(response.read()))
    print("[Done]")
    
    print("Extracting Zip... ", end='')
    zipData.extractall(r"forge")
    print("[Done]")
    
    print("Forge successfully downloaded to /forge/")

def runGradleTask(percent, callList):
    output = 0
    print("\rSetup ForgeGradle... " + str(percent) + "%", end='')
    try:
        execData = [os.path.join(os.getcwd(), gradlePath, "gradlew")]
        execData.extend(callList)
        output = subprocess.call(execData, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=gradlePath)
    except Exception:
        try:
            execData = [os.path.join(os.getcwd(), gradlePath, "gradlew.bat")]
            execData.extend(callList)
            output = subprocess.call(execData, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=gradlePath)
        except Exception as ex:
            print(ex)

    if output != 0:
        print(Fore.RED + Style.BRIGHT + "\nSetup failed with return code " + hex(output) + "!")
        input = raw_input("Do you want to show the log file? [Y/N] > " + Fore.WHITE)
        print(Fore.RESET + Style.NORMAL, end="")
        if input.lower() == "y":
            webbrowser.open("file://" + os.path.join(os.getcwd(), gradlePath, ".gradle/gradle.log"))
        return False
    return True
    
def copyDefBuildGradle():
    shutil.copyfile(os.path.join(gradlePath, "build.gradle"), os.path.join(gradlePath, "src/main/build.gradle"))
    with io.open(os.path.join(gradlePath, "src/main/build.gradle"), mode="a", encoding="utf-8") as buildGradle:
        buildGradle.write(u"\ndependencies {")
        buildGradle.write(u"\n    compile fileTree(dir: 'libs', include: '*.jar')")
        buildGradle.write(u"\n}\n")
        buildGradle.write(u"\nsourceSets {")
        buildGradle.write(u"\n    main {")
        buildGradle.write(u"\n        java { srcDir 'java' }")
        buildGradle.write(u"\n        resources { srcDir 'resources' }")
        buildGradle.write(u"\n    }")
        buildGradle.write(u"\n}\n")
        buildGradle.close()

 
def setupGradle():
    if not runGradleTask(00, ["clean"]):
        return
    if not runGradleTask(25, ["cleanCache"]):
        return
    if not runGradleTask(50, ["setupDecompWorkspace", "--refresh-dependencies", "--stacktrace"]):
        return
    if not runGradleTask(75, ["eclipse"]):
        return
    copyDefBuildGradle()
    print("\rSetup ForgeGradle... [Done]")

def call():
    title.show("Forge Setup")
    hasGradle = False
    if not os.path.isfile("gradlew") and not os.path.isfile("forge/gradlew"):
        input = raw_input(Style.BRIGHT + Fore.YELLOW + "gradlew could not be found! Do you want to set it up here? [Y/N] > " + Fore.WHITE + Style.NORMAL)
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