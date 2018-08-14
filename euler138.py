limit = 12

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

l = []
n = 1
while len(l) < limit:
    N = n**2
    if is_square(5*N+1):
        m = 2*n + isqrt(5*N+1)
        l.append(m**2+N)
    elif is_square(5*N-1):
        m = 2*n + isqrt(5*N-1)
        l.append(m**2+N)
    n += 1

print sum(l)


#Nice pattern emerges by simply looking at the results
#If (m, n) is a pair giving rise to a correct Pyth. triple, then
#(2n+sqrt(5n^2+1),m) or (2n+sqrt(5n^2-1), m) will be the next pair.
#
