'''
skoro mam przekształcic zbiory z1, z2, z3 w jeden zbior to moge przepinac elementy zbiorow z2 i z3 do np z1
ide po koleji przez elementy we wepolnej pętli i jesli element z z2 lub z3 jest mniejszy od aktualnego z z1 
to wpinam je do listy przed z1
'''


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def iloczyn(z1, z2, z3):  
    if z1 == None or z2 == None or z3 == None: 
        return None 
    
    prev = None
    first = z1
    
    while z1 != None and z2 != None and z3 != None:
        if z2.val < z1.val and z2.val < z3.val:
            n = z2
            z2 = z2.next 
            if prev == None:
                first = n
                first.next = z1
            else:
                prev.next = n
                prev = n
                prev.next = z1
        if z3.val < z1.val:
            n = z3
            z3 = z3.next 
            if prev == None:
                first = n
                first.next = z1
            else:
                prev.next = n
                prev = n
                prev.next = z1
        else:
            prev = z1
            z1 = z1.next
            
    if z1 == None:
        z1 = prev
        while z2 != None and z3 != None:
            if z2.val < z3.val:
                z1.next = z2
                z2 = z2.next
            else:
                z1.next = z3
                z3 = z3.next
            z1 = z1.next
            z1.next = None
        
        if z2 == None:
            z1.next = z3
        else:
            z1.next = z2
            
    elif z2 == None or z3 == None:
        
        z = None
        if z2 == None:
            z = z2
        elif z3 == None:
            z = z3
            
        
        while z1 != None and z != None:
            if z.val < z1.val:
                n = z
                z = z.next 
                if prev == None:
                    first = n
                    first.next = z
                else:
                    prev.next = n
                    prev = n
                    prev.next = z1
            else:
                prev = z1
                z1 = z1.next
        
        if z1 == None:
            z1.next = z
          
    z1 = first
    prev = None  
    while z1 != None:
        if prev != None and z1.val == prev.val:
            prev.next = z1.next
        else:
            prev = z1
        z1 = z1.next
            
    return first