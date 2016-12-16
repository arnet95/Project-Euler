#Problem 153: Investigating Gaussian Integers
from fractions import gcd

def main(n):
    #sum of rational integer divisors:
	result = sum(i*(n//i) for i in xrange(1, n+1))
	#Gaussian integers:
	for x in xrange(1, int(n**0.5)+1):
		for y in xrange(1, int(n**0.5)+1):
			#We try each pair of divisors x + iy, x - iy. The sum of these
			#will be 2x. Then we check how many times this pair
			#appears + how often multiples appear using a clever summation.
			#This is why we only do this for gcd(x, y) = 1.
			if gcd(x, y) == 1:
				a = x**2+y**2
				result += 2*x*sum((n//(a*j))*j for j in xrange(1, (n//a) + 1))
	return result

print main(10**8)
