'''
Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), 
gdzie x1, x2, y1, y2 oznaczają proste ograniczające kwadrat x1 < x2, y1 < y2. 
Dana jest tablica T zawierająca opisy N kwadratów. 
Proszę napisać funkcję, która zwraca wartość logiczną 
True, jeśli danej tablicy można znaleźć 13 nienachodzących na siebie kwadratów, których suma pól jest równa 2012 
i False w przeciwnym przypadku.
'''

def get_area(p):
    return (p[1]-p[0]) * (p[4]-p[3])

def does_it_cover_squares(p, T):
    for s in T:
        if ((s[0] <= p[0] and p[0] <= s[1] or
            s[0] <= p[1] and p[1] <= s[1]) 
            and
            (s[3] <= p[3] and p[3] <= s[4] or
            s[3] <= p[4] and p[4] <= s[4])):
                return True
    return False

def can_find_squares(T, i = 0, t = 0, p = 2012):
    if len(t) == 13:
        return p == 0
    
    if i >= len(T) or p <= 0 or len(t) + (len(T) - i - 1) < 13:
        return False
    
    res = can_find_squares(T, i+1, t, p)
    
    if not res and not does_it_cover_squares(T[i], t):
        res = can_find_squares(T, i+1, t + [T[i]], p - get_area(T[i]))
    
    return res