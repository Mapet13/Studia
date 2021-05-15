def reverse(G):
    G_new = {key:[] for key in G.keys()} 
    
    for v in G.keys():
        for u in G[v]:
            G_new[u].append(v)

    return G_new    

def get_strong_connected_components(G):
    time = 0
    time_array = {key:0 for key in G.keys()} 
    visited = {key:False for key in G.keys()}
    
    def DFSVisit(G, u, visited, action):
        visited[u] = True
                
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v, visited, action)
                
        action(u) 
        
    def time_action(u):
        nonlocal time
        
        time_array[u] = time
        time += 1

    for u in G.keys():
        if not visited[u]:
            DFSVisit(G, u, visited, time_action)
    
    reversed_G = reverse(G)
    visited = {key:False for key in reversed_G.keys()}
    result = []

    for u in sorted(list(reversed_G.keys()), key=time_array.__getitem__, reverse=True):
        if not visited[u]:
            result.append([])
            DFSVisit(reversed_G, u, visited, lambda u: result[-1].append(u))
    
    return result
    
G = {
    "a": ["b"],
    "b": ["c", "d"],
    "c": ["a", "h"],
    "d": ["e", "g"],
    "e": ["f"],
    "f": ["d"],
    "g": ["f"],
    "h": ["j"],
    "i": ["h", "g"],
    "j": ["k"],
    "k": ["i"],
}

print(get_strong_connected_components(G))
