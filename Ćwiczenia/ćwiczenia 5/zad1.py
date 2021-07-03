def knapsack(W, P, MaxW):
    n = len(P)
    sum_of_value = sum(P)
    
    #F[i] - najmniejsza waga o łącznej wartości i
    F=[-1] * (sum_of_value + 1)
    F[0] = 0
    
    for i in range(n):
        for j in range(sum_of_value, -1 , -1):
            if F[j] >= 0:
                if F[j+P[i]] == -1:
                    F[j+P[i]] = F[j] + W[i]
                else:
                    F[j+P[i]] = min(F[j] + W[i], F[j+P[i]])
                    
    res = 0
    for i in range(sum_of_value + 1):
        if MaxW >= F[i] >= 0:
            res = max(res, i)
    
    return res
                
    