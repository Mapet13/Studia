def b1(S, P, l, t):
    cost = 0
    n = len(S)
    pos = 0
    curr_l = l - S[0]
    last_s = None
    for i in range(n):
        if S[i] >= t:
            last_s = i
            break
    if last_s is None:
        last_s = n-1
    while S[pos] != t:
        i = pos + 1
        found_cheaper = False
        while S[i] < t and S[i] <= S[pos] + l and not found_cheaper:
            if P[i] < P[pos]:
                if i >= last_s:
                    cost += abs((curr_l-(t-S[pos])))*P[pos]
                    return cost
                curr_l -= S[i] - S[pos]
                if curr_l < 0:
                    cost += abs(curr_l) * P[pos]
                    curr_l = 0
                pos = i
                found_cheaper = True
            i += 1
        if not found_cheaper:
            if t-S[pos] <= l:
                cost += abs(curr_l - (t - S[pos])) * P[pos]
                return cost
            cost += (l - curr_l) * P[pos]
            curr_l = l - (S[pos+1] - S[pos])
            pos += 1