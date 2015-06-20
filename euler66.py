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
print remainders(109)
