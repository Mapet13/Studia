'''
Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy w zapisie dwójkowym
posiadał nieparzystą liczbę jedynek.
'''

def can_correct_remove(t):
    
    def has_odd_count_of_one_in_binary(num):
        count = 0
        while num > 0:
            count += num % 2
            num //= 2
        return (count % 2 == 1)
        
        
    n = len(t)
    
    r_row = -1
    r_col = [-1, -1]
    
    marked_element = [-1, -1]
    
    for i in range(n):
        for j in range(n):
            if i != r_row or j != r_col[0] or j != r_col[1]:
                if not has_odd_count_of_one_in_binary(t[i][j]):
                    if marked_element[0] == -1:
                        marked_element[0] = i
                        marked_element[1] = j
                    elif r_row != -1 and r_col[0] != -1 and r_col[1] != -1:
                        return False
                    elif r_row != -1:
                        if r_col[0] != -1:
                            r_col[0] = j
                        else:
                            r_col[1] = j
                    elif r_col[0] != -1 and r_col[1] != -1:
                        r_row = i
                    elif marked_element[0] == i:
                        r_row = i
                    elif marked_element[1] == j:
                        if r_col[0] != -1:
                            r_col[0] = j
                        else:
                            r_col[1] = j
                    else:
                        return False
                    
    return True


tab = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
]
print(can_correct_remove(tab))
            
tab = [
    [1, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
]
print(can_correct_remove(tab))