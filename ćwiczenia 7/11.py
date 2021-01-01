'''
Lista zawiera niepowtarzające się elementy. 
Proszę napisać funkcję do której przekazujemy wskaźnik na początek oraz wartość klucza. 
Jeżeli element o takim kluczu występuje w liście należy go usunąć z listy. 
Jeżeli  elementu o zadanym kluczu brak w liście należy element o takim kluczu wstawić do listy.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def add_or_remove(first, value):
    prev = None
    ptr = first
    
    if ptr == None:
        return Node(value)
    
    while ptr != None:
        if ptr.value == value:
            if prev == None:
                return ptr.next
            prev.next = ptr.next
            return first
        prev = ptr
        ptr = ptr.next
    
    prev.next = Node(value)
    return first
    
#-------------------------------------------------------------------
def tab_to_linked_list(T):
    if len(T) == 0:
        return None
    
    f = Node(None)
    ptr = f
    
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
test_print(add_or_remove(tab_to_linked_list([]), 1))
test_print(add_or_remove(tab_to_linked_list([1]), 1))
test_print(add_or_remove(tab_to_linked_list([1, 2]), 2))
test_print(add_or_remove(tab_to_linked_list([1, 2]), 1))
test_print(add_or_remove(tab_to_linked_list([1, 2, 3]), 3))
test_print(add_or_remove(tab_to_linked_list([1, 2, 3]), 4))
