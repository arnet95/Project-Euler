#Project Euler 120: Square remainders

def main(n):
    r_max_sum = 0
    for a in xrange(3, n+1):
        r_max = 2
        for n in xrange(1, a):
            r_max = max(r_max, (2*n*a)%(a**2))
        r_max_sum += r_max
    return r_max_sum

print main(1000)
