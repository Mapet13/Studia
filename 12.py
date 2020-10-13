"""
Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.

skożystam z własności że NWD(a, b, c) = NWD(NWD(a, b), c)
"""

a = int(input("1 liczba: "))
b = int(input("2 liczba: "))
c = int(input("3 liczba: "))

# typowy algorytm Euklidesa ale przy uzyciu modulo a nie rekurencji
"""
np dla 138, 27:
    138 % 27 = 3   <- reszta z dzielenia 138/27
    27  % 3  = 0
        y = 0 wiec koncze algorytm i zwracam x(czyli 3)
"""
def NWD(x, y):
    z = 0                       # zmienna pomocnicza
    while (y != 0):             # dopłuki y nie jest dzielnikiem x
        z = x % y               #   przypisanie reszty z dzielenia do zmiennej Z
        x = y                   #   do liczby nr 1 zostaje wpisana wartosc liczby 2
        y = z                   #   do liczby nr 2 zostaje wpisana warosc reszty z dzielenia
    return x                    # zwraca aktualna warosc liczby 1

print(NWD(NWD(a, b), c))