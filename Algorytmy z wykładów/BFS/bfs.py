def BFS(G, s):
    # G = (V, E), s is in V
    
    Q = []
    for v in G.V:
        v.visited = False
        v.d = -1
        v.parent = None
        
    s.d = 0
    s.visited = True
    Q.append(s)
    
    while len(Q) > 0:
        u = Q.pop(0)
        for v in u.neighbors:
            if not v.visited:
                v.visited = True
                v.d = u.d + 1
                v.parent = u
                Q.append(v)
    

G = {
    "a": ["b", "c"],
    "b": ["c", "e"],
    "c": [],
    "d": [],
    "e": ["d", "g", "f"], 
    "f": [], 
    "g": [], 
    "h": ["e"], 
    "i": ["h"],  
}