from __future__ import division
from math import sqrt
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
    elif a == b:
        tmp = ((a-2)*(a-1))//2
        tri_mem[(a, b)] = tmp
        return tmp
    else:
        tmp = 0
        for x in xrange(1, a):
            if (b*x % a) == 0:
                tmp += b - (b*x) // a - 1
            else:
                tmp += int(b - (b*x)/a)
        tri_mem[(a, b)] = tmp
        return tmp

def quad_num(a, b, c, d):
    return tri_num(a, b) + tri_num(b, c) + tri_num(c, d) + tri_num(d, a) + a + b + c + d - 3

def main(n):
    l = [0] * 40000
    for a in xrange(1, n+1):
        for b in xrange(1, n+1):
            for c in xrange(1, n+1):
                for d in xrange(1, n+1):
                    l[quad_num(a, b, c, d)] += 1
    return sum(j if is_square(i) else 0 for i, j in enumerate(l))

print main(100)
