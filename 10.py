"""
Napisać program wyszukujący liczby doskonałe mniejsze od miliona.

liczby doskonałe to takie:
    ze suma równają się swojej sumie dzielnikow
"""
from math import sqrt

for i in range(2, int(10e6)):            
    sum = 0
    for divisor in range(1, int(sqrt(i)) + 1):                  # iteruje od 1 do sqrt(i) + 1
        if i % divisor == 0:                                    # spr podzielnosc
            sum += divisor                                      # dodaje dzielnik
            if i // divisor != divisor and i // divisor != i:     # ==> czyli jesli nie dziele przez 1 lub nie dziele przez sqrt(x)
                sum += i // divisor                              #   to wtedy suma dodatkowo jest rowna temu (X/N)
    if (sum == i):
        print(i)
        
"""
    jest to robione bo wiadomo ze jesli X dzieli sie liczba przez N to bedzie sie tez dzielic przez X/N
    a wiadomo ze nie przerobimy 2 razy X/N bo liczymy do pierwiastka
"""