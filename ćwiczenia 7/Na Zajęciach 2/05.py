class Node:
    def __init__(self):
        self.value = None
        self.next = None
        

def f(ptr):
    firsts = [None for _ in range(10)]
    lasts = [None for _ in range(10)]
    
    while ptr is not None:
        last_dig = ptr.value % 10
        if firsts[last_dig] is None:
            firsts[last_dig] = lasts[last_dig] = ptr
        else:
            lasts[last_dig].next = ptr
            last_dig[last_dig] = ptr
        ptr = ptr.next

    first = None
    for i in range(9, -1, -1):
        if firsts[i] is not None:
            lasts[i] = first
            first = firsts[i]
        
    return first