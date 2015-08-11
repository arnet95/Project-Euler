from math import sqrt

def f(D):
    a, b = int(sqrt(D)), 1
    k = a**2 - D
    while k != 1:
        m = 0
        while ((b*m + a) % k) != 0:
            m += 1
        old_dist = abs(m**2 - D)
        while True:
            m += abs(k)
            new_dist = abs(m**2 - D)
            if new_dist > old_dist:
                m -= abs(k)
                break
            old_dist = new_dist
        a, b, k = (a*m + D*b) / abs(k), (a + b*m) / abs(k), (m**2 - D) / k
    return a

def main(n):
    max_index, max_val = 0, 0
    for D in xrange(2, n+1):
        if sqrt(D) % 1 != 0:
            if f(D) > max_val:
                max_index, max_val = D, f(D)
    return max_index


print main(1000), f(main(1000))
