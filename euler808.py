from eulertools import primes


def find_reversible(l):
    results = []
    s = set(l)
    for c in l:
        rev_c = c[::-1]
        if c != rev_c and rev_c in s:
            results.append(c)
    return results
    

curr_prime_squares = []
curr_len = 1
results = []
for p in primes(10**8):
    s = str(p**2)
    if len(s) > curr_len:
        results += find_reversible(curr_prime_squares)
        if len(results) >= 50:
            break
        curr_prime_squares = [s]
        curr_len = len(s)
    else:
        curr_prime_squares.append(s)


print(sum(int(c) for c in results))