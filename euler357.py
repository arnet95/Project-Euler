#Euler 357
from math import sqrt
from eulertools import primes, squarefree_gen

#def test(i):

def main(n):
    prime_list = primes(n)
    candidates1 = [p-1 for p in prime_list]
    candidates2 = [2*(p-2) for p in prime_list]
    #candidates3 = squarefree_gen(n)
    for i in xrange(len(candidates2)):
        if candidates2[i] > n:
            candidates2 = candidates2[:i]
            break
    candidates = (set(candidates1).intersection(candidates2))#.intersection(candidates3)
    print len(candidates)
    #for num in candidates:


#print main(10**8)
#<print len(squarefree_gen(10**8))

def main(n):
    l = [[1] for i in xrange(n+1)]
    for num in xrange(2, int(n**0.5)+1):
        for num_mult in xrange(num, n+1, num):
            l[num_mult] += [].append(num)
    return l

print main(100)[30]
