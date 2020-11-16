'''
Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
figury była równa zero
'''


def can_set_kings(t):
    def set_kings_recursive(n, tab, x1 = -3, x2 = -3, row = 0, king_sum = 0):
        if row == n:
            #print(king_sum)
            return (king_sum == 0)

        for i in range(n):
            if (i < x1 - 2 or i > x1 + 2) and (i < x2 - 2 or i > x2 + 2):
                #debug_indent = '>' * row
                #print(debug_indent, (row, i))
                if set_kings_recursive(n, tab, i, x1, row + 1, king_sum + tab[row][i]):
                    return True

        return False

    n = len(t)
    return set_kings_recursive(n, t)


tab = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
print(can_set_kings(tab))

tab = [
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [-1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -1],
    [0, 0, 0, 0, 0, 0, 0],
]
print(can_set_kings(tab))

tab = [
    [178, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -11223, 0, 0, 0, 0],
    [0, -111, 0, 0, 0, 0, 111, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -1233,0, 0, 1344, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

print(can_set_kings(tab))

tab = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

print(can_set_kings(tab))
