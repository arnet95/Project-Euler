#Project Euler 3: Largest prime factor
import time

def factorise(n):
    """Returns a list of the prime factors of n"""
    l = []
    i = 2
    while i <= n:
        if n % i == 0:
            #When we find a divisor, we add it to the list, and divide down n.
            #We don't increase i yet, in case n is not square free.
            l.append(i)
            n //= i
        else:
            #If i is not a divisor, we increase i.
            i += 1
    return l

def main(n):
    return max(factorise(n))

print "Result:", main(600851475143)

t0 = time.time()
for i in xrange(1000):
    main(600851475143)
print "Timing"
print "1000 runs:", time.time() - t0

#This is a fairly slow method in general.
#There are some speedups possible, like only checking the odd numbers after 2.
#However, this is fairly concise and fast enough for this particular problem.
