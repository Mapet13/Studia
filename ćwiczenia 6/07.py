'''
Dany jest zestaw odważników T[N]. 
Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy. 
Odważniki można umieszczać tylko na jednej szalce.
'''
def can_weigh(t, x, i = 0):
    if x == 0:
        return True
    if i == len(t) or x < 0: 
        return False
    return can_weigh(t, x - t[i], i + 1) or can_weigh(t, x, i + 1) 


t = [1, 3, 5, 10, 16, 24]
print(can_weigh(t, 23))

t = [1, 3, 5, 10, 16, 23]
print(can_weigh(t, 23))
