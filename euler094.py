def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def test(a, direction):
    if direction:
        #a, a+1, a+1
        m = (3*a+2)*(a+2)
    else:
        #a, a-1, a-1
        m = (3*a-2)*(a-2)
    k = isqrt(m)
    if k**2 == m:
        return (a*k) % 4 == 0
    else:
        return False

def main(n):
    total_sum = 0
    for a in xrange(2, n // 3 + 2, 2):
        if test(a, False):
            if a > 2:
                print a, False, 3*a-2
                total_sum += 3*a-2
        if test(a, True):
            print a, True, 3*a+2
            total_sum += 3*a+2
    return total_sum

print main(10**9)
