"""
Napisać program wyliczający pierwiastek równania 
x^x = 2020 
metodą stycznych
"""
from math import log, e

def f(x):
    return x**x - 2020

def fp(x):
    return x**x * (log(x, e) + 1)

a = 1.0
b = 10.0
while(abs(a-b) > 1e-8):
    a = b
    b = a - (f(a) / fp(a))

print(b)