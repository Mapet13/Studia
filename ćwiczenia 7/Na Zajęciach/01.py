class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
'''
czy element nalezy do zbioru
'''     
def contains(first, val):
    while first != None and first.value < val:
        first = first.next
        
    return first != None and first.value == val

def contains_rec(first, val):
    if first == None or first.value > val:
        return False
    return first.value == val or contains_rec(first.next, val)
'''
wstawianie do zbioru
'''
def wstaw(pointer, x):
    p = pointer 
    q = Node
    
    while p != None and p.value < x:
        q = p
        p = p.next
    
    if p != None and p.value == x:
        return pointer
    
    r = Node(x)
    r.next = p
    
    if q == None:
        return r
    
    q.next = r
    return pointer

'''
wartownik: (X|->) - wartownik zawsze isnieje, gdy tworze liste tworze wartownika,
                    wiec nie ma wstawiania na poczatek bo tam bedzie wartownik
    f->(X|->)[2|->][3|->][5|->][7|->None]
            ^1    ===    ^2
        przypadek teraz jest jeden

wartownik moze być tez na końcu ...[7|->](DUZA LICZBA|->none) aby:
    while p != None and p.value < x:    -->    while p.value < x: 

-------------------------------------------------------------------------------

class Zb:
    __init__():
        ...

z1 = Zb()
    ^-- wtedy np nie musze zwracac pierwszego elemenu bo odrazu updatuje wartości w z1
'''



   
    
        