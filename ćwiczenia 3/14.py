'''
Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, 
że w grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. 
Wyznaczyć wartości prawdopodobieństwa dla N z zakresu 20-40.
'''
from random import randint

def generateArray(n):
    return [randint(1, 365) for _ in range(n)]

def hasEventHappened(n):
    t = generateArray(n)
    found = False
    for i in range(0, n):
        for j in range(i+1, n):
            if t[i] == t[j]:
                found = True
                break
        if found:
            break
    return found


n = int(input("n: "))

e = 1e-5

last = -1
count = 1
event_count = int(hasEventHappened(n))
current = event_count / count

min_iter = n # dla wiekszej pewnosci ze jakies zdazenie nastąpi

while abs(last-current) > e or count < min_iter:
    count += 1
    event_count += int(hasEventHappened(n))
    last = current
    current = event_count / count
    
    
print(current)