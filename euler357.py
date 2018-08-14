from eulertools import primes

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

def dynamic_modified_divisors(n):
	divs = [[], [1]] + [[1 + i] for i in xrange(2, n+1)]
	for i in xrange(2, int(n**0.5) + 1):
		divs[i*i].append(2*i)
		for d in xrange(i*(i+1), n+1, i):
			divs[d].append(i + d // i)
	return divs

def main(n):
    prime_list = primes(n+2)
    #divisors = dynamic_modified_divisors(n)
    result = 1 #1 is a special case, 2 does not divide 1, but all other numbers
    cand1 = [p-1 for p in prime_list]
    cand2 = [2*(p-2) for p in prime_list]
    cands = list(set(cand1).intersection(set(cand2)))

    #Removing non-squarefree numbers
    for p in primes(int(n**0.5)+1):
        cands = [cand for cand in cands if cand % (p**2) != 0]

    for cand in cands:
        flag = True
        for i in xrange(3, int(cand**0.5)+1):
            if cand % i == 0:
                if not isprime(i + cand // i):
                    flag = False
                    break
        if flag:
            result += cand

    return result

print main(10**8)
