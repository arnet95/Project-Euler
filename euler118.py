from eulertools import primes
from itertools import product

def tuple_comp(i1, i2):
    a = sum(i1)
    b = sum(i2)
    if a > b:
        return True
    else:
        return a == b and i1 >= i2

prime_list = [p for p in primes(10**8) if '0' not in str(p) and len(str(p)) == len(set(str(p)))]

dictionary = {i: 0 for i in product([0, 1], repeat=9)}

for p in prime_list:
    digits = tuple([str(i) in str(p) for i in xrange(1, 10)])
    dictionary[digits] += 1

f_mem = {}

def f(i, largest_used):
    if i == (0, 0, 0, 0, 0, 0, 0, 0, 0):
        return 1
    elif (i, largest_used) in f_mem:
        return f_mem[(i, largest_used)]
    elif not tuple_comp(i, largest_used):
        return 0
    else:
        result = 0
        for j in product([0, 1], repeat=9):
            if j != (0, 0, 0, 0, 0, 0, 0, 0, 0):
                if tuple_comp(i, j):
                    new_tuple = tuple([a-b for a, b in zip(i, j)])
                    if min(new_tuple) >= 0:
                        result += dictionary[j]*f(new_tuple, j)
        f_mem[(i, largest_used)] = result
        return result


print f((0, 1, 1, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0))
#print f((1, 1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0))

print f_mem
