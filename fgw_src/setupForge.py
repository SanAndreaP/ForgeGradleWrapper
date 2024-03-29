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
import time

from fgw_src import config, pythonHelper
from fgw_src.WorkingMsg import WorkingMsg
import title
from colorama import Fore, Style


__author__ = 'SanAndreasP'


def get_ver_from_buildgradle():
    with io.open(os.path.join(config.data[config.GRADLE_PATH], "build.gradle"), encoding="utf-8") as buildGradle:
        content = buildGradle.read()
        matches = re.compile(r"minecraft\s*\{.*?version.*?=.*?\"(.*?)\"", re.DOTALL | re.UNICODE).findall(content)
        if not matches is None and len(matches) > 0:
            return matches[0]
        else:
            return ""


def update_buildgradle_ver(mod, version):
    gradle_path = config.data[config.GRADLE_PATH]
    with io.open(os.path.join(gradle_path, "src", mod, "build.gradle"), mode="r+", encoding="utf-8") as buildGradle:
        content = buildGradle.read()
        pattern = re.compile(r"(.*?minecraft\s*\{.*?version.*?=.*?\").*?(\".*)", re.DOTALL | re.UNICODE | re.MULTILINE)
        matcher = pattern.match(content)
        output = matcher.group(1) + version + matcher.group(2)
        buildGradle.seek(0)
        buildGradle.truncate()
        buildGradle.flush()
        buildGradle.write(output)


def update_buildgradles():
    gradle_path = config.data[config.GRADLE_PATH]
    modlist = [f for f in os.listdir(os.path.join(gradle_path, "src"))
               if not os.path.isfile(os.path.join(gradle_path, "src", f))]
    print("There are build.gradle files available for following mods:")
    print("\n".join("- {}".format(v) for k, v in enumerate(modlist)))
    if pythonHelper.get_yesno_input("Want to update the MC version for those as well?\n"
                                    + "Please note that if you don't update them, problems may arise!"):
        newver = get_ver_from_buildgradle()
        for mod in modlist:
            print(Style.BRIGHT + "Updating MC version in mod \"" + mod + "\"" + Style.NORMAL)
            update_buildgradle_ver(mod, newver)
    else:
        print(Fore.YELLOW + Style.BRIGHT + "You choose not to update the version numbers.")
        print("This can cause problems! I suggest you update them anyway." + Fore.WHITE + Style.NORMAL)


def download_gradle():
    gradle_path = config.data[config.GRADLE_PATH]
    wrk_msg = WorkingMsg("Reading JSON data")
    wrk_msg.start()
    url = "http://files.minecraftforge.net/maven/net/minecraftforge/forge/json"
    try:
        time.sleep(3)
        response = urllib2.urlopen(url)
        jsondata = json.loads(response.read())
        packages = {}
        for pkg in jsondata["promos"]:
            forgebuild = jsondata["promos"][pkg]
            if not forgebuild in packages and forgebuild != 965:    # build 965 is NOT recommended!
                packages[str(forgebuild)] = pkg                     # It ships with no gradle!
    except (urllib2.HTTPError, urllib2.URLError) as ex:
        wrk_msg.set_output(0x01)
        wrk_msg.join()
        print(Style.BRIGHT + Fore.RED + "There was a problem reaching the url >>" + url + "<<")
        print(ex.msg)
        print(Style.NORMAL + Fore.RESET)
        return False
    finally:
        wrk_msg.join()

    choice = pythonHelper.menu_with_choice("Following packages are recommended", packages,
                                           "Please enter a preferred build number to continue")

    if gradle_path is not None and os.path.isfile(os.path.join(gradle_path, "build.gradle")):
        filemode = os.stat(os.path.join(gradle_path, "build.gradle"))[stat.ST_MODE]
        os.chmod(os.path.join(gradle_path, "build.gradle"), filemode | stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)

    wrk_msg = WorkingMsg("Downloading Forge")
    wrk_msg.start()
    forgebuild = jsondata["number"][choice]["mcversion"] + "-" + jsondata["number"][choice]["version"]
    url = jsondata["webpath"] + "/" + forgebuild + "/forge-" + forgebuild + "-src.zip"
    try:
        time.sleep(3)
        response = urllib2.urlopen(url)
        zipdata = zipfile.ZipFile(io.BytesIO(response.read()))
    except (urllib2.HTTPError, urllib2.URLError) as ex:
        wrk_msg.set_output(0x01)
        wrk_msg.join()
        print(Style.BRIGHT + Fore.RED + "There was a problem reaching the url >>" + url + "<<")
        print(ex.msg)
        print(Style.NORMAL + Fore.RESET)
        return False
    finally:
        wrk_msg.join()

    print("Extracting Zip... ", end="")
    zipdata.extractall(r"forge")
    print("[Done]")

    print("Forge successfully downloaded to /forge/")
    return True


