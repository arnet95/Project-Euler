from eulertools import primes

def C(n):
    count = 0
    for i in xrange(2, n):
        if pow(i, 3, n) == 1:
            count += 1
    return count

def is_square(n, p):
    return pow(n, (p-1) // 2, p) == 1

prime_list = primes(6426322)

three_primes = []
one_primes = []
for p in prime_list:
    if is_square(p-3, p):
        three_primes.append(p)
    else:
        one_primes.append(p)

print len(three_primes)
