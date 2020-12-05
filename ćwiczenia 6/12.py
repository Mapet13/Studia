'''
Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.
'''

def count(T, product, n, i = 0, current_t = []):
    t_len = len(T)
    
    if n == 1 and product == T[i]:
        for j in range(len(current_t)):
            print(current_t[j], end = ', ')
        print(T[i])
    
    if i < t_len - n:
        count(T, product, n, i + 1, current_t)
        
    if n > 1 and product % T[i] == 0:
        count(T, product // T[i], n - 1, i + 1, current_t + [T[i]])


T = [1, 2, 3, 4, 5, 6]
    
count(T, 12, 2)
print()
count(T, 12, 3)