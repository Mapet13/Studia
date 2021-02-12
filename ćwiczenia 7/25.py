'''
Dana jest lista, który zakończona jest cyklem. 
Napisać funkcję, która zwraca wskaźnik do ostatniego elementu przed cyklem.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def count_elements_before_cycle(first):
    def is_in_cycle(ptr, a):
        b = a.next
        
        while a != b and ptr != b:
            b = b.next
            
        return ptr == b 
    
    
    slower = first
    faster = first.next
    
    while slower != faster:
        faster = faster.next.next
        slower = slower.next
     
    count = 0
    
    prev = None
    while not is_in_cycle(first, slower):
        prev = first
        first = first.next
        
    return prev
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

def print_node(first):
    print(f'[{first if first is None else first.value}]')
    
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
print_node(count_elements_before_cycle(to_circular(tab_to_linked_list([1]))))
print_node(count_elements_before_cycle(to_circular(tab_to_linked_list([1, 2, 3]), 1)))
print_node(count_elements_before_cycle(to_circular(tab_to_linked_list([1, 2, 3]), 2)))
print_node(count_elements_before_cycle(to_circular(tab_to_linked_list([1, 2, 3, 4, 5, 6]), 2)))
print_node(count_elements_before_cycle(to_circular(tab_to_linked_list([1, 2, 3, 4, 5, 6]), 5))) 
print_node(count_elements_before_cycle(to_circular(tab_to_linked_list([1, 2, 3, 4, 5, 6])))) 




