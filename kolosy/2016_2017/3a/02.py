class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
def func(A, B):    

    def get_first_and_prev(p):
        while p.value < p.next.value:
            p = p.next
        return p.next, p
    
    a, ap = get_first_and_prev(A)
    b, bp = get_first_and_prev(B)
    
    aptr = a
    bptr = b

    fa = True
    fb = True

    while (aptr != a or fa) and (bptr != b or fb):
        if aptr.value < bptr.value:
            fa = False
            ap = aptr
            aptr = aptr.next
        elif aptr.value > bptr.value:
            fb = False
            bp = bptr
            bptr = bptr.next
        else:
            should_exit = False
            if aptr == a:
                fa = True
                a = aptr.next
                if a == a.next:
                    A = a = aptr = None
                    should_exit = True
            if bptr == b:
                fb = True
                b = bptr.next
                if b == b.next:
                    B = b = bptr = None
                    should_exit = True
            
            if a != None:
                ap.next = aptr.next
                aptr = aptr.next
            if b != None:
                bp.next = bptr.next
                bptr = bptr.next
            
            if should_exit:
                break

    return aptr, bptr
    
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
#-------------------------------------------------------------------

a = tab_to_linked_list([1, 2, 3, 4])
b = tab_to_linked_list([2, 3, 5, 6, 7])

a.next.next.next.next = a
b.next.next.next.next.next = b

x, y = func(a.next, b.next.next.next)
test_print_circular(x)
test_print_circular(y)

a = tab_to_linked_list([1])
b = tab_to_linked_list([2, 3, 5, 6, 7])

a.next = a
b.next.next.next.next.next = b

x, y = func(a.next, b.next.next.next)
test_print_circular(x)
test_print_circular(y)

a = tab_to_linked_list([5])
b = tab_to_linked_list([2, 3, 5, 6, 7])

a.next = a
b.next.next.next.next.next = b

x, y = func(a.next, b.next.next.next)
test_print_circular(x)
test_print_circular(y)

a = tab_to_linked_list([5])
b = tab_to_linked_list([5])

a.next = a
b.next = b

x, y = func(a.next, b)
test_print_circular(x)
test_print_circular(y)