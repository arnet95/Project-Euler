#Project Euler 1: Multiples of 3 and 5
import time

#Most efficient way, based on the sum of arithmetic sequences:
def tri(n):
    return n*(n+1)//2
    
def sum_of_sequences(n):
    n = n - 1
    return 3*tri(n//3) + 5*tri(n//5) - 15*tri(n//15)

#Expression comprehension:
def comprehension(n):
    return sum(i for i in xrange(1, n) if i%3 == 0 or i%5 == 0)

#Verbose way:
def verbose(n):
    s = 0
    for i in xrange(1, n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s

print sum_of_sequences(1000)

#Timing
t1 = time.time()
for i in xrange(10000):
    sum_of_sequences(1000)
t2 = time.time()
for i in xrange(10000):
    comprehension(1000)
t3 = time.time()
for i in xrange(10000):
    verbose(1000)
t4 = time.time()

print
print "Time taken for 10000 loops:"
print "Using the sum of sequences", t2 - t1
print "Using comprehension", t3 - t2
print "Using verbose for-loops", t4 - t3

#As expected, the version using sum of sequences takes about 1/100 of the time
#of the other two versions, which are about as fast.
