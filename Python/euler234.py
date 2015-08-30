#Project Euler 234: Semidivisible numbers
from eulertools import primes

counter = 0

def f(p1, p2, n=None):
    s1 = range(p1**2 + p1, min(n+1, p2**2+1), p1)
    s2 = range(min(n-(n%p2), p2**2 - p2) , p1**2 - 1, - p2)
    s = 0
    count = 0
    for c in s1:
        if c not in s2:
            s += c
    for c in s2:
        if c not in s1:
            s += c
    return s

n = 999966663333
prime_list = primes(1000000)
print sum(f(prime_list[i], prime_list[i+1], n) for i in xrange(len(prime_list)-1))

#The primary thing to notice here is that for consecutive primes p1 and p2,
#all numbers p1**2 < n < p2**2, we have lps(n) = p1 and ups(n) = p2.
#If n is a perfect square of a prime p, we have lps(n) = ups(n) = p, so it is not
#semidivisible.

#We let f(p1, p2, n) be the sum of semidivisible numbers between p1**2 and p2**2
#not exceeding n. We create two lists of numbers, one containing the numbers
#divisible by p1, and one containing the numbers divisible by p2, and we make sure
#that all numbers are <= n. Then we sum up all the numbers in each list which
#are not members of the other list. This could be made more efficient by using
#arithmetic sequences like in Problem 1, but this is not necessary, as the current
#program runs in about 0.2s on pypy.
