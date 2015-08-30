#Project Euler 265: Binary Circles
from itertools import product


def initial_gen(n):
    l = []
    for tup in product("01", repeat=(2**n - n - 2)):
        s = "".join(tup)
        if s.count("0") == 2**(n-1) - n:
            s = "0" * n + "1" + s + "1"
            if "1" * n in s:
                l.append(s)
    return l

def main(n):
    result = 0
    for s in initial_gen(n):
        main_flag = True
        l = [s[i-1:] + s[:i-1] for i in xrange(n)]
        for tup in product("01", repeat=n):
            seq = "".join(tup)
            bool = False
            for elem in l:
                if seq in elem:
                    bool = True
            if not bool:
                main_flag = False
                break
        if main_flag:
            result += int("0b" + s[n:], 2)
    return result

print main(5)
