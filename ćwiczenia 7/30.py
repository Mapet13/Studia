'''
Dane są dwie niepuste listy, z których każda zawiera niepowtarzające się elementy. 
Elementy w pierwszej liście są uporządkowane rosnąco, w drugiej elementy występują w przypadkowej kolejności. 
Proszę napisać funkcję, która z dwóch takich list stworzy jedną, 
w której uporządkowane elementy będą stanowić sumę mnogościową elementów z list wejściowych.
Do funkcji należy przekazać wskazania na obie listy, 
funkcja powinna zwrócić wskazanie na listę wynikową. 

Na przykład dla list:
2 -> 3 -> 5 ->7-> 11
8 -> 2 -> 7 -> 4
powinna pozostać lista:
2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 11
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge(f1, f2):

    if f2 == None:
        return f1
    
    while f2 != None:
        
        if f1 == None:
            f1 = f2
            f2 = f2.next
            f1.next = None
        else:
            p = f1
            while p.next != None and p.next.value <= f2.value:
                p = p.next
                
            if p.value != f2.value:
                if p == f1 and p.value > f2.value:
                    f1 = f2
                    f2 = f2.next
                    f1.next = p
                else:
                    tmp = p.next
                    p.next = f2
                    f2 = f2.next
                    p.next.next = tmp
            else:
               f2 = f2.next 
    
    return f1

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
        
test_print(merge(tab_to_linked_list([2, 3, 5, 7, 11]), tab_to_linked_list([8, 2, 7, 4])))
test_print(merge(tab_to_linked_list([]), tab_to_linked_list([8, 2, 7, 4])))
test_print(merge(tab_to_linked_list([]), tab_to_linked_list([])))
test_print(merge(tab_to_linked_list([111]), tab_to_linked_list([8, 2, 7, 4])))
test_print(merge(tab_to_linked_list([0]), tab_to_linked_list([8, 2, 7, 4])))
test_print(merge(tab_to_linked_list([2, 3, 5, 7, 11]), tab_to_linked_list([])))
test_print(merge(tab_to_linked_list([2, 3, 5, 7, 11]), tab_to_linked_list([1])))
test_print(merge(tab_to_linked_list([2, 3, 5, 7, 11]), tab_to_linked_list([15])))


