#euler101 - Optimum polynomials
from sympy import *

u = lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def fit(u, n, vals):
    matrix = [[(b+1)**p for p in xrange(n-1, -1, -1)] + [vals[b]] for b in xrange(n)]
    row_reduced = Matrix(matrix).rref()
    coefficients = [row_reduced[0].row(i).col(-1)[0] for i in xrange(n)]
    return sum([c*(n+1)**i for c, i in zip(coefficients, xrange(n-1, -1, -1))])

def main(u, n):
    vals = [u(i) for i in xrange(1, n)]
    return sum(fit(u, i, vals) for i in xrange(1, n))

print main(u, 11)
