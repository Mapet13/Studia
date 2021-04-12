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
    
    def recur(A, parent, i, arr = []):
        arr = [A[i]] + arr
        
        if parent is None:
            for j in range(len(arr)):
                print(arr[j], end=" ") 
            print()
            
        while parent is not None:
            recur(A, P[parent.value], parent.value, arr)
            parent = parent.next
    
    while Parents != None:
        recur(A, P[Parents.value], Parents.value)
        Parents = Parents.next

        
A = [10*k+i for k in range(8) for i in range(6,0,-1)]
#print(len(A))
#print(A)

#A = [1, 2, 3, 5, 2, 3, 4]

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
