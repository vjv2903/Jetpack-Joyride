import sys
class mandoLastFight(object):
    def __init__(self):
        self.__lifeLast = 0
        self.__totalScore = 0
    
    def setterLife(self, x):
        self.__lifeLast = x
    
    def setterTotalScore(self,x):
        self.__totalScore = x

    def fireBullet(self):
        self.__totalScore += 10
    
    def getterLife(self):
        return self.__lifeLast
    def getterTotalScore(self):
        return self.__totalScore

    def bulletHit(self):
        self.__lifeLast -= 1
        if self.__lifeLast < 0:
            strin = "Game Over\nScore: " + str(self.__totalScore) 
            sys.exit(strin)