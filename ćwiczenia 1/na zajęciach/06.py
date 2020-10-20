"""
Proszę napisać program rozwiązujący równanie 
"""
def f(x):
    return x**x - 2020 

p = 0
k = 10
pom = 1e-10

#do-while
while True:
#do
    print(p, k)
    a = (p + k) / 2
    fa = f(a)
    if fa < 0:
        p = a
    else:
        k = a
#while
    if abs(fa) < pom: # albo (abs(p-k) < pom)
        print(a)
        print(a**a)
        break
    
        