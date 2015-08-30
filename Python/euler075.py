#Project Euler 75: Singular integer right triangles

from fractions import gcd

def main(limit):
    lengths = [0] * (limit + 1)
    for m in xrange(2, 1000):
        for n in xrange((m%2)+1, m, 2):
            if gcd(m,n) == 1:
                prim_length = 2*m*(m+n)
                for i in xrange(prim_length, limit+1, prim_length):
                    lengths[i] += 1
    return lengths.count(1)

print main(1500000)

#We use the fact that a = k(m^2 - n^2), b = k(2mn), c = k(m^2 + n^2) for positive
#integers m, n, and k with m > n, m - n odd, and with m and n coprime, will
#uniquely generate all Pythagorean triples (a, b, c). Note that the perimeter of
#such a triple is k*2*m*(m+n). We generate all triples, and store the number of
#triangles with a given perimeter in a list.
#Then, the number of singular right triangles is the number of 1's in this list.
