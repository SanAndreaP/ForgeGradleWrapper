from __future__ import print_function

import title
import buildMod
import colorama
import landscape
import setupBuild
import setupForge
import pythonHelper
import nothingToSeeHereReallyNopeSoEmptyAndNothingness

from collections import OrderedDict

colorama.init()

global menuItm
menuItm = dict()
menuItm["0"] = exit
menuItm["1"] = setupForge.call
menuItm["2"] = setupBuild.call
menuItm["3"] = buildMod.call
menuItm["4"] = landscape.call
menuItm["5"] = nothingToSeeHereReallyNopeSoEmptyAndNothingness.call

global menuTxt
menuTxt = OrderedDict()
menuTxt["1"] = "setup forge"
menuTxt["2"] = "setup mod building"
menuTxt["3"] = "build mod"
menuTxt["0"] = "exit"


def mainmenu():
    title.show()
    choice = pythonHelper.printmenu_and_getchoice("Menu:", menuTxt, "Please choose an item from above")
    menuItm[choice]()

while True:
    mainmenu()
    if not pythonHelper.get_yesno_input("Continue working?"):
        break

colorama.deinit()