from fractions import *

#The three values represent, respectively,
# m - The score of Player 1
# n - The score of Player 2
# k - Whose turn it is

memoize = {}

def P(m, n, k):
    if (m, n, k) in memoize:
        return memoize[(m, n, k)]
    if m >= 100:
        return Fraction(0)
    if n >= 100:
        return Fraction(1)

def find_solution(m, n):
    solution_list = []
    T = 1
    while n + 2**(T-1) < 100:
        x = (Fraction(1, 2**T)*P(m, n+2**(T-1), 1) + P(m+1, n, 2))/(2-Fraction(2**T-1, 2**T))
        y = 2*x - P(m+1, n, 2)
        solution_list.append((x, y))
        T += 1
    x = (Fraction(1, 2**T)*P(m, n+2**(T-1), 1) + P(m+1, n, 2))/(2-Fraction(2**T-1, 2**T))
    y = 2*x - P(m+1, n, 2)
    solution_list.append((x, y))
    return max(solution_list, key=lambda x: x[1])

for m in xrange(99, -1, -1):
    for n in xrange(99, -1, -1):
        x, y = find_solution(m, n)
        memoize[(m, n, 1)] = x
        memoize[(m, n, 2)] = y

print round(float(memoize[(0, 0, 1)]), 8)
