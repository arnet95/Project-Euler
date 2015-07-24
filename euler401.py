def sum_of_squares(n):
    return (n * (n + 1) * (2*n + 1)) / 6

def old_SIGMA2(n):
    return sum((n/i)*pow(i, 2, 10**9) for i in xrange(1, n+1))


def SIGMA2(n):
    s = 0
    for i in xrange(1, n/3 + 1):
        s += ((n/i)*pow(i, 2, 10**9))
    return s + sum_of_squares(n) + sum_of_squares(n/2) - 2*sum_of_squares(n/3)

#print SIGMA2(10**4)
#print old_SIGMA2(10**4)
print sum_of_squares(10**15)
