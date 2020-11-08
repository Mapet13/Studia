def get_longest_correct_sumsequences(tab):
    n = len(tab)
    
    best = 0
    
    for i in range(n):
        index_sum = i
        elements_sum = tab[i]
        if best == 0 and elements_sum == index_sum:
                best = 1
        for j in range(i-1, -1, -1):
            elements_sum += tab[j]
            index_sum += j
            if elements_sum == index_sum and (i - j + 1) > best:
                best = i - j + 1
            
    return best

t = [10, 9, 4, 6, 1, 2] # 3 + 4 = t[3] + t[4]
print(get_longest_correct_sumsequences(t))