'''
Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr 1 oraz B cyfr 0, gdzie A, B > 0. 
Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość wszystkich możliwych do zbudowania liczb, 
takich że pierwsza cyfra w systemie dwójkowym (najstarszy bit) jest równa 1, a zbudowana liczba jest złożona. 
Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to 10010(2), 10100(2), 11000(2)
'''

def is_composite(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return True
        i += 1
    return False

def count_rec(A, B, num, d):
    r = 0
    
    if d < 0:
        print(bin(num)[2:])
        return int(is_composite(num))
    
    if A > 0:
        r += count_rec(A-1, B, num + 2**(d), d-1)
    if B > 0:
        r += count_rec(A, B-1, num, d-1)
        
    return r

def count(A, B):
    return count_rec(A-1, B, 2**(A+B - 1), A+B-2)

print(count(2, 3))