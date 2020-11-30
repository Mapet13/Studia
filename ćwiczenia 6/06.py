'''
Dana jest tablica T[N].
Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie liczebności) podzbiór elementów tablicy, 
dla którego suma elementów jest równa sumie indeksów tych elementów. 
Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10
'''

def get_min_sum_rec(t, sum_e = 0 , sum_i = 0, count = 0, i = 0):
    if i >= len(t):   
        if sum_e != sum_i or count == 0:
            return (len(t) + 1, 0)
        return (count, sum_e)
    
    a = get_min_sum_rec(t, sum_e + t[i], sum_i + i, count + 1, i + 1)
    b = get_min_sum_rec(t, sum_e, sum_i, count, i + 1)
        
    if a[0] < b[0]:
        return a
    return b

def get_min_sum(t):
    (count, sum_e) = get_min_sum_rec(t)
    if count < len(t):
         return sum_e
     
print(get_min_sum([1,7,3,5,11,2]))