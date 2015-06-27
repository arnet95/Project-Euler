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
