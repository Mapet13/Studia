'''
Proszę napisać funkcję wstawiającą na koniec listy nowy element. 
Do funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą wartość.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def push_back(first, value):
    n = Node(value)
    
    if first == None:
        return n
    
    ptr = first
    
    while(ptr.next != None):
        ptr = ptr.next
     
    ptr.next = n
    
    return first
    
    
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

test_print(push_back(None, 1))
test_print(push_back(tab_to_linked_list([1]), 2))
test_print(push_back(tab_to_linked_list([1, 2]), 3))


    