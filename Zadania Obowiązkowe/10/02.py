def get_transitive_closure(G):
    n = len(G)
    R = [[0] * n for _ in range(n)]
    visited = [False] * n
    
    def DFSVisit(G, u):
        visited[u] = True
        
        for v in range(n):
            if G[u][v]:
                R[u][v] = 1
                if not visited[v]:
                    DFSVisit(G, v)
                for z in range(n):
                    if R[v][z]:
                        R[u][z] = 1
                    
    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)
                        
    
    return R

G = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
]

T = get_transitive_closure(G)

for x in T:
    print(x)