from math import inf

def can_travel(G, x, y):        
    def DFSVisit(G, u, e):                
        for v in range(len(G)):
            if G[u][v] > 0 and G[u][v] < e:
                if v == y: return True
                if DFSVisit(G, v, G[u][v]):
                    return True
        return False
        
    return DFSVisit(G, x, inf)