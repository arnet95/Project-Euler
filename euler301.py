#Project Euler 301: Nim

def main(n):
    c = 0
    for i in xrange(1, n+1):
        if i ^ 2*i == 3*i:
            c += 1
    return c


print main(2**30)
