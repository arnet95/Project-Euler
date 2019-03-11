

mod = 109
modinv = 11

mod = 10**7+19
modinv = (mod + 1)//10

two_digit_palindromes = set([11*i for i in xrange(10)])

mem = {}
def f(rem, l):
    if (rem, l) in mem:
        return mem[(rem, l)]
    if l == 1:
        result = (0 <= rem < 10)
    elif l == 2:
        result = rem in two_digit_palindromes
    else:
        result = 0
        n = 10**(l-1) + 1
        for c in xrange(10):
            result += f((rem-(c*n))*modinv % mod, l-2)
    mem[(rem, l)] = result
    #print rem, l, result
    return result


def main(L):
    result = 0
    for l in xrange(len(str(mod)), L+1):
        print l
        n = 10**(l-1) + 1
        for c in xrange(1, 10):
            result += f((-c*n)*modinv % mod, l-2)
    return result

print main(18)
print len(mem)

def test(L):
    count = 0
    for i in xrange(mod, 10**L, mod):
        if str(i) == str(i)[::-1]:
            print i
            count += 1
    return count
    
#print test(17)
