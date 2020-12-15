'''
Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). 
Tablica T[N] zawiera współrzędne N punktów leżących na płaszczyźnie. 
Punkty posiadają jednostkową masę. 
Proszę napisać funkcję, która sprawdza czy istnieje niepusty podzbiór n punktów,
gdzie n¡k oraz n jest wielokrotnością liczby 3, 
którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. 
Do funkcji należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, 
funkcja powinna zwrócić wartość typu bool.
'''

def get_distance(p):
    return (p[0]**2 + p[1]**2)**0.5

def add(current, cd):
    return (
        current[0] +cd[0], 
        current[1] +cd[1]
    )
    
def divide(vec, a):
    return (
        vec[0] / a, 
        vec[1] / a
    )

def func(T, r, k, i = 0, current_center = (0, 0, 0), d = 0):
    if d >= k:
        return False

    if d >= 3  and d % 3 == 0 and get_distance(divide(current_center, d)) <= r:
        return True
    if i >= len(T) or i > len(T) - (3-d):
        return False
    
    return func(T, r, k, i+1, current_center, d) or func(T, r, k, i+1, add(current_center, T[i]), d+1) 

tab = [
    (0, 0, 0),
    (0, 0, 0),
    (100, 100, 0),
    (100, 100, 1),
    (100, 100, 1),
    (100, 100, 1),
    (100, 100, 1),
]
print(func(tab, 1, 5))

tab = [
    (0, 0),
    (0, 0),
    (100, 100),
    (100, 100),
    (100, 100),
    (100, 100),
    (100, 100),
    (0, 1)
]
print(func(tab, 1, 3))

tab = [
    (0, 0),
    (0, 0),
    (100, 100),
    (100, 100),
    (100, 100),
    (100, 100),
    (100, 100),
    (0, 1)
]
print(func(tab, 1, 4))