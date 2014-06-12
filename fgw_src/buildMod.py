from __future__ import print_function

import subprocess
import webbrowser
import os
from collections import OrderedDict

from fgw_src import title, pythonHelper
from colorama import Fore, Style


def call():
    global gradlePath
    gradlePath = r"."
    title.show("Mod Building")
    if os.path.isfile("forge/gradlew"):
        gradlePath = r"forge"
    elif not os.path.isfile("gradlew"):
        print(Fore.RED + Style.BRIGHT + "Gradle could not be found!")
        print("Please setup Forge first and then try to build your mod again!" + Fore.RESET + Style.NORMAL)
        return

    modlist = [f for f in os.listdir(os.path.join(gradlePath, "fgw_src"))
               if not os.path.isfile(os.path.join(gradlePath, "fgw_src", f))]
    menulist = OrderedDict()
    for idx, val in enumerate(modlist):
        menulist[str(idx+1)] = val
    menulist["0"] = "[Abort]"

    choice = pythonHelper.is_integer(
        pythonHelper.menu_with_choice("There are following mods available for building", menulist,
                                      "Please choose a mod to build")
    )
    if 0 < choice <= len(modlist):
        build_mod(os.path.join(gradlePath, "fgw_src", modlist[choice-1]))


def build_mod(mod):
    proc = None
    try:
        gradlew_cmd = "\"" + os.path.join(os.getcwd(), gradlePath, "gradlew\"") + " build --stacktrace"
        proc = subprocess.Popen(gradlew_cmd, cwd=mod)
    except WindowsError:
        try:
            gradlew_cmd = "\"" + os.path.join(os.getcwd(), gradlePath, "gradlew.bat\"") + " build --stacktrace"
            proc = subprocess.Popen(gradlew_cmd, cwd=mod)
        except Exception as ex:
            print(Fore.RED + Style.BRIGHT + ex + Fore.RESET + Style.NORMAL)
    finally:
        if not proc is None:
            try:
                proc.wait()
                if proc.returncode != 0:
                    print(Fore.RED + Style.BRIGHT + "Build failed with return code " + hex(proc.returncode) + "!"
                          + Fore.RESET)
                    if pythonHelper.get_yesno_input("Do you want to show the log file?"):
                        webbrowser.open("file://" + os.path.join(os.getcwd(), mod, ".gradle/gradle.log"))
            except KeyboardInterrupt:
                print(Fore.YELLOW + Style.BRIGHT + "Build cancelled by user!" + Fore.RESET + Style.NORMAL)