"""
Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.

korzystam z wlasności że NWW(a, b, c) = NWW(NWW(a, b), c)
oraz ze NWW(a, b) = ab/NWD(a, b)
"""

a = int(input("1 liczba: "))
b = int(input("2 liczba: "))
c = int(input("3 liczba: "))

def NWD(x, y):
    z = 0
    while(y != 0):
        z = x % y
        x = y
        y = z
    return x

def NWW(m, n):
    return m * n // NWD(m, n)

print(NWW(NWW(a, b), c))
