"""
zestaw 1, zad 5
"""
# musimy zrzutowac na int bo "input() -> str"
x = int(input("wprowadz liczbe: "))

s = 0

a = 1
b = 1
while s < x:
    s = s + a
    c = a + b
    a = b
    b = c

a = 1
b = 1
while s > x:
    s = s - a
    c = a + b
    a = b
    b = c

print(s == x)


