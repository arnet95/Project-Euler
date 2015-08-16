#Project Euler 172: Investigating numbers with few repeated digits

mem = {}
def ndigits(n, tup):
    if (n, tup) in mem:
        return mem[(n, tup)]
    else:
        if n == 0:
            res = 1
        else:
            res = 0
            for i in xrange(10):
                s = tup[i]
                if s < 3:
                    res += ndigits(n-1, tup[:i] + (s+1,) + tup[i+1:])
        mem[(n, tup)] = res
        return res

def main(n):
    return sum(ndigits(n-1, (0,) * i + (1,) + (0,) * (9-i)) for i in xrange(1, 10))

print main(18)
