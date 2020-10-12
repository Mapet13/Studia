# Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona

a = 1
b = 1

while a < 1000000:
    print(a)
    c = a+b
    a = b
    b = c
    
"""
1 1 2 3 5
a b c
  a b c
    a b c
"""