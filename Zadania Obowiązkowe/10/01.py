from math import inf
from queue import PriorityQueue

def decreasing_edges_path(G, s, t):
    parents = [[-1 for _ in range(len(G))] for _ in range(len(G))]
    dist_last = inf
    target_last = -1
    
    for v in G:
        v.sort(key=lambda x: x[1], reverse=True)
        
    queue = PriorityQueue()    
    queue.put((0, inf, -1, s)) # odleglosc od startu, waga ostatniej krawędzi którą weszlismy do wieszchołka, ostatni wieszchołek, wieszchołek 
    
    while not queue.empty():
        dist, last_weight, last, v = queue.get()

        if v == t:
            dist_last = dist 
            target_last = last
            break

        for i in range(len(G[v]) - 1, -1, -1):
            if G[v][i][1] >= last_weight: break # aby wchodzic tylko w krawędzie mniejsze
            queue.put((dist + G[v][i][1], G[v][i][1], v, G[v][i][0])) 
            parents[G[v][i][0]][v] = last 
            G[v].pop() # O(1)

    result = []
    
    if dist_last != inf:
        result.append(t)
        result.append(target_last)
        while parents[t][target_last] != -1:
            result.append(parents[t][target_last])
            t, target_last = target_last, parents[t][target_last]
        result.reverse()
        
    return (result, dist_last)
    

# ([0, 2, 4, 3], 12)
G = [
    [(1, 10), (2, 5)],
    [(0, 10), (2, 1), (3, 3), (4, 2)],
    [(0, 5), (1, 1), (3, 6), (4, 4)],
    [(1, 3), (2, 6), (4, 3), (5, 2)],
    [(1, 2), (2, 4), (3, 3), (5, 1)],
    [(3, 2), (4, 1)]
]
print(decreasing_edges_path(G, 0, 3))