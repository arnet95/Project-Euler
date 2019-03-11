def N(r):
    counta = 0
    countb = 0
    for x in xrange(-r, r+1):
        for y in xrange(-r, r+1):
            if abs(x) + abs(y) <= r:
                if x != y:
                    if y < -x:
                        counta += 1
                    if y > (r//2) - x:
                        countb += 1
    return counta, countb

print N(4)
