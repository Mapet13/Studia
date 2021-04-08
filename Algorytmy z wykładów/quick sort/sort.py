def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def quick_sort2(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort2(A, p, q-1)
        p = q+1

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
            
T = [2, 1, 3, 7, 6, 9, 1, 3]
quick_sort(T, 0, len(T)-1)
print(T)

T = [2, 1, 3, 7, 6, 9, 1, 3]
quick_sort2(T, 0, len(T)-1)
print(T)
    
    