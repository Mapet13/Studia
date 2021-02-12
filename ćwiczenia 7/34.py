'''
Proszę napisać funkcję, która usuwa z listy cyklicznej elementy, których klucz występuje dokładnie k razy.
Do funkcji należy przekazać wskazanie na jeden z elementów listy, oraz liczbę k, 
funkcja powinna zwrócić informację czy usunięto jakieś elementy z listy. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove(ptr, k):
    
    def count(ptr, val):
        flag = True
        counter = 0
        p = ptr
        while p != ptr or flag:
            flag = False 
            if ptr.value == val:
                counter += 1
            ptr = ptr.next
        return counter
    
    
    was_removed = False
    
    flag = True
    
    was_checked = set()
    to_be_removed = set()
    
    prev = ptr
    first = ptr.next
    
    while first != ptr.next or flag:
        flag = False
        
        should_increment_prev = True
        
        if first.value in to_be_removed:
            if first.next == first:
                return None, True
                
            prev.next = first.next
            
            if prev == ptr:
                flag = True
            
            should_increment_prev = False
        
        elif first.value not in was_checked:
            was_checked.add(first.value)
            
            if count(ptr, first.value) == k:
                to_be_removed.add(first.value)
                
                was_removed = True
                
                if first.next == first:
                    print("ech")
                    return None, True

                prev.next = first.next
                
                if prev == ptr:
                    flag = True
                
                should_increment_prev = False
        
        if should_increment_prev:
            prev = first
        
        first = first.next
    
    return first, was_removed

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

def test_print_circular(first):
    f = True
    a = first
    print("( ... --> ", end=' ')
    while (a != first or f) and a != None:
        f = False
        print(a.value, end=' ')
        a = a.next
    print('--> ... )')  
    
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

f, c = remove(to_circular(tab_to_linked_list([2, 1, 1, 2, 1, 2, 1, 1, 2])), 4)
print(c)
test_print_circular(f)

f, c = remove(to_circular(tab_to_linked_list([2, 1, 3, 2, 3, 2, 1, 3, 2, 3])), 4)
print(c)
test_print_circular(f)

f, c = remove(to_circular(tab_to_linked_list([2,  2,  2,  2])), 4)
print(c)
test_print_circular(f)

f, c = remove(to_circular(tab_to_linked_list([2,  2,  2, 1, 5])), 4)
print(c)
test_print_circular(f)
