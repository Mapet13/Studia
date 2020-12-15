'''

Wynik:

Wiersze:  0  1  2  3  4  5  6  7
  T[8]:  [2][4][1][ ][ ][ ][ ][ ]
Kolumny ^^^

Pomocnicze:

wiersze/kolumny T0[8]: [ ][T][T][ ][T][ ][ ] 
przekatne 1    T1[15]: [ ][ ][ ][ ][T][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
przekatne 2    T2[15]: [ ][ ][ ][ ][T][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
'''

def hetmany(N):
    t = [-1 for _ in range(N)]
    
    t0 = [False for _ in range(N)]
    t1 = [False for _ in range(2*N - 1)]
    t2 = [False for _ in range(2*N - 1)]
    
    stop = False
    
    def hetman(w, k):    
        nonlocal stop
        
        if w == N:
            rysuj(t)
            stop = True
            return
                    
        if t0[k] or t1[w+k] or t2[N - 1 + k - w]:
            return
        
        t0[k] = t1[w + k] = t2[N - 1 + k - w] = True
        t[w] = k
        
        for i in range(N):
            if stop:
                return 
            if (w == N - 1 and i > 0):
                break
            hetman(w+1, i)
        
        t0[k] = t1[w+k] = t2[N-1+k-w] = False
       
    def rysuj(tab):
        for i in range(len(tab)):
            for j in range(len(tab)):
                if t[i] == j:
                    print("0 ", end='')
                else:
                    print("- ", end='')   
            print()
        
        print()        
            
       
    for i in range(N):
        hetman(0, i)
        
    
hetmany(20)     
            