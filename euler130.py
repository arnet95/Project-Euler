from eulertools import primes

def A(n):
    rem, counter, old = 1, 1, 1
    while rem:
        old *= 10
        old %= n
        rem += old
        rem %= n
        counter += 1
    return counter

def composites(n):
    prime_list = primes(n)
    l = [i for i in xrange(2, n+1) if i not in prime_list]
    return l

comp_list = composites(15000)
s, counter = 0, 0
for n in comp_list:
    if counter >= 25:
        break
    if n % 5 != 0 and n % 2 != 0:
        if (n-1) % A(n) == 0:
            counter += 1
            s += n
print s
