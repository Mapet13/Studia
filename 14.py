"""
Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.

filmik odnosnie tego szeregu dla cos(x) -> https://www.youtube.com/watch?v=JlDLbjY9xcA&ab_channel=KhanAcademyPoPolsku
"""

e = 1e-6

# standardowy algorytm do wyznaczania silni (iteracyjny) 
def factorial(x):
    y = 1                   # zmienna składująca wynik
    if x == 0 or x == 1:    
        return 1
    for i in range(2, x+1): # mnoze przez kolejne liczby do x
        y *= i
    return y 

alfa = float(input("Podaj kąt w radianach: "))

result = 0
next_element = 1

i = 2
while (abs(next_element) > e):                          # dopóki kolejny element jest juz mało znaczący  
    result += next_element                              # dodaje poprzedni
    next_element = 1/(factorial(i)) * (alfa ** i)       # wyliczam kolejny ze wzoru 
    if i % 4 == 2:                                      # pochodną 2, 6, 10 itp stopnia jest -cos -> wiec daje minus
        next_element = -next_element
    i += 2                                              # iteruje co 2 bo pochodna cosinusa stopnia nieparzystego w zerze daje wynik 0
        
    
print(f"cos({alfa}) = {result + next_element}")