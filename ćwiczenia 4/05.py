'''
Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. 
Proszę napisać funkcję, która zwraca wiersz i kolumnę dowolnego elementu, dla którego 
iloraz sumy elementów w kolumnie w którym leży element 
do sumy elementów wiersza w którym leży element jest największa.


so ugly :<
'''
from random import randint
    

def get_special_element(t, n):
    sum_x = [0] * n
    sum_y = [0] * n

    for i in range(n):
        for j in range(n):
            sum_x[i] += t[i][j]
            sum_y[j] += t[i][j]
            
    biggest_positive_y = -1
    biggest_negative_y = -1
    smallest_positive_x = -1
    smallest_negative_x = -1
    for i in range(1, n):
        if sum_x[i] > 0:
            if smallest_positive_x < 0:
                smallest_positive_x = i
            elif sum_x[i] < sum_x[smallest_positive_x]:
                smallest_positive_x = i
        elif sum_x[i] < 0:
            if smallest_negative_x < 0:
                smallest_negative_x = i
            elif sum_x[i] > sum_x[smallest_negative_x]:
                smallest_negative_x = i
        if sum_y[i] >= 0:
            if biggest_positive_y < 0:
                biggest_positive_y = i
            elif sum_x[i] > sum_x[biggest_positive_y]:
                biggest_positive_y = i
        elif sum_y[i] < 0:
            if biggest_positive_y < 0:
                biggest_positive_y = i
            elif sum_x[i] < sum_x[biggest_positive_y]:
                biggest_positive_y = i
            
    x = -1
    y = -1
    best = 0
    if smallest_positive_x >= 0:
        if biggest_positive_y >= 0:
            best = biggest_positive_y / smallest_positive_x
            x = smallest_positive_x
            y = biggest_positive_y
        elif biggest_negative_y >= 0:
            best = biggest_negative_y / smallest_positive_x
            x = smallest_positive_x
            y = biggest_negative_y
    if smallest_negative_x >= 0:
        if biggest_negative_y >= 0:
            current = biggest_negative_y / smallest_negative_x
            if current > best:
                x = smallest_negative_x
                y = biggest_negative_y
        elif biggest_positive_y >= 0:
            current = biggest_positive_y / smallest_negative_x
            if current > best:
                x = smallest_negative_x
                y = biggest_positive_y
        
    return (x, y)
    
    
        
n = 5
tab = [[randint(-100, 100) for _ in range(n)] for _ in range(n)]

for i in range(n):
        print(tab[i])

(x, y) = get_special_element(tab, n)
if x > 0:
    print((x, y))
else:
    print("Wszystkie wiersze sumują się do zera")
