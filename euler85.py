def num_rect(M, N):
    return (M*(M+1)*N*(N+1))// 4

#We have that it is equal to sum((N-n+1)(M-m+1) for n in xrange(1, N+1) for m in xrange(1, M+1))
#Using arithmetic sequences, we can get the closed form expressions.


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

print f(100) #Good enough
