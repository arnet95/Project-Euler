from math import sqrt, acos, pi

def norm(v):
    return sqrt(sum(vi**2 for vi in v))

def dotproduct(v, w):
    return sum(vi*wi for vi, wi in zip(v, w))

def vecminus(v, w):
    return tuple([vi-wi for vi, wi in zip(v, w)])

def area(p1, p2, p3, r):
    angle1 = acos(dotproduct(vecminus(p2-p1), vecminus(p3-p1))/ (norm(vecminus(p2-p1))*norm(vecminus(p3-p1))))
    angle2 = acos(dotproduct(vecminus(p1-p2), vecminus(p3-p2))/ (norm(vecminus(p1-p2))*norm(vecminus(p3-p2))))
    angle3 = acos(dotproduct(vecminus(p1-p3), vecminus(p2-p3))/ (norm(vecminus(p1-p3))*norm(vecminus(p2-p3))))
    return r**2*((angle1 + angle2 + angle3) - pi)

def Z(r):
    l = []
    for x in xrange(-r, r+1):
        for y in xrange(-r, r+1):
            if x**2 + y**2 <= r**2:
                for z in xrange(-r, r+1):
                    if x**2 + y**2 + z**2 == r**2:
                        l.append((x, y, z))
    return l

#def T(r):
#    l = Z(r)
#    length = len(l)
#    for i in xrange(length):
#        for j in xrange(i+1, length):
#            for k in xrange(j+1, length):


for i in xrange(1, 51):
    length = len(Z(i))
    print i, (length*(length-1)*(length-2))/6
