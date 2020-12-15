def fib(n, a):
    if a[n] != -1:
        return a[n]
    
    a[n] = fib(n-1, a) + fib(n-2, a)
    return a[n]
    
    
if __name__ == "__main__":
    a = [-1 for _ in range(1000)]
    a[0] = 1
    a[1] = 1
    print(fib(100, a))