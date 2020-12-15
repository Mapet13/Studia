def podzial(n, k = 1, l=""):
    if n == 0 and '+' in l[:-1]:
        print(l[:-1])
    else:    
        for i in range(k, n+1):
            podzial(n-i, i, l + str(i) + "+")
          
podzial(10)