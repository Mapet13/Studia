'''
Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych 
zakończonych zerem stanowiącym wyłącznie znacznik końca danych. 
Program powinien wypisać 10 co do wielkości wartość, jaka wystąpiła w ciągu. 
Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.
'''

tab = [0] * 10 # tablica dziesieciu najwiekszych elementow z pośród podanych

last_num = int(input())
while last_num != 0:
    i = 0
    # pokolei iteruje od najmniejszej do najwiekszej i staram sie znalesc odpowiednie miejsce dla liczby
    while i < 10 and tab[i] < last_num:
        if i > 0:  # warunek jest dlatego ze jezeli liczba jest wieksza niz tab[0] no to tab[0] wypada z listy
            tab[i-1] = tab[i]
        tab[i] = last_num
        i += 1
    last_num = int(input())
    
print(tab[0]) # najmniejsza wartosc w tablicy czyli dziwsiąta co do wielkosci podana