from queue import PriorityQueue

def find(x, Parent):
    if x != Parent[x]:
        Parent[x] = find(Parent[x],Parent)
    return Parent[x]

def union(x, y, Parent, Rank):
    x = find(x, Parent)
    y = find(y,Parent)
    
    if x == y: return False
    
    if Rank[x] > Rank[y]:
        Parent[y] = x
    else:
        Parent[x] = y
        if Rank[x] == Rank[y]:
            Rank[y] += 1 
    
    return True

def Kruskal(G):
    E = PriorityQueue()    
    
    for i in range(len(G)):
        for e in G[i]:
            if e[0] > i:
                E.put((e[1], i, e[0]))
    
    A = []
    parent = [i for i in range(len(G))]
    rank = [0] * len(G)
    while not E.empty():
        x = E.get()
        if union(x[1], x[2], parent, rank):
            A.append((x[1], x[2]))
    
    return A

def Kruskal_matrix(G):
    E = PriorityQueue()    
    
    for i in range(len(G)):
        for j in range(i+1, len(G)):
            if (G[i][j] > 0):
                E.put((G[i][j], i, j))
    
    A = []
    parent = [i for i in range(len(G))]
    rank = [0] * len(G)
    while not E.empty():
        x = E.get()
        if union(x[1], x[2], parent, rank):
            A.append((x[1], x[2]))
    
    return A
        
        
G = [
    [(2, 7), (4, 1)],
    [(4, 4),(3, 5), (5, 6)],
    [(0, 7), (3, 2), (5, 3), (4, 8)],
    [(2, 2), (1, 5)],
    [(0, 1), (1, 4), (5, 12), (3, 8)],
    [(4, 12), (1, 6), (2, 3)],   
]
A = Kruskal(G)
for x in A:
    print(x)
    
print("-----------")    
    
G = [
    [0, 0, 7, 0, 1, 0],  
    [0, 0, 0, 5, 4, 6],  
    [7, 0, 0, 2, 8, 3],  
    [0, 5, 2, 0, 0, 0],  
    [1, 4, 8, 0, 0, 12],  
    [0, 6, 3, 0, 12, 0],  
]
A = Kruskal_matrix(G)
for x in A:
    print(x)