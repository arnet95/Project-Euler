def test(n):
    candidates = range(1, n+1)
    result = 0
    l = [1, 2]
    while len(candidates) > 1:
        for i in l:
            new_cand = []
            for cand in candidates:
                if i % cand == 0:
                    result += i // cand
                else:
                    new_cand.append(cand)
            candidates = new_cand
        l = [10*i+j for i in l for j in [0,1,2]]
    return result + 1111333355557778

print test(10000)
