#Project Euler 512: Sums of totients of powers

def sundaram3(n):
    """New prime sieve. Uses less memory than the one in eulertools"""
    numbers = range(3, n+1, 2)
    half = n//2
    initial = 4
    for step in xrange(3, n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)
        if initial > half:
            return filter(None, numbers)

def totient_gen(n):
    phis = range(1, n, 2)
    for p in sundaram3(n):
        phis[p//2] = p - 1
        if 3*p < n:
            for i in xrange(3*p, n, 2*p):
                phis[i//2] = (phis[i//2] // p) * (p-1)
    return phis

def main(n):
    return sum(totient_gen(n))

print main(5*10**8)

#Through some calculations, we get that g(n) is given by the sum of
#odd totients up to, and including n.
#We use a sieve to compute the sum.
