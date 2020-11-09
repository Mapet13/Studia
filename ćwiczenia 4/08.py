'''
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. 
Proszę napisać funkcję, która w poszukuje w tablicy 
najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego co najmniej 3 elementy. 
Do funkcji należy przekazać tablicę. 
Funkcja powinna zwrócić informacje czy udało się znaleźć taki ciąg oraz długość tego ciągu.

|A, a, a, a| |a, A, a, a| |a, a, a, a| 
|a, A, a, a| |a, a, A, a| |A, a, a, a| 
|a, a, A, a| |a, a, a, A| |a, A, a, a|
|a, a, a, A| |a, a, a, a| |a, a, A, a|
'''

def get_new_best(t, x, y, q, current, best, is_last):
    new_q = (t[x-1][y-1] / t[x][y]) if (t[x][y] != 0) else None
    if new_q == q:
        current += 1
    if new_q != q or is_last:
        if current > best:
            best = current 
        q = new_q
        current = 2
    
    return (best, current, q)



def try_to_get_longest_subsequences(t):
    n = len(t)

    if (n < 3):
        return (False, 0)

    best = 0
    for i in range(0, n - 1): # bez zaczynania w 2 najmniejszych czesciach
        current1 = 2
        q1 = (t[i][0] / t[i+1][1]) if (t[i+1][1] != 0) else None
        current2 = 2
        q2 = (t[0][i] / t[1][i+1]) if (t[1][i+1] != 0) else None
        for j in range(2, n-i):
            is_last = j == n - i - 1
            (best, current1, q1) = get_new_best(t, i + j, j, q1, current1, best, is_last)
            if i > 0:
                (best, current2, q2) = get_new_best(t, j, i+j, q2, current2, best, is_last)

        if best > (n-i):
                break

    if best >= 3:
        return (True, best)
    else:
        return (False, 0)
        



# 1 1 1
# 2 4 8 16
t = [
    [2,  10, 50, 999],
    [1,  4,  50, 989],
    [2,  1,  8,  199],
    [90, 10, 1,  16 ],
]
print(try_to_get_longest_subsequences(t))

t = [
    [2,  10, 50, 999],
    [1,  6,  50, 989],
    [2,  1,  8,  199],
    [90, 10, 1,  16 ],
]
print(try_to_get_longest_subsequences(t))

t = [
    [2,  10, 50, 999],
    [1,  6,  50, 989],
    [2,  7,  8,  199],
    [90, 10, 1,  16 ],
]
print(try_to_get_longest_subsequences(t))

t = [
    [2,  10, 50,  999],
    [1,  6,  100, 989],
    [2,  7,  8,   1000],
    [90, 10, 1,   16 ],
]
print(try_to_get_longest_subsequences(t))

t = [
    [10,  10],
    [10, 10],
]
print(try_to_get_longest_subsequences(t))