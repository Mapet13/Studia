from sys import stdin, stdout

n, m = [int(x) for x in stdin.readline().rstrip().split()]

T = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(n)]

F = [-1] * n
for j in range(m):
    l = 0
    while l < n:
        r = l + 1
        while r < n:
            if T[r][j] < T[r-1][j]: break
            r += 1
        while (l < r): 
            F[l] = max(F[l], r) 
            l += 1

print(F)

k = int(stdin.readline())
for _ in range(k):
    l, r = [int(x) for x in stdin.readline().rstrip().split()] 
    if F[l-1] >= r: 
        stdout.write("Yes\n")
    else:
        stdout.write("No\n")
        