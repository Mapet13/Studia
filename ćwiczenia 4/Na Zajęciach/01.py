'''
def f(t):
    N = len(t)
    
    for i in range(N):
        for j in range(N):
            t[i][j] = 0
            
    dx = 0
    dy = 1
    x = 0
    y = 0
    i = 1
    
    while t[x][y] == 0:
        t[x][y] = i
        
        if (x + dx) >= N or (dx != 0 and t[x+dx][y] != 0):
            dy = -dx
            dx = 0
        if (y + dy) >= N or (dy != 0 and t[x][y+dy] != 0):
            dx = dy
            dy = 0
            
        x += dx
        y += dy
        i += 1
'''
def f(t):
    n = len(t)
    a = 0
    b = n - 1
    
    licznik = 1
    while a < b:
        for i in range(a, b):
            t[a][i] = licznik
            # licznik += 1
        #for i in range(a, b):
            t[i][b] = licznik + b - a
            licznik += 1
        licznik += b - a
        for i in range(b, a, -1):
            t[b][i] = licznik
            licznik += 1
        for i in range(b, a, -1):
            t[i][a] = licznik
            licznik += 1 
        a += 1
        b -= 1
    
    if n % 2 == 1:
        t[n//2][n//2] = licznik

t = [[0] * 5 for _ in range(5)]
print(t)
f(t)
print(t)


    

    