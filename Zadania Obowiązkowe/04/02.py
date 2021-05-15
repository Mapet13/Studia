'''
problem suby podzbioru. Stwierdzic czy istnieje podzbiór sumujacy sie dokładnie od T
'''

def f(T, target):
    N = len(T)
    F = [[False] * (target + 1) for _ in range(N)]
    
    if T[0] <= target:
        F[0][T[0]] = True
        
    i = 1
    while i < N and not F[i-1][target]:
        for t in range(target + 1):
            if t >= T[i]: # jezeli element i jest mniejszy od aktualnie sprawdzanej sumy (bo operujemy tylko na naturalnych)
                F[i][t] = F[i-1][t] or F[i-1][t-T[i]] # rekurenycjnośc (F[i-1][t] lub F[i-1][t-T[i]])
            else:
                F[i][t] = F[i-1][t] # czy przedmioty do i-1 maja podciag sumujacy siie do t
        i += 1
        
    return F, F[i-1][target]

T = [1, 21, 2, 9, 3, 5, 13, 7]
F, r = f(T, 15)
print(r)

T = [4, 6, 1]
F, r = f(T, 2)
print(r)
