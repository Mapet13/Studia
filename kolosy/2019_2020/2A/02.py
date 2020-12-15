'''
Na zbiorze liczb całkowitych określono trzy operacje: A,B,C przekształcające liczby:
 A: zwiększa liczbę o 3;
 B: podwaja liczbę;
 C: wszystkie parzyste cyfry w liczbie zwiększa o 1, np. 2356->3357, 1999->1999.

Proszę napisać funkcję która sprawdza czy można przekształcić liczbę X na liczbę Y w nie więcej niż N krokach.
Do funkcji należy przekazać wartości X,Y,N, funkcja powinna zwrócić liczbę możliwych ciągów operacji
przekształcających liczbę X w Y (lub wartość 0 jeżeli takie przekształcenie nie istnieje). Uwaga: zabronione jest
używanie kolejno dwóch tych samych operacji.

Na przykład:
Dla X=11, Y=31, N=4 funkcja powinna zwrócić 3 bo są 3 możliwe ciągi operacji: ABA, ACBC, CABA
Dla X=11, Y=32, N=4 funkcja powinna zwrócić 0.
'''
def a(x):
    return x + 3

def b(x):
    return x * 2

def c(x):
    if x == 0:
        return 1
    
    res = 0
    i = 0
    while x > 0:
        d = x % 10
        if x % 2 == 0:
            d += 1
 
        res += d * 10**i 
        i += 1
        x //= 10    
    
    return res

def func(x, y, n, last = -1):
    counter = 0
    
    if x == y:
        return 1
    if n <= 0:
        return 0
    
    if (last != 0): 
        counter += func(a(x), y, n-1, 0)
    if (last != 1): 
        counter += func(b(x), y, n-1, 1)
    if (last != 2): 
        counter += func(c(x), y, n-1, 2)
             
    return counter        
             
print(func(11, 31, 4))
print(func(11, 32, 4))