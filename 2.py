"""
Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, 
aby w ciągu analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku

troche roziązanie na pałe ale nie widze lepszego aktualnie
"""

target = 2020

a = int(target / 2)
b = target - a
best = (a, b) # w taki sposob aby napewno byla tu suma zarowno dla nieparzystych jak i parzystych

for i in range(1, a):
    for j in range(1, b):   # przeszukuje kolejne pary mniejsze od a i b 
        x = i               # zapisuje pierwsze elementy do x i y 
        y = j               
        sum = x + y
        while sum < target: # dalej standardowo jak w ciagu Fibonacciego
            sum = x + y
            x = y
            y = sum
            if sum == target:                   
                if i + j < best[0] + best[1]:   # sprawdzam czy aktualna suma poczatkowych wyrazow jest mniejsza niz obecnie najlepsza
                    best = (i, j)


print(best)

                