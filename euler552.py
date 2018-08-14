from eulertools import crt, primes

def main(n):
    prime_list = primes(n)
    A = [1]
    prod = 2
    res = 1
    for i in xrange(1, len(prime_list)):
        new_prime = prime_list[i]
        print new_prime
        res = crt(res, i+1, prod, new_prime)
        A.append(res)
        prod *= new_prime
    result = 0
    for i in xrange(1, len(prime_list)):
        curr_prime = prime_list[i]
        print curr_prime
        for j in xrange(1, i):
            if A[j] % curr_prime == 0:
                result += curr_prime
                A[j] //= curr_prime
                break
    return result


print main(3*10**5)
