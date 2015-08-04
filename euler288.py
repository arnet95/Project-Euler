#Project Euler 288: An enormous factorial

def NP(p, q, m):
    res = 0
    s = 290797
    for n in xrange(1, m+1):
        s = pow(s, 2, 50515093)
        res += (s % p) * ((p**n - 1) // (p-1))
    mid = 0
    for n in xrange(m+1, q+1):
        s = pow(s, 2, 50515093)
        mid += (s % p)
    return (res + ((p**m - 1)//(p-1))*mid) % (p**m)

print NP(61, 10**7, 10)
