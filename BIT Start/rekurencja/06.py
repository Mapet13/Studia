

def a(x):
    a = x % 10
    b = (x % 100) // 10
    
    x -= a - b
    x -= b * 10 - a * 10
    return x  

def b(x):
    return x * 3

def c(x):
    num = 0
    while 10**(num+1) < x:
        num += 1
    
    fd = x // 10**num
    x -= fd * 10**num
    return x  
    

def f(x, y, s = 7, res = ''):
    if s == -1:
        return False
    
    if x == y:
        print(res)
        return True
    
    if f(b(x), y, s-1, res+'B'):
        return True
    
    if x >= 10:
        return f(a(x), y, s-1, res+'A') or f(c(x), y, s-1, res+'C') 
    
    return False    
    
f(6, 3)