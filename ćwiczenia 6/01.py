'''
Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą 
i wypisuje wszystkie co najmniej dwucyfrowe liczby pierwsze, 
powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej cyfry.
'''

def get_num_lenth(x):
    dc = 0
    while x > 0:
        dc += 1
        x //= 10
    return dc 



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
    
    
    
def delete_digit(n, x):
    tail = n % (10**(x-1))
    head = (n - (n % (10**x))) // 10
    return head + tail
    
    
    
def rec(num, last_i, current_lenth, original_lenth):
    if current_lenth < original_lenth:
        if is_prime(num):
            print(num)
            
    for i in range(last_i, current_lenth + 1):
        current_num = delete_digit(num, i)
        new_lenth = get_num_lenth(current_num)
        if new_lenth > 1:
            rec(current_num, i, new_lenth, original_lenth)



def get_special_primes(num):
    lenth = get_num_lenth(num)
    return rec(num, 1, lenth,lenth)
    
    
    
get_special_primes(1035)
get_special_primes(203)
get_special_primes(238854903282103)
