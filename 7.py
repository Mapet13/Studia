"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, 
czy liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
"""

target = int(input())

a = 1
b = 1

while (b*b < target):           # generuje ciag Fibonacciego do momentu gdzie kwadrat wyrazu >= szukanej liczbie
    c = b
    b = a + b
    a = c

if (a * b == target):        # sprawdzam czy iloczyn liczb się zgadza 
    print(f"tak, {target} == {a} * {b}")
else:
    print("nie")