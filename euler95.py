from math import sqrt

def sum_of_divisors(n):
    s = 1
    sq = int(sqrt(n))
    for d in xrange(2, sq):
        if n % d == 0:
            s += (d + n/d)
    if n % sq == 0:
        s += sq
    return s

def chain_length(n):
    visited = []
    def chain_sub(k, length):
        if k == n:
            return length + 1
        elif k == 'NO':
            return 0
        elif k in visited:
            return 0
        else:
            visited.append(k)
            if k in numbers:
                return chain_sub(numbers[k], length + 1)
            else:
                return 0
    return chain_sub(numbers[n], 0)

N = 1000000
numbers = {}
chains = {}
s = 0
for i in xrange(1, N):
    a = sum_of_divisors(i)
    if a > N: 
        a = "NO"
    elif a == 1:
        a = "NO"
    numbers[i] = a
for i in xrange(1, N):
    chains[i] = chain_length(i)

max_val = max(chains.values())
for i in xrange(1, N):
    if chains[i] == max_val:
        print i
        break