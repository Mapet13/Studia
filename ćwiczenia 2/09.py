"""
Napisać program, który oblicza pole figury pod wykresem funkcji:
y = 1/x 
w przedziale od 1 do k, 
metodą prostokątów.
"""
k = float(input("k: "))

e = 10e-8

def f(x):
    return 1 / x

result = 0
next_result = (k - 1) * f(k)
i = 2.0
while abs(next_result - result) > e:
    result = next_result
    next_result = 0
    j = 1
    while j <= i:
        next_result += f(((k-1) / i * j) + 1) * (k-1) / i
        j += 1
    i += 1
        
print(next_result)