from eulertools import primes

#D(2n) = 20010 iff {p | p-1 divides 2n} = {2, 3, 5, 23, 29}



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

def main(n):
    divisors = [i for i in xrange(1, 309) if 308 % i == 0]
    result = 308
    count = 1
    for p in primes(10**7):
        divs_to_check = [i*p for i in divisors]
        if not any(isprime(div+1) for div in divs_to_check):
            count += 1
            result = 308*p
            if count == n:
                return result

print main(10**5+1)


for n in xrange(308, 10**7, 308):
    divs = [i for i in xrange(1, n+1) if n % i == 0]
    prime_list = [div+1 for div in divs if isprime(div+1)]
    if prime_list == [2, 3, 5, 23, 29]:
        if not isprime(n // 308):
            print n // 308
