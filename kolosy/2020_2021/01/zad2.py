def distance(T):
    n = len(T)
    
    # indeksy wiersza z najwiekszą liczba i najmniejszą
    najwieksza = 0
    najmniejsza = 0
    
    # na początku wypełniam obie tablice wartościami z 1 wiersza
    max_val = [0] * n
    min_val = [0] * n
    for x in range(n):
        max_val[x] = T[0][x]
        min_val[x] = T[0][x]
    
    for i in range(1, n): # iteruje po kolejnych wierszach
        spr_czy_najmniejsza = True
        for j in range(n): # iteruje przez kolejne cyfry 
            if max_val[j] == T[i][j]: spr_czy_najmniejsza = False
            if max_val[j] < T[i][j]: 
                najwieksza = i
                for x in range(n):  # przepisuje wartośc aktualnego wiersza do tablicy składującej najwieksza wartość
                    max_val[x] = T[i][x]
                break   # kończę przeszukiwac aktualny wiersz
            elif spr_czy_najmniejsza and min_val[j] > T[i][j]:
                najmniejsza = i
                for x in range(n):   # przepisuje wartośc aktualnego wiersza do tablicy składującej najmniejszą wartość
                    min_val[x] = T[i][x]
                break # kończę przeszukiwac aktualny wiersz
    
    return abs(najwieksza - najmniejsza)
# end def
