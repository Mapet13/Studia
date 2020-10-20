"""
Nieskończony iloczyn
sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗sqrt(0.5))) ∗ ... 
ma wartość 2/π. 
Napisz program korzystający z tej zależności i wyznaczający wartość π.
"""

from math import sqrt

e = 10e-8                                                # dokładnośc 

result = 1                                               # 1 dla wygodnego przpisywania
next_element = sqrt(0.5)                                 # pierwszy wyraz ciągu
    
while (abs(next_element - 1) > e):                       # dopóki odleglosc "next_element" od 1 jest wieksza niz dokładnośc (im wieksza odleglosc tym wieksza zmiana rezultatu)        
    result *= next_element                               
    next_element = sqrt(0.5 + 0.5 * next_element)        # wyznaczam kolejny wyraz ciągu ktory jest równy sqrt(0,5 + 0,5 * poprzedni_wyraz_ciagu)

result *= next_element                  

result = 2 / result                                       # 2 / (2 / π) == π

print(result)