'''
Dana jest tablica T[N] zawierająca liczby naturalne. 
Proszę napisać funkcję, która odpowiada na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy 
można utworzyć dwa podzbiory o jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. 
Do funkcji należy przekazać wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.
'''

def f(T, k, i = 0, s1 = 0, s2 = 0):
    if k == 0:
        return s1 == s2
    if i == len(T):
        return False
    
    return (
            f(T, k, i + 1, s1, s2) or 
            f(T, k - 1, i + 1, s1 + T[i], s2) or 
            f(T, k - 1, i + 1, s1, s2 + T[i]))
    
t = [100, 50, 50]
print(f(t, 3))

t = [100, 50, 50, 11]
print(f(t, 3))

t = [100, 50, 25, 11]
print(f(t, 2))