"""
Napisać program sprawdzający czy zadana liczba jest pierwsza.
"""

from math import sqrt

def czy_pierwsza(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5 
    while i <= sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
print(czy_pierwsza(101))