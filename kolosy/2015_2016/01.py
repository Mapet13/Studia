def qsort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        qsort(A, p, q-1)
        p = q+1

def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def sumSort(A, B, n):
    def getSum(i):
        s = 0
        for j in range(n*i, n*(i+1)):
            s += A[j]
        return s
     
    T = [(n*i, getSum(i)) for i in range(n)]
    qsort(T, 0, n-1)
    
    idx = 0
    for i in range(n):
        for j in range(T[i][0], T[i][0] + n):
            B[idx] = A[j]
            idx += 1
    
    return B

T =  [0, 4, 2, 7, 5, 10, 1, 7, 9, 7, 9, 0, 8, 6, 9, 5, 9, 8, 6, 6, 2, 0, 1, 1, 6, 2, 1, 2, 8, 7, 2, 6, 9, 8, 4, 9]
A = [0] * len(T)
print(sumSort(T, A, 6))

for i in range(6):
    s = 0
    for j in range(6*i, 6*(i+1)):
        s += A[j]
    print(f"[{i}]: {s}")