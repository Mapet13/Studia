'''
Tablica T[8][8] zawiera liczby naturalne. 
Proszę napisać funkcję, która sprawdza czy można wybrać z tablicy niepusty podzbiór o zadanej sumie. 
Warunkiem dodatkowym jest aby żadne dwa wybrane elementy nie leżały w tej samej kolumnie ani wierszu. 
Do funkcji należy przekazać wyłącznie tablicę oraz wartość sumy, funkcja powinna zwrócić wartość typu bool.
'''

def find_sum(T, s, i = 0, j = 0, ):
    if s == 0:
        return True
    
    N = len(T)
 
    if s < 0 or N == 0 or i >= N or j >= N:
        return False
    
    t = T[:i]+T[i+1:]
    for x in range(N-1):
        t[x] = t[x][:j] + t[x][j+1:]
    
    return find_sum(t, s - T[i][j], i) or find_sum(T, s, i+1) or find_sum(T, s, i, j+1)

T = [
    [2, 9, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 9, 2, 2, 2, 2],
    [2, 2, 2, 2, 9, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 9, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 9],
]
        
print(find_sum(T, 45))