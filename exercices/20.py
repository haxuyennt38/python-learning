##Equation du secon degre : ax^2+bx+c=0
import math

a = int(input())
b = int(input())
c = int(input())

#Calcul the delta
d = b * b - 4 * a * c

if d > 0 :
    x1 = float((-b + math.sqrt(d))/2 * a)
    x2 = float((-b - math.sqrt(d))/2 * a)
    print("have two solutions :",x1,x2)
elif d == 0 :
    x = float(-b /( 2 * a ))
    print("have only one solution :", x)
else :
    print("have no real solution")

