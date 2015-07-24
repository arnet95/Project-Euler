#Project Euler 114: Counting block combinations I

mem = {}
def f(n, red):
    if (n, red) in mem:
        return mem[(n, red)]
    elif n < 3:
        mem[(n, red)] = 1
        return 1
    elif red:
        a = f(n-1, False)
        mem[(n, red)] = a
        return a
    else:
        a = f(n - 1, False) + sum(f(i, True) for i in xrange(n - 3, -1, -1))
        mem[(n, red)] = a
        return a

print f(50, False)
