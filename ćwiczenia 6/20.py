'''
Zadanie jak powyżej. 
Funkcja powinna dostarczyć drogę króla w postaci tablicy zawierającej kierunki (liczby od 0 do 7) poszczególnych ruchów króla do wybranego celu.

[0][1][2]
[7][X][3]
[6][5][4]
'''
T = [
    [32,  9,  32, 32, 9,  9,  9,  9],
    [9,   32, 9,  32, 9,  9,  9,  9],
    [9,   9,  32, 32, 9,  9,  9, 9],
    [9,   9,  9,  9,  32, 32, 9,  9],
    [9,   9,  9,  9,  9,  9,  32, 9],
    [9,   9,  9,  9,  9,  9,  9,  32],
    [9,   9,  9,  9,  9,  9,  9,  32],
    [32,  32, 32, 32, 9, 32, 32, 32],
]

def assert_first_digit(x, d):
    while x != x % 10:
        x //= 10
    return x > d

def try_to_move_king(k, w, m = []):    
    if w >= 8 or w < 0 or k < 0 or k >= 8:
        return [False, []]
          
    if w == 7 and k == 7:
        return [True, m]
    
    last_digit = T[k][w] % 10 
    
    r = [False, []]
    if k < 7 and w < 7 and assert_first_digit(T[k+1][w+1], last_digit):
        r = try_to_move_king(k + 1, w + 1, m + [4])
    if not r[0] and k < 7 and assert_first_digit(T[k+1][w], last_digit):
        r = try_to_move_king(k + 1, w, m + [5])
    if not r[0] and w < 7 and assert_first_digit(T[k][w+1], last_digit):
        r = try_to_move_king(k, w + 1, m + [3])
   
    return r
    
def try_to_move_king_starting_in_corner():
    r = try_to_move_king(0, 0)
    if not r[0]:
        r = try_to_move_king(7, 0)
    if not r[0]:
        r = try_to_move_king(0, 7)
    return r

    
print(try_to_move_king_starting_in_corner())