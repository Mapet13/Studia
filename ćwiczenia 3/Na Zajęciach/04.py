n = int(input("n: "))

licznik = 1
e = [0] * (n+1)
x = [0] * (n+1)
x[0] = 1

while True:
    # e += x
    p = 0
    for i in range(n, -1, -1):
        e[i] += x[i] + p
        p = e[i] // 10
        e[i] %= 10 
        
    #x = x / licznik
    r = 0
    koniec = True
    for i in range(n+1):
        r = 10*r + x[i]
        x[i] = r // licznik
        if x[i] > 0:
            koniec = False
        r = r % licznik 
    
    #if x == 0: 
    #    break
    if koniec:
        break
    
    licznik += 1
    
print(e[0], end = '.')
for i in range(1, n+1):
    print(e[i], end = '')