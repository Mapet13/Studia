'''
Dana jest posortowana tablica A[1...n] oraz liczba x. 
Proszę napisać program, który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.
'''

def find_sum(A, x):
    n = len(A)
    
    i = 0
    j = n-1
    
    
    while j >= i:
        while A[i] + A[j] > x and j >= i:
            j -= 1
            
        while A[i] + A[j] < x and j >= i:
            i += 1
        
        if A[i] + A[j] == x:
            return i, j
    
    return None


T = [2, 4, 6, 7, 8, 10, 12]
print(find_sum(T, 15))

T = [2, 4, 6, 8, 10, 12]
print(find_sum(T, 15))
            
            