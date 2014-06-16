from __future__ import print_function

import subprocess
import webbrowser
import os
from collections import OrderedDict

from fgw_src import pythonHelper, config, title
from colorama import Fore, Style


def call():
    title.show("Mod Building")
    gradle_path = config.data[config.GRADLE_PATH]
    modlist = [f for f in os.listdir(os.path.join(gradle_path, "src"))
               if not os.path.isfile(os.path.join(gradle_path, "src", f))]
    menulist = OrderedDict()
    for idx, val in enumerate(modlist):
        menulist[str(idx + 1)] = val
    menulist["0"] = "[Abort]"

    choice = pythonHelper.is_integer(
        pythonHelper.menu_with_choice("There are following mods available for building", menulist,
                                      "Please choose a mod to build")
    )
    if 0 < choice <= len(modlist):
        build_mod(os.path.join(gradle_path, "src", modlist[choice - 1]))


def build_mod(mod):
    gradle_path = config.data[config.GRADLE_PATH]
    proc = None
    try:
        gradlew_cmd = "\"" + os.path.join(os.getcwd(), gradle_path, "gradlew\"") + " build --stacktrace"
        proc = subprocess.Popen(gradlew_cmd, cwd=mod)
    except WindowsError:
        try:
            gradlew_cmd = "\"" + os.path.join(os.getcwd(), gradle_path, "gradlew.bat\"") + " build --stacktrace"
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