'''
Proszę napisać funkcję, która rozdziela listę na dwie listy. 
Pierwsza powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
pozostałe elementy należy usunąć z pamięci. 
Do funkcji należy przekazać wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe.
Funkcja powinna zwrócić liczbę usuniętych elementów. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def split(f):
    def push_front(L, ptr): #ptr != None
        a = L
        L = ptr
        ptr = ptr.next
        L.next = a
        return L, ptr
    
    even = None
    odd = None
    
    while f != None:
        if f.value % 2 == 0 and f.value >= 0:
            even, f = push_front(even, f)
        elif f.value % 2 == 1 and f.value < 0:
            odd, f = push_front(odd, f)
        else:
            f = f.next
            
    return even, odd
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

e, o = split(tab_to_linked_list([-1, 2, -1, 2, -1, 2, -1, 2]))
test_print(e)
test_print(o)
print("-----------------")
e, o = split(tab_to_linked_list([-1, -2, -1, -2, -1, -2, -1, -2]))
test_print(e)
test_print(o)
print("-----------------")
e, o = split(tab_to_linked_list([1, -2, 1, -2, 1, -2, 1, -2]))
test_print(e)
test_print(o)
print("-----------------")
e, o = split(tab_to_linked_list([1, 2, 1, 2, 1, 2, 1, 2]))
test_print(e)
test_print(o)
print("-----------------")
e, o = split(tab_to_linked_list([]))
test_print(e)
test_print(o)
print("-----------------")