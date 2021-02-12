'''
w = 4
k = 5

T[w][k]:
[T][F][F][T][T]
[F][T][F][F][T]
[T][F][F][T][F]
[F][T][F][F][T]

Tk[k]:
            0  1  2  3  4
           [V][V][V][V][V]
Tw[w]  0[>][V]>             |
       1[>]            [ ]> | none
       2[>]   [ ]>      V   |
       3[>]    V            |
            -------------
                none
class :
    right
    down

'''
from random import choice


class Node:
    def __init__(self):
        self.right = None
        self.down = None
        
W = 4
K = 5
T = [[choice([True, False]) for _ in range(K)] for _ in range(W)]        

TW = [None for _ in range(W)]
TK = [None for _ in range(K)]

for w in range(W-1, -1, -1):
    for k in range(K-1, -1, -1):
        if T[w][k]:
            head = Node()
            head.right = TW[w]
            head.down = TK[k]
            TW[w] = TK[k] = head
                       
