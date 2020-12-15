'''
def f(s, l, i = 0):    
    if s == 0:    
        return 1
    
    if i == len(l) or s < 0:
        return 0
    
    return f(s-l[i], l, i) + f(s, l, i+1)

t =  [5, 3, 2]
n = 15

print(f(n, t))
'''

def f(n, l, last = -1):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    counter = 0 
    for i in l:
        if i >= last:
            counter += f(n-i, l, i)
    
    return counter  
        

print(f(15, [3, 2, 5]))
