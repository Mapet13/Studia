'''
Poprzednie zadanie. Program powinien wypisywać wybrane odważniki
'''
def can_weigh(t, x, i = 0, wt = []):
    if x == 0:
        print(wt)
        return True
    if i == len(t): 
        return False
    return can_weigh(t, x - t[i], i + 1, wt + [t[i]]) or can_weigh(t, x, i + 1, wt) or can_weigh(t, x + t[i], i + 1, wt + [-t[i]]) 

t = [1, 3, 5, 10, 16, 24]
print(can_weigh(t, 23))

t = [1, 3, 5, 10, 16, 23]
print(can_weigh(t, 23))
