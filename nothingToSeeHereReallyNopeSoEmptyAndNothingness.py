from __future__ import print_function

from colorama import deinit, reinit, Fore, Back, Style
import os
import time
import random
import locale

playerHealth = 100.0
enemyHealth = 100.0

playerStamina = 10.0
enemyStamina = 10.0
enemyName = ""
isPlayerTurn = False

playerAttacks = [
        ["Scratch", 0.1, 1.0],
        ["Kick", 0.5, 4.0],
        ["Punch", 0.4, 3.5],
        ["Fireball", 8.0, 65.0],
        ["Lightbeam", 10.0, 80.5]
    ]
    
enemyAttacks = [
        ["Stab", 0.1, 1.0],
        ["Choke", 0.5, 4.0],
        ["Whip", 0.4, 3.5],
        ["Shockwave", 8.0, 65.0],
        ["Dark Neurosplitter", 10.0, 80.5]
    ]
    
enemyNames = [
        "Lucius",
        "Deadskull",
        "Earthburn",
        "Grossbone The Hunter",
        "Snowrivet The Tracker",
        "Scareghast",
        "Beastshiver The Rancid",
        "Shiverterror",
        "Shockghost The Cremator",
        "Rootstrike The Grotesque"
    ]
    
def doEnemyAttack():
    global enemyStamina, playerHealth
    
    time.sleep(1)
    attempts = 0
    attack = False
    miss = random.randint(0,1) == 1
    while attempts < 3:
        attack = enemyAttacks[random.randrange(len(enemyAttacks))]
        if enemyStamina < attack[1]:
            attempts += 1
            attack = False
        else:
            break
    if attack:
        print(enemyName + " is using " + attack[0])
        time.sleep(1)
        if miss:
            print(enemyName + " missed!")
        else:
            attackPts = float("{0:.2f}".format(random.uniform(attack[2] - attack[2] * 0.1, attack[2])))
            print("It did " + str(attackPts) + " Points of damage!")
            playerHealth -= attackPts
        enemyStamina -= attack[1]
    os.system("PAUSE")

def showUI():
    os.system("CLS")
    print(Style.BRIGHT, end="")
    
    print(Fore.GREEN + "Players health: " + Fore.WHITE + str(playerHealth))
    print(Fore.GREEN + "Players stamina: " + Fore.WHITE + str(playerStamina))
    print(Fore.RED + "Enemys health: " + Fore.WHITE + str(enemyHealth))
    print(Fore.RED + "Enemys stamina: " + Fore.WHITE + str(enemyStamina))
    print("")
    print("It's " + ("the Players" if isPlayerTurn else (enemyName + "'s")) + " turn!")
    print("")
    
    if isPlayerTurn:
        pass
    else:
        doEnemyAttack()
    
def call():
    global enemyName, isPlayerTurn
    
    enemyName = enemyNames[random.randrange(len(enemyNames))]
    isPlayerTurn = random.randint(0,1) == 1

    print("Your enemy is called '" + enemyName + "'")
    os.system("PAUSE")
    print("")
    while playerHealth > 0.0 and enemyHealth > 0.0:
        showUI()
        isPlayerTurn = not isPlayerTurn
        