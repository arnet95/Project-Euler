def f(L):
    d = {(False, )*10: 1}
    for _ in range(L):
        new_d = {}
        #Zero case
        for s in d:
            new_tup = list(s)
            if sum(s) > 0:
                new_tup[0] = True
            new_tup = tuple(new_tup)
            if new_tup in new_d:
                new_d[new_tup] += d[s]
            else:
                new_d[new_tup] = d[s]
        for i in range(1, 10):
            for s in d:
                new_tup = list(s)
                new_tup[i] = True
                new_tup = tuple(new_tup)
                if new_tup in new_d:
                    new_d[new_tup] += d[s]
                else:
                    new_d[new_tup] = d[s]
        d = new_d.copy()
    d[(True, ) + (False, )*9] = 0
    result = 0
    for t1 in d:
        for t2 in d:
            if any(t1[i] and t2[i] for i in range(10)):
                result += d[t1]*d[t2]
    return (result - (10**L-1))//2

print(f(18) % 1000267129)