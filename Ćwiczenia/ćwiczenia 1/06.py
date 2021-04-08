'''
Proszę zaimplementować funkcję, 
która otrzymuje na wejściu posortowaną niemalejąco tablicę A o rozmiarze n oraz liczbę x i sprawdza, czy x występuje w A. 
Jeśli tak, to zwraca najmniejszy indeks, pod którym x występuje.
'''

def binary_search(T, x):
    n = len(T)
    
    r = n-1
    l = 0
    
    while l <= r:
        c = (r + l) // 2
        if T[c] < x:
            l = c + 1
        else:
            r = c - 1
            
    if T[l] == x:
        return l
    else:
        return None

T = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(T, 5))

T = [0, 1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8]
print(binary_search(T, 5))

T = [0, 1, 2, 3, 4, 6, 7, 8]
print(binary_search(T, 5))
