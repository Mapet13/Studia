'''
Problem wież w Hanoi (treść oczywista)
'''

# T1, T2, T3 len = N,
# T2, T3 <- [0, 0, 0...]
# T1 <- [1, 2, 3, ..., N-1, N]
def hanoi(N, T1, T2, T3):
    def move(A, B):
        i = 0
        while A[i] == 0:
            i += 1
        j = len(B) - 1
        while B[j] != 0:
            j -= 1
        B[j] = A[i]
        A[i] = 0
    
    if N > 0:
        hanoi(N-1, T1, T3, T2) 
        move(T1, T3)
        hanoi(N-1, T2, T1, T3)
        
T1 = [1, 2, 3, 4]
T2 = [0] * 4
T3 = [0] * 4

hanoi(4, T1, T2, T3)
print(T1)
print(T2)
print(T3)

print()

T1 = [i+1 for i in range(20)]
T2 = [0] * 20
T3 = [0] * 20

hanoi(20, T1, T2, T3)
print(T1)
print(T2)
print(T3)
