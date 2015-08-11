#Project Euler 115: Counting block combinations II

mem = {}
def f(n, red, m):
    if (n, red, m) in mem:
        return mem[(n, red, m)]
    elif n < m:
        a = 1
    elif red:
        a = f(n-1, False, m)
    else:
        a = f(n-1, False, m) + sum(f(i, True, m) for i in xrange(n - m, -1, -1))
    mem[(n, red, m)] = a
    return a

#We let f(n, red, m) represent the number of tilings of length n using at least
#length m tiles as well as the length 1 black square, and let red represent
#whether the last tile used was red or not. For n < m, the only possibility is
#to tile the rest with black squares, so we return 1. In the other cases, if red
#is True, we only have a black square in this case, so we call f with those
#parametres. If red is False, we have the case when we have a black square, and
#we also have red tiles of lengths m through n, so we add up all the f's
#satisfying those conditions. Memoizing f gives us the answer in ~5 ms.

def F(m, n):
    return f(n, False, m)

def main(m):
    i = 0
    while F(m, i) <= 1000000:
        i += 1
    return i

print main(50)
