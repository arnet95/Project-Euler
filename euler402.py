def works(a, b, c, m):
    return all((n**4+a*n**3+b*n**2+c*n) % m == 0 for n in xrange(1, m))

def M(a, b, c):
    return max(m for m in xrange(a+b+c+2) if works(a, b, c, m))

def S(N):
    result = 0
    for a in xrange(1, N+1):
        for b in xrange(1, N+1):
            for c in xrange(1, N+1):
                if M(a, b, c) > 1:
                    print a, b, c, M(a, b, c)
                result += M(a, b, c)
    return result

print S(10)
