"""
Zmodyfikować wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3.

z wikipedi wzialem wzor na pierwiastek n-stopnia
"""

e = 1e-10 # dokładnośc

s = float(input("podaj liczbę: "))

# randomowe wartosci zeby mnie wpuściło do pętli
a = 1
b = 2 

while abs(a - b) > e: # dopóki różnica miedzy aktualnym a poprzednim wyrazem ciągu jest wieksza niz zadana dokładnośc
    b = a                                # zachowuje wartośc do sprawdzenia
    a = ((2 * a) + (s / a ** 2)) / 3     # kożystam ze wzoru z wikipedia xD

print(f"pierwiastek 3 stopnia z {s} jest równy {a}") 