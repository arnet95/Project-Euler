#Project Euler 93: Arithmetic expressions
from itertools import permutations, combinations_with_replacement
from new_fractions import *

def polish_interpret(s):
    stack = []
    for c in s:
        if c.isdigit():
            stack.append(Fraction(c))
        else:
            try:
                o1 = stack.pop()
                o2 = stack.pop()
                if c == "/":
                    try:
                        stack.append(o1/o2)
                    except ZeroDivisionError:
                        return None
                elif c == "*":
                    stack.append(o1*o2)
                elif c == "+":
                    stack.append(o1+o2)
                else:
                    stack.append(o1-o2)
            except IndexError:
                return None
    return stack.pop()

def f(a, b, c, d):
    s = []
    for p in combinations_with_replacement("+/*-", 3):
        for permut in permutations(str(a) + str(b) + str(c) + str(d) + "".join(p)):
            res = polish_interpret(permut)
            if res is not None:
                if res.is_int():
                    s.append(int(res))
    s = list(set(s))
    i = 1
    while i in s:
        i += 1
    return i - 1

min_set = [0] * 4
min_i = 0

for a in xrange(1, 10):
    for b in xrange(a+1, 10):
        for c in xrange(b+1, 10):
            for d in xrange(c+1,10):
                print a, b, c, d
                s = f(a, b, c, d)
                if s > min_i:
                    min_set = [a, b, c, d]
                    min_i = s

print "".join(map(str, min_set))
