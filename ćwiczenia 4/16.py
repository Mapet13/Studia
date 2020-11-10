'''
Dana jest tablica T[N][N], wypełniona liczbami naturalnymi.
Proszę napisać funkcję która odpowiada na pytanie, 
czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr będących liczbami pierwszymi?
'''

PRIME_DIGITS = [2, 3, 5, 7]

def check(t):
    n = len(t)
    
    for i in range(n):
        correct = False
        for j in range(n):
            num = t[i][j]
            while num > 0:
                last_digit = num % 10
                num //= 10
                is_p = False
                for p in PRIME_DIGITS:
                    if last_digit == p:
                        is_p = True
                        break 
                if not is_p:
                    break
            else:
                correct = True
                break
        if not correct:
            return False

    return True


t = [
    [23, 81227, 1235627],
    [23, 22198743, 17112],
    [16, 12356, 8127],
]
print(check(t))

t = [
    [23, 812312327, 12356],
    [1222, 57777532, 17112],
    [57777532, 17112, 757575752],
]
print(check(t))