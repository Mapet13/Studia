"""
Mamy dane dwa ciągi A,B o następujących zależnościach:
A: a0 = 0, a1 = 1, an = an−1 − bn−1 ∗ an−2
B: b0 = 2, bn = bn−1 + 2 ∗ an−1
Proszę napisać program, który czyta liczby typu int ze standardowego wejścia i tak długo jak liczby te są
kolejnymi wyrazami ciągu An (tj. a0, a1, a2, ...) wypisuje na standardowe wyjście wyrazy drugiego ciągu Bn
(tj. b0, b1, b2, ...).

"""

a_1 = 0
a = 1
b = 2

# dla n = 0
if (int(input())) == a_1:
    print(b)
    
while int(input()) == a_1:
    # wyliczam b i wypisuje
    b_1 = b
    b = b_1 + (2 * a_1)
    print(b)
    
    # wyliczm kolejne a
    a_2 = a_1
    a_1 = a
    a = a_1 -  (b  * a_2)
    
    