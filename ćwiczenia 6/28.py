'''
Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję, która zwraca informację, 
czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym podzbiorze, 
łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była jednakowa. 
Na przykład: 
[2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
[5, 7, 15] → false, podział nie istnieje.
'''

def count_1(x):
    c = 0
    while x > 0:
        c += x % 2
        x //= 2
    return c
        

def can_split_it(T, i = 0, a = 0, b = 0, c = 0):
    if i == len(T):
        return a == b == c
    
    return (
        can_split_it(T, i+1, a + count_1(T[i]), b, c) or 
        can_split_it(T, i+1, a, b + count_1(T[i]), c) or 
        can_split_it(T, i+1, a, b, c + count_1(T[i]))
    )
    
T = [2, 3, 5, 7, 15]
print(can_split_it(T))

T = [5, 7, 15]
print(can_split_it(T))