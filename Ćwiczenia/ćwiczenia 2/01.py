class Node:
    def __init__(self, val, next):
        self.val = val 
        self.next = next



# mamy dwie posortowane tablice i zaimplementowac scalenie ich
def mergeSortedList(list1, list2):
    newList = Node(None, None)
    current = newList
    
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
            
    if list1 is not None:
        current.next = list1
    else:
        current.next = list2
        
    return newList.next

def partition(lst):
    a = list1 = Node(None, None)
    b = list2 = Node(None, None)
    
    append_to_list1 = True
    
    p = lst
    v = p.val
    p = p.next
    
    while p is not None:
        if p.val < v:
            append_to_list1 = not append_to_list1
            
        if append_to_list1:
            a.next = p
            a = a.next
        else:
            b.next = p
            b = b.next
            
    return list1, list2
        
def merge(list1, list2):
    res = Node(None, None)
    
    v1, v2 = list1.val, list2.val
    
    if v1 < v2:
        res.next = list1
        res.next.next = list2
    else:
        res.next = list2
        res.next.next = list1
        
    list1, list2 = list1.next, list2.next      
    
    while list1 is not None and list2 is not None:
        while list1 is not None and list2 is not None and list1.next > v1 and list2 > v2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
            vi, v2 = list1.val, list2.val
            
            while list1 is not None and v1 < list1.val:
                res.next = list1
                v1 = list1.val
                list1 = list1.next

            while list2 is not None and v2 < list2.val:
                res.next = list2
                v2 = list2.val
                list2 = list2.next
    
    return res

def merge_sort(lst):
    l1, l2 = partition(lst)
    while l2.next is not None:
        lst = merge(l1, l2)
        l1, l2 = partition(lst)
        
    return lst


    
    
        
            
                      

    
    
    
    
    