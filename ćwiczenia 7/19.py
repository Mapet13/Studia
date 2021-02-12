'''
Elementy w liście są uporządkowane według wartości klucza. 
Proszę napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. 
Do funkcji przekazujemy wskazanie na pierwszy element listy, funkcja powinna zwrócić liczbę usuniętych elementów.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def uniq(first):
    prev = None
    ptr = first

    count = 0
    
    current_val = None
    current_count = 0
    prev_of_current = None

    while ptr != None:
        if ptr.value != current_val:
            if current_count > 1:
                count += current_count
                prev = prev_of_current
                if prev != None:
                    prev.next = ptr
                else:
                    first = ptr
            current_val = ptr.value
            current_count = 0
            prev_of_current = prev
        current_count += 1
        prev = ptr
        ptr = ptr.next
        
    if current_count > 1:
        count += current_count
        prev = prev_of_current
        if prev != None:
            prev.next = None
        else:
            first = None
    
    return first, count
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

def to_string(first):
    s = "( "
    a = first
    while a != None:
        s = s + str(a.value) + " "
        a = a.next
    s += ")"
    return s
#-------------------------------------------------------------------
f, c = uniq(tab_to_linked_list([]))
print(to_string(f), c)
f, c = uniq(tab_to_linked_list([1]))
print(to_string(f), c)
f, c = uniq(tab_to_linked_list([1, 1]))
print(to_string(f), c)
f, c = uniq(tab_to_linked_list([1, 1, 2]))
print(to_string(f), c)
f, c = uniq(tab_to_linked_list([1, 2, 2]))
print(to_string(f), c)
f, c = uniq(tab_to_linked_list([1, 2, 2, 3]))
print(to_string(f), c)
f, c = uniq(tab_to_linked_list([1, 1, 2, 2, 3, 3]))
print(to_string(f), c)
f, c = uniq(tab_to_linked_list([1, 2, 2, 3, 4, 4]))
print(to_string(f), c)
f, c = uniq(tab_to_linked_list([1, 2, 3, 4, 5]))
print(to_string(f), c)
