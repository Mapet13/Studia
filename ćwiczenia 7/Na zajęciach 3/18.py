class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def usun(L):
    el = L
    
    prev = None 
    while el is not None:
        
        el2 = el.next
        prev2 = el
        flag = False
        while el2 is not None:
            if el2.value == el.value:
                prev2.next = el2.next
                el2 = el2.next        
                flag = True
            else:
                prev2 = prev2.next
                el2 = el2.next
        
        if flag:
            if prev == None:
                L = L.next
            else:
                prev.next = el.next
        else:
            prev = prev.next
            el = el.next
            
        
    return L