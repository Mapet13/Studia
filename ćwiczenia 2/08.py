"""
Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego, 
np. 9,14,15,17,22. 
Proszę napisać program, który wczytuje liczbę naturalną n, 
wylicza i wypisuje następną taką liczbę większą od n. 
Można założyć, że 0 < n < 1000.

nw do konca czy napewno jest poprawne to rozwiązanie no ale daje poprawne wyniki. W kazdym razie to zadanie wypaliło mi mózg
"""

n = int(input("n: "))

a = 0
b = 1
sum = 1

n += 1

while True:
    #tworze ciag az gdy suma wszystkuch elementow nie bedzie wieksza niz n
    while sum < n:            
        c = a + b
        sum += c       
        a = b
        b = c
        
    #trzymam stan sumowania aby potem wrócić jesli sprawdzana liczba nie bedzie taką jaka chce i kontynuuje dla nastepnej
    keep_sum = sum
    keep_a = a
    keep_b = b
    
    still_searching = True
    
    x = 0
    y = 1
    while still_searching:
        # po kolei odejmuje od sumy wyrazy z "początku ciągu"
        # do momentu gdy suma bedzie mniejsza lub rowna sprawdzanej liczba
        while sum > n:
            z = x + y
            x = y
            y = z
            sum -= x
            if x == b:
                print(n)
                exit()
            
        # jesli juz znalazlem to wtedy napewno oddtwarzam stan i bede sprawdzam next liczbe
        if n == sum:
            still_searching = False
        else:
            # jesli nie no to musze dodac do sumy kolejne "b" i przeiterowac fibbonaciego
            c = a + b
            sum += c
            a = b
            b = c

    #odtwarzam stan i bede sprawdzal nastepna liczbę
    n += 1
    sum = keep_sum
    a = keep_a
    b = keep_b
