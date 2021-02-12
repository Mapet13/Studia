'''
Proszę napisać funkcję scalającą dwie posortowane listy w jedną
posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    
    def __repr__(self):
        return self.data


def iter_merge_lists(node_1, node_2):
    res_head = Node(None)
    curr_node = res_head     
    while node_1 != None and node_2 != None:
        curr_node = curr_node.next
        if node_1.data < node_2.data:
            curr_node = node_1
            node_1 = node_1.next
        else:
            curr_node = node_2
            node_2 = node_2.next
        
        
    if node_1 == None:
        curr_node.next = node_2
    else:
        curr_node.next = node_1

    return res_head.next
    
