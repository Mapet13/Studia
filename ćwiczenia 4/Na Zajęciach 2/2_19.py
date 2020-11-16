'''
jesli wystepuja inne niż 2 i 5 to napewno ułamek jest okresowy
ile mianownik ma 2 i 5 w rozkładzie to ilośc liczb przed okresem będzie 
'''


def f(a, b):
    
    def ile_2_5(n):
        counter2 = 0
        while n % 2 == 0:
            counter2 += 1
            n //= 2
            
        counter5 = 0
        while n % 5 == 0:
            counter5 += 1
            n //= 5
            
        return max(counter2, counter5)
                
    result = ''
    #print(a // b, end='')
    result += str(a // b)
    
    r = a % b
    if r > 0:
        #print('.', end='')
        result += "."
        
        for _ in range(ile_2_5(b)):
            r *= 10
            #print(r//b, end='')
            result += str(r // b)
            r %= b
        
        if r > 0:
            #print('(', end='')
            result += "("
            
            
            temp = r
            while True:
                r *= 10
                #print(r//b, end='')
                result += str(r // b)
                
                r %= b
                if r == temp:
                    break
                
            #print(')', end='')
            result += ")"
            
    #print()
    print(len(result))
                            
f(2183871, 198271983)