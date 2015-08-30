from eulertools import primes
prime_list = [1] + primes(10**6)

def main(N):
    for n in xrange(1, len(prime_list), 2):
        if 2 * n * prime_list[n] >= N:
            return n

print main(10**10)

#Similarly to problem 120, we get that r = 2 * n * pn for n odd, and r = 2 for n even.
#Thus we just need to check the odd n's. In this case, we just needed to generate
#the primes up to 10**6, and we get the answer in about 0.1 seconds.
