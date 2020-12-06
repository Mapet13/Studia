'''
Dane są dwie liczby naturalne z których budujemy trzecią liczbę. 
W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. 
Wzajemna kolejność cyfr każdej z liczb wejściowych musi być zachowana. 
Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523, 75123, 17253, itd. 
Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch zadanych liczb.
'''

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5 
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def recur(a,b, num = 0, d = 0):
    if a == b == 0:
        return int(is_prime(num))
    
    count = 0
    if a > 0:
        count += recur(a // 10, b, num + ((a % 10) * 10**d), d + 1)
    if b > 0:
        count += recur(a, b // 10, num + ((b % 10) * 10**d), d + 1)
        
    return count

print(recur(123, 75))
print(recur(2939, 89792))
print(recur(6, 7))
print(recur(13, 55))
