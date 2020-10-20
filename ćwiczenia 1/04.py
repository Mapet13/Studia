# Proszę napisać program obliczający pierwiastek całkowitoliczbowy z liczby naturalnej korzystając z zależności 1 + 3 + 5 + ... = n^2


"""
1+3+5+...+k = n^2 = d
   |> jest ich n

d
9       3
10..15  3
16      4
"""

d = int(input())

s = 0
k = 1
n = 0

while s <= d:
    s += k
    k += 2
    n += 1

print(n - 1)
