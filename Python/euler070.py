#Project Euler 70: Totient permutation
from __future__ import division
from eulertools import totient_gen

def is_permutation(m, n):
    """Checks if numbers are permutations of each other"""
    return sorted(str(m)) == sorted(str(n))

def main(n):
    min_n = 0
    min_ratio = 1000
    totients = totient_gen(n-1)
    #Creates list of totients
    for i in xrange(2, len(totients)):
        if i/totients[i] < min_ratio:
            #If it's a new minimum
            if is_permutation(i, totients[i]):
                #Check if it's a permutation of it's totient
                #and behave accordingly
                min_n = i
                min_ratio = i/totients[i]
    return min_n

print main(10**7)
