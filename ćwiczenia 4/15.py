'''
Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. 
Proszę napisać funkcję, która odpowiada na pytanie, czy w tablicy istnieje wiersz, 
w którym każda liczba zawiera co najmniej jedną cyfrę będącą liczbą pierwszą?
'''

PRIME_DIGITS = [2, 3, 5, 7]

def check(t):
    n = len(t)
    
    for i in range(n):
        correct = True
        for j in range(n):
            num = t[i][j]
            find_p = False
            while num > 0 and not find_p:
                last_digit = num % 10
                num //= 10
                for p in PRIME_DIGITS:
                    if last_digit == p:
                        find_p = True
                        break 
            if not find_p:
                correct = False    
                break
        if not correct:
            return False

    return True


t = [
    [1643, 812312327, 1235627],
    [1222, 22198743, 17112],
    [16, 81927, 8127],
]
print(check(t))

t = [
    [1643, 812312327, 12356],
    [1222, 22198743, 17112],
    [162, 81927, 8588],
]
print(check(t))