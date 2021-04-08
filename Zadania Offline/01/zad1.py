from random import randint, seed




def mergesort(T):
  def merge(T, x, c, y):
    temp = [T[i+x] for i in range(y + 1 - x)] # tablica pomocnicza trzymajaca wartości z obu scalanych połówek 
    
    i = x
    l = x
    r = c+1
    while l <= c and r <= y:   # dołączam kolejne elementy z tablicy pomocniczej w odpowiednie miejsca w tablicy głównej
      if temp[l-x] < temp[r-x]: # dołączenie elementu z lewej częsci
        T[i] = temp[l-x]
        l += 1
      else:                     # dołączenie elementu z prawej częsci
        T[i] = temp[r-x]
        r += 1
      i += 1
      
    while l <= c: # dołaczam pozostałe elementy z lewej połowy jeśli jakieś pozostały
      T[i] = temp[l-x]
      l += 1
      i += 1
      
    while r <= y: # dołaczam pozostałe elementy z prawej połowy jeśli jakieś pozostały
      T[i] = temp[r-x]
      r += 1
      i += 1
      
  
  def sort_recursively(T, x, y):
    if x < y:               # warunek rekurencji
      c = (x + y) // 2      # wyznaczam indeks środka sortowanej części
      
      sort_recursively(T, x, c)   # posortuj lewą połowę tablicy (rekurencyjnie)
      sort_recursively(T, c+1, y) # posortuj prawą połowę tablicy (rekurencyjnie)
      merge(T, x, c, y)           # scal posortowanie półówki w jedną, posortowaną tablicę
    
  
  sort_recursively(T, 0, len(T)-1) # wywołanie dla całej tablicy
  
  return T
  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")
