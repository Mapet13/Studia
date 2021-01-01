'''
Dana jest niepusta lista reprezentująca liczbę naturalną. 
Kolejne elementy listy przechowują kolejne cyfry. 
Proszę napisać funkcję zwiększającą taką liczbę o 1.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    
def increment(first):
    def inc(ptr):
        ptr.value += 1
        if ptr.value == 10:
            ptr.value = 0
            return True
        return False
    
    def rec(ptr):
        if ptr.next == None or rec(ptr.next):
            return inc(ptr)
        return False

    if rec(first):
        n = Node(1)
        n.next = first
        first = n
        
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

test_print(increment(tab_to_linked_list([0])))
test_print(increment(tab_to_linked_list([1])))
test_print(increment(tab_to_linked_list([9])))
test_print(increment(tab_to_linked_list([1,0,0,0,0,0,0,0,0,0,0])))
test_print(increment(tab_to_linked_list([1,9,9,9,9,9,9,9,9,9,9])))
test_print(increment(tab_to_linked_list([9,9,9,9,9,9,9,9,9,9,9])))
