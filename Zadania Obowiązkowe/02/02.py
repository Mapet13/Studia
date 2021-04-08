'''
implementacja wstawiania do kopca
'''

def parent(i): return (i-1) // 2

def swap(T, i, j):
    T[i], T[j] = T[j], T[i]

def insert_to_heap(heap, x):
    heap += [x] # nw czy moge uzyc append X D    
    
    i = len(heap) - 1
    parent_idx = parent(i)  
    while i > 0 and heap[i] > heap[parent_idx]:
        swap(heap, i, parent_idx)
        i = parent_idx
        parent_idx = parent(i)
    
    return heap 

T = [17, 10, 12, 1, 2, 7]
print(insert_to_heap(T, 13))