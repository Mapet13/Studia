def subsetSum(A, T):
    n = len(A)
    poss = [[False for i in range(T+1)] for j in range(n+1)]
    
    for i in range(n):
        poss[i][0] = True
        
    for item_num in range(1, n+1):
        for suma in  range(1, T+1):
            poss[item_num][suma] = (poss[item_num-1][suma] or poss[item_num-1][suma - A[item_num]])
    
    return poss[n][T]