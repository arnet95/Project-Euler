from fractions import *

S_mem = {0: 290797}
def S(n):
    if n in S_mem:
        return S_mem[n]
    else:
        result = pow(S(n-1), 2, 50515093)
        S_mem[n] = result
        return result

def T(n):
    return (S(n) % 2000) - 1000

def SL(n):
    points = []
    for k in xrange(1, n+1):
        points.append((T(2*k-1), T(2*k)))
    print "Done"
    lines = {}
    for i in xrange(len(points)):
        print i
        for j in xrange(i+1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2:
                if "Inf" in lines:
                    lines["Inf"].add(x1)
                else:
                    lines["Inf"] = set([x1])
            else:
                slope = Fraction(y2-y1, x2-x1)
                intercept = y1 - x1*slope
                if slope in lines:
                    lines[slope].add(intercept)
                else:
                    lines[slope] = set([intercept])
    same_slope_list = [len(lines[m]) for m in lines]
    M = sum(same_slope_list)
    print M
    return sum((M - val)*val for val in same_slope_list)

print SL(2500)
