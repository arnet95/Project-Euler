#This is designed for the special case of modulus 14^8
primes = [2, 3, 7]
def phi(n):
    d = {}
    for p in primes:
        if n % p == 0:
            count = 0
            while n % p == 0:
                count += 1
                n //= p
            d[p] = count
    result = 1
    for p in d:
        result *= (p**(d[p] - 1))*(p-1)
    return result

def tetration_mod(a, b, m):
    print a, b, m
    if b == 0:
        return 1
    elif m == 1:
        return 0
    else:
        return pow(a, tetration_mod(a, b-1, phi(m)), m)

result = 0
result += 1 #A(0, 0)
result += 3 #A(1, 1)
result += 7 #A(2, 2)
result += 61 #A(3, 3)
result += (tetration_mod(2, 7, 14**8) - 3) #A(4, 4)
result += (tetration_mod(2, 14**8, 14**8) - 3) #A(5, 5)
result += (tetration_mod(2, 14**8, 14**8) - 3) #A(6, 6)
print result % (14**8)


print tetration_mod(2, 7, 14**8) - 3
print phi(phi(14**8))
print 2**9*7**6*3
