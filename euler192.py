from eulertools import isqrt
from fractions import *

def cf_gen(n):
    m = isqrt(n)
    tup = (n, 0, 1)
    while True:
        n, p, q = tup
        k = (m + p)//q
        yield k
        tup = n, q*k-p, (n - (q*k - p)**2)//q

def mediant(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def update_interval(current_interval, right):
    t1, t2 = current_interval
    if right:
        return (mediant(t1, t2), t2)
    else:
        return (t1, mediant(t1, t2))

def closer(t1, t2, n):
    a = Fraction(*t1)
    b = Fraction(*t2)
    if a > b:
        return (a**2-b**2)**2 <= 4*(a-b)**2*n
    else:
        return (a**2-b**2)**2 >= 4*(a-b)**2*n

def best_approximation(n, d):
    generator = cf_gen(n)
    current_interval = ((generator.next(), 1), (1, 0))
    cont = True
    right = False
    while cont:
        for i in xrange(generator.next()):
            if sum(current_interval[j][1] for j in [0,1]) >  d:
                cont = False
                break
            current_interval = update_interval(current_interval, right)
        right = not right
    if closer(current_interval[0], current_interval[1], n):
        return current_interval[0][1]
    else:
        return current_interval[1][1]

def main(L):
    result = 0
    for n in xrange(2, L+1):
        if isqrt(n)**2 < n:
            result += best_approximation(n, 10**12)
    return result

print main(10**5)
