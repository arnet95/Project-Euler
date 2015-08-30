#Project Euler 387: Harshad Numbers

def isprime(n):
    if n == 2 or n == 3:
        return True
    if pow(2, n-1, n) == 1:
        if pow(3, n-1, n) == 1:
            for i in xrange(5, int(n ** 0.5) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
    return False

def sum_of_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

def gen_right_truncatables(n):
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
#We start with the list of numbers from 1 to 9, which are all clearly
#right truncatable Harshad numbers. Then, for each number in our list, we try
#adding a digit at the end, and then check if the conditions are satisfied.

def gen_strong_right_truncatables(n):
    """Returns a list of all right truncatable Harshad numbers which are also
       strong Harshad numbers"""
    harshad_list = gen_right_truncatables(n)
    return filter(lambda x: isprime(x // sum_of_digits(x)), harshad_list)
#We return the list of all right truncatable Harshad numbers satisfying the
#primality condition.

def main(n):
    s = 0
    for strong_harshad in gen_strong_right_truncatables(n//10):
        for i in [1, 3, 7, 9]:
            num = 10*strong_harshad + i
            if num > n:
                break
            else:
                if isprime(num):
                    s += num
    return s
#We try adding a digit at the end of each of the strong, right truncatable numbers,
#and check if it's a prime, and sum up all of those numbers.

print main(10**14)
