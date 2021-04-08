from math import log10, ceil


        
def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1) // 2

#--------------------------------------------------------------------------------------------------------------
# tworze tablice kubełkow  i przebiegajac po tablicy jednoczesnie tworze i dodaje do konkretnych Logn kubełkow
# wyszukanie odpowiedniego kubełka to log(log(N)) i przebiegniecie po całej tablicy to N wiec wychodzu Nlog(log(N)) FUCK    
# łącze kubełki 
#--------------------------------------------------------------------------------------------------------------

def fill_array(T, heap):
    

def sort(T):
    n = len(T)
    C = [] # heap

    for x in T:
        insert(C, x)

    fill_array(T, C)
    

    
    
    
    