from __future__ import division
from math import sqrt
from math import ceil
from time import time

squares = [i**2 for i in xrange(141)]

def is_square(n):
    return sqrt(n) % 1 == 0

tri_mem = {}
def tri_num(a, b):
    if (a, b) in tri_mem:
        return tri_mem[(a, b)]
    elif (b, a) in tri_mem:
        return tri_mem[(b, a)]
    elif a == 1 or b == 1:
        tri_mem[(a, b)] = 0
        return 0
    else:
        tmp = b - (b//a) - 2 + (a//b) * (b - 1) + tri_num(a-1, b-1)
        tri_mem[(a, b)] = tmp
        return tmp

def quad_num(a, b, c, d):
    return tri_num(a, b) + tri_num(b, c) + tri_num(c, d) + tri_num(d, a) + a + b + c + d - 3


def main(n):
    l = [0] * 20000
    for a in xrange(1, n+1):
        for b in xrange(1, n+1):
            for c in xrange(1, n+1):
                for d in xrange(1, n+1):
                    l[quad_num(a, b, c, d)] += 1
    return sum(j if is_square(i) else 0 for i, j in enumerate(l))

#t0 = time()
print main(1)
#print time() - t0
