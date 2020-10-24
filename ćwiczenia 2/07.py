"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, 
czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem: 
An = n ∗ n + n + 1.
"""

a = int(input("a: "))

still_searching = True

i = 1
next = (i * i) + i + 1 # nie trzeba nawiasów ale ja lubie
while(next <=  a and still_searching):
    if a % next  == 0:
        print(next)
        still_searching = False
        break
    i += 1
    next = (i * i) + i + 1
    
print(not still_searching)