"""
Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

liczby zaprzyjaznione a i b to takie:
    ze suma dzielnikow a jest rowna liczbie b, i analogicznie
"""
from math import sqrt

def get_divisor_sum(i):
    sum = 0
    for divisor in range(1, int(sqrt(i)) + 1): 
        if i % divisor == 0:        
            sum += divisor 
            if i // divisor != divisor and i // divisor != i:
                sum += i // divisor
    return sum

for i in range(2, int(10e6)):            
    sum_1 = get_divisor_sum(i)
    if (sum_1 < i):
        sum_2 = get_divisor_sum(sum_1)
        if (i == sum_2):
            print(sum_1, i)