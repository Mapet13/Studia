'''
Proszę zaimplementować funkcję, 
która mając na wejściu tablicę n elementów oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań.
''' 

def find_min_max(T):
    n = len(T)
    
    min_el = T[0] 
    max_el = T[0] 
    
    for i in range(1, n-1, 2):
        if T[i] < T[i+1]:
            min_el = min(min_el, T[i])
            max_el = max(max_el, T[i+1])
        else:
            min_el = min(min_el, T[i+1])
            max_el = max(max_el, T[i])
    
    if n % 2 == 0:
        min_el = min(min_el, T[n-1])
        max_el = max(max_el, T[n-1])

    return min_el, max_el

T1 = [61, 0, 1, 61, 88, -86, 17, 7, 188, 1, 7, 17]
T2 = [61, 0, 1, 61, 88, -86, 17, 7, 188, 1, 7, 17, 999]
T3 = [61, 0, 1, 61, 88, -86, 17, 7, 188, 1, 7, -777]

print(find_min_max(T1))
print(find_min_max(T2))
print(find_min_max(T3))