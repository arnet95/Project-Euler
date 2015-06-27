#Project Euler 164: Numbers for which no three consecutive digits
#have a sum greater than a given value

mem = {}

def f(xpp, xp, x, n):
    if (xpp, xp, x, n) in mem:
        return mem[(xpp, xp, x, n)]
    elif n == 0:
        a = 1 * ((xpp + xp + x) <= 9)
        mem[(xpp, xp, x, n)] = a
        return a
    elif (xpp + xp + x) > 9:
        mem[(xpp, xp, x, n)] = 0
        return 0
    else:
        a = sum(f(xp, x, i, n-1) for i in xrange(10))
        mem[(xpp, xp, x, n)] = a
        return a

def main(n):
    return sum(f(0, 0, i, n - 1) for i in xrange(1, 10))

print main(20)
