"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, 
czy jej cyfry stanowią ciąg rosnący.
"""

n = int(input("n: "))

prev = 10 # aby napewno poczatkowa cyfra byla najwieksza

is_still_growing = True

while (n > 0) and is_still_growing:
    a = n % 10
    n //= 10
    if a >= prev:
        is_still_growing = False
    prev = a

print(is_still_growing)
        
    
    
