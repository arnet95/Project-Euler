from eulertools import isqrt

def F(k, N):
    result = 0
    d = 1
    while (d*2*(k-2) + (4-k))**2 <= N:
        A = (d*2*(k-2) + (4-k))**2
        B = (d**2*(k-2) + (4-k)*d)//2
        result += (A + B)
        d += 1
    return result

def S(N):
    result = 0
    for k in xrange(3, isqrt(N)+1, 2):
        result += F(k, N)
    return result

print S(10**12)
#print F(3, 10**2)
