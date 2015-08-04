a = 2**30.403243784

def f(x):
    return int(a/(2**(x**2))) * (10**(-9))

def g(x):
    return f(f(x))

s1 = -1
for _ in xrange(10000):
    s1 = g(s1)

s2 = f(-1)
for _ in xrange(10000):
    s2 = g(s2)

print s1 + s2

#By some experimentation, we see that the sequence converges to an alternating
#sequence, and it does so very quickly. This means that
