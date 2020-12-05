'''
Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.

np:
dla:
    t = [1, 2, 3, 4, 5, 6]
    product = 12
    
    n = 2                           # dwójki
    count(t, product, n) -> 2 bo (3, 4), (2, 6)
    
    n = 3                           # trójki
    count(t, product, n) -> 2 bo (1, 3, 4), (1, 2, 6)
'''

def count(T, product, n, i = 0):
    t_len = len(T)
    
    result = 0
    
    if n == 1:
        result += int(product == T[i])
    
    if i < t_len - n:
        result += count(T, product, n, i + 1)
        
    if n > 1 and product % T[i] == 0:
        result += count(T, product // T[i], n - 1, i + 1)
        
    return result


T = [1, 2, 3, 4, 5, 6]
    
print(count(T, 12, 2))
print(count(T, 12, 3))