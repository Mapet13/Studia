'''
Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym
wierszu, bądź kolumnie znajduje się fragmentu ciągu arytmetycznego o długości
większej niż 2, którego elementy są liczbami pierwszymi. Proszę napisać funkcję
która zwróci długość tego ciągu.
'''

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5 
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def f(T):
    N = len(T)

    for i in range(N):
        for j in range(N):
            if is_prime(T[i][j]):
                counter = 1
                r = None
                for col in range(i+1, N):
                    if is_prime(T[col][j]):
                        if r == None:
                            r = T[i][j] - T[col][j]
                        if T[col-1][j] - T[col][j] == r:
                            counter += 1
                        else:
                            break
                    else:
                        break        
                if counter <= 2:
                    counter = 1
                    r = None
                    for row in range(j+1, N):
                        if is_prime(T[i][row]):
                            if r == None:
                                r = T[i][j] - T[i][row]
                            if T[i][row-1] - T[i][row] == r:
                                counter += 1
                            else:
                                break  
                        else:
                            break
                if counter > 2:
                    return counter
                
                        
                        
T = [
    [1, 1, 1, 1],
    [1, 1, 1, 3],
    [1, 1, 1, 5],
    [1, 1, 1, 7],
]
print(f(T))

T = [
    [1, 1, 1, 1],
    [1, 7, 5, 3],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
print(f(T))

T = [
    [1, 1, 1, 1],
    [5, 7, 1, 3],
    [3, 5, 1, 1],
    [1, 1, 1, 1],
]
print(f(T))

T = [
    [1, 1, 1, 3],
    [5, 7, 1, 3],
    [3, 5, 1, 3],
    [1, 1, 1, 3],
]
print(f(T))