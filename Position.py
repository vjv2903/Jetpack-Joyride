class postion(object):
    def __init__(self):
        self.__xp = 0
        self.__yp = 0
        self.__xc = 30
        self.__yc = 39
        self.__changeinX = 0
        self.__changeinY = 0
    
    def setter(self,x,y):
        self.__xp = 0
        self.__yp = 0
        self.__xc = x
        self.__yc = y

    def getterX(self):
        return self.__xc
    
    def getterY(self):
        return self.__yc

    def BossCheck(self):
        if self.__xc >= 120:
            self.__xc = 120

    def moveLeft(self):
        self.__changeinX -= 2
    def moveRight(self):
        self.__changeinX += 2
    def magnetLeft(self):
        self.__changeinX -= 1
    def magnetRight(self):
        self.__changeinX += 1
    def magnetUP(self):
        self.__changeinY -= 1
    def magnetDown(self):
        self.__changeinY += 1
    def moveUP(self):
        self.__changeinY -= 3
    def gravity(self):
        self.__changeinY += 1
    def update(self):
        self.__xp = self.__xc
        self.__yp = self.__yc
        self.__xc += self.__changeinX
        self.__yc += self.__changeinY
        if self.__yc <= 8:
            self.__yc = 8
        if self.__yc >= 39:
            self.__yc = 39
        if self.__xc <= 0:
            self.__xc = 0
        if self.__xc >= 186:
            self.__xc = 186  
        self.__changeinX = 0
        self.__changeinY = 0

    def xprev(self):
        return int(self.__xp)
    
    def yprev(self):
        return int(self.__yp)
    
    def xcur(self):
        return int(self.__xc)
    
    def ycur(self):
        return int(self.__yc)