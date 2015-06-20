#List comprehension:
print sum(i for i in xrange(1, 1000) if i%3 == 0 or i%5 == 0)

#Verbose way:
s = 0
for i in xrange(1, 1000):
    if i%3 == 0 or i%5 == 0:
        s += i
print s