'''
Dana jest tablica zawierająca liczby wymierne.
Proszę napisać funkcję, która policzy występujące w tablicy ciągi arytmetyczne (LA) i geometryczne (LG) 
o długości większej niż 2. 
Funkcja powinna zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG.
'''

##############################################################
def nwd(x, y):
    z = 0                      
    while (y != 0):             
        z = x % y               
        x = y                  
        y = z                  
    return x

def get_common_denominator(x, y): # nww
    return x* y // nwd(x, y)      

def try_to_reduce_fraction(l, m):
    x = nwd(l, m)
    return (l // x, m // x)

def print_num(n):
    l, m = try_to_reduce_fraction(n[0], n[1])
    if l == 0 or m == 1:
        print(l)
    else:
        print(l, '/', m)

def add(a, b):
    l1, m1 = a
    l2, m2 = b
    m = get_common_denominator(m1, m2)
    l = l1 * (m // m1) + l2 * (m // m2) 
    return try_to_reduce_fraction(l, m)

def subtract(a, b):
    l, m = b
    return add(a, (-l, m))

def multiply(a, b):
    l1, m1 = a
    l2, m2 = b    
    x = l1 * l2
    y = m1 * m2
    return try_to_reduce_fraction(x, y)

def divide(a, b):
    l, m = b
    return multiply(a, (m, l))
#################################################################################

def compare_LA_to_LG(t):
    n = len(t)

    LG = 0
    LA = 0

    q = 0
    if t[0][0] != 0:
        q = divide(t[1], t[0])
    current_g_count = 1
    r = subtract(t[1], t[0])
    current_a_count = 1 
    for i in range(2, n):
        #geometric
        if t[i-1][0] != 0:
            nq = divide(t[i], t[i-1])
        elif t[i][0] != 0:
            nq = None
        else:
            nq = 0
        if nq == q: 
            if current_g_count == 1:
                LG += 1
            current_g_count += 1
        else:
            current_g_count = 1
            q = nq
            
        #aritmetic
        nr = subtract(t[i], t[i-1])
        if nr == r: 
            if current_a_count == 1:
                LA += 1
            current_a_count += 1
        else:
            current_a_count = 1
            r = nr
            
    if LA > LG: 
        return 1
    elif LA < LG: 
        return -1
    return 0
            
print(compare_LA_to_LG([
    (1, 1), 
    (1, 2), 
    (1, 4), 
    (1, 8), 
    (1, 16), 
]))

print(compare_LA_to_LG([
    (1, 1), 
    (1, 2), 
    (1, 4), 
    (1, 8), 
    (1, 16), 
    (1, 1), 
    (1, 2), 
    (1, 4), 
    (1, 8), 
    (1, 16),
    (2, 5),
    (6, 10),
    (4, 5),
    (4, 4), 
    (1, 2),
    (0, 16),
]))

print(compare_LA_to_LG([
    (0, 1), 
    (0, 2), 
    (0, 4), 
    (0, 8), 
]))

print(compare_LA_to_LG([
    (0, 1), 
    (0, 2), 
    (1, 4), 
    (1, 8), 
]))

print(compare_LA_to_LG([
    (0, 1), 
    (1, 2), 
    (2, 2), 
    (3, 2), 
]))