"""
Proszę napisać program sprawdzający czy istnieje 
spójny podciąg ciągu Fibonacciego o zadanej sumie
"""

"""
moj algorytm wyglada w nastepujacy sposob 
mam wartosci poczatkowe ia i ib (1, 1)
w petli nadrzednej iteruje je jak normalny ciag fibbonaciego 
i uzywam ich jako wartosci poczatkowe do ciagu podrzednego (a, b)
przez co moje szukanie sumy wyglada w nastepujacy sposob 

np dla wartosci 76:
1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34  > 76
1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 > 76
...
8 + 13 + 21 + 34 = 76 <- ciąg znaleziony

np dla wartosci 30:
1 + 1 + 2 + 3 + 5 + 8 + 13 > 30
...
3 + 5 + 8 + 13 + 21 > 30
5 + 8 + 13 + 21 > 30
8 + 13 + 21 > 30
13 + 21 > 30 <- wiec nie ma takiego spojnego podciagu
"""


target_sum = int(input("podaj szukaną sumę: "))

initial_a = 1
initial_b = 1

has_resault = False

while initial_b + initial_a < target_sum:
    a = initial_a
    b = initial_b
    sum = 0
    while sum < target_sum:
        s = a + b 
        a = b
        b = s
        sum += s
    if sum == target_sum:
        print("Istnieje taki spójny podciąg")
        has_resault = True
        break
    initial_sum = initial_a + initial_b
    initial_a = initial_b
    initial_b = initial_sum
    
if has_resault == False:
    print("Nie istnieje taki spójny podciąg")