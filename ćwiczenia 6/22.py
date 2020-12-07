'''
To samo co zadanie 25 xD

Dana jest tablica T[N] zawierająca liczby naturalne. 
Po tablicy możemy przemieszczać się według następującej zasady: 
z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k 
jeżeli k jest czynnikiem pierwszym liczby t[i] mniejszym od t[i]. 
Proszę napisać funkcję, która zwraca informację czy jest możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. 
Funkcja powinna zwrócić liczbę wykonanych skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.
'''
from math import sqrt, ceil

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5 
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    

def count_jumps(T, i = 0):
    N = len(T)
    
    if i == N-1:
        return 0
    
    if i > N - 1:
        return -1
   
    k = min(ceil(sqrt(T[i])), N - i - 1) 
    while k >= 2:
        if T[i] % k == 0 and is_prime(k):
            jc = count_jumps(T, i + k)
            if jc >= 0:
                return jc + 1
        k -= 1 
    
    return -1


T = [9, 2, 4, 25, 5, 6, 7, 2]
print(count_jumps(T))

T = [9, 2, 4, 25, 5, 6, 7, 2, 4] 
print(count_jumps(T))

T = [2, 2, 6, 25, 5, 6, 7, 2]
print(count_jumps(T))
    
    