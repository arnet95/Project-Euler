from eulertools import primes

N = 10**8

prime_list = primes(N)

def gen_even_radicals(n):
    """Generates a list of a list of prime factors for all numbers <= n"""
    radicals = [2 for i in xrange(n//2+1)]
    for prime in primes(n+1)[1:]:
        for i in xrange(2*prime, n+1, 2*prime):
            radicals[i//2] *= prime
    return radicals

radical_list = gen_even_radicals(N)

dictionary = {p: radical_list[(p+1)//2] for p in prime_list}

reversed_dictionary = {}
for p in dictionary:
    if dictionary[p] in reversed_dictionary:
        reversed_dictionary[dictionary[p]].append(p)
    else:
        reversed_dictionary[dictionary[p]] = [p]


print len(reversed_dictionary)

print max(len(reversed_dictionary[n]) for n in reversed_dictionary)
