from __future__ import print_function

from collections import OrderedDict
import re
import subprocess
from colorama.ansi import Fore, Style

import pythonHelper
import config
from src import title, help
from src.WorkingMsg import WorkingMsg

__author__ = 'SanAndreasP'


def call():
    print("This is the first time you've started this program!")
    if pythonHelper.get_yesno_input("Do you want to see the help page?"):
        help.call()

    title.show("Initial Setup")

    menu_items = OrderedDict()
    menu_items["eclipse"] = "Eclipse Java IDE"
    menu_items["idea"] = "JetBrains IntelliJ IDEA Java IDE"
    usr_input = pythonHelper.menu_with_choice("Following IDEs are supported by ForgeGradle:", menu_items,
                                              "Please enter your preferred IDE:")
    if usr_input in menu_items:
        config.data[config.IDE] = usr_input

    wrk_msg = WorkingMsg("Checking Java Compiler")
    wrk_msg.start()
    proc = None
    try:
        proc = subprocess.Popen("javac -version", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        proc_out = proc.communicate()
        proc_out = proc_out[0].strip("\n\r")
        wrk_msg.set_output(proc.returncode)
        wrk_msg.join()
        j_ver = re.compile(r"javac ([0-9]+?\.[0-9]+?)\..*").match(proc_out).group(1)
        print("Following version of the Java Compiler was detected: "
              + Style.BRIGHT + j_ver + Style.NORMAL + " (" + proc_out + ")")
        if not pythonHelper.get_yesno_input("Is this the version of Java you want to use as default?"):
            menu_items = OrderedDict()
            menu_items["1.6"] = "Java 6"
            menu_items["1.7"] = "Java 7"
            menu_items["1.8"] = "Java 8"
            usr_input = pythonHelper.menu_with_choice("Following versions are supported:", menu_items,
                                                      "Please enter the desired java version")
            j_ver = usr_input
        config.data[config.JAVA_VER] = j_ver
    except Exception as ex:
        if proc is not None:
            wrk_msg.set_output(proc.returncode)
        else:
            wrk_msg.set_output(0x01)
        wrk_msg.join()
        print(Fore.RED + Style.BRIGHT + "There was an error trying to get the Java Compiler version:")
        print(str(ex) + Fore.RESET + Style.NORMAL)
    pythonHelper.pause()