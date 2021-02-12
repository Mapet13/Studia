'''
Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. 
Do funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def check_inclusion(f1, f2):
    def check(o, i):
        while i != None:
            if i == o:
                return True
            i = i.next
        return False
    
    return check(f1, f2) or check(f2, f1) 
    
    
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
#-------------------------------------------------------------------

f1 = tab_to_linked_list([1, 1, 1, 1, 1, 1, 1, 1])
f2 = tab_to_linked_list([1, 1, 1, 1, 1, 1, 1, 1])

print(check_inclusion(f1, f2))
print(check_inclusion(f1, f1))
print(check_inclusion(f1, f1.next.next.next))
print(check_inclusion(f1.next.next.next, f1))

p = f1
while p.next != None:
    p = p.next
    
print(check_inclusion(f1, p))
print(check_inclusion(f1, p.next))