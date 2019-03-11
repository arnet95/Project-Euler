from eulertools import isqrt

def T(n):
    count = 0
    for a in xrange(1, n+1):
        print a
        for k in xrange(1, 101):
                b = a + k
                r = a**2+a*b+b**2
                c = isqrt(r)
                if c**2 == r:
                    if c <= n:
                        count += 1
    return count

def sol_count(k, n):
    count = 0
    a = 1
    f = lambda a: 3*a**2 + 3*a*k + k**2
    while f(a) <= n**2:
        c = isqrt(f(a))
        if c**2 == f(a):
            count += 1
            print a, c
        a += 1
    return count

print sol_count(1, 1000000)
