def H(n):
    return sum(((n-i)*(n-i+1))//2 for i in xrange(2, n, 3))

print H(6)
