'''
check if graph is bipartite
'''

def is_bipartite(G):
    visited = [0] * len(G)
        
    s = 0
    while 0 in visited:
        while visited[s] != 0: s += 1
        
        Q = []
            
        visited[s] = 1
        Q.append(s)    

        while len(Q) > 0:
            u = Q.pop(0)
            for v in G[u]:
                if visited[v] == visited[u]:
                    return False
                if visited[v] == 0:
                    visited[v] = visited[u] * -1
                    Q.append(v)
                
    return True
    
G = [
    [3],
    [2, 4],
    [1],
    [0, 4],
    [1, 3]
]
print(is_bipartite(G)) # T

G = [
    [3],
    [2, 4],
    [1, 4],
    [0, 4],
    [1, 3, 2]
]
print(is_bipartite(G)) # F

G = [
    [1, 3, 4],
    [2, 5, 6],
    [],
    [],
    [],
    [],
    []
]
print(is_bipartite(G)) # T

G = [
    [1, 3, 4],
    [2, 5, 6],
    [],
    [],
    [],
    [],
    [5]
]
print(is_bipartite(G)) # F

G = [
    [3],
    [2],
    [1],
    [0],
    [5, 6],
    [4, 6],
    [5, 4]
]
print(is_bipartite(G)) # F

G = [
    [3],
    [2],
    [1],
    [0],
    [5, 6],
    [4],
    [4]
]
print(is_bipartite(G)) # T

G = [
    [],
    [2],
    [1],
    [],
    [5, 6],
    [4],
    [4]
]
print(is_bipartite(G)) # T

G = [
    [],
    [2],
    [1],
    [],
    [5, 6],
    [4, 6],
    [5, 4]
]
print(is_bipartite(G)) # F
