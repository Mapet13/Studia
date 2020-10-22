"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, 
czy liczba naturalna jest palindromem, 
a następnie czy jest palindromem w systemie dwójkowym.
"""

from math import floor, ceil, log10, log2


num = int(input("Podaj liczbę: "))
is_palindrome_10 = True


decy_num = num    # bede mowyfikowal decy_num zeby zchowac orygionalna wartosc na pozniej
dc = floor(log10(decy_num)) + 1 # liczba cyfr
"""
    dla liczby 1234321:
        sprawdzam 1 i 1, 2 i 2 , 3 i 3, i kończe (jest palindromem)
    dla liczby 1121:
        sprawdzam 1 i 1, 1 i 2 <- nie dziala wiec kończe (nie jest palindromem)
"""
while dc > 1: # bo dla dc == 1 liczba jest palindromem 
    t = decy_num % 10                   # cyfra jednosc
    h = decy_num // (10 ** (dc - 1))    # "ostatnia" cyfra liczby
    if h != t: # jesli sie nie zgadza to kończe dalsze sprawddzanie
        print(f"Liczba '{num}' nie jest palindromem w systemie decymalnym")
        is_palindrome_10 = False
        break 
    decy_num %= 10   # obcinam pierwszą i ostatnią cyfrę liczby 
    decy_num //= 10 
    dc -= 2
    
if is_palindrome_10:
    print(f"Liczba '{num}' jest palindromem w systemie decymalnym")
    
# """
# dla binarnych:
#     dla np 76 -> '1001100' w binarnym (ma 7 cyfr)
#         - przesuwam binarnie w prawo o 4 miejsca (bo sufit z 7/2) [bin_h = 100]
#         - odwracam bin_h negacją bitowa i dostaje [bin_h = 001]
#         - binarne 'and' z 2^3 - 1 czyli z (0000111) i dostaje [bin_t = 100]
#         - sprawdzam czy bin_h == bin_t (w tym przypadku się nie zgadza)
#     dla np 31 -> '11111' w binarnym (ma 5 cyfr)
#         - przesuwam binarnie w prawo o 3 miejsca (bo sufit z (5/2)) [bin_h = 11]
#         - odwracam bin_h negacją bitowa i dostaje [bin_h = 11]
#         - binarne 'and' z 2^2 - 1 czyli z (000011) i dostaje [bin_t = 11]
#         - sprawdzam czy bin_h == bin_t (w tym przypadku się zgadza)
# """
    
# def reverse_bits(n):
#     res = 0
#     while n > 0:
#         res <<= 1   # YYY0
#         if n & 1 == 1: # jezeli LSB w n jest 1 to zamieniam tamto dodane 0 na 1 w res 
#             res ^= 1   #    res xor 0001 -> zamienia ostatnie 0 na 1 a pozostałe bity zostawia 
#         n >>= 1 # 0YYY
#     return res 
        
    
# bin_dc = floor(log2(num)) + 1
# bin_h = reverse_bits(num >> ceil(bin_dc / 2))
# bin_t = num & (2**floor(bin_dc / 2) - 1)
# print(bin(bin_h), bin(bin_t))

# if bin_h == bin_t:
#     print(f"Liczba {bin(num)} jest palindromem w systemie binarnym")
# else:
#     print(f"Liczba {bin(num)} nie jest palindromem w systemie binarnym")

# albo po prostu tak samo jak w 10-tnych
is_palindrome_2 = True 
bin_dc = floor(log2(num)) + 1
bin_num = num
while bin_dc > 1: # bo dla dc == 1 liczba jest palindromem 
    t = bin_num % 2                       # cyfra jednosc
    h = bin_num // (2 ** (bin_dc - 1))    # "ostatnia" cyfra liczby
    if h != t: # jesli sie nie zgadza to kończe dalsze sprawddzanie
        print(f"Liczba '{bin(num)[2:]}' nie jest palindromem w systemie binarnym")
        is_palindrome_2 = False
        break 
    bin_num %= 2   # obcinam pierwszą i ostatnią cyfrę liczby 
    bin_num //= 2 
    bin_dc -= 2
if is_palindrome_2:
    print(f"Liczba '{bin(num)[2:]}' jest palindromem w systemie binarnym")
    
     
     

    