class Node:
    def __init__(self, val = None):
        self.rank = 0
        self.value = val
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent) # path compression 
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y: return 
    
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1 
            
a = Node()
b = Node()
c = Node()
d = Node()
e = Node()

union(a, b)
union(c, d)
union(e, a)

print(find(b) == find(e))
print(find(c) == find(e))
print(find(c) == find(d))
print(find(d) == find(a))
print(find(b) == find(a))

union(e, d)
print(find(c) == find(b))
print(find(d) == find(a))

