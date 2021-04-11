'''
knapsack problem działajacy w czasie O(n*(suma wartości))
'''
def knapsack(W, P, maxW):
    n = len(W)
     
    Sp = 0
    for i in range(n):
        Sp += P[i]
        
    F = [[maxW + 1]*(Sp + 1) for _ in range(n)] 
    
    F[0][P[0]] = W[0]
                
    for i in range(1, n):
        F[i][0] = 0
        for j in range(1, Sp+1):
            F[i][j] = F[i-1][j]
            if j >= P[i]:
                F[i][j] = min(F[i][j], W[i] + F[i-1][j-P[i]])
    
    i = Sp
    while i > 0 and F[n-1][i] > maxW:
        i -= 1
    
    return i, F

def get_solution(F, W, P, i, w_left, c):
    if i < 0: return []
    if i == 0:
       if w_left >= W[0]: return [0]    
       return []
    if F[i-1][c] > F[i][c]:
        return get_solution(F, W, P, i-1, w_left - W[i], c - P[i]) + [i]
    return get_solution(F, W, P, i-1, w_left, c) 

P = [10, 8, 100, 4, 5, 3, 7]
W = [4, 5, 100, 12, 9, 1, 13]
maxW = 24

res, F = knapsack(W, P, maxW)
sol = get_solution(F, W, P, len(P)-1, maxW, res)

for x in F:
    print(x)

print()
print()

print(f"{res}:")
for i in sol:
    print(f"{P[i]:3d} --- {W[i]:3d}") 