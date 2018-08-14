from math import sqrt

def F(n):
    s = set([])
    for b in xrange(2, int(n**(1/3.))+1):
        for a in xrange(2, int(sqrt((n // (b**3))))+1):
            if a**2*b**3 in s:
                print a, b
            else:
                s.add(a**2*b**3)
    return len(s)
print F(3*10**6)
