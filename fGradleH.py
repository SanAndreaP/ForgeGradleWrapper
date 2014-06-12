from __future__ import print_function

from collections import OrderedDict

import colorama
from fgw_src import setupForge, nothingToSeeHereReallyNopeSoEmptyAndNothingness, config, setupBuild, buildMod, \
    landscape, title, pythonHelper

__author__ = 'SanAndreasP'


colorama.init()
config.read_config()

menuItm = dict()
menuItm["0"] = exit
menuItm["1"] = setupForge.call
menuItm["2"] = setupBuild.call
menuItm["3"] = buildMod.call
menuItm["4"] = landscape.call
menuItm["5"] = nothingToSeeHereReallyNopeSoEmptyAndNothingness.call

menuTxt = OrderedDict()
menuTxt["1"] = "setup forge"
menuTxt["2"] = "setup mod building"
menuTxt["3"] = "build mod"
menuTxt["0"] = "exit"


def mainmenu():
    global menuItm, menuTxt
    title.show()
    choice = pythonHelper.menu_with_choice("Menu:", menuTxt, "Please choose an item from above")
    menuItm[choice]()

while True:
    mainmenu()
    if not pythonHelper.get_yesno_input("Continue working?"):
        break

colorama.deinit()
config.write_config()