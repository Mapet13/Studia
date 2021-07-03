# T - tablica zadan
# g(t) - funkcja zwracajaca zysk za zadanie 
# d(t) - funkcja zwracajaca termin zadania

def max_profit(T):
    # sortowanie wzgledem zysku
    T = sorted(T, key=lambda t: g(t))  # sorted(T, key=g) starczy? 

    schedule = [False] * d(max(T, key=d)) 
    profit = 0

    for i in range(len(T)):
        for j in range(d(T[i]), -1, -1):
            if not schedule[j]:
                profit += g(T[i])
                schedule[j] = True
                break

    return profit
