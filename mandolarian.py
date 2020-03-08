import sys
class mando(object):
    def __init__(self):
        self.__life = 10
        self.__time = 0
        self.__shield = False
        self.__shieldCharge = 0
        self.__shieldDecay = 0
        self.__boost = False
        self.__score = 0
    
    def checkShield(self):
        return self.__shield

    def getterLife(self):
        return self.__life

    def getterScore(self):
        return self.__score
        
    def activateBoost(self):
        self.__boost = True

    def deactivateBoost(self):
        self.__boost = False
    
    def checkBoost(self):
        return self.__boost

    def timeInc(self):
        self.__time += 1
        if self.__shield == False:
            self.__shieldCharge += 1
        if self.__shield == True:
            self.__shieldDecay -= 1
            if self.__shieldDecay == 0:
                self.__shield = False

    def avtivateShield(self):
        if self.__shieldCharge > 600:
            self.__shield = True
            self.__shieldCharge = 0
            self.__shieldDecay = 100

    def coinTaken(self):
        self.__score += 2

    def _lifeRemain(self):
        return self.__life
    
    def _travelScore(self):
        return self.__score

    def madoLifeDec(self):
        self.__life -= 1
        if self.__life == -1:
            sys.exit('Game Over')
# print Top bar here    
    def printDetails(self,t):
        if self.__shield == True:
            strin = "YES"
        else:
            strin = "NO"
        if self.__boost == True:
            strin2 = "YES"
        else:
            strin2 = "NO"
        print("                                             Jet Pack Joyride")
        print("                                                   by Vishal Verma")
        print("Score: " + str(self.__score) + "                                    Life: "+str(self.__life)+"                                            Shield Charge: "+ str(self.__shieldCharge)+"/600                               Game Time Left: "+str((1601-t)/10))
        print("Shield Active: "+strin + "                                          Shield Left Time: "+str(self.__shieldDecay) + "/100                   Boost Active:"+strin2)

