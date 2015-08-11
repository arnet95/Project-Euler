#Project Euler 164: Numbers for which no three consecutive digits
#have a sum greater than a given value

mem = {}
def f(xpp, xp, x, n):
    if (xpp, xp, x, n) in mem:
        return mem[(xpp, xp, x, n)]
    elif n == 0:
        a = 1
    else:
        a = sum(f(xp, x, i, n-1) for i in xrange(10 - xp - x))
    mem[(xpp, xp, x, n)] = a
    return a

def main(n):
    """Returns the number of n-digit numbers such that the sum of
       three consecutive digits never exceeds 9"""
    return sum(f(0, 0, i, n-1) for i in xrange(1, 10))

print main(20)

#We let f(xpp, xp, x, n) represent the number of n+3-digit numbers
#where the first three digits are xpp, xp, and x respectively. If we, when we
#recursively call f, makes sure that xpp + xp + x <= n, we never have to check
#that condition later. This makes our base case when n == 0, and then we can
#return 1, as we've found a number satisying the conditions. Otherwise, we
#can call f(xp, x, i, n-1) for all values of i such that xp + x + i <= n.
#If we memoize f, we get the right answer in ~20 ms.
