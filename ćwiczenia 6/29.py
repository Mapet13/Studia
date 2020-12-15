'''
Punkt leżący w przestrzeni jest opisywany trójką liczb typu float (x,y,z). 
Tablica T[N] zawiera współrzędne N punktów leżących w przestrzeni. 
Punkty posiadają jednostkową masę. 
Proszę napisać funkcję, która sprawdza czy istnieje podzbiór punktów liczący co najmniej 3 punkty, 
którego środek ciężkości leży w odległości nie większej niż r od początku układu współrzędnych. 
Do funkcji należy przekazać tablicę T oraz promień r, funkcja powinna zwrócić wartość typu bool.
'''

def get_distance(p):
    return (p[0]**2 + p[1]**2 + p[2]**2)**0.5

def add(current, cd):
    return (
        current[0] +cd[0], 
        current[1] +cd[1], 
        current[2] +cd[2]
    )
    
def divide(vec, a):
    return (
        vec[0] / a, 
        vec[1] / a, 
        vec[2] / a
    )

def func(T, r, i = 0, current_center = (0, 0, 0), d = 0):
    if d >= 3 and get_distance(divide(current_center, d)) <= r:
        return True
    if i >= len(T) or i > len(T) - (3-d):
        return False
    
    return func(T, r, i+1, current_center, d) or func(T, r, i+1, add(current_center, T[i]), d+1) 

tab = [
    (0, 0, 0),
    (0, 0, 0),
    (100, 100, 0),
    (100, 100, 1),
    (100, 100, 1),
    (100, 100, 1),
    (100, 100, 1),
]
print(func(tab, 1))

tab = [
    (0, 0, 0),
    (0, 0, 0),
    (100, 100, 0),
    (100, 100, 1),
    (100, 100, 1),
    (100, 100, 1),
    (100, 100, 1),
    (0, 1, 0.1)
]
print(func(tab, 1))