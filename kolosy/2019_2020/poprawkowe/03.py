class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.next = None
        
def func(first):    
    def link(ptr, lf):
        ptr.next = lf
        return ptr
    
    def rec(ptr, res = None):      
        if ptr == None:
            return res
        
        f = ptr
        prev = None 
        while ptr != None: 
            if res == None or ptr.b == res.a:
                if prev == None:
                    pn = ptr.next
                    a = rec(f.next, link(ptr, res))
                    if a != None:
                        return a 
                    ptr.next = pn
                else:
                    pn = ptr.next
                    prev.next = pn
                    a = rec(f, link(ptr, res))
                    if a != None:
                        return a 
                    prev.next = ptr
                    ptr.next = pn
            prev = ptr
            ptr = ptr.next
        
        return None
            
    return rec(first)
        
          
        
        
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

test_print(func(tab_to_linked_list([(2,9), (3,6) ,(8,2), (2,3), (6,2)])))