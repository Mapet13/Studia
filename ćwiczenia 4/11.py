'''
Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby są identyczne. 
Na przykład: 123 i 321, 211 i 122, 35 3553. 
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. 
Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z przyjaciółkami
'''


def get_num_without_digit(n, d):
    res = 0
    while n > 0:
        if n % 10 != d:
            res = res * 10 + (n % 10)
        n //= 10
    return res



def count_friends(t):
    n = len(t)

    tested = [[None for _ in range(n)] for _ in range(n)]

    count = 0

    for i in range(n):
        for j in range(n):
            if tested[i][j] == None:
                con = False
                for x in range(i-min(1, i), i+min(1, n-1-i)+1):
                    for y in range(j-min(1, j), j+min(1, n-1-j)+1):
                        if (x != i or y != j) and tested[x][y] != True:
                            temp_center = t[i][j]
                            temp_num = t[x][y]
                            while temp_center > 0 and temp_num > 0:
                                d = temp_center % 10
                                temp_center //= 10
                                temp_center = get_num_without_digit(temp_center, d)
                                temp_num = get_num_without_digit(temp_num, d)
                            if temp_num > 0 or temp_center > 0:
                                con = True
                                tested[x][y] = False
                                tested[i][j] = False
                                break
                    if con:
                        break
                if not con:
                    tested[i][j] = True
                    count += 1

    return count



# 3
tab = [
    [123, 321, 66],
    [213, 321, 66],
    [321, 123, 66],
]
print(count_friends(tab))

# 9
tab = [
    [123, 321, 213],
    [213, 321, 213],
    [321, 123, 213],
]
print(count_friends(tab))

# 4
tab = [
    [123, 321, 213, 132],
    [213, 321, 35,  553],
    [321, 123, 53,  335],
    [11,  22,  353, 5553],
]
print(count_friends(tab))
