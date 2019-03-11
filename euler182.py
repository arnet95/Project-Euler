from fractions import gcd

def number_unconcealed(p, q, e):
    return (1 + gcd(e-1, p-1))*(1+gcd(e-1, q-1))

def main(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    d = {}
    for e in xrange(2, phi):
        if gcd(e, phi) == 1:
            d[e] = number_unconcealed(p, q, e)
    minimum = min(d.values())
    return sum(e for e in d if d[e] == minimum)

print main(1009, 3643)
