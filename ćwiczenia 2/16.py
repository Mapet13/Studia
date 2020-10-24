"""
Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących w jej rozkładzie na czynniki pierwsze.
Na przykład: 85 = 5∗17, 8+5 = 5+1+7.
Napisać program wypisujący liczby Smitha mniejsze od 1000000.
"""

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

i = 2
while i < 1000000:
    d_sum = digit_sum(i)
    sum = 0
    a = i
    p = 2
    while  a > 1 and p < i and d_sum >= sum:
        if a % p == 0:
            a //= p
            sum += digit_sum(p)
        else:
            p += 1
    if d_sum == sum:
        print(i)
    i += 1
