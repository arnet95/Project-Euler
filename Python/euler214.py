from eulertools import primes, totient_gen

#The idea is to generate the lengths of all chains from the bottom up.
#The length of a chain starting with i is 1 + the length of the chain starting
#with phi(i).

#We compute all totients in the given range, and fill up a map of chain
#lengths, and traverse that one to get the final answer.

#The program takes about 13 seconds and uses about 3.5GB of memory on my machine.

def main(n, l):
    totients = totient_gen(n)
    d = {1: 1}
    for i in xrange(2, n+1):
        d[i] = 1 + d[totients[i]]
    return sum(p for p in primes(n) if d[p] == l)

print main(4*10**7, 25)
