class Elasticidad:
    def __init__ (self,q1,q2,p1,p2):
        self.__q1 = q1 
        self.__q2 = q2
        self.__p1 = p1
        self.__p2 = p2

    

def formula(self):
    LeftUp = self.__q2 - self.__q1 
    LeftDown = (self.__q1 + self.__q2) / 2
    RightUp = self.__p2 - self.__p2
    RightDown = (self.__p1 + self.__p2) / 2
    
    LeftWhole = LeftUp / LeftDown
    RightWhole = RightUp / RightDown
    Ed = LeftWhole / RightWhole

    return Ed
