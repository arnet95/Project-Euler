from eulertools import primes

for m in xrange(1, 10001):
    if all(pow(a, m+4, m) == a for a in xrange(2, m)):
        print m, [p for p in primes(m+1) if m % p == 0]
