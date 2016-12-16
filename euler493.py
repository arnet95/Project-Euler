from fractions import *
from itertools import product

mem = {}


def p(k, colors):
    if (k, colors) in mem:
        return mem[(k, colors)]
    if sum(colors) == 50:
        return Fraction(k == sum(color != 10 for color in colors))
    else:
        num_zeros = sum(color == 0 for color in colors)
        result = 0
        for i in xrange(7):
            if colors[i] != 0:
                result += Fraction(colors[i], sum(colors))*p(k, colors[:i] + (colors[i]-1, ) + colors[i+1:])
        mem[(k, colors)] = result
        return result

def main():
    return sum(i*p(i, (10,)*7) for i in xrange(1, 8))

print round(float(main()), 9)
