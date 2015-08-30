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


num_sets = [(a, b, c, d) for a in range(1, 10) for b in range(a+1, 10) for c in range(b+1, 10) for d in range(c+1, 10)]
max_set = max(num_sets, key=lambda s: f(*s))
print "".join(map(str, max_set))
