#Project Euler 135: Same differences
from math import sqrt

def poss_candidate(n):
    if n % 2 == 0:
        c = 2
        for i in xrange(3, int(sqrt(n))+1):
            if n % i == 0:
                c += 1
    else:
        c = 1
        for i in xrange(3, int(sqrt(n))+1, 2):
            if n % i == 0:
                c += 1
    return c >= 5

def first_divisors(n):
    if n % 2 == 0:
        l = [1, 2]
        for i in xrange(3, int(sqrt(n)) + 1):
            if n % i == 0:
                l.append(i)
    else:
        l = [1]
        for i in xrange(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                l.append(i)
    return l

def f(n):
    c = 0
    for i in first_divisors(n):
        a, b = i, n/i
        if (a != b):
            if (a + b) % 4 == 0:
                if 3*b > a:
                    c += 1
                if 3*a > b:
                    c += 1
        else:
            if (a + b) % 4 == 0:
                c += 1
    return c == 10

def main(n):
    c = 0
    for i in xrange(1, n):
        if poss_candidate(i):
            if f(i):
                c += 1
    return c

print main(10**6)
