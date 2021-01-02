'''
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy dwukierunkowej, 
usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

def should_remove(x):
    oc = 0
    while x > 0:
        oc += x % 2
        x //= 2
    return oc % 2 == 1
      
        
def remove(first):
    ptr = first
    
    while ptr != None:
        if should_remove(ptr.value):
            if ptr.next != None:
                ptr.next.prev = ptr.prev
            if ptr.prev != None:
                ptr.prev.next = ptr.next
            else:
                first = ptr.next
        ptr = ptr.next
    
    return first        
        
        
#-------------------------------------------------------------------
def tab_to_double_linked_list(T):
    if len(T) == 0:
        return None
    
    f = Node(T[0])
    ptr = f
    
    for e in T[1:]:
        ptr.next = Node(e)
        ptr.next.prev = ptr
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

test_print(remove(tab_to_double_linked_list([])))
test_print(remove(tab_to_double_linked_list([1])))
test_print(remove(tab_to_double_linked_list([1, 1, 1, 1])))
test_print(remove(tab_to_double_linked_list([1, 0, 0, 1])))
test_print(remove(tab_to_double_linked_list([0, 0, 0, 1])))
test_print(remove(tab_to_double_linked_list([0, 1, 0, 1])))
test_print(remove(tab_to_double_linked_list([0, 1, 0, 0])))
test_print(remove(tab_to_double_linked_list([0, 0, 0, 0])))