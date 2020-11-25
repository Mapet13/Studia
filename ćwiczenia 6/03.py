'''
Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
polu startowym i ostatnim także wliczamy do kosztu przejścia.
'''

def get_min_cost(t, k, w = 0, cost = 0):
    cost += t[w][k] # aktualny
    
    if w == 7:
        return cost
    
    next_cost = get_min_cost(t, k, w+1, cost)
    if k - 1 >= 0:
        next_cost = min(next_cost, get_min_cost(t, k-1, w+1, cost))
    if k + 1 < 8:
        next_cost = min(next_cost, get_min_cost(t, k+1, w+1, cost))  
    return next_cost
    
t = [
    [1, 0, 1, 1, 1, 1, 1, 1],
    [0, 2, 2, 2, 2, 2, 2, 2],
    [3, 0, 3, 3, 3, 3, 3, 3],
    [4, 4, 0, 4, 4, 4, 4, 4],
    [5, 5, 0, 5, 5, 5, 5, 5],
    [6, 0, 6, 6, 6, 6, 6, 6],
    [7, 7, 0, 7, 7, 7, 7, 7],
    [8, 8, 8, 0, 8, 8, 8, 8],
]
print(get_min_cost(t, 1))

t = [
    [1, 100, 1, 1, 1, 1, 1, 1],
    [0, 2, 2, 2, 2, 2, 2, 2],
    [3, 0, 3, 3, 3, 3, 3, 3],
    [4, 4, 0, 4, 4, 4, 4, 4],
    [5, 5, 0, 5, 5, 5, 5, 5],
    [6, 0, 6, 6, 6, 6, 6, 6],
    [7, 7, 0, 7, 7, 7, 7, 7],
    [999, 999, 999, 100, 999, 999, 999, 999],
]
print(get_min_cost(t, 1))

t = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 2, 2, 2, 2, 0, 1, 2],
    [3, 3, 3, 3, 0, 3, 3, 1],
    [4, 4, 4, 4, 4, 0, 1, 4],
    [5, 5, 5, 5, 0, 5, 5, 1],
    [6, 6, 6, 0, 6, 6, 1, 6],
    [7, 7, 7, 7, 0, 7, 7, 1],
    [8, 8, 8, 9, 9, 9, 1, 8],
]
print(get_min_cost(t, 6))

t = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 2, 2, 2, 2, 0, 1, 2],
    [3, 3, 3, 3, 0, 3, 3, 1],
    [4, 4, 4, 4, 4, 0, 1, 4],
    [5, 5, 5, 5, 0, 5, 5, 1],
    [6, 6, 6, 0, 6, 6, 1, 6],
    [7, 7, 7, 7, 0, 7, 7, 1],
    [8, 8, 8, 9, 9, 9, 3, 8],
]
print(get_min_cost(t, 6))