def is_square(n):
  x = n // 2
  seen = set([x])
  while x * x != n:
    x = (x + (n // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def f(N):
    Nsq = N**2
    count = 0
    result = 0
    for bprime in xrange(1, isqrt(Nsq//2)+1):
        print bprime
        for cprime in xrange(1, min(bprime, isqrt((Nsq-bprime**2)//(1+4*bprime**2)))+1):
            count += 1
    #        res = bprime**2+cprime**2+4*bprime**2*cprime**2
    #        if is_square(res):
    #            result += isqrt(res)
#    print result
    print count

f(10**10)
