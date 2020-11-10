'''
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. 
Proszę napisać funkcję, która w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1,
którego iloczyn 4 pól narożnych wynosi k. 
Do funkcji należy przekazać tablicę i wartość k. 
Funkcja powinna zwrócić informacje czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.
'''


def try_to_get_squear_pos(t, k):
    n = len(t)
    
    if n < 3:
        return (False, 0, 0)
    
    for i in range(0, n-2):
        for j in range(0, n-2):
            for offset_size in range(2, n - max(i, j), 2):
                if (t[i][j] * t[i + offset_size][j] * t[i][j + offset_size] * t[i + offset_size][j + offset_size] == k):
                    return (True, i + (offset_size // 2), j + (offset_size // 2))
                
    return (False, 0, 0)

tab = [
    [8, 3, 1, 8, 5],
    [3, 1, 4, 5, 4],
    [1, 2, 2, 3, 1],
    [9, 1, 4, 1, 6],
    [8, 3, 2, 9, 2],
]
print(try_to_get_squear_pos(tab, 5))   #true, (2, 2)
print(try_to_get_squear_pos(tab, 16))  #True, (1, 1) 
print(try_to_get_squear_pos(tab, 8))   #True, (3, 3)
print(try_to_get_squear_pos(tab, 640)) #True, (2, 2)
print(try_to_get_squear_pos(tab, 999)) #False

