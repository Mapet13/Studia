"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, 
czy liczba ta zawiera cyfrę równą liczbie swoich cyfr.
"""

n = int(input("n: "))

#wiem ze moge uzyc logarytmu ale na ćwiczeniach prowadzący kazal chyba robic pętlą
dc = 0
while 10**dc <= n:
    dc += 1

has_dc_digit = False    

while n > 0 and not has_dc_digit:
    if  n % 10 == dc:
        has_dc_digit = True
        break
    n //= 10

print(has_dc_digit)

