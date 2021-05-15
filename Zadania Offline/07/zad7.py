'''
Dana jest tablica symboli S oraz tablica ich częstości F
Proszę napisać funkcję która oblicza kod Huffmana dla danych, 
wypisuje każdy symbol (w kolejności z tablicy S) wraz z jegob kodem, 
oraz łączną liczbę bitów potrzebną do wypisania napisu, w którym każdy symbol występuje podaną częstość razy
'''

from queue import PriorityQueue

# S = ["a", "b", "c" ,"d", "e", "f" ]
# F = [10 , 11 , 7 , 13, 1 , 20 ]

S = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "r", "s", "t", "u", "w", "y", "z", "q"]
F = [865, 395, 777, 912, 431, 42, 266, 989, 524, 498, 415, 941, 803, 850, 311, 992, 489, 367, 598, 914, 930, 224, 517]

class Node:
    def __init__(self, v, i, l = None, r = None):
        self.i = i
        self.v = v
        self.l = l
        self.r = r
        
    def __gt__(self, node):
        if node is not None:
            return self.v > node.v
        return False
    
def get_result(S, F, node, code):
    if node.i != -1:
        F[node.i] = code
    else:
        get_result(S, F, node.l, code + "0")
        get_result(S, F, node.r, code + "1")
    
def huffman( S, F ):
    res = ["" for _ in range(len(S))]
    if len(F) == 1:
        get_result(S, res, 0, -1, "0")
    else:
        q = PriorityQueue()
    
        for i in range(len(S)):
            q.put(Node(F[i], i))
            
        while q.qsize() > 1:
            right = q.get()
            left = q.get()
            
            q.put(Node(right.v + left.v, -1, left, right))
            
        res = ["" for _ in range(len(S))]
        t = q.get()
        if t.l == t.r == None:   
            get_result(S, res, t, "0")
        else:
            get_result(S, res, t, "")
            
    sum = 0
    for i in range(len(S)):
        print(f"{S[i]}: {res[i]}")
        sum += len(res[i]) * F[i]
    print(sum)
        
  
  
huffman( S, F )