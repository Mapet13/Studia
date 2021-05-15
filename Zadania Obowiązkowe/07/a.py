# dojedz do stacji [i]
# jesli ma paliwa na dotarcie do stacji [i + 1]
    # jedz do stacji [i + 1]
# jesli nie
    # zatankuj do pełna 
'''
dowod poprawnosci:

jesli optymalna trasa po stacjach zakladala by 
tankowanie na stacji [k] w momencie gdy mozna dojechac do stacji [k + 1]
to na stacji [k+1]:
    - albo bedziemy mieli dosc paliwa na dojechanie na stacje [k + 2]
        ...
        -  na stacjach [k + n]:
            - jesli trzeba tankowac i tankujac na stacji [k+1] zamiast [k] tez by trzeba bylo:
                to nasze rozwiazanie jest równiez optymalne
            - jesli trzeba tankować a nie musielibysmy tankujac na stacji [k+1] zamiast [k]:
                - sprzecznosc: tankujemy wiecej razy niz jakbysmy poczekali i zatankowali raz na stacji [k+1]
    - albo nie i wtedy bedziemy musieli znowu tankować:
        - sprzecznosc: tankujemy wiecej razy niz jakbysmy poczekali i zatankowali raz na stacji [k+1]
'''

def min_count(S, L, T):
    count = 0
    currnetL = L
    recent = 0
    
    for i in range(len(S)): # check if should tank
        if S[i] > T: break
                
        if currnetL <= (S[i] - recent):
            currnetL = L
            count += 1
            recent = S[i]
        
    if currnetL <= (T - recent): # check if should tank on last station
        return count + 1
    
    return count
