'''
Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. 
Proszę napisać funkcję, która odpowiada na pytanie czy jest możliwe pocięcie ciągu na kawałki 
z których każdy reprezentuje liczbę pierwszą. 
Długość każdego z kawałków nie może przekraczać 30. 
Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu 110100 nie jest możliwe.
'''

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


def can_slice(t, start = 0):
    n = len(t)
    
    if start >= n:
        return True
    
    num = 0
    
    for i in range(start, min(start + 30, n)):
        num *= 2
        num += t[i]
        
        if is_prime(num) and can_slice(t, i + 1):
            return True
    
    return False


t = [1,1]
print(can_slice(t))

t = [1,1,1,0,1,1]
print(can_slice(t))

t = [1,1,0,1,0,0]
print(can_slice(t))

t = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
print(can_slice(t))
