from eulertools import primes

prime_list = primes(10**7)

print sum(prime_list)

f = lambda n : n**2 - 3*n - 1
def R(p):
    for i in xrange(1, p**2+1):
        if f(i) % p**2 == 0:
            return i
    return 0

for p in prime_list[:20]:
    print p, R(p) % p
