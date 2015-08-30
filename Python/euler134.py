#Project Euler 134: Prime pair connection
from eulertools import primes, modinv

def f(p1, p2):
    n = 10
    while n < p1:
        n *= 10
    return n*((modinv(n%p2, p2) * (p2-p1)) % p2) + p1

#Rephrasing the question, for a given p1 and p2, and an n such that n = 10^m for
#some positive integer m and n > p1, and for c < m, 10**c < p1, find the smallest k
#such that (k * n + p1) % p2 == 0. If we find this k, S = k * n + p1. We have
#k * n + p1 % p2 == 0 <==> k * n % p2 == (-p1) % p2. We have (-p1) % p2 == p2-p1
#for the values of p1 and p2 we send in.
#Therefore we have k = (modinv(n, p2) * (p2-p1)) % p2.
#This program is a straightforward implementation of this.

def main(n):
    prime_list = primes(n)[2:]
    return sum(f(prime_list[i], prime_list[i+1]) for i in xrange(len(prime_list)-1))

print main(1000004)
