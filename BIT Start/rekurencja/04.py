def f(T, i = 0, j = 0):
    '''
    if i == j == len(T)-1:
        return True
    
    result = False
    if j+1 > len(T)-1 and T[i][j] < T[i][j+1]:
        result = f(T, i, j + 1)
    if i+1 > len(T)-1 and not result and T[i][j] < T[i+1][j]:
        result = f(T, i + 1, j)
        
    return result
    '''
    if i == j == len(T) - 1:
        return True
    
    if i < len(T)-1 and T[i+1][j] > T[i][j]:
        if f(T, i+1, j):
            return True
        
    if j < len(T)-1 and T[i][j+1] > T[i][j]:
        if f(T, i, j+1):
            return True
        
    return False
        

t = [
    [0, 100, 100, 100],
    [1, 100, 100, 100],
    [2, 3, 100, 100],
    [3, 4, 5, 6],
]
print(f(t))
        
        