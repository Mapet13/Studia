"""
Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb o najmniejszej różnicy. 
Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.

szybciej bylo by sprawdzic pierwiastek i potem iterować w "dół" w  poszukiwaniu liczby ktora dzieli i pierwsza taka liczba (i) oraz liczba a//i byly by odpowiedzią
    ^ ale chyba nie moge pierwiastka na WDI Sadge
"""

a = int(input("a: "))

# pierwszy oczywisty iloczyn
best_lower = 1
best_upper = a

i = 2
while i*i <= a: # jako oatstatni bede sprawdza liczbę <= pierwiastkowi bo najmniejszą różnice moze dawać własnie pierwiastek, potem "pary" iloczynow bedą sie powtarzać z już sprawdzonymi
    if a % i == 0: # jeżeli wyższa liczba (ale wciąż mniejsza od sqrt(a)) dzieli a to napewno ona i liczba "a/i" daja mniejszą róznice 
        best_lower = i
        best_upper = a // best_lower
    i += 1
        
print(f"{a} = {best_lower} * {best_upper}")