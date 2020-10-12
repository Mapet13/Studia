"""
Napisać program sprawdzający czy zadana liczba jest pierwsza.

skoro mamy nie uzywac list to standardowy algorytm a nie sito erastotenesa
"""

target = int(input())

is_prime = True

if target > 1:
    i = 2
    while (i*i <= target):
        if target % i == 0:
            is_prime = False
            break
        i += 10

if is_prime:
    print(f"Tak, {target} jest liczba pierwszą")
else:
    print(f"Nie {target} nie jest liczba pierwszą")