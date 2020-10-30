'''
Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym 
wyznacza długość najdłuższego, spójnego podciągu geometrycznego.
'''
from random import randint

def getLongestGeometricSubsequenceLength(t, n):
    #begin_index = 0
    #end_index = 2
    best = 2
    
    current = 2
    #current_begin = 0
    q = (t[1] / t[0]) if t[0] != 0 else 0
    for i in range(2, n):
        new_q = (t[i] / t[i-1]) if (t[i-1] != 0) else 0
        if new_q != q or i == (n - 1):
            if current > best:
                #begin_index = current_begin
                #end_index = i
                best = current
            q = new_q
            #current_begin = i - 1
            current = 2
        else:
            current += 1

    # as debug code
    #for i in range(begin_index, end_index):
    #    print(t[i])

    return best

def generateArray(n):
    return [randint(1, 100) for _ in range(n)]

n = int(input("n: "))
tab = generateArray(n)

# as debug code
print(tab)

print("len:", getLongestGeometricSubsequenceLength(tab, n))