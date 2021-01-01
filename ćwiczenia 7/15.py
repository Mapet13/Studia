'''
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, usuwa z niej wszystkie elementy, 
w których wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def should_remove(x):
    count = [0, 0] 
    while x > 0:
        r = x % 3
        if r != 0:
            count[r - 1] += 1
        x //= 3
    return count[0] > count[1]

def revove(first):
    prev = None
    ptr = first
    
    while ptr != None:
        if should_remove(ptr.value):
            if prev == None:
                first = ptr.next
            else:
                prev.next = ptr.next
        else:
            prev = ptr
        ptr = ptr.next
    
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
test_print(revove(tab_to_linked_list([2, 123, 2])))
test_print(revove(tab_to_linked_list([2, 2, 2])))
test_print(revove(tab_to_linked_list([123])))
test_print(revove(tab_to_linked_list([1, 1, 1, 1])))
test_print(revove(tab_to_linked_list([123, 1, 123, 1])))
test_print(revove(tab_to_linked_list([123, 2, 2, 2, 123])))
