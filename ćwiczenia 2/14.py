"""
Dane są dwie liczby naturalne z których budujemy trzecią liczbę. 
W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. 
Wzajemna kolejność cyfr każdej z liczb wejściowych musi być zachowana. 
Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,75123, 17253, itd. 
Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch zadanych liczb.
"""

a = int(input("a: "))
b = int(input("b: "))


def is_prime(a):
    if a < 2 or a % 2 == 0:
        return False
    i = 3
    if i*i <= a:
        if a % i == 0:
            return False
        i += 2
    return True

"""
dla 12 i 75
 count(12, 75, 0, 0)
    >  count(1, 75, 2, 1)
        > count(0, 75, 12, 2)
            > count(0, 7, 512, 3)
                > count(0, 0, 7512, 4) <- kończe [7512]
        > count(1, 7, 52, 2)
            > count(0, 7, 152, 3)
                > count(0, 0, 7152, 4) <- kończe [7152]
            > count(1, 0, 752, 3)
                 > count(0, 0, 1752, 4) <- kończe [1752]
    >  count(12, 7, 5, 1)
       > count(1, 7, 25, 2)
            > count(0, 7, 125, 3)
                > count(0, 0, 7125, 4) <- kończe [7125]
            > count(1, 0, 725, 3)
                > count(0, 0, 1725, 4) <- kończe [1725]
        > count(12, 0, 72, 2)
            > count(1, 0, 275, 3)
                > count(0, 0, 1275, 4) <- kończe [1275]
"""
def count(x, y, num, dc):
    if x <= 0 and y <= 0: # jeżeli skończe generowac liczbę to sprawdzam czy jest pierwsza 
        return int(is_prime(num))
    prime_count = 0
    if x > 0:
        xd = x % 10
        prime_count += count(x // 10, y, num + xd * 10**dc, dc + 1)
    if y > 0:
        yd = y % 10
        prime_count += count(x, y // 10, num + yd * 10**dc, dc + 1)
    return prime_count

print(count(a, b, 0, 0))
