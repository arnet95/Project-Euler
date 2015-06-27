#Project Euler 113: Non-bouncy numbers

inc_mem = {}
def inc(d, n):
    if (d, n) in inc_mem:
        return inc_mem[(d, n)]
    else:
        if d == 9:
            a = 1
        elif n == 1:
            a = 10-d
        else:
            a = sum(inc(i, n-1) for i in xrange(d, 10))
        inc_mem[(d, n)] = a
        return a


dec_mem = {}
def dec(d, n):
    if (d, n) in dec_mem:
        return dec_mem[(d, n)]
    else:
        if d == 0:
            a = 1
        elif n == 1:
            a = d + 1
        else:
            a = sum(dec(i, n-1) for i in xrange(0, d+1))
        dec_mem[(d, n)] = a
        return a

def f(n):
    """Returns the number of non-bouncy numbers of length n"""
    return inc(1, n) + dec(9, n) - 10

def main(n):
    return sum(f(i) for i in xrange(1, n+1))

print main(100)
