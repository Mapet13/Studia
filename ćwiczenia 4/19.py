'''
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. 
Proszę napisać funkcję, która zwraca liczbę par elementów, o określonym iloczynie,
takich że elementy są odległe o jeden ruch skoczka szachowego.
'''


def get_knight_product(t, k):
    n = len(t)
    
    count = 0
    
    for i in range(n-1):
        for j in range(n): # nie musze sprawdzać ostatniego rzeędu
            
            # sprawdzam po koleji dla poszczególnych skoków
            for dx in range(1, 3): # (1 or 2)
                
                for dx_sign in range(-1, 2, 2): # (-1 or 1)
                    current_x = j + (dx * dx_sign)

                    if current_x >= 0 and current_x < n:
                            dy = 1 + (dx % 2) # if dx == 2 -> dy == 1 ||| if dx == 1 -> dy == 2
                            current_y = i + dy
                            if current_y < n:
                                if k == t[i][j] * t[current_y][current_x]:
                                    #print((i, j), [t[i][j]], (current_y, current_x), [t[current_y][current_x]])
                                    count += 1
                                    
    return count
    

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
print(get_knight_product(t, 90))