'''
Lista reprezentuje wielomian o współczynnikach całkowitych. 
Elementy w liście ułożone są według rosnących potęg. 
Proszę napisać funkcję obliczającą różnicę dwóch dowolnych wielomianów.
Wielomiany reprezentowane są przez wyżej opisane listy. 
Procedura powinna zwracać wskaźnik do nowo utworzonej listy reprezentującej wielomian wynikowy. 
Listy wejściowe powinny pozostać niezmienione.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def substract(w1, w2):
    
    def rm_tail_zeros(w, con = False):
        if w == None:
            return con
        if rm_tail_zeros(w.next, w.value == 0):
            w.next = None
            return True
        return False
        
    first = None
    res = None
    
    while w1 != None and w2 != None:
        n = Node(w1.value - w2.value)
        if res == None:
            res = n
            first = res 
        else:
            res.next = n
            res = res.next
        w1 = w1.next
        w2 = w2.next
            
    rm_tail_zeros(first)
    
    w = w1
    sign = 1
    if w2 != None:
        w = w2
        sign = -1
    
    while w != None:
        n = Node(w.value * sign)
        if res == None:
            res = n
            first = res 
        else:
            res.next = n
            res = res.next
        w = w.next
        
    
    return first

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


test_print(substract(tab_to_linked_list([0, 0, 0, 0, 1]), tab_to_linked_list([0, 0, 0, 0, 1])))
test_print(substract(tab_to_linked_list([0, 0, 0, 0, 1]), tab_to_linked_list([1, 1, 1, 1])))
test_print(substract(tab_to_linked_list([0, 0, 0, 0, 1]), tab_to_linked_list([0, 0, 0, 0, 0, 0, 0, 1])))
test_print(substract(tab_to_linked_list([0, 0, 0, 0, 1]), tab_to_linked_list([0, 1])))
test_print(substract(tab_to_linked_list([0]), tab_to_linked_list([0])))
test_print(substract(tab_to_linked_list([1]), tab_to_linked_list([0])))
test_print(substract(tab_to_linked_list([0]), tab_to_linked_list([1])))
test_print(substract(tab_to_linked_list([1, 1, 1, 1, 1]), tab_to_linked_list([1, 1, 1, 1, 1])))
    