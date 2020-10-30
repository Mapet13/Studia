'''
Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym 
wyznacza długość najdłuższego, spójnego podciągu arytmetycznego.
'''
from random import randint

def getLongestArithmeticSubsequenceLength(t, n):
    begin_index = 0
    end_index = 1
    best = end_index - begin_index
    
    current = 1
    current_begin = 0
    d = t[1] - t[0] 
    for i in range(2, n):
        new_d = t[i] - t[i-1]
        if new_d != d or i == (n -1):
            if current > best:
                begin_index = current_begin
                end_index = i
                best = current
            current_begin = i
            current = 1
        else:
            current += 1

    # as debug code
    print('d =', d)
    for i in range(begin_index, end_index):
        print(t[i])

    return best

def generateArray(n):
    return [randint(1, 100) for _ in range(n)]

n = int(input("n: "))
tab = generateArray(n)

# as debug code
#print(tab)

print("len:", getLongestArithmeticSubsequenceLength(tab, n))