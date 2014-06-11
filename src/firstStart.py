from __future__ import print_function

from collections import OrderedDict
import re
import subprocess
from colorama.ansi import Fore, Style

import pythonHelper
import config
from src import title
from src.WorkingMsg import WorkingMsg

__author__ = 'SanAndreasP'


def call():
    title.show("Initial Setup")

    menu_items = OrderedDict()
    menu_items["eclipse"] = "Eclipse Java IDE"
    menu_items["idea"] = "JetBrains IntelliJ IDEA Java IDE"
    usr_input = pythonHelper.printmenu_and_getchoice("Following IDEs are supported by ForgeGradle:", menu_items,
                                                     "Please enter your preferred IDE:")
    if usr_input in menu_items:
        config.data[config.IDE] = usr_input

    wrk_msg = WorkingMsg("Checking Java Compiler")
    wrk_msg.start()
    proc = None
    try:
        proc = subprocess.Popen("javac -version", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        proc_out = proc.communicate()
        wrk_msg._done_msg = proc_out[0]
        wrk_msg.set_output(proc.returncode)
        wrk_msg.join()
        config.data[config.JAVA_VER] = re.compile(r"javac ([0-9]+?\.[0-9]+?)\..*").match(proc_out[0]).group(1)
    except Exception as ex:
        if proc is not None:
            wrk_msg.set_output(proc.returncode)
        else:
            wrk_msg.set_output(0x01)
        wrk_msg.join()
        print(Fore.RED + Style.BRIGHT + "There was an error trying to get the Java Compiler version:")
        print(str(ex) + Fore.RESET + Style.NORMAL)
    pythonHelper.pause()