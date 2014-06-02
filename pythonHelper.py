import os

from colorama import deinit, reinit, Fore, Back, Style

def pause():
    if os.system("PAUSE") != 0:
        os.system("read -p \"Press [Enter] key to continue...\"")

def clearScr():
    if os.system("CLS") != 0:
        os.system("clear")

def isInteger(s):
    try:
        return int(s)
    except ValueError:
        return False
        
def getYesNoInput(s):
    input = raw_input(Style.NORMAL + Fore.WHITE + s + " [Y/N] > " + Style.BRIGHT)
    while len(input) == 0 or not input in "yn":
        input = raw_input(Style.NORMAL + Fore.WHITE + " "*len(s + " [Y/N] ") + "> " + Style.BRIGHT)
    return input == "y"