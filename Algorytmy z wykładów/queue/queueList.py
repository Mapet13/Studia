class Node:
    def __init__(self, next = None, val = None):
        self.next = next
        self.value = val

class QueueList:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
    
        
    def deque(self):
        if not self.is_empty():
            x = self.head.next.value
            self.head.next = self.head.next.next
            if self.is_empty():
                self.tail = self.head
            return x
        return None
    
    def enque(self, x):
        node = Node(None, x)
        self.tail.next = node
        self.tail = node
        
    def is_empty(self):
        return self.head.next is None
        
q = QueueList()
print(q.deque())

q.enque(100)
print(q.deque())

for i in range(5):
    q.enque(i)
while not q.is_empty():
    print(q.deque())