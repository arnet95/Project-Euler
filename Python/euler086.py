def integer_sp(n1, n2, n3):
    """Assuming n1 <= n2 <= n3, testing whether the cube with those dimensions
    has shortest route of integer length"""
    #It is possible to show that given n1 <= n2 <= n3,
    #the shortest route will be (n1+n2)**2 + n3**2.
    sp_sq = n3**2 + (n1 + n2)**2
    #This works, since the values involved are small enough
    return sp_sq ** 0.5 % 1 == 0

def marginal_M(M):
    """We test all cubes with length of longest side = M"""
    count = 0
    for i in xrange(1, M+1):
        for j in xrange(i, M+1):
            count += integer_sp(i, j, M)
    return count

def main(limit):
    """We do a straightforward brute force search"""
    s, count = 0, 0
    while s <= limit:
        count += 1
        s += marginal_M(count)
    return count

print main(10**6)
