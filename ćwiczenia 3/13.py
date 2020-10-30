'''
Proszę napisać program, który wypełnia N-elementową tablicę t trzycyfrowymi liczbami pseudolosowymi, 
a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego się w tablicy 
    dla którego w tablicy występuje również rewers tego ciągu. 
Na przykład dla tablicy: t= [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4.
'''
from random import randint


def generateArray(n):
    return [randint(100, 999) for _ in range(n)]


n = int(input("n: "))
t = generateArray(n)
#t = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
#n = len(t)

best = 0


current = 0
current_beginig = 0
current_reverse_begine = n-1
i = 0
while i < n:
    if current == 0:
        found = False
        for j in range(current_reverse_begine, -1, -1):
            if t[i] == t[j]:
                found = True
                current = 1
                current_reverse_begine = j
                break
        if not found:
            current_reverse_begine = n - 1
            current_beginig = i + 1
            current = 0
    else:
        offset = i - current_beginig
        if t[i] == t[current_reverse_begine - offset]:
            current += 1
        else:
            if current > best:
                best = current
            current = 0
            i = current_beginig - 1
            current_reverse_begine -= 1
    i += 1

if current > best:
    best = current

print("best: ", best)
