#This follows a very straightforward approach.
#Simply follow the instructions for testing whether a number is a Lychrel number,
#using Python's type conversions to do reversing of numbers.

def is_prob_lychrel(n):
    counter = 0
    while counter < 50:
        n = n + int(str(n)[::-1])
        counter += 1
        if str(n) == str(n)[::-1]:
            return False
    return True

print sum(is_prob_lychrel(n) for n in xrange(1, 10000))
