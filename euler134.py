from eulertools import primes, modinv

def main(n):
    prime_list = primes(n)[2:]
    s = 0
    for i in xrange(len(prime_list)-1):
        p1 = prime_list[i]
        p2 = prime_list[i+1]
        s += f(p1, p2)
    return s

def f(p1, p2):
    n = 10
    while n < p1:
        n *= 10
    return n*((modinv(n%p2, p2) * (p2-p1)) % p2) + p1

print main(1000004)
