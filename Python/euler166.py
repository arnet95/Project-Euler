#Problem 166
from itertools import product

#Given the condition that all rows, columns and diagonals should have the same
#sum, one can first name all the entries in the grid, and then set up some linear
#equations between the different entries.
#Then one can solve these using linear algebra, and get some equations that
#are equivalent with the original ones, now with a smaller number of variables.
#I solved it using Octave.
#Then, it's simply a matter of generating all the relevant variables,
#and checking whether the relevant conditions are satisfied, and counting up.

counter = 0
for h, j, k in product(range(10), range(10), range(10)):
    if 0 <= j + k - h <= 9:
        for l, m in product(range(10), range(10)):
            if 0 <= h + l - m <= 9:
                for n in xrange(10):
                    if 0 <= j + m + m + n - h - k - l <= 9:
                        for o in xrange(10):
                            if 0 <= m + n + o - h - l <= 9:
                                if 0 <= m + m + n + o - h - k - l <= 9:
                                    for p in xrange(10):
                                        if 0 <= h - j + l - m + p <= 9:
                                            if 0 <= h - j + k + l - m - n + p <= 9:
                                                if 0 <= m + n + o + p - j - k - l <= 9:
                                                    counter += 1

print counter
