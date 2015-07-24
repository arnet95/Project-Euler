from math import sqrt

def is_square2(n):
  x = n // 2
  seen = set([x])
  while x * x != n:
    x = (x + (n // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def is_square(n):
    if sqrt(n) % 1 == 0:
        if abs(sqrt(n)**2 - n) < 1E-8:
            return is_square2(n)
    return False

#print "1: 2"
#n = 3
#c = 2
#while True:
#    if is_square(5*n**2 + 2*n + 1):
#        print "%d: %d" % (c, n)
#        c += 1
#        n *= 6
#    if is_square(5*n**2 + 22*n + 25):
#        print "%d: %d" % (c, n + 2)
#        c += 1
#        n *= 6
#    n += 3

fib_cache = {0: 0, 1: 1}
def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    else:
        tmp = fib(n-1) + fib(n-2)
        fib_cache[n] = tmp
        return tmp

print fib(30)*fib(31)
