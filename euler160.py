#Project Euler 160: Factorial trailing digits

def factorial(n):
    s = 1
    for i in xrange(1, n):
        s *= i
    return s

def f(n):
    if n == 1:
        return 36288
    else:
        s = 1
        for i in [3,4,6,7,8,9]:
            s *= pow(i, 10**(n-1), 10**5)
            s %= 100000

        return (s * f(n - 1) * factorial(10**n - 1)**2) % 10**5



print f(2)
print factorial(100)
