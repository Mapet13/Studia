def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

'''
usuniecie rekurencji ogonowej w taki sposob ze wywołuje rekurncje tylko na mniejszej z tych tablic
powoduje to ze wywołanie rekurencyjne zawsze bedzie wywoływane na przynajmneij o połowe mniejszej częsci tablicy, 
ergo tych wywołan rekurencyjnych nie bedzie wiecej niz log2(n)
'''
def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        
        if (q - 1 - p) < (r - (q + 1)):
            quick_sort(A, p, q-1)
            p = q+1
        else:
            quick_sort(A, q+1, r)
            r = q-1
            
            
T = [2, 1, 3, 7, 6, 9, 1, 3]
quick_sort(T, 0, len(T)-1)
print(T)

T = [1, 2, 3, 4, 5, 6, 7, 9, 10]
quick_sort(T, 0, len(T)-1)
print(T)