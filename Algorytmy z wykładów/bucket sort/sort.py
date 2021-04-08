from math import floor

def swap(tab, x, y):
    tab[x], tab[y] = tab[y], tab[x]

def insertionsort(T):
    n = len(T)
    
    for i in range(1, n):
        j = i
        while j > 0 and T[j-1] > T[j]: 
            swap(T, j, j-1)
            j -= 1

def bucketsort(A, upper_bound): 
    n = len(A)
    buckets = [[] for _ in range(n)]
    for x in A:
        buckets[floor(x/(upper_bound/n))].append(x)
    for i in range(len(buckets)):
        print(f"bucket [{((upper_bound/n) * i):.2f}, {((upper_bound/n) * (i+1)):.2f}): {buckets[i]}")
        insertionsort(buckets[i])
        
    b_ix = 0
    for i in range(0, n):
        while len(buckets[b_ix]) == 0:
            b_ix += 1
        A[i] = buckets[b_ix].pop(0)
         
    
    

T = [2.2, 1.1, 3.4, 0.1, 8.8, 7.1, 5.3, 6.7, 9.9, 1.98, 3.0, 4.2, 8.1]
bucketsort(T, 10)
print(T)