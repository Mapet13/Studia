'''
Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o wartościach typu int, 
usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio poprzedzających je elementów. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def revove(first, x):
    ptr = first
    
    while ptr != None and ptr.next != None:
        if ptr.value < x:
            temp = ptr.next
            while temp.next != None and temp.value < x:
                temp = temp.next
            ptr.next = temp.next
        ptr = ptr.next
            
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
test_print(revove(tab_to_linked_list([]), 1))
test_print(revove(tab_to_linked_list([1]), 1))
test_print(revove(tab_to_linked_list([1, 2]), 2))
test_print(revove(tab_to_linked_list([1, 2]), 1))
test_print(revove(tab_to_linked_list([1, 2, 3]), 2))
test_print(revove(tab_to_linked_list([1, 2, 1, 3]), 2))
test_print(revove(tab_to_linked_list([1, 1, 1, 3]), 2))
test_print(revove(tab_to_linked_list([1, 1, 3, 1, 1, 2]), 2))
test_print(revove(tab_to_linked_list([1, 1, 1, 1, 1, 1]), 2))

    