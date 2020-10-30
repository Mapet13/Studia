'''
Proszę napisać program, który 
    - wypełnia N-elementową tablicę t pseudolosowymi liczbami nieparzystymi z zakresu [1..99], 
    - a następnie wyznacza i wypisuje różnicę pomiędzy 
        długością najdłuższego znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy,
        a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy, 
        przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych indeksach.
'''
from random import randint

def generateArray(n):
    return [randint(1, 99) for _ in range(n)]

n = int(input("n: "))
t = generateArray(n)

best = [1, 1]

d = 0
current = 1
for i in range(1, n):
    new_d = t[i] - t[i-1]
    
    if new_d != d or i == (n - 1):
        if d != 0:
            pn_index = int(d < 0)
            if best[pn_index] < current:     
                best[pn_index] = current        
                
        d = new_d   
        current = 2
    else:
        current += 1     

# as debug code
print("pos: ", best[0])
print("neg: ", best[1])

print(abs(best[0] - best[1]))