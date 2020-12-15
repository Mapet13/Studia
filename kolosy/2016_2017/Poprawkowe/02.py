'''
Dana jest tablica booli int t[N][N] reprezentująca szachownicę. Pole szachownicy ma
wartość true, jeżeli stoi na nim figura, a false, jeśli jest ono puste. Proszę napisać
funkcję która sprawdza czy istnieje droga skoczka przemieszczającego się z wiersza
0 do wiersza N-1. Skoczek może poruszać się tylko po polach pustych. Skoczek w
każdym ruchu powinien przybliżać się do N-1 wiersza. Funkcja ma zwrócić
najmniejszą możliwą liczbę ruchów. Skoczek może zacząć poruszać się z dowolnego
pustego pola z wiersza 0. 
N z zakresu 4...20.
'''


def rec(T, i, j, c = 0):
    n = len(T)

    if i >= n or j < 0 or j >= n or T[i][j]:
        return n+1
    if i == n-1:
        return c
    
    move_offsets = [
        (1, -2), (2, -1), (1, 2), (2, 1)
    ]
    
    res = n+1
    for o in move_offsets:
        res = min(res, rec(T, i+o[0], j+o[1], c+1))
        
    return res    
        
def f(T):
    n = len(T)
    res  = n+1
    for j in range(n):
        res = min(res, rec(T, 0, j))
    
    if res == n+1:
        return None    
    return res

tab = [
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
]
print(f(tab))

tab = [
    [False, False, False, False, False],
    [False, False, False, False, False],
    [True, True, True, True, True],
    [False, False, False, False, False],
    [False, False, False, False, False],
]
print(f(tab))

tab = [
    [False, False, False, False, False],
    [False, False, False, False, False],
    [True, True, True, True, True],
    [False, False, False, False, False],
    [True, True, True, True, True],
]
print(f(tab))
