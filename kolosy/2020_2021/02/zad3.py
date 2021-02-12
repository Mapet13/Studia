def chess(T):
    n = len(T)
    
    sum_elements = 0
    for j in range(n):
        sum_elements += T[0][j]
    wiersz1 = 0
    #szukam wiersza o najwiekszej sumie
    for i in range(1, n):
        s = 0
        for j in range(n):
             s += T[i][j]
        if s > sum_elements:
            sum_elements = s
            wiersz1 = i
    
    kolumna1 = 0
    sum_elements = 0
    for j in range(n):
        if j != wiersz1:
            sum_elements += T[j][0]
    # wybieram kolumne dla najlepszego wiersza
    for i in range(1, n):
        s = 0
        for x in range(n):
            if i != wiersz1:
                s += T[x][i]
        if s > sum_elements:
            sum_elements = s
            kolumna1 = i
            
    # zeruje tą kolumne i wiersz:
        for j in range(n):
            if j != wiersz1: 
                T[j][kolumna1] = 0
            if j != kolumna1: 
                T[wiersz1][j] = 0
    
    #powtarzam dla 2 wiezy
    
    sum_elements = 0
    for j in range(n):
        sum_elements += T[0][j]
    wiersz2 = 0
    #szukam 2 wiersza o najwiekszej sumie
    for i in range(1, n):
        s = 0
        for j in range(n):
             s += T[i][j]
        if s > sum_elements:
            sum_elements = s
            wiersz2 = i
            
    
    kolumna2 = 0
    sum_elements = 0
    for j in range(n):
        if j != wiersz2:
            sum_elements += T[j][0]
    # wybieram 2 kolumne dla najlepszego wiersza
    for i in range(1, n):
        s = 0
        for x in range(n):
            if x != wiersz2:
                s += T[x][i]
        if s > sum_elements:
            sum_elements = s
            kolumna2 = i
            
    return (wiersz1, kolumna1, wiersz2, kolumna2)
#end

print(chess([[4,0,2],[3,0,0],[6,5,3]])) # (0,1,1,0) suma=17
print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]])) # (2,3,3,1) suma=35