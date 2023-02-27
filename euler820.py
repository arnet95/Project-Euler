from eulertools import primes, prod
from math import lcm
#from functools import reduce

N = 10**7

def dynamic_divisors(n):
	divs = [[], [1]] + [[1, i] for i in range(2, n+1)]
	for i in range(2, int(n**0.5) + 1):
		divs[i*i].append(i)
		divs[i*i].sort()
		for d in range(i*(i+1), n+1, i):
			divs[d].append(i)
			divs[d].append(d//i)
			divs[d].sort()
	return divs

divisors_list = dynamic_divisors(N)
print("Test")

def prime_factors_gen(n):
    factorisations = [{} for _ in range(n+1)]
    for p in primes(n+1):
        for i in range(p, n+1, p):
            factorisations[i][p] = 1
        k = 2
        while p**k <= n:
            for i in range(p**k, n+1, p**k):
                factorisations[i][p] += 1
            k += 1
    return factorisations

period_mem = {}
def period(p, k):
    if (p, k) in period_mem:
        return period_mem[(p, k)]
    if k == 1:
        for d in divisors_list[p-1]:
            if pow(10, d, p**k) == 1:
                period_mem[(p, 1)] = d
                return d
    else:
        base_period = period(p, 1)
        if p == 3 or p == 487:
            d = p**(k-2)*base_period
            period_mem[(p, k)] = d
            return d
        else:
            d = p**(k-1)*base_period
            period_mem[(p, k)] = d
            return d

def d(n, den_fac):
    factors = set(den_fac.keys())
    if factors <= set([2, 5]):
        return 0
    else:
        #Assumes gcd(den, 2) = gcd(den, 5) = 1
        a = den_fac[2] if 2 in den_fac else 0
        b = den_fac[5] if 5 in den_fac else 0
        rep_period = lcm(*[period(p, den_fac[p]) for p in den_fac if p != 2 and p != 5])
        den = prod([p**den_fac[p] for p in den_fac])
        n = (n - max(a, b)) % rep_period
        if n == 0:
            n = rep_period
        n += max(a, b)
        rem = 1
        for i in range(n):
            digit = (rem*10) // den
            rem = (rem*10 - digit*den)
        return digit

def S(n):
    factorisations = prime_factors_gen(n)
    result = 0
    for k in range(2, n+1):
        if k % 10**4 == 0:
            print(k)
        result += d(n, factorisations[k])
    return result

print(S(N))
