#Project Euler 160: Factorial trailing digits
from math import factorial
#def f(n):

def prod(l):
    p = 1
    for i in l:
        p *= i
    return p

products = [prod(range(i, 100000, 10)) % 100000 for i in xrange(10)]

def g(i, n):
    if n % 100000 == 0:
        if i % 2 == 1:
            return 1
        else:
            return pow(products[i], n//100000, 100000)
    else:
        #Tackle this later
        raise ValueError("n not divisible by 10^5")

print products
print prod(range(1, 10**6, 10**5))
a = factorial(10**5)
print len(str(a))
