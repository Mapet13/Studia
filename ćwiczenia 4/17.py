'''
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. 
Proszę napisać funkcję która zwraca wiersz i kolumnę dowolnego elementu,
dla którego suma otaczających go elementów jest największa.
'''


def get_pos(t):
    n = len(t)
    
    x = y = best = 0
    
    for i in range(n):
        for j in range(n):
            current_sum = 0
            for bx in range(i - min(1, i), i + min(1, n - 1 - i) + 1):
                for by in range(j - min(1, j), j + min(1, n - 1 - j) + 1):
                    if bx != i or by != j:
                        current_sum += t[bx][by]
            if current_sum > best:
                best = current_sum
                x = i
                y = j
                
    return (x, y)


t = [
    [25,  117, 12,  88],
    [99,  1,   212, 99],
    [72,  1,   95,  111],
    [122, 12,  71,  16],
]

print(get_pos(t))