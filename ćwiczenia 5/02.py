'''
Używając funkcji z poprzedniego zadania proszę napisać 
funkcję rozwiązującą układ 2 równań o 2 niewiadomych
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


def get_determinant(x, y, z, w):
    return subtract(multiply(x, y), multiply(z, w))


#a --> tab[2][2] - współczynniki przy x
#b --> tab[2] - wyrazy wolne
def solve(a, b):
    w = get_determinant(a[0][0], a[1][1], a[0][1], a[1][0])
    wx = get_determinant(b[0], a[1][1], b[1], a[0][1])
    wy = get_determinant(a[0][0], b[1], b[0], a[1][0])
    
    if wx[1] == 0 or wy[1] == 0 or w[1] == 0 or ((wx[0] != 0 or wy[0] != 0) and w[0] == 0):
        print("Równanie nie ma rozwiązań")
    elif wx[0] == 0 and wy[0] and 0 and w[0] == 0:
        print("Istnieje nieskończenie wiele rozwiązań")
    else:
        x = divide(wx, w)
        y = divide(wy, w)
        
        print("X: ", end = '')
        print_num(x)
        
        print("Y: ", end = '')
        print_num(y)
    
     
a = [
    [(7, 1), (2, 1)],
    [(3, 1), (4, 1)]
]

b = [
    (1, 1),
    (2, 1)
]
solve(a, b)

print()

a = [
    [(1, 4), (-1, 5)],
    [(1, 2), (1, 3)]
]

b = [
    (-1, 1),
    (9, 1)
]
solve(a, b)