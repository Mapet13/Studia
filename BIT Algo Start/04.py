from sys import stdin, stdout
from math import inf
 
n = int(stdin.readline())
A = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(n)]
 
F = [[inf] * (n+1) for _ in range(n)]
F[0][0] = 0

for j in range(1, A[0][0] + 1):
        F[0][j] = A[0][1]

for i in range(1, n): 
    F[i][0] = 0
    for j in range(n, -1, -1): 
        if j >= (A[i][0] + 1): 
            F[i][j] = min(F[i-1][j], F[i-1][j - (A[i][0]+1)] + A[i][1])
        else: 
            F[i][j] = min(F[i-1][j], A[i][1])
 
for x in F:
    print(x)

stdout.write(str(F[n-1][n])) 