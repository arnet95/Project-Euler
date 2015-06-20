r_max_sum = 0
for a in xrange(3, 1001):
    a2 = a**2
    r_max = 2
    for n in xrange(1, a):
        r_max = max(r_max, (2*n*a)%a2)
    r_max_sum += r_max

print r_max_sum