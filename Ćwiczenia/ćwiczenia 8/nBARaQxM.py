class Vertex:
    def __init__(self, number):
        self.number = number
        self.visited = False
        self.parent = None
        self.left = None
        self.right = None


def DFS(Graph):
    n = len(Graph)
    V = [Vertex(i) for i in range(n)]
    DFSVisit(Graph, V, V[0])
    deleteNode(V[0])


def DFSVisit(Graph, V, v):
    n = len(Graph)
    v.visited = True
    for i in range(n):
        if not V[i].visited and Graph[v.number][i] == 1:
            V[i].parent = v
            if v.left is None:
                v.left = V[i]
            elif v.right is None:
                v.right = V[i]
            DFSVisit(Graph, V, V[i])


def deleteNode(root):
    if root is not None:
        deleteNode(root.left)
        deleteNode(root.right)
        print(root.number)
