from math import sqrt, pi

def integrate(start, stop, f, N=10**6):
    h = float(stop - start)/N
    return h*sum(f(start + i*h) for i in xrange(N))

def P(n):
    d = (1 + 1./n - sqrt(2./n)) / (1 + 1./(n**2))
    return (d**2/(2*n) + integrate(d, 1, lambda x: 1 - sqrt(2*x-x**2))) / (1-pi/4)

def main(limit):
    n = 1
    while P(n) >= limit:
        n *= 2
    a, b = n // 2, n
    while b - a > 1:
        c = (a + b) // 2
        if P(c) >= limit:
            a = c
        else:
            b = c
    return b


print main(0.001)
