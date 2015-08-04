from math import sqrt

def is_square(n):
    return sqrt(n) % 1 == 0
    #if :
#        return abs(sqrt(n)*sqrt(n) - n) < 1E-5#
#    return False

def main(n):
    s = 16
    for k in xrange(4, n+1, 2):
        if k%4 == 2:
            if is_square(k-1):
                if is_square(3*k-1):
                    print k
                    s += (k*2) + 2*(k*2-1)
        else:
            if is_square(k+1):
                if is_square(3*k+1):
                    print k
                    s += (k*2) + 2*(k*2+1)
    return s

print main(100000000)
