'''
Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych wartościami typu float. 
Proszę napisać funkcję, która zwróci najmniejszą odległość 
między środkami ciężkości 2 niepustych podzbiorów tego zbioru.
'''

#tuple
def add(a, b):
    return (a[0]+b[0], a[1] + b[1])

def get_dis(p0, p1):
    return ((p0) ** 2 + (p1) ** 2) ** 0.5

def get_distance_of_closest_centers(T, i = 0, s1 = (0, 0), c1 = 0, s2 = (0, 0), c2 = 0):   
    current = float("inf")
    if c1 != 0 and c2 != 0:
        current = get_dis((s1[0] / c1 - s2[0] / c2), (s1[1] / c1 - s2[1] / c2))
    
    if i == len(T):
        return current
    
    return min(current, 
                get_distance_of_closest_centers(T, i + 1, s1, c1, s2, c2),
                get_distance_of_closest_centers(T, i + 1, add(s1, T[i]), c1 + 1, s2, c2),
                get_distance_of_closest_centers(T, i + 1, s1, c1, add(s2, T[i]), c2 + 1))
  

T = [
    (1.0, 1.0),
    (2.0, 2.0),
]
print(get_distance_of_closest_centers(T))


T = [
    (1.1, 1.2),
    (-3.7, 11.2),
    (-22.7, 0.2),
    (9.7, -13.2),
    (9.7, -1.2),
]
print(get_distance_of_closest_centers(T))