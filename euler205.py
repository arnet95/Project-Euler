from __future__ import division
import time

start_time = time.time()

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
    s = 0
    for i in xrange(n):
        if i < 6:
            s += 0
        else:
            s += colinprobs[i]
    return s

total = 0
for n in xrange(9, 37):
    total += (peterprobs[n]*colin_cumulative(n))

print "Result:", total
print "Time taken:", time.time()-start_time
