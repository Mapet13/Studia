"""
Proszę napisać program rozwiązujący równanie 
x^x = 2020 
metodą bisekcji

metoda bisekcji: 
    - jezeli funckcja jest ciąga oraz:          
        f(a) > 0,
        f(b) < 0
        to miedzy a i b jest pierwiastek tego równania
"""


def f(x):                       # funkcja zdefiniowana dla wygody i czytelnosci
    return pow(x, x) - 2020


min = -6.0  # maksymalna wartośc sprawdzania
max = 6.0   # minimalna wartość sprawdzania
e = 1e-10  # precyzja

# sprawdzam min i max czy nie sa pierwiastkami rownania
if f(min) == 0:
    print(min)
elif f(max) == 0:
    print(max)
elif (f(min) > 0 and f(max) > 0) and (f(min) < 0 and f(max) < 0):
    print("W podanym zakresie nie ma pierwiastka równania")
    exit(0)

# algorytm bisekcji
x = (min + max) / 2
if f(x) != 0:                  # sprawdzam czy ten punkt jest pierwiastkiem
    while abs(f(x)) > e:       # dopóki nie osiągne załozonej dokładności
        if f(x) < 0:           # przypisanie x do min/max w zaleznosci od znaku
            min = x
        else:
            max = x
        x = (min + max) / 2    # wyliczenie nowego x

print("Zanaleziony pierwiastek to:", x)
