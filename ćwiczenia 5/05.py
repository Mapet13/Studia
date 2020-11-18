'''
Dany jest zbiór punktów leżących na płaszczyźnie 
opisany przy pomocy struktury dane = [(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] 
Proszę napisać funkcję, która zwraca  wartość True jeżeli zbiorze istnieją 4 punkty 
    wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, 
    a wewnątrz tego kwadratu nie ma żadnych innych punktów. 
Do funkcji należy przekazać strukturę opisującą położenie punktów.
'''

def is_between_points(x, a, b):
    return (x >= a and x <= b) or (x <=  a and x >= b)

def is_point_in_square(p, a, b, c, d):
    if is_between_points(p[1], a[1], b[1]):
        if is_between_points(p[0], a[0], c[0]):
            return True
    return False
        

def does_square_exist(t):
    n = len(t)
    
    for i in range(n):
        a = t[i] # wubieram 1 pkt
        
        for j in range(i+1, n): # moge tak bo dla wczesniejszych juz sprawdziłem równoległość z A (na osi X)
            b = t[j]
            
            if b[0] == a[0] and b[1] != a[1]:
                for k in range(n):
                    if k != i and k != j:
                        c = t[k]
                        if c[0] != a[0]:
                            c_is_close_to_a = None
                            if c[1] == a[1]: 
                                c_is_close_to_a = True
                            elif c[1] == b[1]: 
                                c_is_close_to_a = False
                            else:
                                continue
                            for g in range(k+1, n):
                                d = t[g]
                                if d[0] == c[0]:
                                    if (c_is_close_to_a and d[1] == b[1]) or (not c_is_close_to_a and d[1] == a[1]):
                                        # w tym miejscu juz wiem że mam kwadrat ale musze sprawdzić punkty
                                        all_points_outside_square = True
                                        for x in range(n):
                                            if x != i and x != j and x != k and x != g:
                                                if is_point_in_square(t[x], a, b, c, d):
                                                    all_points_outside_square = False
                                                    break
                                        if all_points_outside_square:
                                            print(a, b, c, d)
                                            return True
            
    return False
                                        
print(does_square_exist([ # (0, 4) (2, 4) (2, 6) (0, 6)
    (0, 4),
    (0, 6),
    (2, 4),
    (2, 6)
]))

print(does_square_exist([ # False
    (0, 4),
    (0, 6),
    (2, 4),
    (2, 6),
    (0, 6)
]))

print(does_square_exist([ # False
    (0, 4),
    (0, 6),
    (2, 4),
    (2, 6),
    (1, 6),
]))

print(does_square_exist([ # False
    (0, 4),
    (0, 6),
    (2, 4),
    (2, 6),
    (1, 5)
]))

print(does_square_exist([ #(0, 4) (-1, 4) (-1, 3) (0, 3)
    (0, 4),
    (0, 6),
    (2, 4),
    (2, 6),
    (1, 5),
    (0, 3),
    (-1, 3),
    (-1, 4)
]))

print(does_square_exist([ # (-3, -3) (-1, -3) (-1, -1) (-3, -1)
    (-1, -1),
    (-3, -1),
    (-3, -3),
    (-1, -3)
]))
