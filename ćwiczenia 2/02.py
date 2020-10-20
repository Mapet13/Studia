"""
Napisać program wczytujący trzy liczby naturalne a,b,n 
i wypisujący rozwinięcie dziesiętne ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. 
(n jest rzędu 100)

działa jak dzielenie pisemne
"""

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
n = int(input("Podaj n: "))

result = a//b
print(result, '.', sep='', end='') # wypisuje częśc całkowitą ułamka
a -= result * b

for i in range(0, n):
    a *= 10
    result = a // b
    print(result, end='')
    a -= result * b
    if a == 0: # kończe bo po co mam wypisywać 0 do końca
        break
