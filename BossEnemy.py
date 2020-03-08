import sys
class bossEnemy(object):
    def __init__(self):
        self.__health = 1000
    
    def bulletHitBoss(self):
        self.__health -= 10
        if self.__health < 0:
            strin = "HURRAY!!! \nYOU WON!! \nMANDLORIAN RELEASED!!"    
            sys.exit(strin)

    def getterBossLife(self):
        return self.__health
