'''
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. 
Proszę napisać funkcję, która odpowiada na pytanie, 
czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę parzystą.
'''

def check_num(x):
    while x > 0:
        if x % 2 == 0:
            return True
        x //= 10
    return False



def check_array(t, n):
    for i in range(n):
        for j in range(n):
            if not check_num(t[i][j]):
                break
        else:
            return True
    return False
            


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