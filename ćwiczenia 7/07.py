'''
Proszę napisać funkcję usuwającą ostatni element listy. 
Do funkcji należy przekazać wskazanie na pierwszy element listy.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
def pop_back(first):
    if first == None:
        return None
    
    prev = None
    ptr = first
    while ptr.next != None:
        prev = ptr
        ptr = ptr.next
    
    if prev != None:
        prev.next = None
    else:
        return None
        
    return first

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

test_print(pop_back(None))
test_print(pop_back(tab_to_linked_list([1])))
test_print(pop_back(tab_to_linked_list([1, 2])))
    
    