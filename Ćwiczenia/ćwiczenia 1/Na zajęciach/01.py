#sortoanie bąbelkowe

def bubbl_sort(arr):
    n = len(arr)
    
    for i in range(n-1): # n-1 bo po posorotwaniu n-1 liczb ostatnia napewno tez bedzie posortowana
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    
#list insertion sort

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def insert_value(first, val):
    if first is None:
        return Node(val)
    if val < first.val:
        return Node(val, first)
    
    prev = first
    while prev.next is not None and val > prev.next.val:
        prev = prev.next
    
    new = Node(val, prev.next)
    prev.next = new
         
    return first
    
def insert_node(first, node: Node):
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


def find_and_delete_max(head):
    prev_max_node = head
    first_node = head
    
    while head.next is not None:
        if prev_max_node.next.val < head.next.val:
            prev_max_node = head
        head = head.next
    
    max_node = prev_max_node.next
    if first_node.value > max_node.value:
        max_node = first_node
    else:
        prev_max_node = max_node.next
    
    max_node.next = None
    
    return max_node
            
def insertion_sort(head):
    sorted_list = Node()
    first_node = head
    
    while head.next is not None:
        max_node, head = find_and_delete_max(head)
        insert_node(sorted_list, max_node)
        
########################################################################################################

def reverse(first):
    reverse_first = None
    while first is not None:
        temp = first.next
        first.next = reverse_first
        reverse_first = first
        first = temp
        
    return reverse_first