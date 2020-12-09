'''
W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. 
Na ruchy króla nałożono dwa ograniczenia: 
król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na polu na którym stoi 
jest mniejsza od pierwszej cyfry liczby pola docelowego, 
oraz w drodze do obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. 
Dana jest globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. 
Lewy górny narożnik ma współrzędne w=0 i k=0. 
Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego narożnika.
'''
T = [
    [32, 9,  9,  9,  9,  9,  9,  9],
    [9,  32, 9,  9,  9,  9,  9,  9],
    [9,  9,  32, 32, 9,  9,  9,  9],
    [9,  9,  9,  9,  32, 32, 9,  9],
    [9,  9,  9,  9,  9,  9,  32, 9],
    [9,  9,  9,  9,  9,  9,  9,  32],
    [9,  9,  9,  9,  9,  9,  9,  32],
    [9,  9,  9,  9,  9,  9,  9,  32],
]

def assert_first_digit(x, d):
    while x != x % 10:
        x //= 10
    return x > d

def try_to_move_king(w, k):
    if w >= 8 or w < 0 or k < 0 or k >= 8:
        return False
          
    if w == 7 and k == 7:
        return True
    
    last_digit = T[w][k] % 10 
    
    return ((w < 7 and k < 7 and assert_first_digit(T[w+1][k+1], last_digit) and try_to_move_king(w+1, k+1))  
            or (w < 7 and assert_first_digit(T[w+1][k], last_digit) and try_to_move_king(w+1, k)) 
            or (k < 7 and assert_first_digit(T[w][k+1], last_digit) and try_to_move_king(w, k+1)))
    
    
print(try_to_move_king(0, 0))
