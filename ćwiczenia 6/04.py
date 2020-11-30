'''
Problem skoczka szachowego. 
Proszę napisać funkcję, która wypełnia pola szachownicy o wymiarach NxN ruchem skoczka szachowego
'''

# t - tablica z samymi zerami
def insert_values(t, i = 0, j = 0, d = 1):
    n = len(t)
    
    if d == (n * n) + 1:
        return True
    
    if t[i][j] != 0:
        return False
    
    res = False
    t[i][j] = d
    
    if i > 0: 
        if j > 1:
            res |= insert_values(t, i - 1, j - 2, d + 1)
        if not res and j < (n-2): 
            res |= insert_values(t, i - 1, j + 2, d + 1)
    if not res and i > 1: 
        if j > 0:
            res |= insert_values(t, i - 2, j - 1, d + 1)
        if not res and j < (n-1): 
            res |= insert_values(t, i - 2, j + 1, d + 1)
    if not res and i < (n-1): 
        if j > 1:
            res |= insert_values(t, i + 1, j - 2, d + 1)
        if not res and j < (n-2): 
            res |= insert_values(t, i + 1, j + 2, d + 1)
    if not res and i < (n-2):
        if j > 0:
            res |= insert_values(t, i + 2, j - 1, d + 1)
        if not res and j < (n-1): 
            res |= insert_values(t, i + 2, j + 1, d + 1)
            
    if not res:
        t[i][j] = 0
        
    return res


n = int(input("N: "))
t = [[0 for _ in range(n)] for _ in range(n)]

insert_values(t)

for i in range(n):
    print(t[i])


