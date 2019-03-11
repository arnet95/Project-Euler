from __future__ import division
from itertools import product

colincounts = {i:0 for i in xrange(6, 37)}
for tup in product(range(1, 7), repeat=6):
    colincounts[sum(tup)] += 1
colinprobs = {i:colincounts[i]/(6**6) for i in xrange(6, 37)}

petercounts = {i:0 for i in xrange(9, 37)}
for tup in product(range(1, 5), repeat=9):
    petercounts[sum(tup)]+=1
peterprobs = {i:petercounts[i]/(4**9) for i in xrange(9, 37)}

def colin_cumulative(n):
    return sum(colinprobs[i] for i in xrange(6, n))

print sum(peterprobs[n]*colin_cumulative(n) for n in xrange(9, 37))

#This is a fairly basic brute-force approach to solving this problem. Firstly, we simply
#enumerate all the different possible sums in order to calculate the probabilities.
#Since there are only 6**6 + 4**9 = 308800, this is easily within a brute-force
#approach.

#Then, we use this to calculate the probabilities of Colin achieving a score
#(strictly) less than n. And finally, we sum over the probabilities that Peter gets
#a score of n, and Colin getting a score less than n.
