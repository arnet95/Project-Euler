#Prime Frog
from fractions import *
from eulertools import primes

prime_list = primes(500)
def is_prime(n):
    return n in prime_list

mem = {}

def f(pos, seq):
    if (pos, seq) in mem:
        return mem[(pos, seq)]
    if seq == "P":
        tmp = Fraction(1, 3) * (2 if is_prime(pos) else 1)
    elif seq == "N":
        tmp = Fraction(1, 3) * (1 if is_prime(pos) else 2)
    elif pos == 1:
        tmp = Fraction(1, 3) * f(2, seq[1:]) * (1 if seq[0] == "P" else 2)
    elif pos == 500:
        tmp = Fraction(1, 3) * f(499, seq[1:]) * (1 if seq[0] == "P" else 2)
    elif is_prime(pos):
        if seq[0] == "P":
            tmp = Fraction(2, 6) * (f(pos-1, seq[1:]) + f(pos+1, seq[1:]))
        else:
            tmp = Fraction(1, 6) * (f(pos-1, seq[1:]) + f(pos+1, seq[1:]))
    else:
        if seq[0] == "N":
            tmp = Fraction(2, 6) * (f(pos-1, seq[1:]) + f(pos+1, seq[1:]))
        else:
            tmp = Fraction(1, 6) * (f(pos-1, seq[1:]) + f(pos+1, seq[1:]))
    mem[(pos, seq)] = tmp
    return tmp


def main(seq):
    return sum(f(i, seq) for i in xrange(1, 501)) * Fraction(1, 500)

print main("PPPPNNPPPNPPNPN")
