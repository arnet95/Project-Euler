from itertools import combinations
from eulertools import primes

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def prod(l):
    result = 1
    for i in l:
        result *= i
    return result

def interval_count(low, high, n):
    if low % n != 0:
        low += (n - low % n)
    high -= high % n
    return (high - low) // n + 1

def high_gcd_count(low, high, prime_factors):
    s = 0
    for i in xrange(1, len(prime_factors) + 1):
        s += (-1)**(i+1)*sum(interval_count(low, high, prod(l)) for l in combinations(prime_factors, i))
    return s

def rel_prime_interval_count(low, high, prime_factors):
    return (high - low + 1) - high_gcd_count(low, high, prime_factors)

def prime_factors_gen(n):
	phis = [[] for _ in xrange(n+1)]
	for p in primes(n+1):
		for i in xrange(p, n+1, p):
			phis[i].append(p)
	return phis

def P(limit):
    prime_factors = prime_factors_gen(isqrt(limit//2))
    print "Found prime factors"
    n = 1
    result = 0
    while 2*n**2 + 2*n + 1 <= limit:
        low = n+1
        high = isqrt(limit-n**2)
        if n % 2 == 0:
            result += rel_prime_interval_count(low, high, prime_factors[n])
        else:
            result += (high_gcd_count(low, high, [2] + prime_factors[n]) - high_gcd_count(low, high, prime_factors[n]))
        n += 1
    return result

print P(3141592653589793)
