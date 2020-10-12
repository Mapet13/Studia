"""
Napisać program sprawdzający czy zadana liczba jest pierwsza.

skoro mamy nie uzywac list to standardowy algorytm a nie sito Eratostenesa
"""

target = int(input("Podaj liczbę: "))

is_prime = True          # wartośc domyslnie ustawiona na True, jesli sie okaze ze jednak target to nie liczba pierwsza to wartosc tej zmiennej ulegnie zmianie

if target > 1:
    i = 2
    while (i*i <= target):      # wystarczy sprawdzac liczby do sqrt(target)
        if target % i == 0:     # jezeli znajdzie się dzielnik 
            is_prime = False
            break
        i += 1                  

if is_prime:
    print(f"Tak, {target} jest liczba pierwszą")
else:
    print(f"Nie, {target} nie jest liczba pierwszą")