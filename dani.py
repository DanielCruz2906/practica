from os import system,name
def limpiar_pantalla():
    if name=='nt':
        system('cls')
    else:
        system('clear')

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
###########################
        if Ed < 0:
            EdF = Ed * -1
        else:
            EdF = Ed
 ##########################   
        if EdF > 1:
            print(f"La Elasticidad de la demanda es de [{EdF}] esto significa que es ¡ELÁSTICA!")
        elif EdF < 1:
            print(f"La Elasticidad de la demanda es de [{EdF}] esto significa que es ¡INELÁSTICA!")
        elif EdF == 1:
            print(f"La Elasticidad de la demanda es de [{EdF}] esto significa que es ¡UNITARIA!")
        else:
            print("¡X! Los valores no son correctos ¡X!")
        

limpiar_pantalla()
Q1 = float(input("¿Cual es la primera cantidad demandada?:"))
limpiar_pantalla()
P1 = float(input("¿A que precio?:"))
limpiar_pantalla()
Q2 = float(input("¿Cual es la segunda cantidad demandada?:"))
limpiar_pantalla()
P2 = float(input("¿A que precio?:"))
limpiar_pantalla()
input('presiona enter para continuar...')
limpiar_pantalla()

Formula = Elasticidad(Q1,Q2,P1,P2)
Formula.formula()