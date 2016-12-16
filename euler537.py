from eulertools import primes

prime_list = primes(10**6)


num_pi = [1]
for i in xrange(len(prime_list)-1):
    num_pi.append(prime_list[i+1] - prime_list[i])

modulus = 1004535809

def T(n, k):
    l = num_pi
    for i in xrange(2, k+1):
        new_l = []
        for m in xrange(n+1):
            new_l.append(sum(num_pi[j]*l[m-j] % modulus for j in xrange(m+1)) % modulus)
        l = new_l
    return l[n]

for i in xrange(0, 11):
    print T(10, i)
