#Euler 51
from eulertools import primes

prime_list = primes(10**6)

def number_count(n, a):
    l = [0 for i in xrange(10)]
    n = n/10
    while n > 10:
        i = n % 10
        l[i] += 1
        n = n/10
    for i in l:
        if i >= a:
            return True
    return False

l = []
for p in prime_list:
    if p > 100000:
        if number_count(p, 3):
            l.append(p)

dictionary = {}
for i in xrange(1,10):
    for j in [1, 3, 7, 9]:
        dictionary[(i, j)] = []

for i in l:
    dictionary[(i/100000, i%10)].append(i)


#for item in dictionary[(8, 7)]:

print dictionary[(7, 9)]



