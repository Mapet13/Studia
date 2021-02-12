'''
Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. 
W pierwszej liście liczby są posortowane rosnąco, a w drugiej nie. 
Proszę napisać funkcję usuwającą z obu list liczby występujące w obu listach. 
Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę usuniętych elementów. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# f1 - posortowana
# f2 - nie posortowana
def remove(f1, f2):
    
    if f2 == None or f1 == None:
        return f1, f2, 0
    
    first1 = f1
    first2 = f2
    
    counter = 0
    
    prev = None
    while f2 != None:
        
        prev1 = None
        f1 = first1
        while f1 != None and f1.value < f2.value:
            prev1 = f1
            f1 = f1.next
            
        if f1 != None and f2.value == f1.value:
            counter += 2 
            if prev != None:
                prev.next = f2.next
            else:
                first2 = f2.next
            if prev1 != None:
                prev1.next = f1.next
            else: 
                first1 = first1.next
        else:
            prev = f2
        
        f2 = f2.next
        
    return first1, first2, counter
            
            
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

f1, f2, c = remove(tab_to_linked_list([1, 2, 3, 4, 5, 6]), tab_to_linked_list([4, 1, 2, 3, 6, 5]))
test_print(f1)
test_print(f2)
print(c)

print("-----------")

f1, f2, c = remove(tab_to_linked_list([1, 2, 3, 4, 5, 6]), tab_to_linked_list([1, 6, 2]))
test_print(f1)
test_print(f2)
print(c)

print("-----------")

f1, f2, c = remove(tab_to_linked_list([1, 3, 5]), tab_to_linked_list([2, 6, 4]))
test_print(f1)
test_print(f2)
print(c)

print("-----------")

f1, f2, c = remove(tab_to_linked_list([2, 3, 4, 5]), tab_to_linked_list([2, 1, 3, 5, 4, 6]))
test_print(f1)
test_print(f2)
print(c)

print("-----------")

f1, f2, c = remove(tab_to_linked_list([]), tab_to_linked_list([]))
test_print(f1)
test_print(f2)
print(c)