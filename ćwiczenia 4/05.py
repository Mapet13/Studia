'''
Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. 
Proszę napisać funkcję, która zwraca wiersz i kolumnę dowolnego elementu, dla którego 
iloraz sumy elementów w kolumnie w którym leży element 
do sumy elementów wiersza w którym leży element jest największa.

'''
from random import randint
    

def get_special_element(t, n):
    sum_x = [0] * n
    sum_y = [0] * n

    max_num = t[0][0]
    min_num = t[0][0]
    for i in range(n):
        for j in range(n):
            sum_x[i] += t[i][j]
            sum_y[j] += t[i][j]
            if t[i][j] > max_num:
                max_num = t[i][j]
            elif t[i][j] < min_num:
                min_num = t[i][j]
            
    best = min_num*n / max_num*n
    x = -1
    y = -1
    for i in range(0, n):
        if sum_x[i] != 0:
            for j in range(0, n):
                curernt = sum_y[j] / sum_x[i]
                if curernt > best:
                    best = curernt
                    x = i
                    y = j
                    
    return (x, y)
    
    
        
n = 5
tab = [[randint(-100, 100) for _ in range(n)] for _ in range(n)]

for i in range(n):
        print(tab[i])

(x, y) = get_special_element(tab, n)
if x >= 0:
    print((x, y))
else:
    print("Wszystkie wiersze sumują się do zera")
