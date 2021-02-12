class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
def func(A, B):    
    fb = B
    fa = A
    
    fb_prev = None
    while fb != None:
        fa = A
        while fa != fb and fa != None:
            fa = fa.next
        
        if fa == fb:
           if fb_prev != None:
                fb_prev.next = None
           break  
    
        fb_prev = fb
        fb = fb.next
    
    
    if fa == None:
        fa = A
        
    while fa != None:
        n = Node(fa.value)

        if fb_prev == None:
            B = n
            fb_prev = B
        else:
            fb_prev.next = n
            fb_prev = fb_prev.next
        
        fa = fa.next
            
            
    return A, B
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

a = tab_to_linked_list([5, 11, 3, 2])
b = tab_to_linked_list([13, 7, 17])
b.next.next.next = a.next.next

x, y = func(a, b)
test_print(x)
test_print(y)

while x != None:
    z = y
    while z != None:
        if z == x:
            print("blad")
        z = z.next
    x = x.next
    
    
a = tab_to_linked_list([5, 11, 3, 2])
b = a

x, y = func(a, b)
test_print(x)
test_print(y)

while x != None:
    z = y
    while z != None:
        if z == x:
            print("blad")
        z = z.next
    x = x.next
    
a = tab_to_linked_list([5, 11, 3, 2])
b = a.next.next

x, y = func(a, b)
test_print(x)
test_print(y)

while x != None:
    z = y
    while z != None:
        if z == x:
            print("blad")
        z = z.next
    x = x.next