#Project Euler 178: Step Numbers

mem = {}
def f(rem, curr, min_seen, max_seen):
    if (rem, curr, min_seen, max_seen) in mem:
        return mem[(rem, curr, min_seen, max_seen)]
    else:
        if rem == 0:
            tmp = (min_seen == 0 and max_seen == 9)
        elif curr == 0:
            tmp = f(rem - 1, 1, 0, max_seen)
        elif curr == 9:
            tmp = f(rem - 1, 8, min(8, min_seen), 9)
        else:
            tmp = f(rem - 1, curr - 1, min(curr - 1, min_seen), max_seen)
            tmp += f(rem - 1, curr + 1, min_seen, max(curr + 1, max_seen))
        mem[(rem, curr, min_seen, max_seen)] = tmp
        return tmp

#We let f(rem, curr, min_seen, max_seen) represent the number of pandigital step numbers
#of length rem with current digit curr, where the previously minimal number seen
#is min_seen, and the previously maximal number seen is max_seen.
#If rem is 0, we return whether min_seen is 0 and max_seen is 9, which means that
#the number is 0-9 pandigital. In the case when curr == 0, the only way to create
#a step number is for the next digit to be 1, so we call f with relevant parameters.
#The case curr == 9 is similar, but the next digit must be 8.
#In the other cases, we call f with rem - 1, curr +- 1, and min_seen and max_seen
#updated accordingly.

#Memoizing f will give us the answer in <20 ms.

def g(n):
    """Returns the number of pandigital step numbers of length n"""
    return sum(f(n-1, i, i, i) for i in xrange(1, 10))

def h(n):
    """Returns the number of pandigital step numbers less than 10^n"""
    return sum(g(i) for i in xrange(1, n+1))

print h(40)
