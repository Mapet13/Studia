def knapsack(W, P, maxW):
    n = len(W)
    F = [[0]*(maxW + 1) for _ in range(n)]
    
    for i in range(W[0], maxW + 1):
        F[0][i] = P[0]
    
    
    for i in range(1, n):
        for w in range(1, maxW + 1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]] + P[i])
                
    return F[n-1][maxW], F

def get_solution(F, W, P, i, w):
    if i < 0: return []
    if i == 0:
        if w >= W[i]: return [0]
        return []
    if w >= W[i] and F[i][w] == F[i-1][w-W[i]] + P[i]:
        return get_solution(F, W, P, i-1, w-W[i]) + [i]
    return get_solution(F, W, P, i-1, w)

P = [10, 8, 4, 5, 3, 7, 100]
W = [4, 5, 12, 9, 1, 13, 100]
maxW = 24

res, F = knapsack(W, P, maxW)
sol = get_solution(F, W, P, len(P)-1, maxW)

for x in F:
    print(x)

print()
print()

print(f"{res}:")
for i in sol:
    print(f"{P[i]:3d} --- {W[i]:3d}") 