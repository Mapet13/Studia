'''
Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o wartościach typu int, 
usuwającą wszystkie elementy, których wartość dzieli bez reszty wartość bezpośrednio następujących po nich elementów
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def revove(first, x):
    prev = None
    ptr = first
    
    while ptr != None and ptr.next != None:
        if ptr.next.value % x == 0:
            if prev == None:
                first = ptr.next
            else:
                prev.next = ptr.next
        else:
            prev = ptr
        ptr = ptr.next
    
    return first

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
#-------------------------------------------------------------------
test_print(revove(tab_to_linked_list([]), 1))
test_print(revove(tab_to_linked_list([1]), 1))
test_print(revove(tab_to_linked_list([1, 1]), 1))
test_print(revove(tab_to_linked_list([1, 2]), 2))
test_print(revove(tab_to_linked_list([2, 2, 3]), 2))
test_print(revove(tab_to_linked_list([1, 2, 1, 2]), 2))
test_print(revove(tab_to_linked_list([1, 2, 3, 4]), 1))
test_print(revove(tab_to_linked_list([2, 2, 2, 3, 2, 2, 2, 2, 3]), 2))
test_print(revove(tab_to_linked_list([1, 1, 1, 1, 1, 1]), 2))

    