# BST tree node prev and next


class BST_Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        
def min(node):
    if node is None: return None
    
    while node.left is not None:
        node = node.left
        
    return node

def max(node):        
    if node is None: return None
    
    while node.right is not None:
        node = node.right
        
    return node


def next(node):
    if node is None: return None
    if node.right is not None: return min(node.right)
    else:
        parent = node.parent
        while parent is not None:
           if node == parent.left: return parent
           node = parent
           parent = node.parent  
        return None
        

def prev(node):
    if node is None: return None
    if node.left is not None: return max(node.left)
    else: 
        parent = node.parent
        while parent is not None:
           if node == parent.right: return parent
           node = parent
           parent = node.parent  
        return None
    


def set_left_child(node, child):
    node.left = child
    child.parent = node
    
def set_right_child(node, child):
    node.right = child
    child.parent = node


node_20 = BST_Node(20)
node_10 = BST_Node(10)
node_5 = BST_Node(5)
node_15 = BST_Node(15)
node_13 = BST_Node(13)
node_27 = BST_Node(27)
node_22 = BST_Node(22)
node_30 = BST_Node(30)
node_28 = BST_Node(28)
node_35 = BST_Node(35)
node_40 = BST_Node(40)

set_left_child(node_20, node_10)
set_left_child(node_10, node_5)
set_left_child(node_15, node_13)
set_left_child(node_27, node_22)
set_left_child(node_30, node_28)

set_right_child(node_20, node_27)
set_right_child(node_10, node_15)
set_right_child(node_27, node_30)
set_right_child(node_30, node_35)
set_right_child(node_35, node_40)

print(max(node_20).key)
print(min(node_20).key)

print(max(node_30).key)
print(min(node_30).key)

print(next(node_20).key)
print(prev(node_20).key)

print(next(node_15).key)
print(prev(node_15).key)

print(prev(node_40).key)

node_16 = BST_Node(16)
node_17 = BST_Node(17)
node_18 = BST_Node(18)

set_right_child(node_15, node_16)
set_right_child(node_16, node_17)
set_right_child(node_17, node_18)

print("--------------")

print(next(node_20).key)
print(prev(node_20).key)

print(next(node_15).key)
print(prev(node_15).key)

print(next(node_18).key)
print(prev(node_18).key)


node_21 = BST_Node(21)
node_20_5 = BST_Node(20.5)
node_20_25 = BST_Node(20.25)

set_left_child(node_22, node_21)
set_left_child(node_21, node_20_5)
set_left_child(node_20_5, node_20_25)

print("--------------")


print(next(node_20).key)
print(prev(node_20).key)

print(next(node_22).key)
print(prev(node_22).key)

print(next(node_20_25).key)
print(prev(node_20_25).key)



