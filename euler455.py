l = []
for x in xrange(2, 10**9, 2):
    print x
    if pow(2, x, 10**9) == x:
        l.append(x)
