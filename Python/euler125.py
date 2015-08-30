#Project Euler 125: Palindromic sums

def sum_of_squares(n, m):
    """Returns the sum of i**2 for n <= i < m"""
    return ((2*(m-1)**3 + 3*(m-1)**2 + (m-1)) - (2*(n-1)**3+3*(n-1)**2+(n-1))) // 6

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def max_num(N):
    """Returns the n such that any sum of > n consecutive squares is greater than N"""
    n = 1
    while sum_of_squares(1, n) < N:
        n += 1
    return n

def all_sums(i, N):
    """Returns a list of all numbers < N which can be written as the sum of
       i consecutive squares."""
    result = []
    n = 1
    while True:
        s = sum_of_squares(n, n+i)
        if s >= N:
            return result
        result.append(s)
        n += 1

def main(N):
    max_n = max_num(N)
    sums = []
    for k in xrange(2, max_n+1):
        sums += all_sums(k, N)
    #Creates a list of all possible sums of consecutive squares, and
    #returns the sum of all those sums which are also palindromes.
    return sum(s for s in set(sums) if is_palindrome(s))

print main(10**8)
