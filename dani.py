class Elasticidad():
    def __init__(self,q1,q2,p1,p2):
        self.__q1 = q1 
        self.__q2 = q2
        self.__p1 = p1
        self.__p2 = p2
    
    def formula(self):
        LeftUp = self.__q2 - self.__q1 
        LeftDown = float(self.__q1 + self.__q2) / 2
        RightUp = self.__p2 - self.__p1
        RightDown = float(self.__p1 + self.__p2) / 2
    
        LeftWhole = LeftUp / LeftDown
        RightWhole = RightUp / RightDown
        Ed = float(LeftWhole) / float(RightWhole)
        print("\n*****************************\n")
        print(f"La elasticidad de la demanda {Ed}")
        print("\n*****************************\n")
        if Ed > 1:
            print("La demanda es elástica")
        elif Ed < 1:
            print("La demanda es inelástica")
        elif Ed == 1:
            print("La demanda es elasticad unitaria")
        else:
            print("Los valores no son correctos")
        print("\n*****************************\n")

Q1 = float(input("Dame el q1"))
Q2 = float(input("Dame el q2"))
P1 = float(input("Dame el p1"))
P2 = float(input("Dame el p2"))

Formula = Elasticidad(Q1,Q2,P1,P2)
Formula.formula()