def universal_vent(G):
    n = len(G)
    arr = [1]*n
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                arr[i] = 0
            elif i != j:
                arr[j] = 0
    for x in arr:
        if x == 1:
            print(x)
