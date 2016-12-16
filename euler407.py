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

def main(n):
	divs = dynamic_divisors(n)
	M = [0] + [1]*n
	for a in xrange(2, n+1):
		for i in [i*j for i in divs[a] for j in divs[a-1] if a < i*j <= n]:
			M[i] = a
	return sum(M) - 1

print main(10**7)
