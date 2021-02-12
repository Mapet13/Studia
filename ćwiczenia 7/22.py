'''
Dana jestlista, który być może zakończona jest cyklem.
Napisać funkcję, która sprawdza ten fakt.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def is_circular(first):
    slower = first
    
    while first != None and first.next != None:
        slower = slower.next
        first = first.next.next
        
        if first == slower:
            return True
    
    return False

#-------------------------------------------------------------------
def tab_to_linked_list(T):
    if len(T) == 0:
        return None
    
    f = Node(T[0])
    ptr = f
    
    for e in T[1:]:
        ptr.next = Node(e)
        ptr = ptr.next
  
    return f

def test_print(first):
    a = first
    print("(", end=' ')
    while a != None:
        print(a.value, end=' ')
        a = a.next
    print(')')  
    
def to_circular(first, index = 0):
    if first == None:
        return first
    
    i = 0
    ptr = first
    
    circle_start = None 
        
    while ptr.next != None:
        if i == index:
            circle_start = ptr 
        i += 1
        ptr = ptr.next
        
    if i == index:
        circle_start = ptr
    
    ptr.next = circle_start
        
    return first
#-------------------------------------------------------------------
print(is_circular(tab_to_linked_list([])))
print(is_circular(tab_to_linked_list([1])))
print(is_circular(tab_to_linked_list([1, 2, 3])))
print(is_circular(to_circular(tab_to_linked_list([1]))))
print(is_circular(to_circular(tab_to_linked_list([1, 2, 3]), 1)))
print(is_circular(to_circular(tab_to_linked_list([1, 2, 3]), 2)))
