#Project Euler 94: Almost equilateral triangles

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def main(limit_perimeter):
    s = 0
    for m in xrange(2, isqrt(limit_perimeter // 4) + 2):
        if m % 3 != 0:
            val = (m*m - 1)
            n = isqrt(val // 3)
            if val == 3*n*n:
                print (m*m - n*n, 2*m*n, m*m + n*n), 4*m*m
                s += 4*m*m
    return s

print main(10**9)
