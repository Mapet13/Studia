'''
Używając funkcji z poprzedniego zadania 
proszę napisać funkcję rozwiązującą równanie kwadratowe o współczynnikach zespolonych.
'''

##############################################################
def get_input():
    re = int(input("re: "))
    im = int(input("im: "))
    return (re, im)

def print_num(n):
    re, im = n
    if im != 0:
        if re != 0:
            print(re, end = '')
        s = ""
        if abs(im) == 1:
            if im == -1:
                s = "-"
            print(s, 'i', sep='')
        else:
            if re != 0 and im > 0:
                s = "+"
            if im < 0:
                s = '-'
            print(s, abs(im), 'i', sep='')
    else:
        print(re)
        
def subtract(a, b):
    return add(a, (-b[0], -b[1]))        

def add(a, b):
    return (a[0] + b[0], a[1] + b[1]) 

def multiply(a, b):
    return ((a[0] * b[0]) - (a[1] * b[1]), (a[0] * b[1]) + (a[1] * b[0]))       

def power(a, n):
    r = (1, 0)
    for _ in range(n):
        r = multiply(r, a)
    return r

def get_conjugate(a):
    return (a[0], -a[1])

def divide(a, b):
    if b[1] == 0:
        return (a[0] / b[0], a[1] / b[0])
    else:
        cb = get_conjugate(b)
        l = multiply(a, cb)
        m = multiply(b, cb)
        return divide(l, m)
##############################################################

# (a * x^2) + (b * x) + c
def solve(a, b, c):
    delta = subtract(power(b, 2), multiply(multiply((4, 0), a), c))
    if delta[0] == 0 and delta[1] == 0:
        x = divide((-b[0], -b[1]), multiply((2, 0), a))
        return (x, x)
    
    


a = (2, 3)
b = (1, 2)
c = (-2, -9)

