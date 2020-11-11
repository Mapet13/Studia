'''
Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, 
tak aby suma liczb na „szachowanych” przez wieże polach była największa. 
Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie wież. 
Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
'''

def get_biggest_tower_product(t):
    n = len(t)

    value_tab = [[1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for d in range(n):
                if i != d:
                    value_tab[d][j] *= t[i][j]
                if j != d:
                    value_tab[i][d] *= t[i][j]
                    
    x1 = x2 = y1 = y2 = best = 0
    for i in range(n):
        for j in range(n):
            if value_tab[i][j] >= best:
                x2 = x1
                y2 = y1
                best = value_tab[i][j]
                x1 = j
                y1 = i
                
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