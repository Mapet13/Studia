'''
Liczby wymierne są reprezentowane przez krotkę (l,m). 
Gdzie: l - liczba całkowita oznaczająca licznik, 
m - liczba naturalna oznaczająca mianownik. 
Proszę napisać podstawowe operacje na ułamkach, 
m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie.
'''

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



def get_input():
    l = int(input("l: "))
    m = int(input("m: "))
    return try_to_reduce_fraction(l, m)



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
    l1, m1 = a
    l2, m2 = b
    
    m = get_common_denominator(m1, m2)
    l = l1 * (m // m1) - l2 * (m // m2) 
    
    return try_to_reduce_fraction(l, m)



def power(a, p):
    l, m = a
    
    return try_to_reduce_fraction(l ** p, m ** p)



def multiply(a, b):
    l1, m1 = a
    l2, m2 = b
    
    x = l1 * l2
    y = m1 * m2
    
    return try_to_reduce_fraction(x, y)



def divide(a, b):
    l1, m1 = a
    l2, m2 = b
    
    x = l1 * m2
    y = l2 * m1
    
    return try_to_reduce_fraction(x, y)
    
    

n1 = (2, 5)
n2 = get_input()

print()

print_num(n2)
print_num(add(n1, n2))
print_num(subtract(n1, n2))
print_num(multiply(n1, n2))
print_num(divide(n1, n2))
print_num(power(n2, 2))