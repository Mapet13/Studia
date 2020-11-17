'''
Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). 
Położenie hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] 
Proszę napisać funkcję, która odpowiada na pytanie: 
czy żadne dwa hetmany się nie szachują?
Do funkcji należy przekazać położenie hetmanów.

hetman == królowa
'''

def are_they_in_check(data):
    n = len(data)
    t = [[False for _ in range(100)] for _ in range(100)]
    
    for i in range(n):
        w, k = data[i]
        if t[w][k]:
            return True
        else:
            t[w][k] = True
        
        #góra, dół, boki    
        for p in range(100):
            if (p != w and t[p][k]) or (p != k and t[w][p]):
                return True
        
        # skosy (ugly code alert)
        o = 1
        c = [True] * 4
        while(c[0] or c[1] or c[2] or c[3]):
            if w + o >= 100:
                c[0] = False
            if w - o < 0:
                c[1] = False
            if o + k >= 100:
                c[2] = False
            if k - o < 0:
                c[3] = False    
            
            if c[1] and c[3]:
                if t[w - o][k - o]:
                    return True
            if c[1] and c[2]:
                if t[w - o][k + o]:
                    return True
            if c[0] and c[3]:
                if t[w + o][k - o]:
                    return True
            if c[0] and c[2]:
                if t[w + o][k + o]:
                    return True
            
            o += 1 
                
    return False

                    
tab = [
    (4, 3),
    (0, 0),
    (7, 5),
    (1, 4)
]
print(are_they_in_check(tab))

tab = [
    (4, 3),
    (0, 0),
    (7, 5),
    (1, 4),
    (5, 7)
]
print(are_they_in_check(tab))
    
    

