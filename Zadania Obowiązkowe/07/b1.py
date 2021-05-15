# dojedz do stacji [i]
# jesli stacja [i] jest najtansza z tych do ktorych ma zasieg:
    # zatankuj min(min tyle by zasieg zwiekszyl sie do nastepnej tanszej stacji, do pełna) 
# jesli nie:
    # jedz do [i + 1] stacji
    
'''
dowod poprawnosci:

    jesli zatankujemy wiecej na stacji najtanszej do ktorej w momencie wjechania na stacje ma sie zasieg:
        - sprzecznosc przepłaca sie 
    jesli zatankuje sie na drozszej stacji:
         - sprzecznosc przepłaca sie     

'''

from math import inf

def min_price(S, P, L, T):
    currentL = L;
    current_pos = 0
    price_count = 0
    
    S.append(T) # just to keep it simple
    P.append(-inf)
    
    for i in range(len(S) - 1):
        currentL -= (S[i] - current_pos) 
        current_pos = S[i] 
        
        j = i + 1

        current_min_price = i
        while j < len(S) and currentL >= (S[j] - current_pos):
            current_min_price = min(current_min_price, j, key=P.__getitem__)
            j += 1  
            
        if current_min_price == i: # if we tank on current station
            while L >= (S[j] - current_pos):
                if P[j] < P[i]:
                    price_count += P[i] * ((S[j] - current_pos) - currentL) # tank as little as possible to came to next chipest station
                    currentL = S[j] - current_pos;
                    break
                j += 1
            else: # if current station is the chipest in max range just tank maximum
                price_count += P[i] * (L - currentL)
                currentL = L
    
    return price_count
                
S = [8, 11, 15, 16]
P = [40, 7, 15, 12]
t = 23

print(min_price(S, P, 10, t))

l = 14
S = [1, 9, 15, 16, 17, 27, 28]
P = [1, 100, 10, 15, 1, 30, 30]
t = 30
print(min_price(S, P, l, t))
    