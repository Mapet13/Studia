'''
Dana jest tablica T[N][N]. 
Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami naturalnymi po spirali.

00 01 02    1 2 3
10 11 12 -> 8 9 4
20 21 22    7 6 5

'''

n = 10
tab = [[0] * n for _ in range(n)]

current_x_change = 0
current_y_change = 1
x = 0
y = 0

i = 1
while tab[x][y] == 0:
    tab[x][y] = i
    
    if  x + current_x_change >= n or (current_x_change != 0 and tab[x+current_x_change][y] != 0):
        current_y_change = -current_x_change
        current_x_change = 0
    elif y + current_y_change >= n or (current_y_change != 0 and tab[x][y+current_y_change] != 0):
        current_x_change = current_y_change
        current_y_change = 0
    
    x += current_x_change
    y += current_y_change 
    i += 1
                   
        
for i in range(n):
    print(tab[i])
        