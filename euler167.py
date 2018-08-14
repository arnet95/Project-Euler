
def gen_seq(a, b, N):
    print a
    print b
    l = [a, b]
    candidates = [a+b]
    for _ in xrange(N):
        while candidates.count(candidates[0]) > 1:
            n = candidates[0]
            while n in candidates:
                candidates.remove(n)
        appending = candidates[0]
        print appending
        for i in l:
            candidates.append(i+appending)
        l.append(appending)
        candidates.remove(appending)
        candidates = sorted(candidates)

gen_seq(2, 5, 100)
