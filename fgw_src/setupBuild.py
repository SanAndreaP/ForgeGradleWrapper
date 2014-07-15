from __future__ import print_function

from collections import OrderedDict
from fgw_src import title, pythonHelper, config
from colorama import Style, Fore

import os
import io
import re
import json


def call():
    title.show("Mod Build Setup")
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
        chosen_mod = modlist[choice-1]

        title.show("Mod Build Setup - " + chosen_mod)

        menu_items = OrderedDict()
        menu_items["1"] = ("[NYI] Change authors", chng_authors)
        menu_items["2"] = ("[NYI] Change version", lambda(mod): None)
        menu_items["3"] = ("[NYI] Change mod group", lambda(mod): None)
        menu_items["4"] = ("[NYI] Change archive base name", lambda(mod): None)
        menu_items["5"] = ("[NYI] Change logo", lambda(mod): None)
        menu_items["6"] = ("[NYI] Change description", lambda(mod): None)
        menu_items["7"] = ("[NYI] Change mod URL", lambda(mod): None)
        menu_items["8"] = ("Manage dependencies", manage_dependencies)
        menu_items["0"] = ("[Abort]", lambda(mod): None)

        choice = pythonHelper.menu_with_choice("Following options are available:", menu_items,
                                               "Please choose an option from above")
        title.show("Mod Build Setup - " + chosen_mod)
        menu_items[choice][1](chosen_mod)


def chng_authors(mod):
    pass


def manage_dependencies(mod):
    title.show("Mod Build Setup - " + mod)
    gradle_path = config.data[config.GRADLE_PATH]
    mod_folder = os.path.join(gradle_path, "src", mod)

    dependencies = []
    try:
        with io.open(os.path.join(mod_folder, "dependencies.json")) as dep_file:
            dependencies = json.load(dep_file, encoding="utf-8")
    except IOError:
        print(Fore.YELLOW + Style.BRIGHT + "There was no dependencies.json found." + Fore.RESET + Style.NORMAL)
        add_dependency(mod, dependencies)

    choice = pythonHelper.get_yesno_input("You want to save your changes?")
    if choice:
        try:
            with io.open(os.path.join(mod_folder, "dependencies.json"), "w") as dep_file:
                dep_file.write(json.dumps(dependencies, sort_keys=False, indent=4, ensure_ascii=False))
        except IOError as ex:
            print(Fore.RED + Style.BRIGHT + "There was an error while saving the dependencies:")
            print(ex)
            print(Fore.RESET + Style.NORMAL, end="")

    # choice = pythonHelper.get_yesno_input("You want to update your build.gradle?")
    # if choice:
    #     update_build_gradle(mod, dependencies)


# def update_build_gradle(mod, dependencies):
#     gradle_path = config.data[config.GRADLE_PATH]
#     with io.open(os.path.join(gradle_path, "src", mod, "build.gradle"), mode="r+", encoding="utf-8") as buildGradle:
#         content = buildGradle.read()
#         pattern = re.compile(r"(.*^dependencies {).*?(^})", re.DOTALL | re.UNICODE | re.MULTILINE)
#         matcher = pattern.match(content)
#         output = matcher.group(1)
#         buildGradle.seek(0)
#         buildGradle.truncate()
#         buildGradle.flush()
#         buildGradle.write(output)


def add_dependency(mod, dependencies):
    gradle_path = config.data[config.GRADLE_PATH]
    mod_folder = os.path.join(gradle_path, "src", mod)

    menu_items = OrderedDict()
    menu_items["1"] = "add local mod dependency"
    menu_items["2"] = "[NYI] add local, external dependency"
    menu_items["3"] = "[NYI] add remote dependency"
    menu_items["0"] = "[Abort]"
    choice = pythonHelper.menu_with_choice("Following options are available:", menu_items,
                                           "Please choose an option from above")

    if choice == "1":
        modlist = [f for f in os.listdir(os.path.join(gradle_path, "src"))
                   if not os.path.isfile(os.path.join(gradle_path, "src", f)) and not f == mod]
        menu_items = OrderedDict()
        for idx, val in enumerate(modlist):
            menu_items[str(idx + 1)] = val
        menu_items["0"] = "[Abort]"

        choice = pythonHelper.is_integer(
            pythonHelper.menu_with_choice("", menu_items, "Please choose a mod as a dependency")
        )
        if 0 < choice <= len(modlist):
            dep_dir = raw_input("Please enter the dependency directory within the mod path (e.g. \"build/libs\")\n> "
                                + Fore.YELLOW + Style.BRIGHT)

            print(Fore.RESET + Style.NORMAL + "Please enter the filename of the dependency")
            print("(note that you can also use wildcards, e.g. *, to grab multiple files")
            print(" like \"*.jar\" to grab all .jar files)\n> " + Fore.YELLOW + Style.BRIGHT, end="")
            dep_file_wc = raw_input("")
            print(Fore.RESET + Style.NORMAL, end="")

            dep_data = OrderedDict()
            dep_data["type"] = "local_mod"
            dep_data["mod"] = modlist[choice-1]
            dep_data["path"] = dep_dir
            dep_data["file"] = dep_file_wc
            dependencies.append(dep_data)