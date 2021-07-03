def floyd_warshall(T):
    S = [
            [
                0 if (i == j) else 
                T[i][j] if (T[i][j] > 0) else 
                inf 
                for i in range(len(T))
            ] 
        for j in range(len(T))
    ]
    
    for v in range(len(T)):
        for u in range(len(T)):
            for w in range(len(T)):
                S[u][w] = min(S[u][w], S[u][v] + S[v][w])
    
    return S    