'''
Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 
i sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
'''

from random import randint 

n = int(input("n: "))

t = [0] * n
for i in range(n):
    t[i] = randint(1, 1000)

#tylko żeby sprawdzić
print(t)

is_correct = True

#najchetniej poączył bym te 2 pętle ale nw czy w tym zadaniu to legalne xD
i = 0
while i < n and is_correct: 
    num = t[i]
    is_num_not_correct = True
    while num > 0:
        if num % 2 != 0:
            is_num_not_correct = False
            break
        num //= 10
    if is_num_not_correct:
        is_correct = False
        break
    i += 1

print(is_correct)