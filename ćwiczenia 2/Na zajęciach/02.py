a = int(input("a:  "))
b = int(input("b:  "))
n = int(input("n:  "))

print(a//b, end='.')

for i in range(n):
    a = a%b
    a = a * 10
    print(a // b, end='')
    
    
    
    