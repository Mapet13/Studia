s = float(input())

a = 2
b = 1

e = 1e-8

while abs(a - b) > e:
    print(a, b)
    b = a
    a = (s/a+a)/2
    
print(b)


