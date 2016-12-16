#Project Euler 211: Divisor Square Sum
from math import sqrt
from eulertools import dynamic_sigma

#The basic idea is to just create a list of sums of squares of divisors.
#Then we go through the list and check if the relevant number is square.
#We use a fairly dumb square check, but it suffices in this case since the
#numbers to check are small enough.

def main(n):
    l = dynamic_sigma(2, n)
    return 1 + sum(i for i in xrange(2, len(l)) if sqrt(l[i]) % 1 == 0)

print main(64*10**6)

#Uses about 1GB of memory, and takes about 35 seconds to complete.
