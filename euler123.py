from eulertools import primes
prime_list = [1] + primes(10**7)

def main(N):
    for n in xrange(1, len(prime_list)):
        if n % 2 != 0:
            if 2 * n * prime_list[n] >= N:
                return n

print main(10**10)
