'''
Dana jest duża tablica t. 
Proszę napisać funkcję, która zwraca informację czy w tablicy zachodzi następujący warunek: 
„wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są liczbami złożonymi, 
a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”
'''
from random import randint

MAX_VALUE = 100000

n = int(input("n: "))
t = [randint(1, MAX_VALUE) for _ in range(n)]

a = 1
b = 1

prime_tab = [True] * MAX_VALUE
prime_tab[0] = prime_tab[1] = False 
current_max = 1

found_prime = False
allFibonacciIndexesAreCompositeNumbers = True

for i in range(n):
    if current_max * current_max < t[i]: # "rozszerzam zakres" sita erastotenesa
        while current_max * current_max <= t[i]:
            if prime_tab[current_max]:
                for j in range(current_max * current_max, MAX_VALUE, current_max):
                    prime_tab[j] = False
            current_max += 1
            
    if b == i:
        c = a + b
        a = b
        b = c
        if prime_tab[t[i]]:
            allFibonacciIndexesAreCompositeNumbers = False
            break
    elif not found_prime: 
        found_prime = prime_tab[t[i]]
        
print(found_prime and allFibonacciIndexesAreCompositeNumbers)
