def num_rect(M,N):
    s=0
    for m in xrange(1,M+1):
        for n in xrange(1,N+1):
            s += (M+1-m)*(N+1-n)
    return s


def f(n):
    a,b = 0,0
    diff = 2000000
    for i in xrange(1,n+1):
        for j in xrange(1,n+1):
            x = num_rect(i,j)
            if abs(x - 2000000) < diff:
                a, b = i, j
                diff = abs(2000000 - x)
            if x > 2000000:
                break
    return a,b
