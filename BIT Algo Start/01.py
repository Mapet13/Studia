from sys import stdin, stdout

n, k = [int(x) for x in stdin.readline().rstrip().split()]
a = [int(x) for x in stdin.readline().rstrip().split()]
t = [int(x) for x in stdin.readline().rstrip().split()]

curent = 0
s = 0

for i in range(n):
    if t[i] == 1: 
        s += a[i]
    
for i in range(k):
    if t[i] == 0: curent += a[i]

current_k = curent
for i in range(k, n):
    if t[i-k] == 0: current_k -= a[i-k]
    if t[i] == 0: current_k += a[i]
    curent = max(curent, current_k)
        
stdout.write(str(curent + s))
