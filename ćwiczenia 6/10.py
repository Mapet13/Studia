'''
Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)
'''

def det(matrix):
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    
    det_value = 0
    for i in range(n):
        if matrix[0][i] != 0:
            s = (-1)**i
            smaller_matrix = [[matrix[x][y] if y < i else matrix[x][y+1] for y in range(n-1)] for x in range(1, n)]
            det_value += s * matrix[0][i] * det(smaller_matrix)
        
    return det_value
    
M = [
    [2, 3],
    [-1, 7]
] 
print(det(M)) # -17     
    
M = [
    [2, 5, 0],
    [-1, -3, 0],
    [0, 4, 2],
]
print(det(M)) # -2     
        
M = [
    [7, 6, 5, 4, 4, 2],
    [9, 7, 8, 9, 3, 3],
    [7, 4, 9, 7, 0, 0],
    [5, 3, 6, 1, 0, 0],
    [0, 0, 5, 6, 0, 0],
    [0, 0, 6, 8, 0, 0]
]
print(det(M)) #24   