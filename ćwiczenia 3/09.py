'''
Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym 
wyznacza długość najdłuższego, spójnego podciągu rosnącego.
'''
from random import randint

def getLongestAscendingSubsequenceLength(t, size):
    begin_index = 0
    end_index = 1
    best = end_index - begin_index
     
    current = 1
    current_begin = 0
    for i in range(1, size):
        if t[i] <= t[i-1] or i == (size - 1):  # ten 2 warunek aby sprawdzić czy czasem podciąg kończący sie na ostatnim nie jest czasem największy
            if best < current:
                begin_index = current_begin
                best = current
                end_index = i
            current_begin = i
            current = 1
        else:
            current += 1

    # as debug code
    #for i in range(begin_index, end_index):
    #    print(t[i])
        
    return (end_index - begin_index)
    
    
def getRandomArray(n):
    return [randint(1, 10e3) for _ in range(n)]


n = int(input("n: "))
tab = getRandomArray(n)

# as debug code
print(tab)

print(getLongestAscendingSubsequenceLength(tab, n))