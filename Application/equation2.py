# equation ax^2 + bx + c = 0
import math
a = int(input("Entre la valeur de a:"))
b = int(input("Entre la valeur de b:"))
c = int(input("Entre la valeur de c:"))
delta = (b**2 -  4*a*c)
if(delta < 0):
    print(" Cas non traiter")
elif(delta == 0):
    x = -b/(2*a)
    print("L'equation admet une solution double qui est:", x)
else:
    print("L'equation admet deux solutions")
    x1 = (-b - math.sqrt(delta))/ (2*a)
    x2 = (-b + math.sqrt(delta))/ (2*a)
    print("x1 = ", x1, " x2 = ",x2)