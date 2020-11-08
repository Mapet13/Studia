'''
Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000. 
Proszę napisać funkcję, która zwraca długość najdłuższego, spójnego fragmentu tablicy, 
    dla którego w iloczynie jego elementów każdy czynniki pierwszy występuje co najwyżej raz. 
Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5.
'''

# pokracznie ale bez appendu
def generate_prime_table():
    count = 0

    t = [True] * 100
    t[0] = False
    t[1] = False

    i = 2
    while i * i <= 100:
        if t[i]:
            for j in range(i*i, 100, i):
                t[j] = False
        i += 1

    for j in range(100):
        if t[j]:
            count += 1

    primes = [0] * count
    i = 0
    for j in range(100):
        if t[j]:
            primes[i] = j
            i += 1

    return primes


def get_length_of_longest_correct_subsequence(tab):
    n = len(tab)

    prime_table = generate_prime_table()
    prime_count = len(prime_table)

    num_fc = [[0 for _ in range(prime_count)] for _ in range(n)]
    has_unique_factors = [True] * n
    for i in range(n):
        pi = 0
        x = tab[i]
        while x > 1 and prime_table[pi] * prime_table[pi] <= x:
            if x % prime_table[pi] == 0:
                x //= prime_table[pi]
                if x % prime_table[pi] == 0:
                    has_unique_factors[i] = False
                    break
                num_fc[i][pi] = 1
            pi += 1

    factors_count = [0] * prime_count
    bi = ei = 0
    best = 0
    current = 0
    while ei < n:
        if not has_unique_factors[ei]:
            current = 0
            bi = ei = ei + 1
            factors_count = [0] * prime_count
        else:
            if best == 0:
                best = 1

            if bi != ei:
                for i in range(prime_count):
                    factors_count[i] += num_fc[ei][i]

                    while factors_count[i] > 1 and bi < ei:
                        if ei - bi + 1 < best:
                            break
                        else:
                            for j in range(prime_count):
                                factors_count[j] -= num_fc[bi][j]
                            bi += 1

                    if bi == ei:
                        break
                    if ei - bi + 1 >= best:
                        best = ei - bi + 1
                    else:
                        bi = ei = ei + 1
                        factors_count = [0] * prime_count
                        break

            if bi == ei and ei < n:
                for i in range(prime_count):
                    factors_count[i] = num_fc[ei][i]
            ei += 1

    return best


t = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
print(get_length_of_longest_correct_subsequence(t))
