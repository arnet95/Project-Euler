from eulertools import primes

prime_list = primes(2*10**6)

def factorise(n):
    prime_factors = []
    for p in prime_list:
        if n == 1:
            break
        while n % p == 0:
            n //= p
            prime_factors.append(p)
    return list(reversed(prime_factors))

phi_mem = {}
def pi(x):
    prime_list = [1] + primes(int(x**0.5)+1)
    def phi(x, a):
        if (x, a) in phi_mem:
            return phi_mem[(x, a)]
        elif a == 1:
            return (x + 1) // 2
        else:
            t = phi(x, a-1) - phi(x // prime_list[a], a-1)
            phi_mem[(x, a)] = t
            return t
    return phi(x, len(prime_list) - 1) + len(prime_list) - 2

def main():
    result = 1
    count = 0
    for s in xrange(7, 5**9+1, 6):
        l = factorise(s)
        min_result = 1
        for i in xrange(len(l)):
            min_result *= prime_list[i]**(l[i]-1)
        if min_result <= 10**36:
            count += 1
            print l
    print count

main()
