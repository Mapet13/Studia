def LIS(self, A):
    tails = [0] * len(A)
    size = 0
    for x in A:
        i, j = 0, size
        while i != j:
            m = (i + j)/2
            if(tails[m] < x):
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i+1, size)
    return size


A = [5, 2, 7, 8, 6, 2, 1, 5, 3]

print(LIS(A))