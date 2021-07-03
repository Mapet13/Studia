# F[i]-minimalna ilosc klockow ktore trzeba usunac z klockow A[0]...A[i], tak zeby wieza konczyla sie na A[i]

def klocki(A):
    n = len(A)
    F = [0] * n
    for i in range(1, n):
        F[i] = i
        for j in range(i-1):
            if A[i][0]>=A[j][0] and A[i][1]<=A[j][1]:
                F[i] = min(F[i], F[i] + i - j - 1)
    result = F[n-1]
    for i in range(n-1):
        result = min(F[i]+n-1-i, result)
    return result