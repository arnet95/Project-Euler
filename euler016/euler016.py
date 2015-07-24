#Project Euler 16: Power digit sum
import time

#Uses Python's dynamic typing to convert the number to a string and summing
#over the integer values of the characters.
def type_conversion(n):
    return sum(int(c) for c in str(n))

#Uses modular arithmetic to extract the last digit
#and integer division to get rid of it
def modular_arithmetic(n):
    s = 0
    while n >= 10:
        s += n % 10
        n = n / 10
    return s + n

print type_conversion(2**1000)


#Timing

t1 = time.time()
for i in xrange(10000):
    type_conversion(2**1000)
t2 = time.time()
for i in xrange(10000):
    modular_arithmetic(2**1000)
t3 = time.time()
print
print "Timing"
print "Using type conversion:", t2 - t1
print "Using modular arithmetic:", t3 - t2

#It turns out that the version using type conversion uses half as much time as
#the version using modular arithmetic, which is somewhat surprising.
#This probably happens because doing arithmetic on large numbers takes more time than
#doing type conversion on single digits.
