#euler146

def gen_list_2(n):
    #We generate all the possible such n's. We have found some limitations on
    #what n must be modulo small primes.
    #One possible way to improve this algorithm ight be to automate
    #this process of excluding remainders.
    l = []
    for i in xrange(10,n,10):
        if i%3 != 0:
            if i%7 not in [0,1,2,5,6]:
                if i%11 not in [2,3,8,9]:
                    if i%13 not in [0,2,5,6,7,8,11]:
                        if i%17 not in [2,4,5,12,14,15]:
                            if i%19 not in [4,5,7,12,14,15]:
                                if i%23 not in [4,19]:
                                    if i%29 not in [4,7,12,14,15,17,22,25]:
                                        l.append(i)
    return l

def isprime(n):
    #We use the Fermat prime test, which is not guaranteed to work, but does in
    #this case!
    if pow(2,n-1,n) == 1:
        return True
    return False

def main(n):
    #We do a very straightforward test of all the possibilities.
    s = 0
    for k in gen_list_2(n):
        x = k**2
        if isprime(x+1):
            if isprime(x+3):
                if isprime(x+7):
                    if isprime(x+9):
                        if isprime(x+13):
                            if not isprime(x+19):
                                if not isprime(x+21):
                                    if isprime(x+27):
                                        s += k
    return s

print main(150000000)
