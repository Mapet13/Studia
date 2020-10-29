'''
Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.
'''
from math import sqrt

n = int(input("n = "))

t = [True] * n
t[0] = t[1] = False

for i in range(2, int(sqrt(n))):
    if t[i]:
        for j in range(2 * i, n, i):
            t[j] = False

for i in range(1, n):
    if t[i]:
        print(i)
