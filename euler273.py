from itertools import product
from eulertools import primes

def compl_mult(t1, t2):
    return (t1[0]*t2[0] - t1[1]*t2[1], t1[0]*t2[1] + t1[1]*t2[0])

def S(div_pairs):
    result = 0
    length = len(div_pairs)
    for picker in product([0,1], repeat=length):
        curr_prod = (1, 0)
        for i in xrange(length):
            if picker[i] == 0:
                curr_prod = compl_mult(curr_prod, div_pairs[i])
            else:
                curr_prod = compl_mult(curr_prod, (div_pairs[i][0], -div_pairs[i][1]))
        for multiplier in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            a, b = compl_mult(curr_prod, multiplier)
            if 0 <= a and a <= b:
                result += a
    return result

def main(n):
    current_primes = [p for p in primes(n) if p % 4 == 1]
    prime_divisors = []
    for p in current_primes:
        signal = False
        for i in xrange(1, n):
            if signal:
                break
            for j in xrange(1, i):
                if p == i**2 + j**2:
                    prime_divisors.append((i, j))
                    signal = True
                    break
    num_primes = len(current_primes)
    final_result = 0
    for picker in product([0, 1], repeat=num_primes):
        div_list = []
        for i in xrange(num_primes):
            if picker[i]:
                div_list.append(prime_divisors[i])
        final_result += S(div_list)
    return final_result

print main(150)
