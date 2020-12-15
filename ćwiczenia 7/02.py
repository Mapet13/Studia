'''
Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy funkcje:
– inicjalizującą tablicę,
– zwracającą wartość elementu o indeksie n,
– podstawiającą wartość value pod indeks n.
'''

class Node:
    def __init__(self):
        self.value = None
        self.next = None
        
class Array:
    def __init__(self, N):
        self.first = None
        
        current = None
        
        if N > 0:
            self.first = Node()
            self.first.value = 0
            current = self.first
        
        for _ in range(1, N):
            current.next = Node()
            current.next.value = 0
            current = current.next
        
        self.last = current
        
    def get(self, n):
        current = self.first
        
        for _ in range(0, n):
            if current == None:
                return None
            current = current.next

        if current == None:
                return None
        return current.value
        
    
    def set(self, n, x):
        current = self.first
        
        for _ in range(0, n):
            if current == None:
                return
            current = current.next
            
        if current != None:
            current.value = x
        
def test_print(s):
    a = s.first
    print("(", end=' ')
    while a != None:
        print(a.value, end=' ')
        a = a.next
    print(')')        
        
t = Array(10)
t0 = Array(0)
test_print(t)
test_print(t0)

t.set(0, 1)
test_print(t)
        
t.set(9, 1)
test_print(t)

print(t.get(0))
print(t.get(1))
print(t.get(9))
print(t.get(10))

t0.set(1, 1)
test_print(t0)
print(t0.get(0))