from sys import stdin, stdout
from math import log10, floor

def construct_quasi(n):
    n = str(n)
    x = ""
    
    for i in n:
        if int(i) > 0:
            x += "1"
        else:
            x += "0"
            
    return int(x)

n = int(stdin.readline())
T = []

while n > 0:
    x = construct_quasi(n)
    n -= x
    T.append(x)    

stdout.write(str(len(T)) + '\n')
stdout.write(" ".join(str(x) for x in T))



