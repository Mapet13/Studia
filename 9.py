"""
Napisać program wypisujący podzielniki liczby
"""

n = int(input("podaj liczbę: "))

i = 2
while n > 0 and i*i <= n:   # wystarczy sprawdzac do sqrt(n)
    if n % i == 0:          # jezeli znajde dzielnik:  
        print(i)        
        n //= i             #   zaktualizuj wartosc n 
    else:                   # w przeciwnym razie:
        i += 1              #   sprawdzaj kolejny dzielnik 
    
if n > 0:                   # wypisz na koncu zaktualizowaną liczbe n bo ona w koncu tez jest dzielnikiem 
    print(n)