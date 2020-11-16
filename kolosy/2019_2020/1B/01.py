'''
Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
iloczynem dokładnie dwóch liczb pierwszych. Oba kawałki powinny być jednakowej długości.
'''

from random import randint

def is_two_primes_product(num):
    if num < 4:
        return False
    
    pt = [True for _ in range(num + 1)]
    pt[0] = pt[1] = False
    
    i = 2
    while i * i <= num:
        if pt[i]:
            for j in range(i * i, num + 1, i):
                pt[j] = False
        i += 1
    

    i = 2
    while i * i <= num:
        if num % i == 0 and pt[i] and pt[num // i]:
            print(num, " = ", i, " * ", num // i)
            return True
        i += 1
    
    return False

def can_get_correct_slices(t1, t2):
    n = len(t1)
    
    for i in range(n):
        element_sum_1 = 0
        for j in range(i, n):
            slice_len = j - i + 1
            element_sum_1 += t1[j]
            for x in range(0, n - slice_len + 1):
                current_sum = element_sum_1
                c = 0
                for y in range(x, x + slice_len):
                    c += 1
                    current_sum += t2[y]
                if is_two_primes_product(current_sum):
                    return True
    return False


tab1 = [1, 0, 1]
tab2 = [1, 0, 1]
print(can_get_correct_slices(tab1, tab2))

tab1 = [randint(20, 100) for _  in range(30)]
tab2 = [randint(20, 100) for _  in range(30)]
print(can_get_correct_slices(tab1, tab2))