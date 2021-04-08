from random import randint, shuffle, seed

def linearselect( A, k ):
  def swap(A, x, y):
    A[x], A[y] = A[y], A[x]
  
  def medianof5(A, p, r): # na podstawie insertion sort (sortuje i zwracam indeks środkowego elementu)
    for i in range(p+1, r+1):
        j = i
        while j > p and A[j-1] > A[j]: 
            swap(A, j, j-1)
            j -= 1
    return (p+r) // 2
  
  def getpivot(A, p, r):
    if r - p < 5: # gdy elementow jest 5 lub mniej to jest tylko jedna grupa wiec jej mediana będzie "medianą median"
      return medianof5(A, p, r)
    for i in range(p, r+1, 5): # iteruje po grupach
      right = min(i+4, r) # ostatni element z grupy (obliczane, bo ostatnia grupa moze byc mniejsza)
      swap(A, medianof5(A, i, right), p + ((i-p)//5)) # ustawiam wstawiam kolejne mediany na poczatek listy
    mid = ((r-p) // 10) + p # wyznaczam pozycje na ktorej bedzie mediana median 
    return select(A, p, p+((r - p)//5), mid) # przy uzyciu select wyznaczam mediane median (szukam środkowego elementu na częsci gdzie powstawiałem mediany z poszczególnych grup)
  
  def partition(A, p, r): # standardowe partition z tą róznicą że wyznczam pivota na podstawie magicznych piątek
    pivot = getpivot(A, p, r)
    swap(A, pivot, r)
    i = p - 1
    for j in range(p, r):
        if A[j] <= A[r]:
            i += 1
            swap(A, i, j)
    swap(A, i+1, r)
    return i+1
  
  def select(A, p, r, k): # algorytm select jak na wykładzie
    if p == r:
      return A[p]
    q = partition(A, p, r)
    if q == k:
      return A[q]
    elif k < q:
      return select(A, p, q - 1, k)
    else:
      return select(A, q + 1, r, k)
    
  return select(A, 0, len(A)-1, k) # wywołanie select na całej tablicy A

seed(42)

n = 11
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = linearselect( A, i )
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)
    
print("OK")

