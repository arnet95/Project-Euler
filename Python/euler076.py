#Project Euler 76: Counting summations

mem = {}
def f(n, max_allowed):
    if (n, max_allowed) in mem:
        return mem[(n, max_allowed)]
    if max_allowed == 1:
        tmp = 1
    elif n == max_allowed:
        tmp = 1 + f(n, max_allowed - 1)
    else:
        tmp = sum(f(n-i, min(i, n-i)) for i in xrange(1, max_allowed+1))
    mem[(n, max_allowed)] = tmp
    return tmp

def main(n):
    return f(n, n-1)

print main(100)

#We let f(n, max_allowed) represent the number of ways to write n as a sum of
#one or more positive integers with none of these exceeding max_allowed. Then,
#if we must use at least two positive integers, we simply call f(n, n-1), since
#then it's not possible to just use one number in the sum.

#We can describe f(n, max_allowed) recursively. If max_allowed == 1, the only
#possibility is to use only 1's in the rest of the sum, so then we return 1.
#If n == max_allowed, we have the sum of only max_allowed, and others with
#max_allowed not included in the sum, so we return 1 + f(n, max_allowed - 1).
#In all the other cases, we use all numbers from 1 up to max_allowed as the first
#number in our remaining sum, and we force this to be the biggest number in the
#remainder of the sum, so we update n and max_allowed accordingly. We return
#the sum of all these possibilities in this case. Memoizing this function finds
#the answer in about 30ms.
