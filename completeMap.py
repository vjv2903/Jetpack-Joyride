from random import randint
from os import system
import time
from colorama import Fore, Back, Style
#from player import Player
from mandolarian import mando
from Position import postion
class completeMap(mando, postion):
    def __init__(self):

        self.__mainMap = list()
        for i in range(50):
            temp = list()
            for j in range(1800):
                temp.append(" ")
            self.__mainMap.append(temp)
        mando.__init__(self)    
        postion.__init__(self)    
    
    def __putBoundary(self):
        for i in range(0, 1790):
            for a in range(4, 8):
                self.__mainMap[a][i] = 'Z'
            for b in range(42, 46):
                self.__mainMap[b][i] = 'Z'
        for i in range(1786,1790):
            for a in range(8,42):
                self.__mainMap[a][i] = 'Z'
            
    def __putBeam(self):
        for i in range (100, 1500, 30):
            x = randint(0,3)
            #horizontal beam
            if x == 0: 
                y = randint(8,40)
                for j in range(i, i+10):
                    self.__mainMap[y][j] = 'X'
                    self.__mainMap[y+1][j] = 'X'
            #vertical beam
            elif x == 1:
                y = randint(20, 31)
                for j in range(y, y+10):
                    self.__mainMap[j][i] = 'X'
                    self.__mainMap[j][i+1] = 'X'
            #angled 45 degree beam
            elif x == 2:
                y = randint(20,41)
                for j in range(0,10):
                    self.__mainMap[y-j][i+j] = 'X'
                    self.__mainMap[y-j-1][i+j] = 'X'
            #angled 135 degree beam 
            elif x == 3:
                y = randint(8,31)
                for j in range(0,10):
                    self.__mainMap[y+j][i+j] = 'X'
                    self.__mainMap[y+j+1][i+j] = 'X'
    
    def __putCoin(self):
        for i in range(121, 1500, 30):
            x = randint(8,39)
            for j in range(i,i+7):
                self.__mainMap[x][j] = '$'
                self.__mainMap[x+1][j] = '$'
                self.__mainMap[x+2][j] = '$'

    def __putMagnet(self):
        #magnet 1 which is horizontal
        for i in range(600, 610):
            for j in range(20,30):
                if j == 25:
                    self.__mainMap[j][i] = 'M'
                else :
                    self.__mainMap[j][i] = '.'
        #magnet 2 which is vertical
        for i in range(1200, 1210):
            for j in range(20,30):
                if i == 1205:
                    self.__mainMap[j][i] = 'M'
                else :
                    self.__mainMap[j][i] = '.'
    
    def __putEnemy(self):
        i = 9
        j = 1722
        with open("alien2.txt") as f:
            while True:
                c = f.read(1)
                if not c:
                    break
                else:
                    if c == "\n":
                        i+=1
                        j=1722
                    else:
                        self.__mainMap[i][j]=c
                        j+=1    
    
    def coinUpdate(self, x, y):
        for a in (x, x+2):
            for b in (y, y+2):
                if self.__mainMap[b][a] == '$':
                    self.__mainMap[b][a] == 'c'
                    
                    self.coinTaken()
                    #calculate score
    
    def checkDeath(self, x, y):  #check shield in main if its inactive then come hee to check death
        f = False
        for a in (x, x+2):
            for b in (y, y+2):
                if self.__mainMap[b][a] == 'M':
                    self.__mainMap[b][a] = ' '
                    f = True
                if self.__mainMap[b][a] == 'X':
                    self.__mainMap[b][a] = ' '
                    f = True
        return f

    def checkMagnet(self, x, y):
        if x in range(598, 610) and y in range(18,22):
            self.magnetDown()            # force is downward
        elif x in range(598, 610) and y in range(26, 30):
            self.magnetUP()              # force upward
        elif x in range(1198, 1202) and y in range(18, 30):
            self.magnetRight()           # force attracts toward right
        elif x in range(1206, 1210) and y in range(18, 30):
            self.magnetLeft()            # force attracts toward left     

    def printMap(self, currentPos):
        system('clear')
        self.printDetails(currentPos)
        for j in range(4,47):            
            for i in range(0, 189):
                if self.__mainMap[j][i + currentPos] == 'Z':
                    print(Fore.BLUE + self.__mainMap[j][i + currentPos],end = '')
                elif self.__mainMap[j][i + currentPos] == 'X':
                    print(Fore.RED + self.__mainMap[j][i + currentPos],end = '')
                elif self.__mainMap[j][i + currentPos] == '$':
                    print(Fore.YELLOW + self.__mainMap[j][i + currentPos],end = '')
                elif self.__mainMap[j][i + currentPos] == 'M':
                    print(Fore.GREEN +self.__mainMap[j][i + currentPos],end = '')
                elif self.__mainMap[j][i + currentPos] == '.':
                    print(Fore.MAGENTA + self.__mainMap[j][i + currentPos],end = '')
                else :
                    print(self.__mainMap[j][i + currentPos],end = '')
            print("")

    def printMap2(self,curpos):
        system('clear')
        self.printDetails(curpos)
        for j in range(4,47):
            for i in range(0,189):
                if self.__mainMap[j][i + curpos] == 'Z':
                    print(Fore.BLUE + self.__mainMap[j][i+curpos], end = '')
                elif self.__mainMap[j][i + curpos] == ' ':
                    print(self.__mainMap[j][i + curpos], end = '')
                else:
                    print(Fore.GREEN + self.__mainMap[j][i+curpos], end = '')
            print("")

    def checkMando(self, curpos):
        x = self.xcur() + curpos
        y = self.ycur()
        self.checkMagnet(x,y) 
        if self.checkShield() == False:
            if self.checkDeath(x,y) == True:
                self.madoLifeDec()  
        self.coinUpdate(x,y)

    def EraseAndPutMando(self, currentpos):
        xpr = self.xprev()
        ypr = self.yprev()
        xcr = self.xcur()
        ycr = self.ycur()
        for i in range(xpr+currentpos-1,xpr+2+currentpos):
            for j in range(ypr,ypr+3):
                self.__mainMap[j][i] = ' '
        if self.checkShield() == True:
            self.__mainMap[ycr][xcr+currentpos] = '#'
            self.__mainMap[ycr][xcr+1+currentpos] = '#'
            self.__mainMap[ycr][xcr+2+currentpos] = '#'
            self.__mainMap[ycr+1][xcr+currentpos] = '#'
            self.__mainMap[ycr+1][xcr+1+currentpos] = '@'    #    ###
            self.__mainMap[ycr+1][xcr+2+currentpos] = '#'    #    #@#
            self.__mainMap[ycr+2][xcr+currentpos] = '#'      #    ###
            self.__mainMap[ycr+2][xcr+1+currentpos] = '#'
            self.__mainMap[ycr+2][xcr+2+currentpos] = '#'
        else:
            self.__mainMap[ycr][xcr+currentpos] = '<'
            self.__mainMap[ycr][xcr+1+currentpos] = '0'          #   <0>
            self.__mainMap[ycr][xcr+2+currentpos] = '>'          #   /|\
            self.__mainMap[ycr+1][xcr+currentpos] = '/'          #   / \
            self.__mainMap[ycr+1][xcr+1+currentpos] = '|'
            self.__mainMap[ycr+1][xcr+2+currentpos] = '\\'
            self.__mainMap[ycr+2][xcr+currentpos] = '/'
            self.__mainMap[ycr+2][xcr+1+currentpos] = ' '
            self.__mainMap[ycr+2][xcr+2+currentpos] = '\\'
        
            
    def startingMap(self):
        self.__putBoundary()
        self.__putBeam()
        self.__putCoin()
        self.__putMagnet()
        self.__putEnemy()

