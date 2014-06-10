from __future__ import print_function

from collections import OrderedDict
import subprocess

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
    try:
        proc = subprocess.Popen("javac -version", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        proc_out, proc_err = proc.communicate()
        wrk_msg._done_msg = proc_out
    except Exception as ex:
        wrk_msg._error_msg = ex.__str__()
        wrk_msg.set_output(0x01)
    wrk_msg.join()
    pythonHelper.pause()