"""
Napisać program wyszukujący liczby doskonałe mniejsze od miliona.
"""

for i in range(2, int(10e6)):            
    sum = 0
    for divisor in range(i-1, 0, -1):      # iteruje od i-1 w dół sprawdzajc kolejne liczby czy nie są dzielnikami i
        if i % divisor == 0:        
            sum += divisor        
    if (sum == i):
        print(i)