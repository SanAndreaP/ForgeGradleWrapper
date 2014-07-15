from __future__ import print_function

import subprocess
import webbrowser
import shutil
import glob
import json
import io
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
    if os.path.isfile(os.path.join(mod, "dependencies.json")):
        print(Fore.GREEN + Style.BRIGHT + "A dependencies.json file was found! Copying dependencies now!" + Fore.RESET
              + Style.NORMAL)
        try:
            with io.open(os.path.join(mod, "dependencies.json")) as dep_file:
                dependencies = json.load(dep_file, encoding="utf-8")
                for dep_data in dependencies:
                    if dep_data["type"] == "local_mod":
                        files = glob.iglob(os.path.join(gradle_path, "src", dep_data["mod"], dep_data["path"],
                                                        dep_data["file"])
                        )
                        for dep in files:
                            if os.path.isfile(dep):
                                dst_folder = os.path.join(mod, "build/dependencies")
                                if not os.path.exists(dst_folder):
                                    os.makedirs(dst_folder)
                                shutil.copy(dep, dst_folder)
        except IOError as ex:
            print(Fore.RED + Style.BRIGHT + "Following error occured while grabbing the dependencies:")
            print(ex)
            print("The build will proceed, but severe errors may occur!" + Fore.RESET + Style.NORMAL)

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