'''
Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element listy. 
Do funkcji należy przekazać wskazanie na pierwszy element listy.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
def alternate(first):
    remove = False
   
    prev = None
    ptr = first
    while ptr != None:
        if remove:
            prev.next = ptr.next
        else:
            prev = ptr
        remove = not remove
        ptr = ptr.next
    
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

test_print(alternate(tab_to_linked_list([1])))
test_print(alternate(tab_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
test_print(alternate(tab_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])))