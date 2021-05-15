def topological_sort(G):    
    visited = {key:False for key in G.keys()}
    result = []
    
    def DFSVisit(G, u, result):        
        visited[u] = True
        
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v,result)
                
        result.insert(0, u)

    for u in G.keys():
        if not visited[u]:
            DFSVisit(G, u, result)
                        
    return result
                

    
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

print(topological_sort(G))