'''
Dany jest spójny graf nieskierowany G = (V,E). Proszę
zaproponować algorytm, który znajdzie taką kolejność usuwania
wierzchołków, która powoduje że w trakcie usuwania graf nigdy nie
przestaje być spójny (usunięcie wierzchołka usuwa, oczywiście, wszystkie
dotykające go krawędzie).
'''

from math import inf

def get_removing_order(G):    
    visited = {key:False for key in G.keys()}
    result = []
    
    def DFSVisit(G, u):        
        visited[u] = True
        
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)

        result.append(u)
        

    for u in G.keys():
        if not visited[u]:
            DFSVisit(G, u)
            
    return result
    
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
print(get_removing_order(G))


# from math import inf

# def get_removing_order(G):    
#     visited = [False] * len(G)
#     result = []
    
#     def DFSVisit(G, u):        
#         visited[u] = True
        
#         for v in G[u]:
#             if not visited[v]:
#                 DFSVisit(G, v)

#         result.append(u)
        

#     for u in range(len(G)):
#         if not visited[u]:
#             DFSVisit(G, u)
            
#     return result
    
# G = [
#     [1, 4],   
#     [0, 2],   
#     [1, 3, 4],   
#     [2, 6, 5],   
#     [0, 2, 7],   
#     [3, 6],   
#     [3, 5],   
#     [4],   
# ]
# print(get_removing_order(G))