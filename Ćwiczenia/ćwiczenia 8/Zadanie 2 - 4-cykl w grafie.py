def cycle_of_4(G):
    n = len(G)
    H = [[0]*n for _ in range(n)]
    edge_list = [[] for _ in range(n)]

    def get_cycle(a: int, b: int, x: int):
        for a_neigh in edge_list[a]:
            if a_neigh == x:
                continue
            if b in edge_list[a_neigh]:
                return x, a, a_neigh, b

    for v in range(n):
        for u in range(n):
            if G[v][u]:
                edge_list[v].append(u)

    for v in range(n):
        for n1 in range(1, len(edge_list[v])):
            for n2 in range(n1):
                if H[edge_list[v][n1]][edge_list[v][n2]] == 1:
                    return get_cycle(edge_list[v][n1], edge_list[v][n2], v)
                H[edge_list[v][n1]][edge_list[v][n2]] = 1

    return None


G = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0]
]

print(["ABCDEFGHIJKLM"[i] for i in cycle_of_4(G)])