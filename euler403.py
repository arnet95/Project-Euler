from eulertools import isqrt

def is_square(n):
  if n == 0 or n == 1:
    return True
  x = n // 2
  seen = set([x])
  while x * x != n:
    x = (x + (n // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True


def L(a, b):
    x1 = (a - isqrt(a**2+4*b))//2
    x2 = (a + isqrt(a**2+4*b))//2
    return sum(a*x + b + 1 - x**2 for x in xrange(x1, x2+1))

def G(a, N):
    if a == 0:
        return (isqrt(N)+1)*(2*N*(isqrt(N)+1) + 5*isqrt(N) + 6)//6
    else:
        if a % 4 == 0 or a % 4 == 1:
            result = 0
            if a**2 >= 4*N:
                minm
            else:
                minm

            maxm = (-a + isqrt(a**2 + 4*N))//2
            for m in xrange(minm, maxm):
                result += sum(a*x + a*m + m**2 + 1 - x**2 for x in xrange(-m, a+m+1))
            return result
        else:
            return 0
        return result

def S(N):
    return G(0, N) + 2*sum(G(i, N) for i in xrange(1, N+1))

print S(100)
