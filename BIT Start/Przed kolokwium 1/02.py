'''
Zadanie 1.1a (2017/2018)
Dwie liczby naturalne są “różnocyfrowe”, jeżeli nie posiadają żadnej wspólnej cyfry. Proszę
napisać program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy
systemu (w zakresie 2-16), w którym liczby są różnocyfrowe. Program powinien wypisać
znalezione podstawy; jeżeli podstawa taka nie istnieje, należy wypisać komunikat o jej braku.
Na przykład: dla liczb 123 i 522 odpowiedzią jest podstawa 11, bo 123(10) = 102(11) i 522(10) = 435(11)
'''

def number_to_n_sys(num, k):
    cnt = 1
    while num >= k ** cnt:
        cnt += 1
    result = [None for _ in range(cnt)]
    index = cnt - 1
    while num != 0:
        result[index] = num % k
        num //= k
        index -= 1
    return result

def compare_nums(a, b):
    k = 2
    while k <= 16:
        conv_a = number_to_n_sys(a, k)
        conv_b = number_to_n_sys(b, k)
        
        different_numbers = True
        for i in range(len(conv_a)):
            if conv_a[i] in conv_b:
                different_numbers = False
                break
        
        if different_numbers:
            return k
        
        k += 1
    return "Base not found"
            
print(compare_nums(123, 522))