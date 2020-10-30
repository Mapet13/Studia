'''
Dana jest N-elementowa tablica t zawierająca liczby naturalne. 
W tablicy możemy przeskoczyć z pola o indeksie k o n pól w prawo 
    jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. 
Napisać funkcję sprawdzającą czy jest możliwe przejście
z pierwszego pola tablicy na ostatnie pole.
'''

from random import randint

n = int(input("n: "))

t = [randint(1, 10000) for _ in range(n)]

#only as debug code
print(t)

def try_go_to_last(k):
    if k == n - 1:
        return True
    
    a = n - 1 - k
    while a > k:
        if t[k] % a == 0 and try_go_to_last(a):
            return True
        a -= 1
    
    return False

print(try_go_to_last(0))