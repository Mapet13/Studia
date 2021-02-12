'''
Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą. 
Proszę napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę rosnącą.
Warunkiem usunięcia jest istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def remove(first):
    best_len = 0
    start_prev = None
    end = None
    
    should_be_removed = False
    
    ptr = first
    prev = None
    
    cuurent_start_prev = None
    count = 0
    
    while ptr != None:
        if prev == None or ptr.value > prev.value:
            count += 1
        else:
            if best_len == count:
                should_be_removed = False
            elif best_len < count:
                should_be_removed = True
                end = prev 
                start_prev = cuurent_start_prev
                best_len = count
            count = 1
            cuurent_start_prev = prev
        prev = ptr
        ptr = ptr.next  
        
    if best_len == count:
        should_be_removed = False
    elif best_len < count:
        should_be_removed = True
        end = prev 
        start_prev = cuurent_start_prev
        best_len = count         

    if should_be_removed:
        if start_prev == None:
            first = end.next
        else:
            start_prev.next = end.next
        
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
test_print(remove(tab_to_linked_list([])))
test_print(remove(tab_to_linked_list([1])))
test_print(remove(tab_to_linked_list([1, 2, 3])))
test_print(remove(tab_to_linked_list([1, 2, 3, 2, 3, 4]))) 
test_print(remove(tab_to_linked_list([4, 3, 2, 1])))
test_print(remove(tab_to_linked_list([1, 2, 3, 3, 4, 5])))
test_print(remove(tab_to_linked_list([2, 1, 1, 3, 5, 99])))
test_print(remove(tab_to_linked_list([12, -12, 0, 12])))