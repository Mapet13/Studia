'''
Dana jest tablica int t[N] wypeªniona liczbami caªkowitymi. Prosz¦ napisa¢ funkcj¦, która sprawdza, czy
mo»liwe jest "poci¦cie" tablicy na co najmniej 2 kawaªki o jednakowych sumach elementów. Do funkcji nale»y
przekaza¢ tablic¦, funkcja powinna zwróci¢ najwi¦ksz¡ liczb¦ kawaªków, na któr¡ mo»na poci¡¢ tablic¦, lub
warto±¢ 0, je±li takie poci¦cie nie jest mo»liwe. Na przykªad: dla tablicy [1,2,3,1,5,2,2,2,6] odpowiedzi¡
powinno by¢ 4, bo [1,2,3|1,5|2,2,2|6].
'''

def f(T, s = None, i = 0, c = 0):
    N = len(T)
    if i == N and c > 1:
        return c
    if s == None:
        s = 0
        count = 0
        for x in range(N-1):
            s += T[x]
            count = max(count, f(T, s, x+1, 1))
        return count
    else:
        cs = T[i]
        count = 0
        for x in range(i+1, N):
            if cs == s:
                count = max(count, f(T, cs, x, c+1))
            cs += T[x]
        if cs == s:
            count = max(count, f(T, cs, N, c+1))
        return count

t = [1,2,3,1,5,]
print(f(t))

t = [2, 2, 2, 6, 5, 1, 7, -1, 8, -2, 10, -4, 6, 6]
print(f(t))

t = [1, 2, 89999, 1, 12]
print(f(t))