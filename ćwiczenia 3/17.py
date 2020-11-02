'''
Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. 
Z wartości w obu tablicach możemy tworzyć sumy. 
„Poprawna” suma to taka, która zawiera co najmniej jeden element (z tablicy t1 lub t2) o każdym indeksie. 
Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] 
    poprawnymi sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. 
Proszę napisać funkcje generującą i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. 
Do funkcji należy przekazać dwie tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.
'''
from random import randint


def is_prime(num):
    if num == 2 or num == 3: 
        return True
    if num <= 1 or num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 7
    while i * i <= num:
        if num % (i - 2) == 0 or num % i == 0:
            return False
        i += 6
    
    return True   
    


def count_and_print(t1, t2, n, add_from_1, add_from_2, sum, index):
    if add_from_1:
        sum += t1[index]
    if add_from_2:
        sum += t2[index]
        
    count = 0    
    
    if is_prime(sum) and index == n - 1:
        print(sum)
        count += 1
    
    index += 1
    if index < n:
        count += count_and_print(t1, t2, n, True, False, sum, index)
        count += count_and_print(t1, t2, n, False, True, sum, index) 
        count += count_and_print(t1, t2, n, True, True, sum, index)
    
    return count



def count_and_print_correct_sums(t1, t2):
    n = len(t1)
    count = count_and_print(t1, t2, n, True, False, 0, 0)
    count += count_and_print(t1, t2, n, False, True, 0, 0) 
    count += count_and_print(t1, t2, n, True, True, 0, 0)
    return count
    
    
    

n = 2

t1 = [1, 4]
t2 = [3, 5]

print("count: ", count_and_print_correct_sums(t1, t2))

