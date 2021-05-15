def DFS(G):
    # G = (V, E)
    
    for v in G.V:
        v.visited = False
        v.parent = None
        
    time = 0
    
    for u in G.V:
        if not u.visited:
            DFSVisit(G, u)
                        
    def DFSVisit(G, u):
        nonlocal time
        
        time += 1
        u.visited = True
        
        for v in u.neighbors:
            if not v.visited:
                v.parent = u
                DFSVisit(G, v)
                
        time += 1
    
    