from __future__ import print_function

from colorama import Style
import pythonHelper
from src import title

__author__ = 'SanAndreasP'


def call():
    title.show("Manual")
    print("")
    print(Style.BRIGHT + "NAME")
    print("  ForgeGradleWrapper" + Style.NORMAL + " - A helper for ForgeGradle to easily set up")
    print("                       a workspace and manage mods")
    print("")
    print(Style.BRIGHT + "DESCRIPTION" + Style.NORMAL)
    print("  This program is intended to simplify the (re-)setup of ForgeGradle, managing")
    print("  key settings of your build.gradle files, have local dependencies without")
    print("  manually copying any jars and finally building your mods.")
    print("")
    print(Style.BRIGHT + "FIRST START" + Style.NORMAL)
    print("  Upon first start you will need to configure some things. First you need to")
    print("  choose which IDE you want to use.")
    print("  After that the program will check for the installed Java Compiler. If it")
    print("  fails, it's usually because 1. you didn't install the JDK, or 2. your JDK is")
    print("  not listed in the PATH!")
    print("")
    pythonHelper.pause()
    title.show("Manual")
    print(Style.BRIGHT + "SETUP FORGE" + Style.NORMAL)
    print("  The first thing you want to do is setup a workspace with ForgeGradle. Here")
    print("  you need to enter which build number you want to download. To make it easier")
    print("  for you, the program will list you recommended packages. After that, you just")
    print("  have to wait until it completes the setup.")
    print("  If anything goes wrong, the program will ask you if you want to show the log")
    print("  to see what went wrong.")
    print("")
    print(Style.BRIGHT + "SETUP MOD BUILDING" + Style.NORMAL)
    print("  Here you can easily edit general settings of your build.gradle without")
    print("  manually messing with it.")
    print("  You can also define local and remote dependencies. Remote dependencies are")
    print("  directly defined within your build.gradle. Local dependencies are archives")
    print("  containing their unobfuscated, compiled code")
    print("")
    pythonHelper.pause()
    title.show("Manual")
    print(Style.BRIGHT + "BUILD MOD" + Style.NORMAL)
    print("  This is with SETUP FORGE the easiest command, as you only need to select")
    print("  which mod needs to be build and wait for it to finish.")
    print("  Like with SETUP FORGE, if something goes wrong, you have the option to look")
    print("  at the logs.")
    print("")
    pythonHelper.pause()