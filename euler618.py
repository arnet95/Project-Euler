from eulertools import primes


print len(prime_list)

def S_gen(limit):
    S = [(0, 0) for _ in xrange(limit+1)]
    for p in primes(limit+1):
