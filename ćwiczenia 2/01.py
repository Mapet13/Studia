"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, 
czy liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

pomysł dośc prosty 
na poczatku tworze po kolei ciag fibbonaciego
    - jesli iloczyn dwóch kolejnych wyrazow (czyli aktualnie najwiekszy iloczyn) jest mniejszy niz target to dalej iteruje tworzenie ciągu
    - jesli w koncu jest mniejszy to teraz biorę ten największy wyraz ciągu i po kolei teraz iteruje drugi ciąg "od końca"
        - jesli iloczyn maxa w 1 ciągu i min w 2 ciagu jest mniejszy niz target to przestaje iterowac drugi ciąg
        - jesli znalazlem iloczyn no to POG
    - jesli znalazlem iloczyn no to POG
    - iteruje tak az do momentu gdy nastepny element bedzie juz wiekszy/równy (aby sie łapało też np 1 * target)
"""

target = int(input("Podaj liczbę: "))

still_searching = True

b = 1
s = b
while s <= target and still_searching:
    a = b
    b = s
    s = a + b
    pro = a * b
    if pro == target:
        print(a, b)
        still_searching = False
    if pro > target:
        x = b - a
        y = a
        z = x + a
        while pro > target and still_searching:
            x = y - x
            y = z - y
            z = x + y
            pro = b * y
            if pro == target:
                print(y, b)
                still_searching = False
                
if still_searching:
    print("Podana liczba nie jest takim iloczynem")