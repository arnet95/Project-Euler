#Project Euler 346: Strong Repunits
from math import sqrt

def f(n):
    l = [1]
    for b in xrange(2, int(sqrt(n)) + 1):
        s = 1 + b + b**2
        i = 3
        while s < n:
            l.append(s)
            s += b**i
            i += 1
    return sum(set(l))

print f(10**12)

#First we note that all numbers n > 2 is a repunit in base b = n - 1, so
#we only need to care about the numbers expressible as a repunit of length >= 2.
#We go through the possible bases, generate all repunits of length >= 2,
#and add them to the list. Finally, we sum over the list with any duplicates removed.
#(This is done by the call to set(l))
