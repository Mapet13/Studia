'''
Proszę napisać funkcję scalającą dwie posortowane listy w jedną
posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
- funkcja iteracyjna,
- funkcja rekurencyjna
'''

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

#----------ITERACYJNIE----------------------------------------------
def merge_iter(ptr1, ptr2):    
    prev = None
    ptr = ptr1
    
    while ptr != None and ptr2 != None:
        if ptr2.value < ptr.value:
            if prev != None:
                prev.next = ptr2
            else:
                ptr1 = ptr2
            prev = ptr2
            ptr2 = ptr2.next
            prev.next = ptr
        else:
            prev = ptr
            ptr = ptr.next
    
    if ptr2 != None:
        prev.next = ptr2
    
    return ptr1
#----------REKURENCYJNIE--------------------------------------------
def merge_recur(ptr1, ptr2, ptr = Node(None)):
    if ptr2 == None:
        ptr.value = ptr1.value
        ptr.next = ptr1.next
    elif ptr1 == None:
        ptr.value = ptr2.value
        ptr.next = ptr2.next
    else:
        if ptr1.value > ptr2.value:
            ptr.value = ptr2.value
            ptr2 = ptr2.next
        else:
            ptr.value = ptr1.value
            ptr1 = ptr1.next
        ptr.next = Node(None)   
        merge_recur(ptr1, ptr2, ptr.next)
    return ptr
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
    
t1 = [-3, 0, 10, 99, 123]
t2 = [-4, 0, 10, 98, 99, 100]

print("------ITER----------")
test_print(merge_iter(tab_to_linked_list(t1), tab_to_linked_list(t2)))
test_print(tab_to_linked_list(t1))
test_print(tab_to_linked_list(t2))
test_print(merge_iter(tab_to_linked_list(t2), tab_to_linked_list(t1)))
test_print(tab_to_linked_list(t1))
test_print(tab_to_linked_list(t2))
print("------RECUR----------")
test_print(merge_recur(tab_to_linked_list(t1), tab_to_linked_list(t2)))
test_print(tab_to_linked_list(t1))
test_print(tab_to_linked_list(t2))
test_print(merge_recur(tab_to_linked_list(t2), tab_to_linked_list(t1)))
test_print(tab_to_linked_list(t1))
test_print(tab_to_linked_list(t2))

