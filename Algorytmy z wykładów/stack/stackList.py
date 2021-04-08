class Node:
    def __init__(self, next = None, val = None):
        self.next = next
        self.value = val
        

class StackList:
    def __init__(self):
        self.top = Node(None, None)
    
    def push(self, x):
        node = Node(self.top, x)
        self.top = node    
    
    def pop(self):
        if not self.is_empty():
            node = self.top
            self.top = self.top.next
            return node.value
        return None
    def is_empty(self):
        return self.top.next is None


s = StackList()
print(s.pop())

s.push(100)
print(s.pop())

for i in range(5):
    s.push(i)
while not s.is_empty():
    print(s.pop())