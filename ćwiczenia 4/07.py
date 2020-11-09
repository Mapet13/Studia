'''
Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: 
T1[N][N] i T2[M], gdzie M=N*N. 
W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby naturalne. 
Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
powinny zawierać zera.
'''

def f(t1, t2):
    n = len(t1[0])
    m = n * n
    
    for i in range(n):
        t2[i] = t1[0][i]
    
    last = n
    
    for i in range(1, n):
        min_i = 0
        for j in range(n):
            max_i = last
            inserted = False
            while not inserted:
                c = (max_i+min_i) // 2 # zawsze zaokraglane w dół (czyli jak max = min+1 => c = min)
                if t2[c] == t1[i][j] or max_i == min_i:
                    for x in range(last, c, -1):
                        t2[x] = t2[x-1]
                    t2[c] = t1[i][j]
                    inserted = True
                    last += 1
                if t2[c] > t1[i][j]:
                    max_i = c
                elif t2[c] < t1[i][j]:
                    min_i = c + 1

                
    
t2 = [9 for _ in range(16)] 
tab = [
    [3, 5, 7, 11],
    [0, 1, 3, 4],
    [11, 19, 20, 27],
    [2, 5, 11, 19],
]
f(tab,t2)
print(t2)

t2 = [11 for _ in range(16)] 
tab = [
    [1, 2, 3, 4],
    [6, 7, 8, 9],
    [12, 13, 14, 16],
    [20, 21, 22, 23],
]
f(tab,t2)
print(t2)
            
            
        
    