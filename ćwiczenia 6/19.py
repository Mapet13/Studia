'''
Zadanie jak powyżej. 
Funkcja sprawdzająca czy król może dostać się z pola w,k do któregokolwiek z narożników.
'''
T = [
    [12,  9,  12, 12, 9,  9,  9,  9],
    [9,   12, 9,  12, 9,  9,  9,  9],
    [9,   9,  9,  12, 9,  9,  9,  9],
    [9,   9,  9,  9,  12, 12, 9,  9],
    [9,   9,  9,  9,  9,  9,  12, 9],
    [9,   9,  9,  9,  9,  9,  9,  12],
    [9,   9,  9,  9,  9,  9,  9,  12],
    [12,  12, 12, 12, 12, 12, 12, 12],
]

def assert_first_digit(x, d):
    while x != x % 10:
        x //= 10
    return x < d

def try_to_move_king(w, k):
    if w >= 8 or w < 0 or k < 0 or k >= 8:
        return False
          
    if w == 7 and k == 7:
        return True
    
    last_digit = T[w][k] % 10 
    
    return ((w < 7 and k < 7 and assert_first_digit(T[w+1][k+1], last_digit) and try_to_move_king(w+1, k+1))  
            or (w < 7 and assert_first_digit(T[w+1][k], last_digit) and try_to_move_king(w+1, k)) 
            or (k < 7 and assert_first_digit(T[w][k+1], last_digit) and try_to_move_king(w, k+1)))
    
def try_to_move_king_starting_in_corner():
    return try_to_move_king(0, 0) or try_to_move_king(7, 0) or try_to_move_king(0, 7)
    
print(try_to_move_king_starting_in_corner())
