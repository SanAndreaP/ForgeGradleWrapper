import os

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