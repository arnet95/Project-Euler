#Project Euler 76: Counting summations

mem = {}
def f(n, max_allowed):
    if (n, max_allowed) in mem:
        return mem[(n, max_allowed)]
    if max_allowed == 1:
        tmp = 1
    elif n == max_allowed:
        tmp = 1 + f(n, max_allowed - 1)
    else:
        tmp = sum(f(n-i, min(i, n-i)) for i in xrange(1, max_allowed+1))
    mem[(n, max_allowed)] = tmp
    return tmp

def main(n):
    return f(n, n-1)

print main(100)
