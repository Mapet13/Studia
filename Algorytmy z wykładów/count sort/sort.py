def countsort(A, k): 
    C = [0] * k
    B = [0] * len(A)
    
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(len(A)):
        A[i] = B[i]


T = [2, 1, 3, 7, 6, 9, 1, 3]
countsort(T, 10)
print(T)