from __future__ import division
from math import ceil

def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a
    

primitives = []
for m in xrange(2, 1000):
    for n in xrange((m%2)+1, m, 2):
        if gcd(m,n) == 1:
            x = 2*m*(m+n)
            if x <= 1500000:
                primitives.append(2*m*(m+n))

lengths = []
for prim in primitives:
    x = 1.5e6/prim
    k = 1
    while k <= ceil(x):
        y = prim*k
        if y <= 1500000:
            lengths.append(y)
        k += 1
print len(lengths)

lengths = sorted(lengths)
def f(l):
    counter = 0
    i = 0
    while i < len(l)-2:
        var1 = l[i]
        var2 = l[i+1]
        if var1 != var2:
            counter += 1
            i += 1
        else:
            while var1 == var2:
                try:
                    var2 = l[i+2]
                    i += 1
                except:
                    return counter
            i += 1
    if i == len(l)-1:
        counter += 1
    else:
        counter += 2
    return counter


print f(lengths)
