'''
Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, 
tak aby suma liczb na „szachowanych” przez wieże polach była największa. 
Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie wież. 
Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
'''

def get_biggest_tower_product(t):
    n = len(t)

    value_tab_col = [0 for _ in range(n)]
    value_tab_row = [0 for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            value_tab_col[i] += t[i][j]
            value_tab_row[j] += t[i][j]
                    
    x1 = x2 = y1 = y2 = best = 0
    for a in range(n):
        for b in range(n):
            for c in range(a, n):
                for d in range(n):
                    if b != d or a != c:
                        current = value_tab_row[a] + value_tab_row[c] + value_tab_col[b] + value_tab_col[d]
                        current = current - t[a][b] - t[a][d] - t[c][b] - t[c][d]
                        if current > best:
                            best = current
                            x1 = a
                            y1 = b
                            x2 = c
                            y2 = d                    
            
    return ((x1, y1), (x2, y2))
            


t = [
    [1, 1, 1, 1],
    [1, 1, 2, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
print(get_biggest_tower_product(t))

t = [
    [1, 1, 2, 1],
    [2, 2, 2, 2],
    [1, 1, 2, 1],
    [1, 1, 2, 1]
]
print(get_biggest_tower_product(t))

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
print(get_biggest_tower_product(t))