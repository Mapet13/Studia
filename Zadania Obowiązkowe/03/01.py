'''
sortowanie n liczb z zakresu 0..(n^2-1)
'''

from random import randint
from timeit import default_timer as timer

# działa jak radix sort ale na liczbach o podstawie n
# wtedy beda potrzebne tylko 2 wywołania count sorta
# egro:
# 2 razy wywołamy algorytm sotowania o złożonosci czasowej O(n+k) i pamieciowej O(n + k)
# wiec złozonosc czawowa ostatecznie algorytmu bedzie liniowa
def sort(T):
    n = len(T)
    countsort(T, n, 1)
    countsort(T, n, n)
    
# zwykły count sort z taka roznica ze jest przekazany jeszcze argument x
# jest potrzebny do wyznaczenia wzgledem jakiej cyfry działamy
def countsort(A, k, x): 
    C = [0] * k
    B = [0] * len(A)
    
    for i in range(len(A)):
        C[(A[i] // x) % k] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[(A[i] // x) % k] -= 1
        B[C[(A[i] // x) % k]] = A[i]
    for i in range(len(A)):
        A[i] = B[i]
    

N = int(input("N: "))
measurements = []
for _ in range(100):
    T = [randint(0, (N**2)-1) for _ in range(N)]
    #print(T)
    start = timer()
    sort(T)
    end = timer()
    #print(T)

    for i in range(len(T)-1):
        if T[i] > T[i+1]:
            print("Błąd sortowania!")
            exit()
        

    measurements.append(end-start)

print(f"avrage time: {sum(measurements) / len(measurements) }")
print(f"max time: {max(measurements) }")
print(f"min time: {min(measurements) }")
