#n is a golden nugget <=> 5n^2+14n+1 is a perfect square

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

#def poss_n(modulus):
#    s = set([pow(k, 2, modulus) for k in xrange(modulus)])
#    return [n for n in xrange(modulus) if (5*n**2+14*n+1) % modulus in s]

#print len(poss_n(13**5)), 13**5

f = lambda k: 5*k**2 + 14*k + 1

a_mem = {1: 2, 2: 5, 3: 21, 4: 42}
def a(k):
    if k in a_mem:
        return a_mem[k]
    else:
        return 3*isqrt(f(a(k-2))) + a(k-4)

print sum(a(k) for k in xrange(1, 31))
