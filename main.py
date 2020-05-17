from elasticidad import Elasticidad

Q1 = float(input("Dame el q1"))
Q2 = float(input("Dame el q2"))
P1 = float(input("Dame el p1"))
P2 = float(input("Dame el p2"))


E = Elasticidad(Q1,Q2,P1,P2)

E.formula()
