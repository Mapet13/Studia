from collections import deque


class Vertex:
    def __init__(self, i):
        self.i = i
        self.visited = False
        self.d = -1
        self.parent = None


def zad_3(G, s, t):
    V, E = G
    Q = deque()
    s = V[s]
    s.d = 0
    s.visited = True
    Q.append(s)
    done = False
    result = deque()
    while len(Q) > 0:
        u = Q.popleft()
        if u.i == t:
            while u.i is not None:
                result.appendleft(u.i)
                u = u.parent
        if done:
            break
        for neighbour in E[u.i]:
            if not V[neighbour].visited:
                V[neighbour].visited = True
                V[neighbour].d = u.d + 1
                V[neighbour].parent = u
                Q.append(V[neighbour])
    if len(result) > 0:
        print(result)
    else:
        print(None)
