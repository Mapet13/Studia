# f(k) - maksymalny zysk ze zcięcie drzew ze zbioru 0...k-1, trzeba zciac drzewo k 

def wycinka(P):
    f = [P[0], max(P[0], P[1])]
    f.append(max(f[0]+P[2], f[1]))
    for i in range(3, len(P)):
        f.append(max(f[-2], f[-3]) + p[i])
    return man(f[-1], f[-2])
