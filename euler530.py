from eulertools import primes, isqrt
from bisect import bisect_left
from sys import setrecursionlimit



prs = primes(10**8+100)
prime = [0, 0] + [1]*(10**8-2)
for i in xrange(2, 10**4):
    if prime[i]:
        for goUp in xrange(i*i, 10**8, i):
            prime[goUp] = 0


numpr = [0]
prime_count = 0
for i in xrange(1, 10**8):
    if prime[i]:
        prime_count += 1
    numpr.append(prime_count)

phicache = [0]*5*10**8
for i in xrange(5*10**6):
    phicache[i*100] = i
for i in xrange(1, 100):
    for j in xrange(1, 5*10**6):
        phicache[j*100+i] = phicache[j*100+i-1] - phicache[(j//prs[i-1])*100+i-1]

def phi(m, n):
    if m < 5*10**6 and n < 100:
        return phicache[m*100+n]
    prn = prs[n]
    if m < prn:
        return 1
    if m < 10**8 and m < prn*prn:
        return numpr[m]-n+1
    res = m
    for i in xrange(n):
        nex = m//prs[i];
        if nex < 10**8 and i > numpr[nex]:
            res += (i-n)
        res -= phi(nex, i)
    return res

def countPrime(n):
    if n < 10**8:
        return numpr[n]
    prsq = numpr[isqrt(n)] + 1
    return phi(n, prsq) - 1 + prsq

print countPrime(10**13)



def f(p, k):
    m = k // 2
    if k % 2 == 0:
        return (p**(m+1) + p**m - 2)//(p-1)
    else:
        return 2*(p**(m+1)-1)//(p-1)

mem = {}
def H(n, i):
    if (n, i) in mem:
        return mem[(n, i)]
    if n < prime_list[i]:
        return 1
    curr_prime = prime_list[i+1]
    if curr_prime <= n < curr_prime**2:
        return 2*(countPrime(n) - countPrime(prime_list[i]))
        #Using that f(p) = 2 for all primes p
    else:
        result = 0
        k = 0
        while curr_prime**k <= n:
            result += f(curr_prime, k)*H(n//(curr_prime**k), i+1)
            k += 1
        mem[n] = result
        return result

#print H(1000, 0)
