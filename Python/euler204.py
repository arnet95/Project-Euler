#Project Euler 204: Generalised Hamming Numbers
from math import log

def main(limit):
    prime_list = [2, 3, 5]
    l = [1]
    for prime in prime_list:
        new_l = list(l)
        for elem in l:
            if prime > limit // elem:
                break
            for i in xrange(1, int(log(limit//elem, prime))+1):
                new_l.append(elem*prime**i)
        new_l.sort()
        l = new_l
    return len(new_l)

print main(10**9)

#The numbers will be of the form 2^k*3^l*5^m, so we generate all those numbers.
#First, generate all 2^k. Then, for each 2^j, generate all 2^j*3^l and for each
#2^j*3^i generate all 2^j*3^i*5^m.
