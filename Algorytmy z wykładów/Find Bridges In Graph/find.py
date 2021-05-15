from math import inf

def find_bridges_in_graph(G):    
    time = 0
    time_array = {key:inf for key in G.keys()} 
    low_array = {key:inf for key in G.keys()} 
    visited = {key:False for key in G.keys()}
    parents = {key:None for key in G.keys()}
    
    def DFSVisit(G, u):        
        nonlocal time
        
        visited[u] = True
        time_array[u] = time
        low_array[u] = time
        time += 1
        
        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                DFSVisit(G, v)
                low_array[u] = min(low_array[u], low_array[v])
                
                if low_array[v] > time_array[u]:
                    print(f"{v}, {u}") 
                
            elif v != parents[u]:
                low_array[u] = min(low_array[u], time_array[v])
        

    for u in G.keys():
        if not visited[u]:
            DFSVisit(G, u)
    
G = {
    "f": ["d", "g"],   
    "e": ["a", "c", "h"],   
    "d": ["c", "g", "f"],   
    "c": ["b", "d", "e"],   
    "g": ["d", "f"],   
    "b": ["a", "c"],   
    "h": ["e"],   
    "a": ["b", "e"],   
}
find_bridges_in_graph(G)