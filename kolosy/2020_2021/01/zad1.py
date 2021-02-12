def multi(T):
    n = len(T)
    
    # wyznaczam długość maksymalnej "bazy" napisu wielokrotnego
    max_len = 0
    if n % 2 == 0:
        max_len = n // 2
    else:
        max_len = (n-1) // 2
        
    best = 0
               
    for part_len in range(1, max_len): # długośc sprawdzanej bazy
        for i in range(n - part_len): 
            con = False
            for j in range(i + part_len, n, part_len):
                current_len = 0
                for x in range(part_len - 1):
                    if T[i + x] != T[j + x]:
                        current_len = 0
                        con = True
                        break
                else:
                    current_len += part_len
                if con:
                    break
                if current_len > best:
                    best = current_len 
    
    return best
# end def

print(multi(['a', 'b', 'c', 'd']))