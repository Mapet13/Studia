"""
Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych potęg cyfr liczby jest równa tej liczbie, 
np. 153 = 1^3 + 5^3 + 3^3
"""

n = int(input("n: "))

i = 10**(n-1)
while i < 10**n:
    a = i
    sum = 0
    while a > 0:
        sum += (a % 10)**n
        a //= 10
    if sum == i:
        print(i)
    i += 1
    