from collections import OrderedDict

from fgw_src import title, pythonHelper


def call():
    title.show("Mod Build Setup")

    menu_items = OrderedDict()
    menu_items["1"] = ("[NYI] Change authors", chng_authors)
    menu_items["2"] = ("[NYI] Change version", lambda: None)
    menu_items["3"] = ("[NYI] Change mod group", lambda: None)
    menu_items["4"] = ("[NYI] Change archive base name", lambda: None)
    menu_items["5"] = ("[NYI] Change logo", lambda: None)
    menu_items["6"] = ("[NYI] Change description", lambda: None)
    menu_items["7"] = ("[NYI] Change mod URL", lambda: None)
    menu_items["8"] = ("[NYI] Manage local dependencies", lambda: None)
    menu_items["9"] = ("[NYI] Manage remote dependencies", lambda: None)
    menu_items["0"] = ("Abort", lambda: None)

    choice = pythonHelper.menu_with_choice("Following options are available:", menu_items,
                                           "Please choose an option from above")
    title.show("Mod Build Setup")
    menu_items[choice][1]()


def chng_authors():
    pass