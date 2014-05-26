from __future__ import print_function

import subprocess
import os
import os.path
import title
import pythonHelper
import webbrowser

from colorama import deinit, reinit, Fore, Back, Style

gradlePath = r"."

def buildMod(mod):
    p = None
    try:
        gradlewCmd = "\"" + os.path.join(os.getcwd(), gradlePath, "gradlew\"") + " build --stacktrace"
        p = subprocess.Popen(gradlewCmd, cwd=mod)
    except Exception:
        try:
            gradlewCmd = "\"" + os.path.join(os.getcwd(), gradlePath, "gradlew.bat\"") + " build --stacktrace"
            p = subprocess.Popen(gradlewCmd, cwd=mod)
        except Exception as ex:
            print(Fore.RED + Style.BRIGHT + ex + Fore.RESET + Style.NORMAL)
    finally:
        if not p is None:
            try:
                p.wait()
                if p.returncode != 0:
                    print(Fore.RED + Style.BRIGHT + "Build failed with return code " + hex(p.returncode) + "!")
                    input = raw_input("Do you want to show the log file? [Y/N] > " + Fore.WHITE)
                    print(Fore.RESET + Style.NORMAL, end="")
                    if input.lower() == "y":
                        webbrowser.open("file://" + os.path.join(os.getcwd(), mod, ".gradle/gradle.log"))
            except KeyboardInterrupt as ex:
                print(Fore.YELLOW + Style.BRIGHT + "Build cancelled by user!" + Fore.RESET + Style.NORMAL)

def call():
    title.show("Mod Building")
    if os.path.isfile("forge/gradlew"):
        global gradlePath
        gradlePath = r"forge"
    elif not os.path.isfile("gradlew"):
        print(Fore.RED + Style.BRIGHT + "Gradle could not be found! Please setup Forge first and then try to build your mod again!" + Fore.RESET + Style.NORMAL)
        return
    modList = [f for f in os.listdir(os.path.join(gradlePath, "src")) if not os.path.isfile(os.path.join(gradlePath, "src", f))]
    
    print("There are following mods available for build:", end="\n\n")
    i = 0
    for f in modList:
        i += 1
        print(" [" + Style.BRIGHT + str(i) + Style.NORMAL + "] " + f)
    print
    choice = raw_input("\nPlease enter a number from above > " + Style.BRIGHT)
    print(Style.NORMAL, end="")
    choice = pythonHelper.isInteger(choice)
    if choice and choice > 0 and choice <= len(modList):
        buildMod(os.path.join(gradlePath, "src", modList[choice-1]))
    