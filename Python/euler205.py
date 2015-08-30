from __future__ import division

colincounts = {i:0 for i in xrange(6, 37)}
for a in xrange(1, 7):
    for b in xrange(1, 7):
        for c in xrange(1, 7):
            for d in xrange(1, 7):
                for e in xrange(1, 7):
                    for f in xrange(1, 7):
                        colincounts[a+b+c+d+e+f]+=1
colinprobs = {i:colincounts[i]/(6**6) for i in xrange(6, 37)}

petercounts = {i:0 for i in xrange(9, 37)}
for a in xrange(1, 5):
    for b in xrange(1, 5):
        for c in xrange(1, 5):
            for d in xrange(1, 5):
                for e in xrange(1, 5):
                    for f in xrange(1, 5):
                        for g in xrange(1, 5):
                            for h in xrange(1, 5):
                                for i in xrange(1, 5):
                                    petercounts[a+b+c+d+e+f+g+h+i]+=1
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
