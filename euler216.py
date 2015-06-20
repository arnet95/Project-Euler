#Euler 216


def isprime(n):
    #not good enough
    return pow(2,n-1, n) == 1

def f(n):
    s = 0
    for i in xrange(2, n):
        if isprime(2*i*i-1):
            s += 1
    return s


for i in range(10):
    print (4*i*i + 2*i + 1 )% 7