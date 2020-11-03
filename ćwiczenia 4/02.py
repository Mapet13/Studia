'''
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. 
Proszę napisać funkcję, która odpowiada na pytanie, 
czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie z nieparzystych cyfr.
'''

# from random import randint

def is_only_odd_digit_number(x):
    while x > 0:
        if x % 2 == 0:
            return False
        x //= 10
    return True    
            

def check_array(t, n):
    for i in range(n):
        for j in range (n):
            if is_only_odd_digit_number(tab[i][j]):
                break
        else:
            return False
    return True


# n = int(input("n: "))
# tab = [[randint(1, 10000) for _ in range(n)] for _ in range(n)]
n = 3
tab = [
    [11, 45, 22], 
    [22, 73, 90], 
    [12, 97, 87]
    # [11, 45, 22], 
    # [22, 73, 90], 
    # [12, 45, 67]
]

for i in range(n):
    print(tab[i])

print("result: ", check_array(tab, n))
