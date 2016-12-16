g_mem = {1:1}
def g(n):
    if n in g_mem:
        return g_mem[n]
    else:
        res = sum(g(d) for d in xrange(1, n) if n % d == 0)
        g_mem[n] = res
        return res

for i in xrange(1, 100001):
    if g(i) == i:
        print i
