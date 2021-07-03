'''

A = [2, 1, 3, 7, 6, 9, 4, 2, 0]
B = [3, 7, 2, 6, 1, 9, 3, 2, 7]
 
f(i, j) = {  <<-- długosc max podciagu dla A[0...(i-1)], B[0...(j-1)]
    if A[i] == B[j]: f(i-1, j-1) + 1    
    else:            MAX(f(i-1, j), f(i, j-1)) 
}

samo algo:
    złożonośc czasowa: O(n^2)
    złonośc pamięcowa: O(n^2)
'''
def get_result(A, B, F, i, j):
    if i == 0:
        if A[i] == B[j]: 
            return [A[i]]
        if j == 0:
            return []
        else:
            return get_result(A, B, F, i, j-1)
    if j == 0:
        if A[i] == B[j]: 
            return [A[i]]
        if i == 0:
            return []
        else:
            return get_result(A, B, F, i-1, j)
    if A[i] == B[j]:
        return get_result(A, B, F, i-1, j-1) + [A[i]]
    if F[i][j-1] > F[i-1][j]:
        return get_result(A, B, F, i, j-1)
    return get_result(A, B, F, i-1, j)



A = [2, 1, 3, 7, 6, 9, 4, 2, 0]
B = [3, 7, 2, 6, 1, 9, 3, 2, 7]
n = len(A)

F = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if A[i] == B[j]:
           if (i > 0 and j > 0): F[i][j] = F[i-1][j-1]  
           F[i][j] += 1
        else: 
            if (i > 0): F[i][j] = F[i-1][j]  
            if (j > 0): F[i][j] = max(F[i][j], F[i][j-1]) 

for x in F:
    print(x)

print("MAX: ", F[n-1][n-1])
print("res: ", get_result(A, B, F, n-1, n-1))

