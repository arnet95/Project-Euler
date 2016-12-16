from eulertools import primes

def dynamic_divisors(n):
	divs = [[], [1]] + [[1, i] for i in xrange(2, n+1)]
	for i in xrange(2, int(n**0.5) + 1):
		divs[i*i].append(i)
		divs[i*i].sort()
		for d in xrange(i*(i+1), n+1, i):
			divs[d].append(i)
			divs[d].append(d//i)
			divs[d].sort()
	return divs

def old_main(n):
	counter = 0
	divs_list = dynamic_divisors(n-1)
	for i in xrange(1, n):
		divs = divs_list[i]
		count = sum((3*(i//a) > a) and ((a + (i // a)) % 4 == 0) for a in divs)
		if count == 1:
			counter += 1
	return counter

def main(n):
	s = sum(p % 4 == 3 for p in primes(n-1))
	divs_list = dynamic_divisors((n-1)//4)
	for i in xrange(1, len(divs_list)):
		divs = divs_list[i]
		actual_divs = list(set(divs + [2*d for d in divs] + [4*d for d in divs]))
		n = 4*i
		count = sum((3*(n//a) > a) and ((a + (n // a)) % 4 == 0) for a in actual_divs)
		if count == 1:
			s += 1
	return s

print main(5*10**7)
