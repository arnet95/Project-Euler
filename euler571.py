from itertools import permutations

def digits(n, base):
    s = set([])
    while n > 0:
        s.add(n % base)
        n //= base
    return s

def pandigital(n, base):
    s = set([])
    while n > 0:
        s.add(n % base)
        n //= base
        if len(s) == base:
            return True
    return len(s) == base

def main(m):
    result, count = 0, 0
    for perm in permutations(range(m), m):
        if perm[0] != 0:
            perm = perm[::-1]
            n = sum(perm[i]*m**i for i in xrange(m))
            if all(pandigital(n, base) for base in range(2, m)):
                count += 1
                result += n
                if count == 10:
                    print "Done"
                    break
    return result

print main(12)
