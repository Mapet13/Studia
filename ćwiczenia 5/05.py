'''
Dany jest zbiór punktów leżących na płaszczyźnie 
opisany przy pomocy struktury dane = [(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] 
Proszę napisać funkcję, która zwraca  wartość True jeżeli zbiorze istnieją 4 punkty 
    wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, 
    a wewnątrz tego kwadratu nie ma żadnych innych punktów. 
Do funkcji należy przekazać strukturę opisującą położenie punktów.
'''


def get_distance_pow(a, b):
    return ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) 

def get_trangle_area(a, b, c):
    return 0.5 * abs(((b[0] - a[0]) * (c[1] - a[1])) - ((b[1] - a[1]) * (c[0] - a[0])))

def are_point_in_square(p, a, b, c, d, area):
    area_with_p = get_trangle_area(a, b, p)
    area_with_p += get_trangle_area(a, c, p)
    area_with_p += get_trangle_area(d, b, p)
    area_with_p += get_trangle_area(d, c, p)
    
    if area_with_p == area:
        return True
    
    return False
        

def does_square_exist(t):
    n = len(t)
    
    for i in range(n):
        a = t[i] # wubieram 1 pkt
        for j in range(i + 1, n):
            if j == i:
                continue
            b = t[j] # wybieram 2 pkt
            side_len = get_distance_pow(a, b) # kwadrat dlugosci bo nie musze dawac sqrt bo po co
            for k in range(n):
                if k == i or k == j:
                    continue
                c = t[k]
                if side_len == get_distance_pow(a, c) and (2 * side_len == get_distance_pow(b, c)): # jesl te 3 pkt tworzą trójkat prostokątny o równych przeciwprostokątnych
                    for g in range(n):
                        if g == i or g == j or g == k:
                            continue
                        d = t[g]
                        if get_distance_pow(d, c) == get_distance_pow(d, b):
                            all_points_outside_square = True
                            for x in range(n):
                                if x != i and x != j and x != k and x != g:
                                    p = t[x]
                                    if are_point_in_square(p, a, b, c, d, side_len): # moge jako pole przesłac side_len bo nie pierwiastkowałem tego wiec to jakby a**a
                                        all_points_outside_square = False
                                        break
                            if all_points_outside_square:
                                print(a, b, c, d)
                                return True
    return False
                                        
print(does_square_exist([ # ((0, 4) (4, 6) (2, 0) (6, 2))
    (0, 4),
    (4, 6),
    (2, 0),
    (6, 2)
]))

print(does_square_exist([ # (4, 6) (6, 2) (0, 4) (2, 0)
    (4, 6),
    (6, 2),
    (2, 0),
    (0, 4)
]))

print(does_square_exist([ # (2, 0) (6, 2) (0, 4) (4, 6)
    (2, 0),
    (6, 2),
    (4, 6),
    (0, 4)
]))

print(does_square_exist([ # false 
    (2, 0),
    (6, 2),
    (4, 4),
    (4, 6),
    (0, 4) 
]))

print(does_square_exist([ # (2, 0) (6, 2) (0, 4) (4, 6)
    (-1, 1),
    (5, 7),
    (1, 5),
    (7, 3),
    (3, 1),
    (2, -1),
    (3, -5),
    (7, 1),
]))

print(does_square_exist([ # false
    (-1, 1),
    (5, 7),
    (1, 5),
    (7, 3),
    (3, 1),
    (5, 5),
    (2, -1),
    (3, -5),
    (7, 1),
]))


