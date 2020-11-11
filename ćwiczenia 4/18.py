'''
Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. 
Proszę napisać funkcję, która wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. 
Maksymalna długość podciągu może wynosić 10 elementów. 
Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę maksymalnego podciągu.
'''

def get_biggest_sum(t):
    n = len(t)
    
    best = 0
    
    for i in range(n):
        current_sum_x = t[i][0]
        current_sum_y = t[0][i]
        for j in range(1, n):
            if j >= 10:
                best = max(best, current_sum_x, current_sum_y)
                current_sum_x -= t[i][j-10]
                current_sum_y -= t[j-10][i]  
            current_sum_x += t[i][j]
            current_sum_y += t[j][i]
        best = max(best, current_sum_x, current_sum_y)    

    return best

t = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
]

print(get_biggest_sum(t))