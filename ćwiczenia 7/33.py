'''
Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza” od pierwszej litery s2. 
Według tej zasady rozmieszczono napisy w liście cyklicznej, 
na przykład:

  -> bartek ──> leszek ──> marek ──> ola ──> zosia --V
  ^                                                  |
  |__________________________________________________|

Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy napis z zachowaniem zasady poprzedzania. 
Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis, 
funkcja powinna zwrócić wartość logiczną wskazującą, czy udało się wstawić napis do listy. 
Po wstawieniu elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

def is_corect_order(s1, s2):
    if len(s1) == 0:
        return False
    if len(s2) == 0:
        return True
    return s1[-1] < s2[0]


def push(first, text):
    if first == None:
        if is_corect_order(text, text):
           n = Node(text)
           n.next = n
           return n, True
        else:
            return None, False
    
    ptr = first
    flag = True
    while ptr != first or flag:
        flag = False
        if is_corect_order(ptr.value, text) and is_corect_order(text, ptr.next.value):
            n = Node(text)
            n.next = ptr.next
            ptr.next = n
            return n, True
        ptr = ptr.next
    
    return first, False

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
    while a != first or f:
        f = False
        print(a.value, end=' ')
        a = a.next
    print('--> ... )')  
    
def to_circular(first, index = 0):
    if first == None:
        return first
    
    i = 0
    ptr = first
    
    circle_start = None 
        
    while ptr.next != None:
        if i == index:
            circle_start = ptr 
        i += 1
        ptr = ptr.next
        
    if i == index:
        circle_start = ptr
    
    ptr.next = circle_start
        
    return first
#-------------------------------------------------------------------
        
f, s = push(to_circular(tab_to_linked_list(["bartek", "marek",])), "zosia")
test_print_circular(f)
print(s)
f, s = push(f, "ola")
test_print_circular(f)
print(s)
f, s = push(f, "leszek")
test_print_circular(f)
print(s)
f, s = push(f, "zorro")
test_print_circular(f)
print(s)
f, s = push(f, "żżżżż")
test_print_circular(f)
print(s)
f, s = push(f, "")
test_print_circular(f)
print(s)
    


