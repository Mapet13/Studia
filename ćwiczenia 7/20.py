'''
Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
Krańce przedziałów określa uporządkowana para liczb całkowitych. 
Proszę napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]
'''

class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.next = None
        
def reduce(first):
    ptr_prev = None
    ptr = first
    
    while ptr != None:
        prev = first
        while prev != ptr:
            to_remove = False
            if prev.a >= ptr.a and prev.a <= ptr.b:
                prev.a = ptr.a
                to_remove = True
            if prev.b <= ptr.b and prev.b >= ptr.a:
                prev.b = ptr.b
                to_remove = True
            if to_remove:
                ptr_prev.next = ptr.next # ptr_prev nigdy nie jest Nonem w tym miejscu
                break
            prev = prev.next
        else:
            ptr_prev = ptr
        ptr = ptr.next
         
    return first

#-------------------------------------------------------------------
def tab_to_linked_list(T):
    if len(T) == 0:
        return None
    
    f = Node(T[0][0], T[0][1])
    ptr = f
    
    for e in T[1:]:
        ptr.next = Node(e[0], e[1])
        ptr = ptr.next
  
    return f

def test_print(first):
    a = first
    print("(", end=' ')
    while a != None:
        print('[', a.a, ', ', a.b, ']', sep='', end=' ')
        a = a.next
    print(')')  
#-------------------------------------------------------------------
test_print(reduce(tab_to_linked_list([(15,19), (2,5) ,(7,11), (8,12), (5,6), (13,17)])))
test_print(reduce(tab_to_linked_list([(1, 2)])))
test_print(reduce(tab_to_linked_list([(1, 2), (1, 2)])))
test_print(reduce(tab_to_linked_list([])))
test_print(reduce(tab_to_linked_list([(1, 2), (3, 4), (5, 6)])))
test_print(reduce(tab_to_linked_list([(1, 2), (2, 4), (4, 6)])))
test_print(reduce(tab_to_linked_list([(1, 2), (10, 11), (0, 2), (11, 12), (0, 3)])))
test_print(reduce(tab_to_linked_list([(1, 2), (0, 3)])))

