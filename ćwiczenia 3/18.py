'''
Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. 
Proszę napisać funkcję, która zwraca długość najdłuższego spójnego podciągu 
    będącego palindromem złożonym wyłącznie z liczb nieparzystych. 
Do funkcji należy przekazać tablicę, 
funkcja powinna zwrócić długość znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
'''

#from random import randint

def find_longest_odd_palindrom(tab):
    best = 0
    for i in range(len(tab)):
        if tab[i] % 2 != 0:
            for j in range(len(tab) - 1, i-1, -1):
                if tab[j] != tab[i]:
                    continue
                
                temp_i = i
                
                is_palindrome = True
                count = 0
                while i < j:
                    if tab[j] != tab[i] or tab[i] % 2 == 0 or tab[j] % 2 == 0:
                        is_palindrome = False
                        break
                    i += 1
                    j -= 1
                    count += 2
                    
                if i == j: 
                    if tab[i] == tab[j] and tab[i] % 2 != 0 and tab[j] % 2 != 0:
                        count += 1
                    else:
                        is_palindrome = False
                        
                if is_palindrome and count > best:
                    best = count
                    
                i = temp_i
    
    return best

#n = int(input("n: "))
#t = [randint(1, 1000) for _ in range(n)]
n = 8
t = [0, 1, 7, 3, 1, 3, 7, 1, 2, 2, 1, 7, 3, 1, 3, 5, 5, 5, 5]

print(find_longest_odd_palindrom(t))
