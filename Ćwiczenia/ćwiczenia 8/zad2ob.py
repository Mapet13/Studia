G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]


def kwmacierzy(G):
    n = len(G)
    result = []
    for i in range(n):
        result.append([0] * n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += G[i][k] * G[k][j]
    return result


def czy4cykl(G):
    tmp = kwmacierzy(G)
    print(tmp)
    for i in range(len(G)):
        tmp[i][i] = 0
    print(tmp)
    result = kwmacierzy(tmp)
    print(result)
    for i in range(len(G)):
        if (result[i][i]):
            return True
    return False


print(czy4cykl(G))