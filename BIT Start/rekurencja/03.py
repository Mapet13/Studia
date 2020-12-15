def f(T, i = 0):
    N = len(T)
    
    if i >= (N // 2):
        return
    
    T[i], T[N-1-i] = T[N-1-i], T[i]
    f(T, i+1)
    
    

a = [1, 2]
f(a)
print(a)

a = [1]
f(a)
print(a)

a = []
f(a)
print(a)
    
a = [1, 2, 3, 4, 5, 6]
f(a)
print(a)

a = [1, 2, 3, 4, 5, 6, 7]
f(a)
print(a)