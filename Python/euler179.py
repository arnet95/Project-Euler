#Euler 179
from math import sqrt

def d_sieve(n):
    divs = [0, 1] + [2] * (n - 1)
    for i in xrange(2, int(sqrt(n)) + 1):
        divs[i*i] += 1
        for d in xrange(i*(i+1), n+1, i):
            divs[d] += 2
    return divs

def main(n):
    count = 0
    divs = d_sieve(n)
    old = divs[2]
    for div in divs[3:]:
        if div == old:
            count += 1
        old = div
    return count

print main(10**7)

#We use a sieve to generate the number of divisors for all numbers up to n.
#We let d(0) = 0 and d(1) = 1, but that is fairly arbitrary.
#Then, we simply go through the list, and count the number of times divs[i] == divs[i+1]
