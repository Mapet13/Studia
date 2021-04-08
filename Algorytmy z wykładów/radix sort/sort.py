def countsort(A, idx): 
    C = [0] * (ord('z') - ord('a'))
    B = [0] * len(A)
    
    for i in range(len(A)):
        C[ord(A[i][idx]) - ord('a')] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[ord(A[i][idx]) - ord('a')] -= 1
        B[C[ord(A[i][idx]) - ord('a')]] = A[i]
    for i in range(len(A)):
        A[i] = B[i]

def radixsort(A, len): 
    for i in range(len-1, -1, -1):
        countsort(A, i)
        print(f"idx = {i}; {A}")


T = ["kra", "art", "kot", "kit", "ati", "kil"]
radixsort(T, 3)
print(T)