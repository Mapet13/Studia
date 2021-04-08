'''
Proszę zaimplementować jeden ze standardowych algorytmów sortowania tablicy działający w czasie O(n^2) 
(np. sortowanie bąbelkowe, sortowanie przez wstawianie, sortowanie przez wybieranie).
'''

def swap(tab, x, y):
    tab[x], tab[y] = tab[y], tab[x]

######################################################
def bubble_sort(tab):
    n = len(tab)
    
    for i in range(n-1):
        for j in range(n-1-i):
            if tab[j] > tab[j+1]:
                swap(tab, j, j+1)

t = [3, 4, 1, 5, 2, 7, 10, 9]
bubble_sort(t)
print(t)
######################################################
def seletion_sort(tab):
    n = len(tab)
    
    for i in range(n-1):
        min_id = i
        for j in range(i+1, n):
            if tab[j] < tab[min_id]:
                min_id = j 
        
        if min_id != i:
            swap(tab, i, min_id)
    

t = [3, 4, 1, 5, 2, 7, 10, 9]
seletion_sort(t)
print(t)
######################################################
def insertion_sort(tab):
    n = len(tab)
    
    for i in range(1, n):
        j = i
        while j > 0 and tab[j-1] > tab[j]: 
            swap(tab, j, j-1)
            j -= 1
    

t = [3, 4, 1, 5, 2, 7, 10, 9]
insertion_sort(t)
print(t)
######################################################