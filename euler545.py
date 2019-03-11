from eulertools import primes, isqrt
from itertools import product
from Queue import *
#D(2n) = 20010 iff {p | p-1 divides 2n} = {2, 3, 5, 23, 29}

def isprime(n):
    if n == 2 or n == 3:
        return True
    if pow(2, n-1, n) == 1:
        if pow(3, n-1, n) == 1:
            for i in xrange(5, isqrt(n) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
    return False

def test(n):
    divs = [i for i in xrange(1, n+1) if n % i == 0]
    curr_primes = [div+1 for div in divs if isprime(div+1)]
    return curr_primes == [2, 3, 5, 23, 29]

divisors308 = [i for i in xrange(1, 309) if 308 % i == 0]

def test(factors):
    d = {}
    for p in factors:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
    prime_list = sorted(d.keys())
    l = [range(d[p]+1) for p in prime_list]
    length = len(l)
    divisors = []
    for picker in product(*l):
        divisor = 1
        for i in xrange(length):
            divisor *= (d[p]**i)
        divisors.append(divisor)
    return [div+1 for div in divisors if isprime(div+1)] == [2, 3, 5, 23, 29]

def F(n):
    count = 1
    candidates = PriorityQueue()
    max_val = 5*10**6
    l =  []
    for p in primes(5*10**6):
        candidates.put((p, [p]))
    while count < n:
        cand = candidates.get()
        if all(not isprime(div+1) for div in [i*cand for i in divisors308]):
            if test()
            if cand not in l:
                count += 1
                l.append(cand)
                for i in l:
                    if i*cand > max_val:
                        break
                    else:
                        candidates.put(i*cand)
    return 308*l[-1]

print F(10**5)
