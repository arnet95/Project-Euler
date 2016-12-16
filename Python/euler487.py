#Using Faulhaber's formula, we know that the sum of k'th powers
#can be written as a polynomial of degree k+1. And when you sum up many of these
#you get a polynomial of degree k+2. Then, one can use some polynomial
#interpolation method to find this polynomial. I use Lagrange interpolation
#modulo p, which works out nicely, although takes a decent amount of time.
#About 30 minutes on my computer.

from eulertools import modinv

def isprime(n):
    if n == 2 or n == 3:
        return True
    if pow(2, n-1, n) == 1:
        if pow(3, n-1, n) == 1:
            for i in xrange(5, int(n ** 0.5) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
    return False

S = lambda k, n, p: sum((n+1-i)*pow(i, k, p) % p for i in xrange(1, n+1)) % p

def l(i, n, p, degree):
    numerator, denominator = 1, 1
    for m in xrange(degree+1):
        if m != i:
            numerator *= (n - m)
            numerator %= p
            denominator *= (i-m)
            denominator %= p
    return (numerator*modinv(denominator, p)) % p

def main(k, n, prime_list):
    return sum((sum(S(k, i, p)*l(i, n, p, k+2) % p for i in xrange(k+3)) % p) for p in prime_list)

prime_list = [i for i in xrange(2*10**9, 2*10**9+2001) if isprime(i)]
print main(10000, 10**12, prime_list)
