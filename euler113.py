#Project Euler 113: Non-bouncy numbers

inc_mem = {}
def inc(d, n):
    """Returns the number of n-digit increasing numbers with starting digit d"""
    if (d, n) in inc_mem:
        return inc_mem[(d, n)]
    elif n == 0:
        a = 1
    else:
        a = sum(inc(i, n-1) for i in xrange(d, 10))
    inc_mem[(d, n)] = a
    return a

dec_mem = {}
def dec(d, n):
    """Returns the number of n-digit decreasing numbers with starting digit d"""
    if (d, n) in dec_mem:
        return dec_mem[(d, n)]
    elif n == 0:
        a = 1
    else:
        a = sum(dec(i, n-1) for i in xrange(d+1))
    dec_mem[(d, n)] = a
    return a

def f(n):
    """Returns the number of non-bouncy numbers of length n"""
    return inc(1, n) + dec(9, n) - 10

def main(n):
    """Returns the number of non-bouncy numbers less than 10^n"""
    return sum(f(i) for i in xrange(1, n+1))

print main(100)
