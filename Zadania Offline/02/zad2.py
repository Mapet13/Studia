from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None
    



def qsort( L ):  
  def append(to_L, from_L):
    to_L.next = from_L
    from_L = from_L.next
    to_L = to_L.next 
    return to_L, from_L
  
  def sort(L):
    # warunek kończący rekurencje (pustej albo jednolemenetowej listy nie trzeba sortować)
    if L is None or L.next is None:
      return L, L
    
    # tworze wartownikow do wygodniejszego wstawiania do list pomocniszych
    lesser = Node()
    equal = Node()
    greater = Node()
    
    #zapamietuje poczatki list pomocniczych
    lesser_head = lesser
    equal_head = equal
    greater_head = greater
    
    pivot = L # pivotem zostaje pierwszy element listy
    
    # iteruje przez liste i dopinam kolejne elementy do odpowiednich list pomocniczych 
    while L is not None:
      if L.value < pivot.value:
        lesser, L = append(lesser, L) 
      elif L.value > pivot.value:
        greater, L = append(greater, L) 
      else:
        equal, L = append(equal, L) 
      
    #usuwam wartownikow  
    greater_head = greater_head.next
    lesser_head = lesser_head.next
    equal_head = equal_head.next
    
    # przed rekurenycjnym wywołaniem na listach pomocniczych upewniam sie ze nie wskazuja na inne elementy
    lesser.next = None
    greater.next = None
    
    # wywołuje rekurencyjnie quick sort na elementach mniejszych i wiekszych od Pivota
    greater_head, greater_tail = sort(greater_head)
    lesser_head, lesser_tail = sort(lesser_head)
    
    head = None
    # dopinam listy pomocnicze aby stanowiły razem liste wynikową
    if lesser_head is not None:
      head = lesser_head
      lesser_tail.next = equal_head
    else:
      head = equal_head
    equal.next = greater_head
    if greater_tail is None:
      tail = equal
    else:
      tail = greater_tail
    
    return head, tail
    
  return sort(L)[0]





def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")


