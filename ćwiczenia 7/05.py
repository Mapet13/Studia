'''
Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
należy połączyć w jedną listę odsyłaczową, która jest posortowana
niemalejąco według ostatniej cyfry pola val.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def sort_ll(first):
    tf = [None for _ in range(10)]
    t = [None for _ in range(10)]
    
    while first != None:
        last_digit = first.value % 10
        
        if t[last_digit] == None:     
            t[last_digit] = Node(first.value)
            tf[last_digit] = t[last_digit]
        else:
            t[last_digit].next = Node(first.value)
            t[last_digit] = t[last_digit].next
            
        first = first.next
        
    i = 0
    j = i+1
    while i < 9 and j <= 9:
        if t[i] == None:
            i += 1
        elif i >= j or tf[j] == None:
            j += 1
        else:
            t[i].next = tf[j]
            i += 1
            j += 1     
    
    return tf[0]

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

T = [12, 34, 14, 14, 56, 82, 0, 90, 72, 68, 99, 61, 31, 123, 182, 71, 8888, 191, 1561, 575545, 11, 2221, 345512, 545, 8288180]
test_print(sort_ll(tab_to_linked_list(T)))