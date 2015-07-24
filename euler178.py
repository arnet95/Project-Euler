#Project Euler 178: Step Numbers

mem = {}
def f(rem, curr, min_seen, max_seen):
    if (rem, curr, min_seen, max_seen) in mem:
        return mem[(rem, curr, min_seen, max_seen)]
    else:
        if rem == 0:
            tmp = 1*(min_seen == 0 and max_seen == 9)
        elif curr == 0:
            tmp = f(rem - 1, 1, 0, max_seen)
        elif curr == 9:
            tmp = f(rem - 1, 8, min(8, min_seen), 9)
        else:
            tmp = f(rem - 1, curr - 1, min(curr - 1, min_seen), max_seen)
            tmp += f(rem - 1, curr + 1, min_seen, max(curr + 1, max_seen))
        mem[(rem, curr, min_seen, max_seen)] = tmp
        return tmp

def g(n):
    """Returns the number of pandigital step numbers of length n"""
    return sum(f(n-1, i, i, i) for i in xrange(1, 10))

def h(n):
    """Returns the number of pandigital step numbers less than 10^n"""
    return sum(g(i) for i in xrange(1,n+1))

print h(40)
