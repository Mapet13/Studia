class node:
    def __init__(self, ind, next=[]):
        self.ind = ind
        self.next = next
        self.visited = False


G = [node(0, [1, 2]), node(1, [0, 2]), node(2, [0, 1]), node(3, [])]


def DFS(v, G):
    if G[v].visited:
        return

    G[v].visited = True
    for u in G[v].next:
        if not G[u].visited:
            DFS(u, G)


def spojneSkladowe(G):
    q = [u.ind for u in G]
    skladowe = 0
    while len(q) != 0:
        DFS(q[0], G)
        q = [u for u in q if not G[u].visited]
        skladowe += 1

    return skladowe


print(spojneSkladowe(G))