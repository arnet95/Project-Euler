#Euler71
target = (3, 7)

def greater_than(a, b):
    return a[0]*b[1] > a[1]*b[0]

def f(k):
    s = (1, k)
    for d in xrange(1, k+1):
        if d%10000 == 0:
            print d
        for n in xrange(int((42.0/100)*d),d):
            x = (n, d)
            if greater_than(target, x):
                if greater_than(x, s):
                    s = x
            else:
                break
    return s[0]

print f(10**6)
