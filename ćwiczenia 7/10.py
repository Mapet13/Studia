'''
Liczby naturalne reprezentowane jak poprzednim zadaniu. 
Proszę napisać funkcję dodającą dwie takie liczby. 
W wyniku dodawania dwóch liczb powinna powstać nowa lista. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    
def add(f1, f2):
    def get_length(f):
        c = 0
        while f != None:
            c += 1
            f = f.next
        return c     
    
    def rec(p1, p2, r):
        p2n = p2
        p2v = 0
        if r <= 0:
            p2n = p2.next
            p2v = p2.value
       
        node = Node(0)
        
        carry = 0
        if p1.next != None:
            node.next, carry = rec(p1.next, p2n, r-1)
        
        node.value = p1.value + p2v + carry
        carry = 0
        if node.value >= 10:
            node.value %= 10
            carry = 1
        
        return node, carry 
            
    
    len1 = get_length(f1)
    len2 = get_length(f2)
    r = abs(len1 - len2)
    if len1 < len2:
        f1, f2 = f2, f1
        
    n, c = rec(f1, f2, r)
    
    if c == 0:
        return n
    else:
        f = Node(1)
        f.next = n
        return f
     
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

test_print(add(tab_to_linked_list([0]), tab_to_linked_list([0])))
test_print(add(tab_to_linked_list([1]), tab_to_linked_list([0])))
test_print(add(tab_to_linked_list([9]), tab_to_linked_list([9])))
test_print(add(tab_to_linked_list([5]), tab_to_linked_list([5])))
test_print(add(tab_to_linked_list([1, 1, 1, 1, 1]), tab_to_linked_list([9, 9, 9, 9, 9])))
test_print(add(tab_to_linked_list([9, 9, 9, 9, 9]), tab_to_linked_list([1])))
test_print(add(tab_to_linked_list([1]), tab_to_linked_list([9, 9, 9, 9, 9])))
test_print(add(tab_to_linked_list([1]), tab_to_linked_list([2, 0, 0])))