'''
Proszę zaimplementować funkcję printAllLIS( A ), 
która otrzymuje na wejściu tablicę liczb naturalnych A i wypisuje na ekran 
wszystkie najdłuższe ciągi rosnące oraz zwraca ich liczbę.
'''

class Node:
    def __init__(self, next = None, val = None):
        self.next = next
        self.value = val
        

def lis(A):
    N = len(A)
    F = [1] * N
    P = [None for _ in range(N)]
    
    for i in range(1, N):
        parents = None
        current_best = 0
        for j in range(i-1, -1, -1):
            if A[j] < A[i] and F[j] + 1 >= F[i]:
                F[i] = F[j] + 1
                if F[j] == current_best:
                    parents = Node(parents, j)
                else:
                    parents = Node(None, j)
                    current_best = F[j]
        P[i] = parents
    
    return max(F), F, P

def print_solution(A, P, Parents):
    
    def recur(A, P, i):
        if P[i] == None:
           print(A[i], end=' ')
           return True
       
        if recur(A, P, P[i].value):
            P[i] = P[i].next
            
        print(A[i], end=' ')
        return P[i] == None
    
    while Parents != None:
        i = Parents.value
        if recur(A, P, i):
            Parents = Parents.next
        print()

        
A = [13, 7, 21, 42, 8, 2, 44, 53]
_, F, P = lis(A)

parents = None
current_best = 0
for i in range(len(A)):
    if F[i] == current_best:
        parents = Node(parents, i)
    elif F[i] > current_best:
        parents = Node(None, i)
        current_best = F[i]
        
print_solution(A, P, parents)
