from eulertools import primes, modinv

def f(p1, p2):
    n = 10
    while n < p1:
        n *= 10
    return n*((modinv(n%p2, p2) * (p2-p1)) % p2) + p1

#Rephrasing the question, for a given p1 and p2, and an n such that n = 10^m for
#some positive integer m and n > p1, and for m < n, n < p1, find the smallest k
#such that k * n + p1 % p2 == 0. We have
#k * n + p1 % p2 == 0 <==> k * n % p2 == (-p1) % p2


def main(n):
    prime_list = primes(n)[2:]
    return sum(f(prime_list[i], prime_list[i+1]) for i in xrange(len(prime_list)-1))

print main(1000004)
