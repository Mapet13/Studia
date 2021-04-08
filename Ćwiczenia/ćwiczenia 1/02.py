'''
Zadanie 2. (sortowanie listy jednokierunkowej) Proszę zaimplementować algorytm sortowania listy jednokierunkowej. 
W szczególności należy:
    1. Zdefiniować klasę w Pythonie realizującą listę jednokierunkową.
    2. Zaimplementować wstawianie do posortowanej listy.
    3. Zaimplementować usuwanie maksimum z listy.
    4. Zaimplementować sortowanie przez wstawianie lub sortowanie przez wybieranie na podstawie powyższych funkcji
'''

# (1)
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
# (2)
def insert_node(first, node):
    if first is None:
        return node
    if node.val < first.val:
        node.next = first
        return node
    
    prev = first
    while prev.next is not None and node.val > prev.next.val:
        prev = prev.next
    
    node.next =  prev.next
    prev.next = node
         
    return first

# (3)
# return max, first node of list without max
def find_and_delete_max(first):
    if first is None:
        return None
    
    head = Node(None, first)
    prev_max_node = head
    node = first
    
    while node.next is not None:
        if prev_max_node.next.val < node.next.val:
            prev_max_node = node
        node = node.next
    
    max_node = prev_max_node.next
    prev_max_node.next = max_node.next
    max_node.next = None
    
    return max_node, head.next

# (4)
def insertion_sort(first):
    sorted_list = None
    
    while first is not None:
        node = first
        first = first.next
        node.next = None
        insert_node(sorted_list, first)
        
    return sorted_list