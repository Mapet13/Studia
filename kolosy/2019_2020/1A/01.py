'''
Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
co najmniej drugą potęgą dowolnej liczby naturalnej. Łączna długości obu kawałków powinna wynosić 24.
'''
from random import randint

def can_get_correct_slices(t1, t2):
    n = len(t1)
    
    for i in range(n-25):
        for j in range(i+1, i + 24):
            if j >= n:
                break
            
            slice_1_len = j - i
            
            
            elements_sum = 0
            for a in range(i, j):
                elements_sum += t1[a]
            
            for x in range(0, n - (24 - slice_1_len)):
                for a in range(x, x + 24 - slice_1_len):
                    elements_sum += t2[a]
                    
            num = 2
            while (num * num <= elements_sum):
                power = num * num
                while power < elements_sum:
                    power *= num
                if elements_sum == power:
                    print(num, power)
                    return True 
                num += 1
            
    return False
                    
                             
tab1 = [randint(1, 10) for _  in range(30)]
tab2 = [randint(1, 10) for _  in range(30)]
print(can_get_correct_slices(tab1, tab2))