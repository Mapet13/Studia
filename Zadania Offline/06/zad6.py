from math import sqrt, inf

def dist(a, b):
    return sqrt((a[1]-b[1])**2 + (a[2]-b[2])**2) 

def tspf(i, j, F, D):

    if F[i][j] != None: 
        return F[i][j]
    
    if i == j-1:
        best = tspf(0, j-1, F, D) + D[0][j]
        for k in range(1, j-1):
            best = min(tspf(k, j-1, F, D) + D[k][j], best)
        F[j-1][j] = best
    else:
        F[i][j] = tspf(i, j-1, F, D) + D[j-1][j]
        
    
    return F[i][j]


def bitonicTSP( C ):
    C.sort(key=lambda tup: tup[1])
    n = len(C)
    
    
    D = [[dist(C[i], C[j]) for j in range(n)] for i in range(n)]
    F = [[None] * n for i in range(n)] 
     
    
    F[0][1] = D[0][1]
    
    res = tspf(0, n-1, F, D) + D[0][n-1]
    i = 0
    for k in range(1, n-1):
        x = tspf(k, n-1, F, D) + D[k][n-1]
        if x < res:
            res = x
            i = k
    
    last_value = F[i][n-1]
    route_data = [None] * n
    
    for k in range(i+1, n):
        route_data[k] = False
      
    route_flag = True
    j = n-1
    while i > 0:
        last_j = j
        j = i
        
        min_diff = inf
        for k in range(0, j):
            distance = D[k][j+1]
            for x in range(j+1, last_j):
                distance += D[x][x+1]
            current_diff = abs(last_value - (F[k][j] + distance))
            if current_diff < min_diff:
                min_diff = current_diff
                i = k
        

        for k in range(i + 1, j + 1):
            route_data[k] = route_flag

        route_flag = not route_flag
        last_value = F[i][j]
    
    for k in range(n):
        if not route_data[k]:
            print(C[k][0], end=' ')
    for k in range(n-1, -1, -1):
        if route_data[k]:
            print(C[k][0], end=' ')
    print(C[0][0])
    print(res)
    

  
C = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]
bitonicTSP( C )