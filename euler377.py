mem = {}
def c(n):
    if n in mem:
        return mem[n]
    elif n <= 0:
        mem[n] = 0
        return 0
    elif n <= 9:
        result = sum(c(n-d) for d in xrange(1, 10)) + 1
        mem[n] = result
        return result
    else:
        result = sum(c(n-d) for d in xrange(1, 10))
        mem[n] = result
        return result

for i in xrange(1, 50):
    print i, c(i), 2**(i-1) - c(i)
