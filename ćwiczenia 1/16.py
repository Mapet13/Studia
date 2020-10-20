"""
Dany jest ciąg określony wzorem: 
An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. 
Napisać program, który znajdzie wyraz początkowy z przedziału 2-10000 
dla którego wartość 1 jest osiągalna po największej liczbie kroków
"""

# w tych zmiennych bede zapisywał najlepszy wynik 
max_iterations = 0
current_best = 2

for i in range(2, 10000):    # iteruje i sprawdzam dla kolejnych liczb
    iterations = 0                                          
    a = i                    # wyraz początkowy
    while a != 1:            # dopóki nie osiągne wartości 1
        mod_2 = a % 2        # dla wygody aby nie liczyc 2 razy
        a = mod_2 * (3 * a + 1) + (1 - mod_2) * a / 2       # liczę z podanego wzoru
        iterations += 1
    if iterations > max_iterations: # sprawdzam czy zostalo wykonane wiecej operacji i jesli to aktualizuje najlepszy wynik
        max_iterations = iterations
        current_best = i

print(f"{current_best} -> {max_iterations} iteracji")
