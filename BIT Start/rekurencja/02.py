def f(n, k):
    if n == 0:
        return

    r = n % k
    f(n // k, k)
    
    if r > 9:
        r = chr(ord('A') + r - 10)
    
    print(r, end='')
       
 
f(13, 16)
print()