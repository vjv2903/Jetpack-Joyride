from Position import postion
import sys
from MandoLastFight import mandoLastFight
from BossEnemy import  bossEnemy
from os import system
from colorama import Fore, Back, Style
from random import randint
import time

class BossFight(postion, mandoLastFight, bossEnemy):
    def __init__(self):
        postion.__init__(self)
        mandoLastFight.__init__(self)
        self.__snowBall = list()
        self.__Bullet = list()
        bossEnemy.__init__(self)
        self.__endMap = list()
        for i in range(50):
            temp = list()
            for j in range(200):
                temp.append(" ")
            self.__endMap.append(temp)

    def shootBullet(self):
        x = self.getterX()
        y = self.getterY()
        self.__Bullet.append([x+1,y+1,0])

    def shootsnowball(self):
        x = self.getterX()
        y = self.getterY()
        self.__snowBall.append([119,y,0])

    def checkMandoGotHit(self):
        x = self.getterX()
        y = self.getterY()
        for snow in self.__snowBall:
            if snow[2] == 0:
                if snow[0] >= x and snow[0] <= x+2:
                    if snow[1] >= y and snow[1] <= y+2:
                        self.bulletHit()
                        snow[2] = 1

    def addsnowBalls(self):
        for snow in self.__snowBall:
            if snow[2] == 0:
                self.__endMap[snow[1]][snow[0]] = ' '
                snow[0] -= 2
                if snow[0] < 0:
                    snow[2] = 1
                else:
                    self.__endMap[snow[1]][snow[0]] = 'O'

    def addBullets(self):
        for bull in self.__Bullet:
            if bull[2] == 0:
                self.__endMap[bull[1]][bull[0]] = ' '
                bull[0] += 2
                if bull[0]>119:
                    self.bulletHitBoss()
                    self.fireBullet()
                    bull[2] = 1
                else:
                    self.__endMap[bull[1]][bull[0]] = '>' 

    def __putBoundary(self):
        for i in range(0,190):
            for j in range(4,8):
                self.__endMap[j][i] = 'Z'
            for k in range(42,46):
                self.__endMap[k][i] = 'Z'
        for i in range(4,46):
            for j in range(185,190):
                self.__endMap[i][j] = 'Z'

    def __storeEnemy(self):
        i = 9
        j = 120
        with open("alien2.txt") as f:
            while True:
                c = f.read(1)
                if not c:
                    break
                else:
                    if c == "\n":
                        i+=1
                        j=120
                    else:
                        self.__endMap[i][j]=c
                        j+=1    

    def GotHit(self,x,y): # checks whethe bullet hits mando or not 
        xcur = self.getterX()
        ycur = self.getterY()
        if x >= xcur and x <= xcur+2:
            if y >= ycur and y <= ycur+2:
                return True
        return False 

    def checkBullet(self,x,y): # checks given bullet hits mando and is game over 
        if self.GotHit(x,y) == True:
            if self.bulletHit() == False:
                print("Game Over")
                print("Score:    " + str(self.getterTotalScore()))
    
    def printMando(self):
        xpr = self.xprev()
        ypr = self.yprev()
        xcr = self.xcur()
        ycr = self.ycur()
        for i in range(xpr,xpr+2+1):
            for j in range(ypr,ypr+3):
                self.__endMap[j][i] = ' '
        self.__endMap[ycr][xcr] = '<'
        self.__endMap[ycr][xcr+1] = '0'          #   <0>
        self.__endMap[ycr][xcr+2] = '>'          #   /|\\
        self.__endMap[ycr+1][xcr] = '/'          #   / \
        self.__endMap[ycr+1][xcr+1] = '|'
        self.__endMap[ycr+1][xcr+2] = '\\'
        self.__endMap[ycr+2][xcr] = '/'
        self.__endMap[ycr+2][xcr+1] = ' '
        self.__endMap[ycr+2][xcr+2] = '\\'
        
    def printMap(self):
        #system('clear')
        #self.printDetails(curpos)
        print("                                                     Final Battle of JETPACK-JOYRIDE")
        print("                                                                     by Vishal Verma")
        print("Score: "+str(self.getterTotalScore()) + "                                   Lifes left: "+str(self.getterLife()))
        print("Enemy Health: "+str(self.getterBossLife()) + "/1000")
        self.addBullets()
        self.addsnowBalls()
        self.printMando()
        self.checkMandoGotHit()
        for j in range(4,47):
            for i in range(0,189):
                if self.__endMap[j][i] == 'Z':
                    print(Fore.BLUE + self.__endMap[j][i], end = '')
                elif self.__endMap[j][i] == ' ':
                    print(self.__endMap[j][i], end = '')
                else:
                    print(Fore.GREEN + self.__endMap[j][i], end = '')
            print("")

    def startingEndBattle(self):
        mandoLastFight.__init__(self)

        self.__putBoundary()
        self.__storeEnemy()