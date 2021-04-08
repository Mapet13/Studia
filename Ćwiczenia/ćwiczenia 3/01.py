# zad 1 obowiazkowe: quick_sort zluzywajazy O(logn) pamieci stosu
def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        
        if (q - 1 - p) < (r - (q + 1)):
            quick_sort(A, p, q-1)
            p = q+1
        else:
            quick_sort(A, q+1, r)
            r = q-1

#zad 2 obowiazkowe: dodawanie elementu do kopca
def parent(i): return (i-1) // 2

def swap(T, i, j):
    T[i], T[j] = T[j], T[i]

def insert_to_heap(heap, x):
    heap.append(x)
    
    i = len(heap) - 1
    parent_idx = parent(i)  
    while i > 0 and heap[i] > heap[parent_idx]:
        swap(heap, i, parent_idx)
        i = parent_idx
        parent_idx = parent(i)
    
    return heap 

# zad 3: quick sort bez rekurencji
def quick_sort(arr, l, h):
    size = h - l + 1
    stack = [0] * size
    top = -1
    
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        
        p = partition(arr, l, h)
        if p-1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p-1    

        if p+1 < h:
            top += 1
            stack[top] = p+1
            top += 1
            stack[top] = h

            
#zad 4: scalenie k posortowanych list
'''
posluzymy sie kopcem minimalnym,
dodajemy do kopca pierwsze elementy z list w krotlack (element, nr kopca)
[...]
wywolujemy heapify 
[...]
jesli sie jakas tablica skonczy to wtedy znajdujemy min element z pozostałych i tam wrzucamy w korzeń

złożonosc obliczeniowa:
    O(nlog(k))
    
jeszcze jakies z dziekl i zwyciezan:
    łączymy sąsiednie listy jakoś  
'''

#zad5: struktura co ma insert, removeMin, removeMax w O(log(n))
'''
2 kopce jedyn min drugi max, element kopca -> (wskaznik na element, wskaznnik na element w 2 kpopcu)
'''

# zad6: insert i removeMedian w O(logn)
'''
minHeap i maxHeap 
'''

#zad 7: partition hoare
def partition(A, p, r):
    x = A[p]  # pivot
    i = p + 1
    j = r
    while i < j:
        while A[i] < x:
            i += 1
        while A[j] > x:
            j -= 1
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    A[p], A[i] = A[i], A[p]
         
# zad 9: znajdowanie k-tego co do wielkosci elementu dzieki qsort z randomizowanym partition