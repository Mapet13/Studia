n = int(input("N: "))

result = 1
for i in range(2, n+1):
    while i % 10 == 0:
        i //= 10
    #end
    
    result *= i
    while result % 10 == 0:
        result //= 10    
    #end
#end

result %= 10

print(result)