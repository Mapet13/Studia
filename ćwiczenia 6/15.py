'''
Problem 8 Hetmanów (treść oczywista)
'''

def rec(T, i = 0, j = 0, d = -1):
    n = len(T)
    
    if i == n:
        return True
    
    if j >= n:
        return False
    
    if T[i][j] == 0:
        T[i][j] = 1
        
        for x in range(1, n - i):
            if T[i + x][j] == 0: T[i+x][j] = d #down
            if j + x < n: #right diagonal
                if T[i + x][j + x] == 0: T[i + x][j + x] = d
            if j - x >= 0: #left diagonal
                if T[i + x][j - x] == 0: T[i + x][j - x] = d
           
        if rec(T, i + 1, 0, d - 1):
            return True
        else: 
            T[i][j] = 0
            for x in range(1, n - i):
                if T[i + x][j] == d: T[i+x][j] = 0 #down
                if j + x < n: #right diagonal
                    if T[i + x][j + x] == d: T[i + x][j + x] = 0
                if j - x >= 0: #left diagonal
                    if T[i + x][j - x] == d: T[i + x][j - x] = 0
                    
    return rec(T, i, j + 1, d)


# T <- [[0, 0, ...], ...]
def QueenProblem(T):
    rec(T)
    
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j] < 0:
                T[i][j] = 0




T = [[0 for _ in range(8)] for _ in range(8)]
QueenProblem(T)

for x in T:
    print(x)
    
print()    
    
T = [[0 for _ in range(20)] for _ in range(20)]
QueenProblem(T)

for x in T:
    print(x)