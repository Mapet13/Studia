'''
Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne. 
Do funkcji należy przekazać wskazanie na pierwszy element listy.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
 
def uniq(first):
    prev = None
    ptr = first
    
    while ptr != None:
        x = ptr.value
        should_be_removed = False
        
        ptr1 = ptr.next
        prev1 = ptr
        while ptr1 != None:
            if ptr1.value == x:
                prev1.next = ptr1.next
                should_be_removed = True
            else:
                prev1 = ptr1
            ptr1 = ptr1.next
        
        if should_be_removed:
            if prev != None:
                prev.next = ptr.next
            else:
                first = ptr.next
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
test_print(uniq(tab_to_linked_list([])))
test_print(uniq(tab_to_linked_list([1])))
test_print(uniq(tab_to_linked_list([1, 2, 3])))
test_print(uniq(tab_to_linked_list([1, 2, 3, 1])))
test_print(uniq(tab_to_linked_list([1, 2, 2, 1])))
test_print(uniq(tab_to_linked_list([1, 1, 1, 1])))
test_print(uniq(tab_to_linked_list([2, 1, 1, 3])))
test_print(uniq(tab_to_linked_list([2, 1, 2, 1])))