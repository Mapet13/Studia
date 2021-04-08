from math import ceil, log2

def radixsort(A):
    n = len(A)

    t = [(0,0,0)]*n
    for i in range(0,n):
        t[i] = (A[i], A[i]//n, A[i]%n)
    
    countsort(t, 2)
    countsort(t, 1)

    for i in range(0, n):
        A[i] = t[i][0]
    
def sortowanie(array):
    uniq = [0] * ceil(log2(n))
    cnt = [0] * ceil(log2(n))
    uniq[0] = array[0]
    uniq_size = 1
    for i in range(1, n):
        if binary_search(uniq, array[i], uniq_size) < 0:
            insert(uniq, array[i]) 
            uniq_size += 1
    for i in range(n):
        x = binary_search(uniq, array[i], len(uniq)-1)
        cnt[x] += 1
    index = i = j = 0
    while index < n:
        if cnt[i] != 0:
            array[index] = uniq[i]
            cnt[i] -= 1
            index += 1
        else:
            i += 1


def partition(T, l, r):
    i = l-1
    j = r
    p = l-1
    q = r
    pivot = T[r]
    while i < j:
        i += 1
        while T[i] < pivot:
            i += 1
        j -= 1
        while T[j] > pivot:
            j -= 1
        if i < j:
            T[i], T[j] = T[j], T[i]
            if T[i] == pivot:
                p += 1
                T[p], T[i] = T[i], T[p]
            if T[j] == pivot:
                q -= 1
                T[q], T[j] = T[j], T[q]
    T[r], T[i] = T[i], T[r]

    if T[j] != pivot:
        for k in range(l, p+1):
            T[k], T[j] = T[j], T[k]
            j -= 1
    else: j = l

    i += 1
    if T[i] != pivot:
        for k in range(r-1, q-1, -1):
            T[k], T[i] = T[i], T[k]
            i += 1
    else: i = r

    return j, i


def quickerSort(T, l, r):
    if l < r:
        i, j = partition(T, l, r)
        if i > l:
            quickerSort(T, l, i)
        if j<r:
            quickerSort(T, j, r)


def anagram(A, B, k):
    letter = [0]*k
    for i in range(len(A)):
        letter[A[i]] = 0
        letter[B[i]] = 0
    
    for i in range(len(A)):
        letter[A[i]] += 1
        letter[B[i]] -= 1
        
    for i in range(len(A)):
        if letter[A[i]] != 0:
            return False
    return True

def kolory(A):
    k = [0 for _ in range(k)]
    l = k
    i = 0
    j = 0
    wyn = len(A)
    p =(0,len(A)-1)
    while(j<len(A)):
        if k[A[j]] == 0:
            l -= 1
        k[A[j]] += 1
        if l == 0:
            while k[A[i]] > 1:
                k[A[i]] -= 1
                i+=1
            if wyn > j-i:
                wyn = j-i
                p = (i,j)
        j += 1

    if l == 0:
        return p
    return 