"""
Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. 
Ile różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. 
Np. dla 2315 będą to: 21, 35, 231, 315.
"""

from math import floor, log10

liczba = int(input("Podaj sprawdzaną liczbę: "))
div = int(input("Podaj dzielnik: "))

dc = floor(log10(liczba)) + 1

# dla 2315
# dla 1 wywołania dostaje [0, 4]
# i chce dostać wywołania:
    # [2, 3]
        # [23, 2]
            # [231, 1]
                # 2315 i  kończe
        # [23, 1]
            # 235 i kończe
        # 23 i kończe
    # [2, 2]
        # [21, 1]
            # 215 i kończę
        # 21 i kończe
    # [2, 1]
        # 25 i kończe
    # 2 i kończe
    
def get_digit_from_num_index(index):
    return (liczba % 10**index - liczba % 10**(index-1)) / 10**(index-1)
     
def check_all_subsequences(current_num, next_index):
    current_num = current_num * 10 + get_digit_from_num_index(next_index)
    count = int(current_num % div == 0) # jezeli aktualnie sprawdzana liczba jest dzielnikiem
    for i in range(next_index-1, 0, -1):
        count += check_all_subsequences(current_num, i) # zsumuj tez z wszystkimi nastepnymi ciągami
    return count; 

count = 0
for index_końca in range(dc, 0, -1):
    count += check_all_subsequences(0, index_końca)

print(count)
        
        
    
    