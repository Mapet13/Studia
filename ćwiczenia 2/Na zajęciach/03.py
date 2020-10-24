n = int(input("n: "))

'''
k = n
d = 0
while n > 0:
    d += 1
    n //= 10
    
j = 1
while j < d:
    if k - k%10**(d-1) / 10**(d-1) != k %10**j - k %10**(j-1) / 10**(j-1):
        print("nie jest palindromem w systemie dziesiętnym")
        break
    d -= 1
    k -= 1
if   k - k%10**(d-1) / 10**(d-1) == k %10**j - k %10**(j-1) / 10**(j-1):
    print('tak jest palindromem w systemie dziesiętnym')
'''

'''
a = n % 10 # dostaje cyfre jednosci
n  //= n  # kasuje ostatnia cyfre {123 -> 12}
n = 10*n + c # dopisuje cyfre na końcu {12, 3 -> 123}
'''

rev = 0
k = n
while (n > 0):
    rev = 10*rev + n % 10
    n //= 10
    
if k == rev:
    print("tak 10")
else:
    print("nie 10")
    
rev = 0
n = k
while (n > 0):
    rev = 2*rev + n % 2
    n //= 2
    
if k == rev:
    print("tak 2")
else:
    print("nie 2")

