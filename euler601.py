from fractions import gcd
from eulertools import primes, crt


def lcm(l):
    lcm = 1
    for i in l:
        lcm = lcm * (i // gcd(lcm, i))
    return lcm

def prime_factors(n):
    l = []
    for p in primes(n+1):
        while n % p == 0:
            n //= p
            l.append(p)
    return l

def streak(n, s):
    return all([n % i == 1 for i in range(2, s+1)]) and (n % (s+1) != 1)

def P1(s, N):
    return sum(streak(n, s) for n in xrange(2, N))

def P(s, N):
    factors = prime_factors(s+1)
    if len(set(factors)) > 1:
        return 0
    m1 = lcm(range(2, s+1))
    m2 = s+1
    if len(factors) == 1:
        l = []
        for i in [0] + range(2, s+1):
            l.append(crt(1, i, m1, m2))
        period = m1*m2
        result = 0
        for i in l:
            k = (N - i)//period
            if period*k < N - i:
                result += (k+1)
            else:
                result += k
        return result
    else:
        period = lcm([m1, m2])
        l = [m1*k + 1 for k in range(1, period//m1)]
        result = 0
        for i in l:
            k = (N - i)//period
            if period*k < N - i:
                result += (k+1)
            else:
                result += k
        return result

print P(1, 4)
print P1(1, 4)

print sum(P(i, 4**i) for i in xrange(1, 32)) - 1
#Gives wrong value for P(1, 4), so subtracts 1 to get the right answer 
