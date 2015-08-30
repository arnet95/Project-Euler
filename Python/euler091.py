#Project Euler 91: Right triangles with integer coordinates

def f(n):
    counter = 0
    for x1 in xrange(n+1):
        for y1 in xrange(n+1):
            for x2 in xrange(n+1):
                for y2 in xrange(n+1):
                    if (x1 != 0 or y1 != 0) and (x2 != 0 or y2 != 0):
                        if (x1 != x2 or y1 != y2):
                            dot_prod = x1 * x2 + y1 * y2
                            if dot_prod == 0:
                                counter += 1
                            elif dot_prod == x1**2 + y1**2:
                                counter += 1
                            elif dot_prod == x2**2 + y2**2:
                                counter += 1
                            else:
                                pass
    return counter/2

print f(50)

#Since the three points of the triangles are (0, 0), (x1, y1) and (x2, y2), we
#have that the three vectors between the points are given by
#(x1, y1), (x2, y2) and (x2 - x1, y2 - y1). Since we have that two vectors are
#orthogonal (form a right triangle) if and only if the scalar product between
#the vectors are 0. This means that for a given triangle x1, x2, y1, y2,
#it has a right angle if and only if one of the following hold:
#  *  x1*x2 + y1*y2 == 0
#  *  x1*x2 - x1**2 + y1*y2 - y1**2 == 0 <==> x1*x2 + y1*y2 == x1**2 + y1**2
#  *  x2**2 - x2*x1 + y2**2 - y2*y1 == 0 <==> x1*x2 + y1*y2 == x2**2 + y2**2

#Since there are only 51**4 == 6765201 options, this is within a brute force
#approach, which is what we do. We note that we need to exclude a set if any of
#the points P or Q are the origin, and we also need to make sure that P != Q.
#Finally, we divide by 2, since we count each triangle twice as when we loop
#through all possible values of x1, x2, y1, y2, we will have one duplicate for
#each triangle.
