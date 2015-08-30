#An equivalent condition is that 2s_5(i) < 1 + s_5(2i-1)
from math import log

def legendre(n):
    return sum(n // (5**k) for k in xrange(1, int(log(n)/log(5)) + 1))

def convert_to(b, n):
    k = int(log(n)/log(b))
    l = [0]*(k+1)
    while n > 0:
        l[k] = n/(b**k)
        n = n % (b**k)
        k -= 1
    return l

def T5(n):
    counter = 0
    for i in xrange(5, n+1, 5):
        if legendre(2*i-1) < 2*legendre(i):
            print i, convert_to(5, i)[::-1], convert_to(5, 2*i-1)[::-1]
            counter += 1
    return counter

def new_l(l):
    

print T5(1000)
