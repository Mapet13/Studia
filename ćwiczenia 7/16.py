'''
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, 
przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym. 

?? czy jak tych piatek jest 0 to tez powinno przenosic ??
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def should_move_to_front(x):
    fc = 0
    while x > 0:
        if x % 8 == 5:
            fc += 1
        x //= 8
    return fc % 2 == 0

def sort_fc(first):
    if first == None:
        return first
    
    prev = first
    ptr = first.next
    
    while ptr != None:
        if should_move_to_front(ptr.value):
            prev.next = ptr.next
            tmp = ptr.next 
            ptr.next = first
            first = ptr
            ptr = tmp
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
test_print(sort_fc(tab_to_linked_list([5, 123123123])))
test_print(sort_fc(tab_to_linked_list([1, 2, 3])))
test_print(sort_fc(tab_to_linked_list([123123123])))
test_print(sort_fc(tab_to_linked_list([5, 5, 5, 5])))
test_print(sort_fc(tab_to_linked_list([123123123, 5, 123123123, 5])))
test_print(sort_fc(tab_to_linked_list([5, 123123123, 5, 123123123, 5])))
test_print(sort_fc(tab_to_linked_list([123123123, 5, 2, 2, 123123123])))