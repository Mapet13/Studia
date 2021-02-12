from math import floor, log10

# zamiana numeru na liste
def num_to_list(n):
    if n == 0:
        return [0]
    
    N = floor(log10(n)) + 1
    T = [0] * N
    
    for i in range(N-1, -1, -1):
        T[i] = n % 10
        n //= 10
        
    return T
#end

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
#end

def divide(num):
    t = num_to_list(num) # zamieniam liczbe na liste
    
    def recur_divide(T, i = 0, c = 0):
        if i == len(T): # warunek końca
            return is_prime(c) # sprawdzam czy liczba podziałów jest liczbą pierwszą
        num = 0 # rozpoczynam budowanie liczby dla aktualnego podziału
        while i < len(T):
            num *= 10
            num += T[i]
            if is_prime(num) and recur_divide(T, i+1, c + 1): # tworze kolejny podział rekurencyjnie tylko gdy aktualny kawałek jest liczbą pierwszą
                return True
            i += 1
        
        return False
    
    return recur_divide(t) # wywołuje funkcje rekurencyjna zagnieżdżoną 
#end