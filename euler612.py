def f_test(n):
    count = 0
    for q in xrange(1, n):
        for p in xrange(1, q):
            if len(set(str(q)).intersection(set(str(p)))) > 0:
                count += 1
    return count

print f_test(10**4)
