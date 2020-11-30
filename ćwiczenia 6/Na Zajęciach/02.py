def weight(n):
    counter = 0
    podzielnik = 2
    while n > 1 and podzielnik < n**0.5:
        is_primary = False
        while n % podzielnik == 0:
            is_primary = True
            n //= podzielnik
        if is_primary:
            counter += 1
        podzielnik  += 1
    if n > 1:
        counter += 1
    return counter

def zbiory(t):
    
    def z(t, s1, s2, s3, l):
        if l == len(t):
            return s1 == s2 == s3
        return z(t, s1 + t[l], s2, s3, l + 1) or z(t, s1, s2 + t[l], s3, l + 1) or z(t, s1, s2, s3 + t[l], l + 1)
    
    
    ws = 0
    wa = [0] * len(t)
    
    for i in range(len(t)):
        wa[i] = weight(t[i])
        ws += wa[i]
    if ws % 3  != 0:
        return False
    return z(t, 0, 0, 0)