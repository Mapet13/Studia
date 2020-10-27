'''
Napisać program wczytujący dwie liczby naturalne i odpowiadający na pytanie 
czy są one zbudowane z takich samych cyfr, 
np. 123 i 321, 1255 i 5125, 11000 i 10001.
'''

# np: (12345, 2) -> 1235
def get_numer_without_index(n, index):
    first_digits = (n - (n % 10**index)) // 10
    last_digits = n % 10**(index-1)
    return first_digits + last_digits

a = int(input("a: "))
b = int(input("b: "))

has_same_digits = True

# iterujemy po kolejnych cyfrach w 'a' 
while a > 0 and has_same_digits:
    last_a_digit = a % 10
    a //= 10
    
    i = 1
    temp = b
    # iterujemy po cyfrach w 'b' i jeśli trafię tą cyfre to ja "kasuje" z liczby 'b'
    while b > 0 and has_same_digits:
        last_b_digit = b % 10
        b //= 10
        if last_a_digit == last_b_digit:
            b = get_numer_without_index(temp, i)
            break
        i += 1
    else: # heh chcialem tego uzyc xD (a jakby co to z if mozna sprawdzic czy b < 0)
        has_same_digits = False
     
print(has_same_digits)

