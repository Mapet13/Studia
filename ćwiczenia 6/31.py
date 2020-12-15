'''
Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną 
i zwraca sumę iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby.
Można założyć, że liczba podzielników pierwszych nie przekracza 20, 
zatem w pierwszym etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej. 
Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71
'''

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

def get_sum_of_all_products(T, N, p = 0, i = 0):
    if i == N:
        return p
    r = p * T[i]
    if p == 0:
        r = T[i]
    return get_sum_of_all_products(T, N, p, i+1) + get_sum_of_all_products(T, N, r, i+1)

def f(x):
    T = [0] * 20
    i = 0
    
    p = 2
    while x > 1:
        if not is_prime(p) or x % p != 0:
            p += 1
            if T[i] != 0:
                i += 1
        else:
            x //= p  
            T[i] = p
    
    if T[i] != 0:
        i += 1     
         
    return get_sum_of_all_products(T, i)

print(f(60))