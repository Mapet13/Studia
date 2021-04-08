class StackArray:
    def __init__(self, n):
       self.arr = [0] * n
       self.elements = 0
    
    def push(self, x):
        if len(self.arr) == self.elements:
            arr = [self.arr[i] if i < len(self.arr) else 0 for i in range(2*len(self.arr))]
            self.arr = arr
            
        self.arr[self.elements] = x
        self.elements += 1
    
    def pop(self):
        if not self.is_empty():
            self.elements -= 1
            return self.arr[self.elements]
        return None
        
    def is_empty(self):
        return self.elements == 0


s = StackArray(2)
print(s.pop())

s.push(100)
print(s.pop())


for i in range(5):
    s.push(i)
    print(s.arr)
while not s.is_empty():
    print(s.pop())