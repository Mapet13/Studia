def czy_dwudzielny(G):
    Q = []
    color = [None for _ in range(len(G))]
    color[0] = True
    Q.append(0)
    while Q:
        s = Q.pop(0)
        for v in G[s]:
            if v != s:
                if color[v] == None:
                    Q.append(v)
                    color[v] = not color[s]
                elif color[v] == color[s]:
                    return False
    return True
