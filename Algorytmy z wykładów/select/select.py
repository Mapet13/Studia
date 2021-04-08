def select(A, p, r, k):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    if q == k:
        return A[q]
    elif k < q:
        return select(A, p, q-1, k)
    else:
        return select(A, q+1, r, k)
        