'''
Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą kΩ. 
Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R 
(równej całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory.

szeregowo:  R1 + R2 + ...
równolegle: 1/R1 + 1/R2 + ... 
'''

def can_receive_resultant_resistance(T, s, i = 0, d = 0):
    if i >= len(T):
        return False
    
    if d == 3: 
        return s == 0
    
    return (can_receive_resultant_resistance(T, s - T[i], i + 1, d + 1) or 
            can_receive_resultant_resistance(T, s - (1/T[i]), i + 1, d + 1) or 
            can_receive_resultant_resistance(T, s, i + 1, d))
    
T = [4, 4, 4, 4, 5, 6, 7, 8, 9]
print(can_receive_resultant_resistance(T, 19))

T = [4, 4, 2, 2, 5, 6, 7, 1, 9]
print(can_receive_resultant_resistance(T, 2))

T = [4, 4, 2, 2, 5, 6, 7, 6, 9]
print(can_receive_resultant_resistance(T, 5))

T = [4, 4, 4, 4, 5, 6, 7, 8, 9]
print(can_receive_resultant_resistance(T, 4))

T = [4, 4, 4, 4, 5, 6, 7, 8, 9]
print(can_receive_resultant_resistance(T, 23))
