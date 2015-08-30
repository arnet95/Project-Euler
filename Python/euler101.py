#Project Euler 101: Optimum polynomials
from sympy import *

def fit(u, k, vals):
    matrix = [[(b+1)**p for p in xrange(k-1, -1, -1)] + [vals[b]] for b in xrange(k)]
    row_reduced = Matrix(matrix).rref()
    coefficients = [row_reduced[0].row(i).col(-1)[0] for i in xrange(k)]
    return sum([c*(k+1)**i for c, i in zip(coefficients, xrange(k-1, -1, -1))])

def main(u, n):
    vals = [u(i) for i in xrange(1, n)]
    return sum(fit(u, i, vals) for i in xrange(1, n))

u = lambda n: sum((-n)**i for i in xrange(11))
print main(u, 11)

#The important thing to notice for this problem is that we can rephrase it
#as solving a system of linear equations. As an example, if we have two
#elements {a1, a2} in the sequence, we have:
#   c1 * 1 + c2 = a1
#   c1 * 2 + c2 = a2

#We can do similar things for all finite sets of sequences, and we can then use
#a matrix library to do the necessary row reduction. Then, once we've found the
#coefficients for our polynomial, we insert k+1 into it, it being the FIT for
#a sequence of length k. Then, we sum over these FITs, giving us the right answer.
