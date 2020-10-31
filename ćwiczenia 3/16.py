'''
Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. 
Proszę napisać funkcję zwracającą wartość typu bool oznaczającą, 
czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie jeden element największy 
(liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej wartości).
'''
from random import randint

n = int(input("n: "))
t = [randint(1, 1000) for _ in range(n)]

min = t[0]
max = t[0]
count_min = 1
count_max = 1

for i in range(2, n):
    if t[i] == max:
        count_max += 1
    if t[i] == min:
        count_min += 1
    if t[i] > max:
        max = t[i]
        count_max = 1
    if t[i] < min:
        min = t[i]
        count_min = 1

print("max: ", count_max == 1)
print("min: ", count_min == 1)