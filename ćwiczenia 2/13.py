"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy liczba zakończona jest unikalną cyfrą.
"""

a = int(input("a: "))

end = a % 10
a //= 10

is_unique = True

while a > 0 and is_unique:
    if a % 10 == end:
        is_unique = False
        break
    a //= 10
    
print(is_unique)