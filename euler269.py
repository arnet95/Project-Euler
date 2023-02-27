from itertools import *

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

S = powerset(range(-9,1))
counts = {t: 0 for t in S}

for n in range(1, 10000001):
    l = [int(w) for w in list(str(n))][::-1]
    p = lambda x: sum(l[i]*x**i for i in range(len(l)))
    solutions = []
    for r in range(-9, 1):
        if p(r) == 0:
            solutions.append(r)
    solutions = tuple(solutions)
    counts[tuple(solutions)] += 1

new_counts = {}

for t in counts:
    if counts[t] != 0:
        new_counts[t] = counts[t]

print(new_counts)
