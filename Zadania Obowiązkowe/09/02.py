'''
zgrubsza chodzi o znalezienie takich dwuch wieszchołkow ktore sasiaduja 
z dwoma niesoasiadujacymi wieszchołkami
'''

def get_circut_length_4(G):
    N = len(G)
    A = [[-1] * N for _ in range(N)]
              
    for v in range(N):
        for u in range(N):
            if G[v][u] == 1:
                for z in range(u+1, N):
                    if G[v][z] == 1:
                        if A[u][z] != -1: return [(v, u), (u, A[u][z]), (A[u][z], z), (z, v)] 
                        else: A[u][z] = v
    
    



M = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
]

print(get_circut_length_4(M))