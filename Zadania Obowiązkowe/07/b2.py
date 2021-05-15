'''
f(i) - oblicza min koszt dotarcia ze stacji i do T startujac z full paliwem

f(i) = {
    if starczy paliwa do konca: 0
    else:
        j = i + 1
        current_min = F[j] + Koszt tankowania na stacji j 
        while (starczy na dotarcie do stacji j):
            current_min = min(current_min, F[j+1] + koszt tankowania na stacji j+1)
            j += 1
} 
'''
from math import inf


def min_price(S, P, L, T):        
    
    S = [0] + S         # just to keep it simple
    P = [inf] + P
    
    F = [None for _ in range(len(S))]
              
    def recur(S, P, L, T, F, i):        
        if F[i] != None:
            return F[i]
        
        if L >= (T - S[i]):
            F[i] = 0
            return F[i]    
            
        current_min = recur(S, P, L, T, F, i+1) + (P[i+1] * (S[i+1] - S[i]))
        j = i + 2
        while j < len(S) and L >= (S[j] - S[i]):
            current_min = min(current_min, recur(S, P, L, T, F, j) + (P[j] * (S[j] - S[i])))
            j += 1
        
        F[i] = current_min
        return F[i]
    
    return recur(S, P, L, T, F, 0)
    
    
S = [8, 11, 15, 16]
P = [40, 7, 15, 12]
t = 23

print(min_price(S, P, 10, t))

l = 14
S = [1, 9, 15, 16, 17, 27, 28]
P = [1, 100, 10, 15, 1, 30, 30]
t = 30
print(min_price(S, P, l, t))