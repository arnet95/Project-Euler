def isprime(n):
    if n == 2 or n == 3:
        return True
    if pow(2, n-1, n) == 1:
        if pow(3, n-1, n) == 1:
            for i in xrange(5, int(n ** 0.5) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
    return False

for x in xrange(1, 100001):
    for y in xrange(1, x):
        a = (x**2+y**2)*(x-y)
        b = x**2-x*y+y**2
        if a % b == 0:
            if isprime(a // b):
                print x, y, a//b, x-y
