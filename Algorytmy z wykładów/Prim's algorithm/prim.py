from math import inf
from queue import PriorityQueue

def prim(G):
    parent = [None] * len(G)
    visited = [False] * len(G)
    value = [inf] * len(G)
    
    V = PriorityQueue()    
    V.put((0, 0))
    
    S = []
    
    while not V.empty():
        _, t = V.get()
        if not visited[t]:
            
            if t != 0: S.append((t, parent[t])) 
            
            visited[t] = True
            for e in G[t]:
                if e[1] < value[e[0]]:
                    value[e[0]] = e[1]
                    parent[e[0]] = t
                    V.put((value[e[0]], e[0]))

    return S

G = [
    [(2, 7), (4, 1)],
    [(4, 4),(3, 5), (5, 6)],
    [(0, 7), (3, 2), (5, 3), (4, 8)],
    [(2, 2), (1, 5)],
    [(0, 1), (1, 4), (5, 12)],
    [(4, 12), (1, 6), (5, 12)],   
]
A = prim(G)
for x in A:
    print(x)
    
    
