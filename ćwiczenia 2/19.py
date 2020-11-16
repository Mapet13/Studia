def count_2_or_5(n):
    counter2 = 0
    while n % 2 == 0:
        counter2 += 1
        n //= 2
        
    counter5 = 0
    while n % 5 == 0:
        counter5 += 1
        n //= 5
        
    return max(counter2, counter5)

def print_fraction(a, b):                
    print(a // b, end='')
    
    rest = a % b
    if rest > 0:
        print('.', end='')
        
        for _ in range(count_2_or_5(b)):
            rest *= 10
            print(rest // b, end='')
            rest %= b
        
        if rest > 0:
            print('(', end='')
            
            temp = rest
            while True:
                rest *= 10
                print(rest // b, end='')
                
                rest %= b
                if rest == temp:
                    break
                
            print(')', end='')
            
    print()
                            
print_fraction(22, 7)