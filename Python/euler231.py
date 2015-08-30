#Project Euler 231: The prime factorisation of binomial coefficients
from eulertools import primes
from math import log

def convert_to(b, n):
    k = int(log(n)/log(b))
    l = [0]*(k+1)
    while n > 0:
        l[k] = n/(b**k)
        n = n % (b**k)
        k -= 1
    return l

def g(p, n):
    return sum(b*((p**i-1)//(p-1)) for i, b in enumerate(convert_to(p, n)))

def legendre(p, n):
    return sum(n // (p**k) for k in xrange(1, int(log(n)/log(p)) + 1))

def f(n):
    s = 0
    for p in primes(n):
        if p > n // 2:
            s += p
        else:
            s += p*legendre(p, n)
    return s


def main(m, n):
    return f(m) - f(n) - f(m-n)

print main(20000000, 15000000)

#Given n = p1**e1 * p2**e2 * ... * pn**en, sum_factor(n) = p1*e1 + p2*e2 + ... + pn*en.
#This reduces our tasks to finding ei for a given n.
#Also, since mCn = (m!) // ((n!) * ((m-n)!)), we have
#sum_factor(mCn) = sum_factor(m!) - sum_factor(n!) - sum_factor((m-n)!).
#We here let f(n) = sum_factor(n!). What we need to do, is to find the largest ei
#such that pi**ei | n!. We can do this two ways. One way is to use Legendre's formula,
#which states that ei = sum(n//(pi**k)) for all positive k. Alternatively, we
#can analytically show that if n = sum(ci * pi**i for i in xrange(k+1)), then
#ei = sum(ci* ((pi**i - 1) // (p-1)) for i in xrange(k+1)) for some k.
#Using this, it's fairly straightforward finding f(n). As an optimisation, we
#can recognise that if p > n // 2, ei = 1 regardless of p. In all other cases,
#we add up p*legendre(p, n) where legendre(p, n) returns the largest ei such that
#pi**ei | n!.
