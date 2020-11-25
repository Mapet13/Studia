'''
”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
''' 

def get_weight(x):
    count = 0
    
    i = 2
    while i <= x:
        if x % i == 0:
            count += 1
            while x % i == 0:
                x //= i
        i += 1         
    
    return count



def can_be_divided(t, i = 0, s1 = 0, s2 = 0, s3 = 0):
    if i == len(t):
        #debug code
        # if s1 == s2 == s3:
        #    print(">>", s1, s2, s3)
        #end debug code  
        return s1 == s2 == s3
    w = get_weight(t[i])  
    #debug code
    # print(">>", t[i], w)
    #end debug code  
    return can_be_divided(t, i+1, s1 + w, s2, s3) or can_be_divided(t, i+1, s1, s2 + w, s3) or can_be_divided(t, i+1, s1, s2, s3 + w)
      
      
      
      
t = [1, 2, 6, 30, 64]
print(can_be_divided(t))

t = [1, 2, 6, 30, 64, 18]
print(can_be_divided(t))

t = [1, 2, 6, 30, 64, 18, 12, 45, 55, 12, 74, 62, 1, 45, 1]
print(can_be_divided(t))
   
    
    
    
    