#euler108

def find_solutions(n):
    counter = 0
    for x in xrange(n+1,2*n):
        if (n*x)%(x-n) == 0:
            counter += 1
    return counter+1

def f():
    n = 1
    while True:
        if n%10000 == 0:
            print n
        if find_solutions(n) > 1000:
            return n
        n += 1

#print f()

def new_main(n):
    l = [1] * (n//3+1)
    min_next_log = [2*log(prime_list[i]) for i in xrange(len(l))]
