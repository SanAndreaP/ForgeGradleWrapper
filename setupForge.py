from __future__ import print_function
from collections import OrderedDict

import subprocess
import webbrowser
import urllib2
import zipfile
import shutil
import json
import stat
import io
import os
import re

import pythonHelper
import title
from colorama import Fore, Style


gradlePath = r"."


def getverfrombuildgradle():
    with io.open(os.path.join(gradlePath, "build.gradle"), mode="r", encoding="utf-8") as buildGradle:
        content = buildGradle.read()
        pattern = re.compile(r"minecraft\s*\{.*?version.*?=.*?\"(.*?)\"", re.DOTALL | re.UNICODE)
        matches = pattern.findall(content)
        if not matches is None and len(matches) > 0:
            return matches[0]
        else:
            return ""


def updatebuildgradlever(mod, version):
    with io.open(os.path.join(gradlePath, "src", mod, "build.gradle"), mode="r+", encoding="utf-8") as buildGradle:
        content = buildGradle.read()
        pattern = re.compile(r"(.*?minecraft\s*\{.*?version.*?=.*?\").*?(\".*)", re.DOTALL | re.UNICODE | re.MULTILINE)
        matcher = pattern.match(content)
        output = matcher.group(1) + version + matcher.group(2)
        buildGradle.seek(0)
        buildGradle.truncate()
        buildGradle.flush()
        buildGradle.write(output)


def updatebuildgradles():
    modlist = [f for f in os.listdir(os.path.join(gradlePath, "src"))
               if not os.path.isfile(os.path.join(gradlePath, "src", f))]
    print("There are build.gradle files available for following mods:")
    print("\n".join("- {}".format(v) for k, v in enumerate(modlist)))
    if pythonHelper.get_yesno_input("Want to update the MC version for those as well?"):
        newver = getverfrombuildgradle()
        for mod in modlist:
            print(Style.BRIGHT + "Updating MC version in mod \"" + mod + "\"" + Style.NORMAL)
            updatebuildgradlever(mod, newver)
    else:
        print(Fore.YELLOW + Style.BRIGHT + "You choose not to update the version numbers.")
        print("This can cause problems! I suggest you update them anyway." + Fore.WHITE + Style.NORMAL)


def downloadgradle():
    print("Reading JSON data... ", end="")
    response = urllib2.urlopen("http://files.minecraftforge.net/maven/net/minecraftforge/forge/json")
    jsondata = json.loads(response.read())
    packages = {}
    for pkg in jsondata["promos"]:
        forgebuild = jsondata["promos"][pkg]
        if not forgebuild in packages and forgebuild != 965:  # build 965 is NOT recommended! It ships with no gradle!
            packages[str(forgebuild)] = pkg
    print("[Done]")

    choice = pythonHelper.printmenu_and_getchoice("Following packages are recommended", packages,
                                                "Please enter a preferred build number to continue")

    if os.path.isfile(os.path.join(gradlePath, "build.gradle")):
        filemode = os.stat(os.path.join(gradlePath, "build.gradle"))[stat.ST_MODE]
        os.chmod(os.path.join(gradlePath, "build.gradle"), filemode | stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)

    print(Style.NORMAL + "Downloading Forge... ", end="")
    forgebuild = jsondata["number"][choice]["mcversion"] + "-" + jsondata["number"][choice]["version"]
    response = urllib2.urlopen(jsondata["webpath"] + "/" + forgebuild + "/forge-" + forgebuild + "-src.zip")
    zipdata = zipfile.ZipFile(io.BytesIO(response.read()))
    print("[Done]")

    print("Extracting Zip... ", end="")
    zipdata.extractall(r"forge")
    print("[Done]")

    print("Forge successfully downloaded to /forge/")


def rungradletask(percent, calllist):
    output = 0
    print("\rSetup ForgeGradle... " + str(percent) + "%", end='')
    try:
        execdata = [os.path.join(os.getcwd(), gradlePath, "gradlew")]
        execdata.extend(calllist)
        subprocess.check_call(execdata, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=gradlePath)
    except subprocess.CalledProcessError:
        try:
            execdata = [os.path.join(os.getcwd(), gradlePath, "gradlew.bat")]
            execdata.extend(calllist)
            subprocess.check_call(execdata, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=gradlePath)
        except subprocess.CalledProcessError as ex:
            output = ex.returncode
            print(ex)

    if output != 0:
        print(Fore.RED + Style.BRIGHT + "\nSetup failed with return code " + hex(output) + "!" + Fore.RESET)
        if pythonHelper.get_yesno_input("Do you want to show the log file?"):
            webbrowser.open("file://" + os.path.join(os.getcwd(), gradlePath, ".gradle/gradle.log"))
        return False
    return True


def copydefbuildgradle():
    print("Copy build.gradle...", end="")
    if os.path.isfile(os.path.join(gradlePath, "src/main/build.gradle")):
        print("\rbuild.gradle already copied! Skipping.")
        filemode = os.stat(os.path.join(gradlePath, "build.gradle"))[stat.ST_MODE]
        os.chmod(os.path.join(gradlePath, "build.gradle"), filemode & ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH)
        return

    shutil.copyfile(os.path.join(gradlePath, "build.gradle"), os.path.join(gradlePath, "src/main/build.gradle"))
    filemode = os.stat(os.path.join(gradlePath, "build.gradle"))[stat.ST_MODE]
    os.chmod(os.path.join(gradlePath, "build.gradle"), filemode & ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH)
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


def setupgradle():
    copydefbuildgradle()
    if not rungradletask(00, ["clean"]):
        return
    if not rungradletask(25, ["cleanCache"]):
        return
    if not rungradletask(50, ["setupDecompWorkspace", "--refresh-dependencies", "--stacktrace"]):
        return
    if not rungradletask(75, ["eclipse"]):
        return
    print("\rSetup ForgeGradle... [Done]")


def call():
    title.show("Forge Setup")
    if not os.path.isfile("gradlew") and not os.path.isfile("forge/gradlew"):
        print(Style.BRIGHT + Fore.YELLOW + "ForgeGradle could not be found!" + Fore.RESET + Style.NORMAL)
        if pythonHelper.get_yesno_input("Do you want to set it up here?"):
            downloadgradle()
            global gradlePath
            gradlePath = r"forge"
            setupgradle()
    else:
        if os.path.isfile("forge/gradlew"):
            global gradlePath
            gradlePath = r"forge"
        menuitems = OrderedDict()
        menuitems["1"] = "rebuild workspace"
        menuitems["2"] = "update ForgeGradle"
        print(Style.BRIGHT + Fore.GREEN + "ForgeGradle has been found!" + Fore.RESET + Style.NORMAL, end="")
        choice = pythonHelper.printmenu_and_getchoice("", menuitems, "Please choose an option from above")
        if choice == "1":
            setupgradle()
        elif choice == "2":
            downloadgradle()
            setupgradle()
        elif choice == "3":
            updatebuildgradles()
