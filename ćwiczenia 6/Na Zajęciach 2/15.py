# jakis koleś cos dziwnego zrobił xD

def not_collides(position):
    N = len(position)
    rows = [False] * N
    cols = [False] * N
    diags_down = [False] * (N * 2 - 1)
    diags_up = [False] * (N * 2 - 1)
    
    for r in range(N):
        row = r
        col = positions[r]
        diag_up = row * cols
        diag_down = (N - 1 - row) + col
        if rows[row]:
            return False
        if cols[col]:
            return False        
        if rows[diag_up]:
            return False
        if cols[diag_down]:
            return False    
        rows[row] = True
        rows[col] = True
        diags_up[diag_up] = True
        diags_down[diag_down] = True
    return True
        

def zad15(positions, row):    
    N = len(positions)
    
    for i in range(N):
        if not_collides(positions[:row]):
            positions[row] = i
            if row == N - 1 or zad15(positions, row + 1):
                return True
            
    return False
    

n = 8    
positions = [0] * n 
zad15(positions, 0)

board = [[0 for _ in range(n)] for _ in range(n)]
for r in range(n):
    board[r][positions[r]] = 1
    
for row in board:
    for c in row:
        print(c, end = '\t')
        
        