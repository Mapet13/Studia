'''
Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, 
zwraca wartość True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 
oraz wartość False w przeciwnym przypadku.
'''

#with bonus tab
# def is_correct_tab(t):
#     n = len(t)
    
#     t_col = [False] * n
    
#     for i in range(n):
#         zero_in_row = False
#         for j in range(n):
#             if t[i][j] == 0:
#                 zero_in_row = True
#                 t_col[j] = True
#                 break
#         if not zero_in_row:
#             return False
    
#     for i in range(n):
#         if t_col[i] == False:
#             return False
    
#     return True

def is_correct_tab(t):
    n = len(t)
    
    for i in range(n):
        zero_in_row = False
        zero_in_col = False
        for j in range(n):
            if t[i][j] == 0:
                zero_in_row = True
            if t[j][i] == 0:
                zero_in_col = True
            if zero_in_row and zero_in_col:
                break
        if not zero_in_row or not zero_in_col:
            return False
    
    return True
    
tab = [
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1],
]
print(is_correct_tab(tab))

tab = [
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 1, 0],
]
print(is_correct_tab(tab))

tab = [
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
]
print(is_correct_tab(tab))

        
