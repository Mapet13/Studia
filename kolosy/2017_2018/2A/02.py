'''
Dana jest tablica int t[9], w której nale»y umie±ci¢ liczby od 1 do 9 tak, aby byªy speªnione warunki:
1) warto±ci na s¡siednich polach tablicy musz¡ si¦ ró»ni¢ o co najmniej 2
2) liczby pierwsze nie mog¡ zajmowa¢ s¡siednich pól tablicy
Warto±¢ 1 zostaªa ju» umieszczona w pierwszym (pod indeksem 0) elemencie tablicy. Prosz¦ napisa¢ program,
który wypisuje wszystkie poprawne rozmieszczenia liczb w tablicy.
'''

def is_prime(x):
    return (x == 2 or x == 3 or x == 5 or x == 7)

counter = 0

# zakładam ze pozostale sa wypelnione 0
def f(T, i = 2):
    global counter 
    
    if i == 10:
        counter += 1
        print(T)
        return
    
    for x in range(1, 9):
        if T[x] == 0:
            if (
                ((abs(i - T[x-1]) > 1) and (x == 8 or abs(i - T[x+1]) > 1)) and not 
                (is_prime(i) and ((x == 8 and is_prime(T[x-1])) or (x != 8 and (is_prime(T[x-1]) or is_prime(T[x+1])))))
                ):
                
                T[x] = i
                f(T, i+1)
                T[x] = 0
                
T = [1, 0, 0, 0, 0, 0, 0, 0, 0]
f(T)

print(counter)