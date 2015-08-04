#Project Euler 387: Harshad Numbers
import time

def isprime(n):
    """Returns True if n is prime, and False otherwise"""
    if n == 2 or n == 3:
        return True
    else:
        if pow(2, n-1, n) == 1:
            if pow(3, n-1, n) == 1:
                for i in xrange(5, int(n ** 0.5) + 1, 6):
                    if n % i == 0 or n % (i + 2) == 0:
                        return False
                return True
        return False

def sum_of_digits(n):
    """Returns the sum of the digits of n"""
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

def f(n):
    """Generate all right truncatable Harshad numbers up to n"""
    l = []
    curr_list = range(1, 10)
    while curr_list != []:
        new_list = []
        for harshad in curr_list:
            l.append(harshad)
            digit_sum = sum_of_digits(harshad)
            for i in xrange(10):
                num = 10*harshad + i
                if num % (digit_sum + i) == 0:
                    if num < n:
                        new_list.append(num)
        curr_list = new_list
    return l

def g(n):
    harshad_list = f(n)
    strong_harshads = []
    for harshad in harshad_list:
        if isprime(harshad // sum_of_digits(harshad)):
            strong_harshads.append(harshad)
    return strong_harshads

def main(n):
    s = 0
    for strong_harshad in g(n//10):
        for i in [1, 3, 7, 9]:
            num = 10*strong_harshad + i
            if num > n:
                break
            else:
                if isprime(num):
                    s += num
    return s

t = time.time()
print main(10**14)
print time.time() - t
