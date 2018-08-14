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

def divisors_from_primes(prime_factorisation):
    """Format: [(p1, r1), ..., (pk, rk)]"""
    l = [1]
    for prime_factor in prime_factorisation:
        tmp = [prime_factor[0]**k for k in xrange(1, prime_factor[1]+1)]
        l += [i*p for i in l for p in tmp]
    return sorted(l)

def is_power(n, r):
    """Checks if n = r^m for m > 0, and returns m if it does"""
    m = 0
    while n % r == 0:
        n //= r
        m += 1
    if n == 1 and m != 0:
        return m
    else:
        return None

def correct_form(d, p):
    """Checks if d = p^k(p-1) for k > 0, and returns k if it does"""
    if d % (p-1) == 0:
        return is_power(d//(p-1), p)
    return None


def compute_number(path):
    result = 1
    for prime_factor in path:
        result *= (prime_factor[0]**prime_factor[1])*(prime_factor[0]-1)
    return result

def construct_e1(prime_factorisation):
    divisors = divisors_from_primes(prime_factorisation)
    n = divisors[-1]
    primes = [factor[0] for factor in prime_factorisation]
    current_paths = []
    divisors_with_pairs = {}
    for d in divisors:
        if isprime(d+1):
            current_paths.append((d+1, d, d+1))
            if d not in divisors_with_pairs:
                divisors_with_pairs[d] = [(d+1, 0)]
            else:
                divisors_with_pairs[d].append((d+1, 0))
        for p in primes:
            k = correct_form(d, p)
            if k is not None:
                current_paths.append((p, d, p**(k+1)))
                if d not in divisors_with_pairs:
                    divisors_with_pairs[d] = [(p, k)]
                else:
                    divisors_with_pairs[d].append((p, k))
    completed_paths = []
    while current_paths != []:
      print len(current_paths)
      new_paths = []
      for path in current_paths:
        done = False
        new_divisors = [d/path[1] for d in divisors if d % path[1] == 0]
        for d in new_divisors:
          if d in divisors_with_pairs:
            l = divisors_with_pairs[d]
            for i in l:
              if i[0] > path[0]:
                done = True
                new_paths.append((i[0], path[1]*d, path[2]*(i[0]**(i[1]+1))))
        if not done and path[1] == n:
          completed_paths.append(path)
      current_paths = new_paths
    return sorted([path[2] for path in completed_paths])

l = construct_e1([(2, 10), (3, 5), (5, 2), (7, 1), (11, 1), (13, 1)])
print l[149999]
