'''
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. 
Proszę napisać funkcję, która zwraca wiersz i kolumnę dowolnego elementu, dla którego 
iloraz sumy elementów w kolumnie w którym leży element 
do sumy elementów wiersza w którym leży element jest największa.
'''
from random import randint

def get_special_element(t, n):
    sum_x = [0] * n
    sum_y = [0] * n

    for i in range(n):
        for j in range(n):
            sum_x[i] += t[i][j]
            sum_y[j] += t[i][j]
            
    biggest_y = 0
    smallest_x = 0
    for i in range(1, n):
        if sum_x[i] < sum_x[smallest_x]:
            smallest_x = i
        if sum_y[i] > sum_y[biggest_y]:
            biggest_y = i
            
    return (smallest_x, biggest_y)



n = 5
tab = [[randint(1, 100) for _ in range(n)] for _ in range(n)]

for i in range(n):
        print(tab[i])

print(get_special_element(tab, n))
    
