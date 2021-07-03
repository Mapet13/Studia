def Stacje1(S, L, t):
    p = 0
    Odwiedzone =[]
    i = 0
    while (p < t):
        if t-p <= L :
            return Odwiedzone
        while (i < len(S) and S[i]-p <=L):
            i+=1

        p = S[i-1]
        Odwiedzone.append(i-1)

    return Odwiedzone
