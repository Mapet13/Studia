'''
Reszta
Proszę napisać funkcję, która dla podanej sumy i listy
nominałów wypisuje ilość możliwości na jakie możliwości
na jakie można wydać daną sumę.
'''

def reszty(suma, nominaly, index = 0, x = []):
    if suma == 0:
        return 1
    
    if suma < 0:
        return 0
    
    if index >= len(nominaly):
        return 0
    
    return reszty(suma-nominaly[index], nominaly, index, x + [nominaly[index]]) + reszty(suma, nominaly, index + 1, x)

print(reszty(5, [1, 2, 5]))
    
    
        
    