'''
Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne.
W obu listach liczby są posortowane rosnąco. 
Proszę napisać funkcję usuwającą z każdej listy liczby nie występujące w drugiej. 
Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę usuniętych elementów. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove(f1, f2):
    def rm(p1, p2):
        f1 = p1
        f2 = p2
        
        c = 0
        
        prev = None
        while p1 != None:
            while p2 != None and p2.value < p1.value:
                p2 = p2.next
            if p2 == None or p2.value != p1.value:
                c += 1
                if prev == None:
                    f1 = f1.next
                else: 
                    prev.next = p1.next
            else:
                prev = p1
                
            p1 = p1.next
        
        return f1, f2, c    
    
    if f1 == None or f2 == None:
        return None, None
    
    f1, f2, c1 = rm(f1, f2)
    f2, f1, c2 = rm(f2, f1)
    
    return f1, f2, c1 + c2
    
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

f1, f2, c = remove(tab_to_linked_list([1, 2,3, 4, 5, 6]), tab_to_linked_list([1, 2, 3, 4, 5, 6]))
test_print(f1)
test_print(f2)
print(c)

print("-----------")

f1, f2, c = remove(tab_to_linked_list([2, 4, 6]), tab_to_linked_list([1, 2, 3, 4, 5, 6]))
test_print(f1)
test_print(f2)
print(c)

print("-----------")

f1, f2, c = remove(tab_to_linked_list([2, 4, 6]), tab_to_linked_list([1, 3, 5]))
test_print(f1)
test_print(f2)
print(c)

print("-----------")

f1, f2, c = remove(tab_to_linked_list([1, 2, 3, 4, 5, 6]), tab_to_linked_list([2, 3, 4, 5]))
test_print(f1)
test_print(f2)
print(c)

print("-----------")

f1, f2, c = remove(tab_to_linked_list([2, 3, 4, 5, 6]), tab_to_linked_list([1, 2, 3, 4, 5]))
test_print(f1)
test_print(f2)
print(c)