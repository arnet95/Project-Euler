from math import log2
from eulertools import primes
from bisect import bisect

def log_hybrid(p, q):
    return q*log2(p) + p*log2(q)

def C(m):
    q = 1
    while log_hybrid(2, q) < m:
        q *= 2
    result = 0
    ps = primes(q)
    i = 0
    while log_hybrid(ps[i], ps[i+1]) <= m:
        p = ps[i]
        L = 0
        R = len(ps)-1
        while L <= R:
            mid = (L+R)//2
            if log_hybrid(p, ps[mid]) <= m:
                L = mid + 1
            else:
                R = mid - 1
        #print(log_hybrid(p, ps[L-1]) > m)
        result += (L-i-1)
        i += 1
    return result

#print(C(800*log2(800)))
print(C(800800*log2(800800)))