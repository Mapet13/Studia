"""
Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż 2,3,5. 
Jedynka też jest taką liczbą. 
Napisz program, który wylicza ile takich liczb znajduje się w przedziale od 1 do N włącznie
"""

"""
nie ma co wiecej tłumaczyć po prostu dziele maksymalną ilośc razy przez liczby 1, 3 i 5 i patrze czy wyjscowa liczba jest równa 1
"""

def divide_max_times(n, d):
    while n % d == 0:
        n /= d
    return n

N = int(input("Podaj koniec przedziału: "))
counter = 1
for i in range(2, N+1):
    i = divide_max_times(i, 5)
    i = divide_max_times(i, 3)    
    i = divide_max_times(i, 2)
    if i == 1:
        counter += 1
        
print(f"w przedziale od 1 do {N} włącznie jest {counter} takich liczb")
            
        