def run_gradle_task(calllist):
    gradle_path = config.data[config.GRADLE_PATH]
    output = 0
    thread = WorkingMsg("Setup ForgeGradle: " + calllist[0])
    thread.start()
    try:
        execdata = [os.path.join(os.getcwd(), gradle_path, "gradlew")]
        execdata.extend(calllist)
        subprocess.check_call(execdata, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=gradle_path)
    except (subprocess.CalledProcessError, WindowsError):
        try:
            execdata = [os.path.join(os.getcwd(), gradle_path, "gradlew.bat")]
            execdata.extend(calllist)
            subprocess.check_call(execdata, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=gradle_path)
        except subprocess.CalledProcessError as ex:
            output = ex.returncode
            if ex.returncode == 0xff:
                print(ex)
    finally:
        thread.set_output(output)
        thread.join()
    if output != 0x00 and output != 0xff:
        print(Fore.RED + Style.BRIGHT + "Setup failed with return code " + hex(output) + "!" + Fore.RESET)
        if pythonHelper.get_yesno_input("Do you want to show the log file?"):
            webbrowser.open("file://" + os.path.join(os.getcwd(), gradle_path, ".gradle", "gradle.log"))
        return False
    elif output == 0xff:
        return pythonHelper.get_yesno_input(Fore.YELLOW + Style.BRIGHT
                                            + "You've cancelled the task! Continue?"
                                            + Fore.RESET + Style.NORMAL)
    return True


def copy_def_buildgradle():
    print("Copy build.gradle...", end="")
    gradle_path = config.data[config.GRADLE_PATH]
    if os.path.isfile(os.path.join(gradle_path, "src", "main", "build.gradle")):
        print("\rbuild.gradle already copied! Skipping.")
        filemode = os.stat(os.path.join(gradle_path, "build.gradle"))[stat.ST_MODE]
        os.chmod(os.path.join(gradle_path, "build.gradle"), filemode & ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH)
        return

    shutil.copyfile(os.path.join(gradle_path, "build.gradle"), os.path.join(gradle_path, "src", "main", "build.gradle"))
    filemode = os.stat(os.path.join(gradle_path, "build.gradle"))[stat.ST_MODE]
    os.chmod(os.path.join(gradle_path, "build.gradle"), filemode & ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH)
    with io.open(os.path.join(gradle_path, "src", "main", "build.gradle"), mode="a", encoding="utf-8") as buildGradle:
        buildGradle.write(u"\nsourceSets {")
        buildGradle.write(u"\n    main {")
        buildGradle.write(u"\n        java { srcDir 'java' }")
        buildGradle.write(u"\n        resources { srcDir 'resources' }")
        buildGradle.write(u"\n    }")
        buildGradle.write(u"\n}\n")
        buildGradle.close()


def setup_gradle():
    copy_def_buildgradle()
    if not run_gradle_task(["clean"]):
        return
    if not run_gradle_task(["cleanCache"]):
        return
    if not run_gradle_task(["setupDecompWorkspace", "--refresh-dependencies", "--stacktrace"]):
        return
    if not run_gradle_task([config.data[config.IDE]]):
        return
    if not run_gradle_task(["setupDecompWorkspace", "--stacktrace"]):    # workaround for 1.7.10 Forge crash
        return
    print("\rSetup ForgeGradle... [Done]")


def call():
    title.show("Forge Setup")
    if config.data[config.GRADLE_PATH] is None:
        print(Style.BRIGHT + Fore.YELLOW + "ForgeGradle could not be found!" + Fore.RESET + Style.NORMAL)
        if pythonHelper.get_yesno_input("Do you want to set it up here?"):
            if not download_gradle():
                return
            config.data[config.GRADLE_PATH] = r"forge"
            setup_gradle()
    else:
        menu_items = OrderedDict()
        menu_items["1"] = "rebuild workspace"
        menu_items["2"] = "update ForgeGradle"
        menu_title = Style.BRIGHT + Fore.GREEN + "ForgeGradle has been found!" + Fore.RESET + Style.NORMAL
        choice = pythonHelper.menu_with_choice(menu_title, menu_items, "Please choose an option from above")
        if choice == "1":
            setup_gradle()
        elif choice == "2":
            download_gradle()
            setup_gradle()
        elif choice == "3":
            update_buildgradles()