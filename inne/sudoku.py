def check_digit(T, i, j, d):
    for x in range(len(T)):
        if (i != x and T[x][j] == d or 
            j != x and T[i][x] == d):
            return False

    sj = ((j // 3) * 3)
    si = ((i // 3) * 3)
    
    for x in range(3):
        for y in range(3):
            if (i != (si + y) and j != (sj + x) and T[si+y][sj+x] == d):
                return False
    
    return True


def find_next_free_after(T, i, j):
    j += 1
    if j >= 9:
        j -= 9
        i += 1
        
    if i >= 9:
        return (-1, -1)

    while T[i][j] != 0:
        j += 1
        if j >= 9:
            j -= 9
            i += 1
            
        if i >= 9:
            return (-1, -1)

    return (i, j)

def solve_rec(T, i, j):
    if i == j == -1:
        return True
    
    for d in range(1, 10):
        if check_digit(T, i, j, d):
            T[i][j] = d
            (x, y) = find_next_free_after(T, i, j)
            if solve_rec(T, x, y):
                return True
            T[i][j] = 0
        
    return False
    

def solve(T):
    i = j = 0
    if T[i][j] != 0:
        (i, j) = find_next_free_after(T, i, j)
        
    solve_rec(T, i, j) 


def print_sudoku(T):
    N = len(T)
    
    print()
    for i in range(N):
        for j in range(N):
            s = ' '
            if (j+1) % 3 == 0:
                s = '\t'
            print(T[i][j], end=s) 
        print()
        if (i+1) % 3 == 0:
            print() 

T = [
    [3, 0, 0,    4, 0, 0,    6, 0, 0],
    [7, 0, 0,    0, 9, 0,    0, 0, 3],
    [8, 0, 0,    3, 0, 0,    0, 0, 0],
    
    [0, 3, 0,    5, 2, 1,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 9, 0],
    [0, 2, 0,    0, 3, 0,    0, 4, 0],
    
    [0, 4, 8,    0, 0, 2,    0, 0, 0],
    [0, 0, 6,    0, 0, 0,    1, 0, 0],
    [0, 0, 0,    0, 0, 7,    4, 0, 0],
]

solve(T)
print_sudoku(T)

T = [
    [7, 0, 0,  0, 0, 1,  3, 0, 0],
    [2, 0, 0,  4, 8, 3,  0, 7, 0],
    [9, 0, 1,  0, 0, 0,  6, 0, 8],

    [6, 0, 3,  0, 4, 0,  0, 2, 7],
    [1, 7, 0,  0, 2, 8,  5, 0, 9],
    [0, 0, 0,  0, 3, 0,  0, 0, 0],

    [0, 1, 0,  2, 0, 4,  7, 8, 5], 
    [0, 0, 7,  0, 0, 6,  0, 0, 0],
    [0, 5, 9,  8, 0, 0,  2, 0, 0],
]

solve(T)
print_sudoku(T)