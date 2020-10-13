"""
Napisać program wyznaczający wartość liczby e korzystając z zależności: 
e = 1/0! + 1/1! + 1/2! + 1/3! + ...
"""

# program dzialajacy jak wszystkie pozostale z nieskonczonymi ciagami

def factorial(x):
    y = 1
    if x == 0 or x == 1:
        return 1
    for i in range(2, x + 1):
        y *= i
    return y


precision = 1e-8

result = 0
next_element = 1

i = 1
while(next_element > precision):
    result += next_element
    next_element = 1 / factorial(i)
    i += 1
    
print(f"e = {result + next_element}")