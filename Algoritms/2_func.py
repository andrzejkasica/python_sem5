import math as m
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))
delta = b**2 - (4*a*c)

if delta < 0:
    print("Delta mniejsza niż 0!")
elif delta == 0:
    print("Jedno rozwiązanie x0 = ", (-b/(2*a)))
else:
    x1 = (-b - (m.sqrt(delta)))/(2*a)
    x2 = (-b + (m.sqrt(delta)))/(2*a)
    print("Dwa rozwiazania x1: ", x1, "x2: " ,x2)

