'''
Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000
i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.
'''

from random import randint

n = int(input("n: "))

t = [randint(1, 1000) for _ in range(n)]

#only as debug code
print(t)

still_searching = True
for i in range(n):
    is_fully_odd = True
    while t[i] > 0:
        if t[i] % 2 == 0:
            is_fully_odd = False
            break
        t[i] //= 10
    if is_fully_odd:
        still_searching = False
        break
    
print(not still_searching)

