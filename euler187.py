#Euler 187
from time import time

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

t_start = time()
a = rwh_primes1(5*(10**7))
l = []

for i in a:
    for j in a:
        x = i*j
        if x < 10**8:
            l.append(x)
        else:
            break

print len(set(l))

t_finish = time()
print t_finish-t_start