'''
Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników. 
Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2
'''

def print_all(n, original = -1, l = 1, s = ""):
    if original == -1:
        original = n
    
    if n < l or l == original:
        return
    
    if n == l:
        print(s + str(l))
    
    print_all(n - l, original, l, str(l) + " + " + s)
    print_all(n, original, l + 1, s)
    

print_all(4)