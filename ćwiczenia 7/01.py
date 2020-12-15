'''
Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze struktury listy odsyłaczowej.
- czy element należy do zbioru
- wstawienie elementu do zbioru
- usunięcie elementu ze zbioru
'''

class Node:
    def __init__(self):
        self.value = None
        self.next = None
         
         
         
class IntegerSet:
    def __init__(self):
        self.first = None
        self.last = None
    
    def push(self, x):
        if self.contains(x):
            return
        
        q = Node()
        q.value = x
        
        if self.first == None:
            self.first = q
            self.last = q
        else:
            self.last.next = q
            self.last = q
        

    def pop(self, x):
        prev = None
        current = self.first
        
        while current != None:
            if current.value == x:
                if current == self.first:
                    self.first = self.first.next
                else:
                    prev.next = current.next
                if current == self.last:
                    self.last = prev
            prev = current
            current = current.next
                
                
    def contains(self, x):
        p = self.first
        while p != None:
            if p.value == x:
                return True
            p = p.next
        return False
        
        
        
        
    
def test_print(s):
    a = s.first
    print("(", end=' ')
    while a != None:
        print(a.value, end=' ')
        a = a.next
    print(')')
    
s = IntegerSet()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

test_print(s)

print(s.contains(1))
print(s.contains(4))
print(s.contains(10))

s.pop(1)
s.pop(3)
test_print(s)
print(s.contains(1))
print(s.contains(3))
print(s.contains(2))

s.pop(4)
s.push(5)
s.push(5)
test_print(s)
print(s.contains(4))
print(s.contains(5))
        
            
          
        
        