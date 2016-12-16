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
    l = [1]*(n+1)
    for m in xrange(3, n):
        for div in set([i*j for i in divs[m-1] for j in divs[m+1] if m < i*j-1 < n]):
            l[div] = m
    return l[3:]

print sum(main(2*10**7))
