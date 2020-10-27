"""
Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.
"""

n = int(input("Podaj liczbę: "))
base = int(input("Na jaki system numeryczny [2 - 16] chcesz zamienic tą liczbę: "))

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

result = ""

if n == 0:
    print(0)
else:
    while n > 0:
        result = digits[n % base] + result
        n //= base
    
print(result)
 