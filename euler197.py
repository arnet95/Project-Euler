a = 2**30.403243784

def f(x):
    return int(a/(2**(x**2))) * (10**(-9))

def g(x):
    return f(f(x))

s = -1
for _ in xrange(10000):
    s = g(s)

s2 = f(-1)
for _ in xrange(10000):
    s2 = g(s2)

print s + s2
#Works!!!
#The sequences alternates, and very quickly indeed.
