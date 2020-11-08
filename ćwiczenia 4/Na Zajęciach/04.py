from random import randint

def f(t):
    n = len(t)
    pom_k = 0
    pom_w = 10 ** 100

    for x in range(n):
        sw = 0
        sk = 0
        for y in range (n):
            sw += t[x][y]
            sk += t[x][y]
        if pom_w > sw:
            pom_w = sw
            w = x
        if pom_k < sk:
            pom_k = sk
            k = x 
            
    return w, k

t = [[randint(1, 9) for _ in range(4)] for _ in range(4)]
print(t)
print(f(t))