'''
Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.
'''

n = int(input())

tab = [True] * n

i = 2
while i*i <= n:
    if tab[i]:
        print(i)
        j = 2 * i
        while j < n:
            tab[j] = False
            j += i
    i += 1
