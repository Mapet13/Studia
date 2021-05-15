from math import sqrt

def dist(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) 

X = [(0, 6), (1, 0), (2, 3), (5, 4), (6, 1), (7, 5), (8, 2)]
n = len(X)

D = [[dist(X[i], X[j]) for j in range(n)] for i in range(n)]

F = [[None] * n for i in range(n)] 

F[0][1] = D[0][1]

def tspf(i, j, F, D): # i < j

    if F[i][j] != None: 
        return F[i][j]
    
    if i == j-1:
        best = tspf(0, j-1, F, D) + D[0][j]
        for k in range(1, j-1):
            best = min(best, tspf(k, j-1, F, D) + D[k][j])
        F[j-1][j] = best
    else:
        F[i][j] = tspf(i, j-1, F, D) + D[j-1][j]
    
    return F[i][j]

res = tspf(0, n-1, F, D) + D[0][n-1]
for i in range(1, n-1):
    res = min(res, tspf(i, n-1, F, D) + D[i][n-1])
    
print(res)
