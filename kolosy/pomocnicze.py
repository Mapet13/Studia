from math import sqrt, floor, log10

def NWD(x, y):
    #jesli x,y może być ujemne to trzeba znaleźć abs()
    while y != 0:
        z = x % y
        x = y
        y = z
    return x

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5 
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def NWW(x, y):
    return x * y // NWD(x, y)

def is_power(n):
    for i in range(2, int(sqrt(n))+1):
        num = n
        while num % i == 0:
            num //= i
        if num == 1:
            return True
    return False



def decimal_to_binary(x):
    if x == 0:
        return 0
    b = 1
    while x > 1:
        b = b * 10 + x % 2
        x //= 2
    return b


def num_to_list(n):
    if n == 0:
        return [0]
    
    N = floor(log10(n)) + 1
    T = [0] * N
    
    for i in range(N-1, -1, -1):
        T[i] = n % 10
        n //= 10
        
    return T

def list_to_int(t):
    num = 0
    for i in range(len(t)):
        num *= 10
        num += t[i]
    return num


def cut_arr(T, i, j):
    t = T[:i]+T[i+1:]
    for x in range(len(T)-1):
        t[x] = t[x][:j] + t[x][j+1:]
    return t


def podz_l(n, k=1, l=[]):
    if n == 0:
        print(l)
    else:
        for i in range(k, n+1):
            podz_l(n-i, i, l+[i])

def prime_divisors(n):
    nums = set({})
    num = n
    div = 2
    while div <= sqrt(n)+1 and num != 1:
        while num % div == 0:
            nums.add(div)
            num //= div
        div += 1
    if num == n and num != 1:
        nums.add(num)
    return list(nums)
