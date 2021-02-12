def g(T):
    result = 0

    def f(arr, last=None, moves=0):
        nonlocal result
        for i in range(len(arr)):
            if last is None:
                f(arr, arr[i][0])
                f(arr, arr[i][1])
            if arr[i][0] == last:
                f(arr[:i] + arr[i + 1:], arr[i][1], moves+1)
            if arr[i][1] == last:
                f(arr[:i] + arr[i + 1:], arr[i][0], moves+1)
        if moves > result:
            result = moves
    
    f(T)
    return result
        

T = [
    (2, 8), (0, 1), (2, 3), (3, 6), (2, 6), (2, 9), (3, 4), (6, 7)
]
print(g(T))