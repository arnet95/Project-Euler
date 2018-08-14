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

for k in xrange(1, 101):
    for l in xrange(1, k+1):
        res = k**2+l**2+(2*k*l)**2
        if is_square(res):
            print k, l, isqrt(res)
