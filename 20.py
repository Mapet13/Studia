"""
Dane są ciągi: 
An+1 = sqrt(An ∗ Bn) 
oraz Bn+1 = (An + Bn)/2.0. 
Ciągi te są zbieżne do wspólnej granicy nazywanej średnią arytmetyczno-geometryczną. 
Napisać program wyznaczający średnią arytmetyczno-geometryczną dwóch liczb.
"""

# program napisany analogicznie jak zad nr 5 i kazdy inny z ciagami

from math import sqrt


e = 1e-6

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

while abs(a-b) > e:
    next_a = sqrt(a * b)
    b = (a + b) / 2.0
    a = next_a
    
print(f"średnia arytmetyczno-geometryczna tych liczb to {a}")