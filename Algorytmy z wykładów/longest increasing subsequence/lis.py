def lis(A):
    N = len(A)
    F = [1] * N
    P = [-1] * N
    
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
    
    return max(F), F, P

def print_solution(A, P, i):
    if P[i] != -1:
        print_solution(A, P, P[i])
    print(A[i])
    
A = [13, 7, 21, 42, 8, 2, 44, 53]
_, F, P = lis(A)
max_index = max(range(len(F)), key=A.__getitem__)
print_solution(A, P, max_index)
