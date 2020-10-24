"""
Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry. 

Proszę napisać program, który wczytuje dwie liczby naturalne i poszukuje 
najmniejszej podstawy systemu (w zakresie2-16) w którym liczby są różno-cyfrowe. 

Program powinien wypisać znalezioną podstawę, jeżeli podstawa taka nie istnieje należy wypisać komunikat o jej braku.

Na przykład: dla liczb 123 i 522 odpowiedzią jest
podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11).
"""

x = int(input("x: "))
y = int(input("y: "))

has_not_find_same_digits = True

base = 2
while base <= 16:
    a = x
    still_searching = True
    while (a > 0) and still_searching:
        b = y
        digit_a = a % base
        while b > 0:
            digit_b  = b % base
            if digit_a == digit_b:
                still_searching = False
                break
            b //= base
        a //= base
    if still_searching:
        has_not_find_same_digits = False
        break
    base += 1        
    
if has_not_find_same_digits:
    print("Brak takiej podstawy w tym zakresie")
else:
     print(base)