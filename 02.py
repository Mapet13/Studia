"""
Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, 
aby w ciągu analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku

troche roziązanie na pałe ale nie widze lepszego aktualnie
"""

target = 13844

a = int(target / 2)
b = target - a
best = (a, b) # w taki sposob aby napewno byla tu suma zarowno dla nieparzystych jak i parzystych

for i in range(1, a):
    for j in range(1, i+1):   # przeszukuje kolejne pary mniejsze od a i b (i, j) gdzie j jest mniejszy niz i 
        x = j                 # zapisuje pierwsze elementy do x i y (x - mniejsza)(y - wieksza)
        y = i               
        sum = x + y
        while sum < target: # dalej standardowo jak w ciagu Fibonacciego
            sum = x + y
            x = y
            y = sum
            if sum == target:                   
                if i + j < best[0] + best[1]:   # sprawdzam czy aktualna suma poczatkowych wyrazow jest mniejsza niz obecnie najlepsza
                    best = (j, i)


print(best)