def isprime(n):
	if n == 2 or n == 3:
		return True
	if pow(2, n-1, n) == 1:
		if pow(3, n-1, n) == 1:
			for i in xrange(5, int(n ** 0.5) + 1, 6):
				if n % i == 0 or n % (i + 2) == 0:
					return False
			return True
	return False

def hamming(n):
	l = [1]
	i = 1
	while 2**i <= n:
		l.append(2**i)
		i += 1
	for m in [3, 5]:
		i = 1
		while m**i <= n:
			new_l = []
			k = m**i
			for j in l:
				if j*k > n:
					break
				new_l.append(j*k)
			l += new_l
			l = sorted(l)
			i += 1
	return sorted(list(set(l)))

def S(n):
	s = 0
	l = hamming(n)
	primes = [i+1 for i in l if isprime(i+1)][3:]
	for p in primes:
		new_l = []
		for i in l:
			if i*p > n:
				break
			new_l.append(i*p)
		new_l = list(set(new_l))
		l += new_l
		l = sorted(l)
		s += sum(i*(i > n//p) for i in l)
		l = [i for i in l if i <= n//p]
	return s + sum(l)

print S(10**12)
