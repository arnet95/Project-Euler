#Project Euler 115: Counting block combinations II

def F(m, n):
    mem = {}
    def f(n, red):
        if (n, red) in mem:
            return mem[(n, red)]
        elif n < m:
            mem[(n, red)] = 1
            return 1
        elif red:
            a = f(n-1, False)
            mem[(n, red)] = a
            return a
        else:
            a = f(n - 1, False) + sum(f(i, True) for i in xrange(n - m, -1, -1))
            mem[(n, red)] = a
            return a

    return f(n, False)

def main():
    i = 0
    while True:
        if F(50, i) > 1000000:
            return i
        i += 1

print main()
