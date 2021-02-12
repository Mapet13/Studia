'''
algorytm to proste sprawdzanie kolejnych kolejnych liczb jako "pierwszej" w trojce 
i patrzeenie czy stanowi ona trojke liczbą oddalą o 1 lub 2 od pierwszej 
i oddalonej o 1 lub 2 od drugiej
'''

#algorytm euklidesa z modulo
def NWD(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x
#end

#funkcja pomocnicza sprawdzajaca warunek (1)
def checkNWD(a, b, c):
    return NWD(a, b) == NWD(a, c) == NWD(b, c) == 1 
#end

def trojki(T):
    N = len(T) # dla wygody len zapisuje do zmiennej 
    
    counter = 0 # licznik wystapien trojek
    
    for i in range(N-2):  # sprawdzam pierwsza liczbe z trojki
        for o1 in range(1, 3): # kolejna liczba moze byc oddalona od pierwszej o 1 lub 2
            for o2 in range(1, 3):  # kolejna liczba moze byc oddalona od drugiej o 1 lub 2
                if i+o1+o2 < N: # sprawdzam czy nie wychodze poza dlugosc tablicy
                    if checkNWD(T[i], T[i+o1], T[i+o1+o2]): #jesli te liczby stanowia trojke to zwieksze licznik
                        counter += 1
                        
    return counter
#end def
