from math import sqrt

def is_square(n):
    if sqrt(n) % 1 == 0:
        if n > 0:
            return sqrt(n) * sqrt(n) == n
    return False

def remainders(d):
    ret = [1]
    for i in xrange(2, d):
        if pow(i,2,d) == 1:
            ret.append(i)
    return ret

def main(n):
    max_res, max_d = 0, 0
    for d in [i for i in xrange(1, n+1) if sqrt(i) % 1 != 0]:
        n = 0
        rems = remainders(d)
        a = True
        while a:
            for rem in rems:
                x = n*d + rem
                if is_square((x**2-1)/d):
                    if x > max_res:
                        max_res = x
                        max_d = d
                    a = False
                    break
            n += 1
        print d
    return max_d


def f(D):
    a = int(sqrt(D))
    b = 1
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
