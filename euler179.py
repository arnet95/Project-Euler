#Euler 179
from math import sqrt

def f(n):
    divs = [0, 1] + [2] * (n - 1)
    for i in xrange(2, int(sqrt(n)) + 1):
        divs[i*i] += 1
        for d in xrange(i*(i+1), n+1, i):
            divs[d] += 2
    return divs

def main(n):
    c = 0
    divs = f(n)
    old = divs[2]
    for div in divs[3:]:
        if div == old:
            c += 1
        old = div
    return c

print main(10**7)
