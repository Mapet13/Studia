"""
Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.
"""

def get_divisor_sum(i):
    sum = 0
    for divisor in range(i-1, 0, -1): 
        if i % divisor == 0:        
            sum += divisor 
    return sum

for i in range(2, int(10e6)):            
    sum = get_divisor_sum(i)
    if (sum < i):
        sum_2 = get_divisor_sum(sum)
        if (i == sum_2):
            print(sum, i)