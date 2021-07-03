def change(M, coins):
    subM = [float("inf")] * (M + 1)
    subM[0] = 0
    for i in range(1, M + 1):
        for c in coins: subM[i] = min(subM[i], subM[i - c] + 1)
    return subM[M]