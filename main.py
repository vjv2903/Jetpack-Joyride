import os
import sys
import select
from completeMap import completeMap
import termios
import tty
from mandolarian import mando
from math import fmod, sqrt
from os import system
import time
from Position import postion
from BossFight import BossFight

def is_input():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def quitGame(): 
    sys.exit('Game Quit by Player')

obj1 = completeMap()
obj1.startingMap()
currentTime = 0
T = True
while T:
    global INPUT_W
    global INPUT_A
    global INPUT_D
    global INPUT_Shield
    global INPUT_ActiveBoost
    global INPUT_DeactiveBoost
    global INPUT_Quit
    INPUT_W = False
    INPUT_A = False
    INPUT_D = False
    INPUT_Shield = False
    INPUT_ActiveBoost = False
    INPUT_DeactiveBoost = False
    INPUT_Quit = False
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    if currentTime < 1601 :
        if obj1.checkBoost() == True:
            time.sleep(0.05)
        else:
            time.sleep(0.2)
    else:
        T = False
    system('clear')
    
    if is_input():
        ch = sys.stdin.read(1)
        if ch == "w" or ch == "W":
            INPUT_W = True
        if ch == "a" or ch == "A":
            INPUT_A = True
        if ch == "d" or ch == "D":
            INPUT_D = True
        if ch == "S" or ch == "s":
            INPUT_Shield = True
        if ch == "B" or ch == "b":
            INPUT_ActiveBoost = True
        if ch == "N" or ch == "n":
            INPUT_DeactiveBoost = True
        if ch == "Q" or ch == "q":
            INPUT_Quit = True

        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)        

    if INPUT_A == True:
        obj1.moveLeft()         #calling function to move madalorian left
    if INPUT_W == True:
        obj1.moveUP()         #calling function to move madolarian up
    if INPUT_D == True:
        obj1.moveRight()        #calling function to move madalorian right
    if INPUT_Shield == True:
        obj1.avtivateShield()     #calling function to activate shield
    if INPUT_ActiveBoost == True:
        obj1.activateBoost()      #calling function to activate boost
    if INPUT_DeactiveBoost == True:
        obj1.deactivateBoost()    #calling function to Deactivate boost
    if INPUT_Quit == True:
        quitGame()                    #calling function to quit game
    obj1.gravity()              #putting gravity
    obj1.update()               #update position
    obj1.checkMando(currentTime)
    obj1.EraseAndPutMando(currentTime)
    
    if currentTime < 1500:
        obj1.printMap(currentTime)
    else:
        obj1.printMap2(currentTime)
    obj1.timeInc()
    currentTime += 1
#boss fight begins
T = True
obj2 = BossFight()
obj2.setter(obj1.getterX(), obj1.getterY())
obj2.BossCheck()
obj2.startingEndBattle()
obj2.setterLife(obj1.getterLife())
obj2.setterTotalScore(obj1.getterScore())
while T:
    global INPUT_w
    global INPUT_a
    global INPUT_d
    global INPUT_Fire
    INPUT_Fire = False
    INPUT_w = False
    INPUT_a = False
    INPUT_d = False
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    time.sleep(0.1)
    if is_input():
        ch = sys.stdin.read(1)
        if ch == "w" or ch == "W":
            INPUT_w = True
        if ch == "a" or ch == "A":
            INPUT_a = True
        if ch == "d" or ch == "D":
            INPUT_d = True
        if ch == " ":
            INPUT_Fire = True
        if ch =="q" or ch == "Q":
            T = False
        if ch == "f" or ch == "F":
            INPUT_Fire = True            
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)        

    if INPUT_a == True:
        obj2.moveLeft()         #calling function to move madalorian left
    if INPUT_w == True:
        obj2.moveUP()           #calling function to move madolarian up
    if INPUT_d == True:
        obj2.moveRight()        #calling function to move madalorian right
    if INPUT_Fire == True:
        obj2.shootBullet()      #calling function to fire a bullet     
    obj2.shootsnowball()
    obj2.gravity()
    obj2.update()
    obj2.BossCheck()
    system('clear')
    obj2.printMap()

#code ends here 