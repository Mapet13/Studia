
class QueueArray:
    def __init__(self, n):
        self.arr = [0] * n
        self.elements = 0
        self.head = 0
       
    def deque(self):
        if not self.is_empty():
            self.elements -= 1
            return self.arr[self._get_current_id(self.elements)]
        return None
    
    def enque(self, x):
        if len(self.arr) == self.elements:
            arr = [self.arr[self._get_current_id(i)] if i < len(self.arr) else 0 for i in range(2*len(self.arr))]
            self.arr = arr
            self.head = 0
            
        self.arr[self._get_current_id(self.elements)] = x
        self.elements += 1
        
    def _get_current_id(self, x): return (self.head + x) % len(self.arr)
        
    def is_empty(self):
        return self.elements == 0
        
q = QueueArray(2)
print(q.deque())

q.enque(100)
print(q.deque())

for i in range(5):
    q.enque(i)
while not q.is_empty():
    print(q.deque())