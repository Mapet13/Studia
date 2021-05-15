
def get_euler_circuit(G):
    result = []
    
    def DFSVisit(G, u, result):        
        for v in G[u]:
            G[u].remove(v)
            if u != v: G[v].remove(u)
            DFSVisit(G, v, result)
        result.append(u)
                

    DFSVisit(G, list(G.keys())[0], result)
                 
    return result

G = {
    "a": ["b", "e"],
    "b": ["a", "e", "c", "f"],
    "c": ["b", "e", "f", "d"],
    "d": ["c", "f"],
    "e": ["a", "b", "f", "c"], 
    "f": ["d", "b", "e", "c"], 
}
print(get_euler_circuit(G))

G = {
    "a": ["b", "c"],
    "b": ["a", "c", "e", "d"],
    "c": ["a", "b"],
    "d": ["b", "e"],
    "e": ["d", "b"], 
}
print(get_euler_circuit(G))