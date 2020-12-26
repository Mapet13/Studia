'''
Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.
'''

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
def reverse(first):
    next_node = None
    
    while first != None:
        ptr = first.next         
        first.next = next_node  
        next_node = first       
        first = ptr               
        
    return next_node


#-------------------------------------------------------------------
def tab_to_linked_list(T):
    f = Node(None)
    ptr = f
    
    if len(T) > 0:
        ptr.value = T[0]
    
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
#-------------------------------------------------------------------

t = [-4, 0, 10, 98, 99, 100]
test_print((tab_to_linked_list(t)))