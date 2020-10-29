from math import sqrt, ceil

n = int(input("n = "))

t = [True] * n
t[0] = t[1] = False

for i in range(2, ceil(sqrt(n))):
    if t[i]:
        for j in range(i * i, n, i):
            t[j] = False

for i in range(1, n):
    if t[i]:
        print(i)  
     