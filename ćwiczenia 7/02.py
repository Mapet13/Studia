'''
Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy funkcje:
– inicjalizującą tablicę,
– zwracającą wartość elementu o indeksie n,
– podstawiającą wartość value pod indeks n.
'''

class Node:
    def __init__(self, v, i):
        self.value = v
        self.index = i
        self.next = None
        
class Array:
    def __init__(self):
        self.first = None
        
    def get(self, n):
        current = self.first
        
        while current != None and current.index <= n:
            if current.index == n:
                return current.value
            current = current.next
            
        return 0      
        
        
    def set(self, n, x):        
        prev = None
        current = self.first
        
        while current != None and current.index <= n:
            if current.index == n:
                if x == 0: # wykreslanie jak value == default
                    if prev == None:
                        self.first = self.first.next
                    else:
                        prev.next = current.next
                else:    
                    current.value = x
                return
            
            prev = current
            current = current.next

        if x == 0:
            return

        a = Node(x, n)
        if prev == None:
            a.next = self.first
            self.first = a
        else:
            a.next = current
            prev.next = a
        
        
def test_print(s):
    a = s.first
    print("(", end=' ')
    while a != None:
        print(f"[{a.index} -> {a.value}]", end=' ')
        a = a.next
    print(')')        
        
t = Array()
print(t.get(10181))
print(t.get(0))
print(t.get(999999999999))
test_print(t)
t.set(99, 1)
t.set(0, 12)
test_print(t)
t.set(98, 1)
t.set(99, 2)
t.set(100, 3)
t.set(0, 123)
test_print(t)
t.set(123982197921987319872, 1230)
test_print(t)
print(t.get(123982197921987319872))
print(t.get(98))
print(t.get(99))
print(t.get(100))
print(t.get(0))
t.set(0, 0)
t.set(123982197921987319872, 0)
t.set(99, 0)
t.set(101, 0)
t.set(0, 0)
test_print(t)