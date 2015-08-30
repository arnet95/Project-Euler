#Project Euler 62: Cubic permutations
from __future__ import division

def final(goal):
    """Returns a list of all cubes which are permutations of goal"""
    cube_length = len(goal)
    lower = int(10 ** ((cube_length-1)/3))
    upper = int(10 ** (cube_length/3))
    return [x**3 for x in xrange(lower, upper + 1) if ''.join(sorted(str(x**3))) == goal]

def f(target):
    n = 1
    satisfying_cubes = []
    while satisfying_cubes == []:
        lower = int(10 ** ((n-1)/3))
        upper = int(10 ** (n/3))
        d = {}
        for x in xrange(lower, upper+1):
            s = ''.join(sorted(str(x**3)))
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        for key in d:
            if d[key] == target:
                satisfying_cubes += final(key)
        n += 1
    return min(satisfying_cubes)

print f(5)

#Here we exploit that, for two numbers to be anagrams, they must have the same
#number of digits. We simply generate all cubes of length n, and store them in
#a dictionary as a sorted string with the number of cubes with those digits.
#Finally, if there are any numbers satisfying the given condition, we return
#the minimum of all those numbers.
