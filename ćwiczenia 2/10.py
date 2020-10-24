"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, 
czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem 
An = 3 ∗ An−1 + 1, 
a pierwszy wyraz jest równy 2.
"""

num = int(input("a: "))

still_searching = True

a = 2
while a <= num and still_searching:
    if num % a == 0:
        still_searching = False
        break
    a = (3 * a) + 1

print(not still_searching)
